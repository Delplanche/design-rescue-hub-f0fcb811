# -*- coding: utf-8 -*-
"""Vectorillustraties voor de hexalogie.

Geen stockbeeld, geen machinetekeningen. De visuele taal bestaat uit gelaagde
glaspanelen met fijne architecturale lijnen — dezelfde esthetiek als de hero van
de website — en sobere fineliner-motieven. Alles wordt als vector getekend op de
perkamentkleur, zonder externe bestanden.
"""
from __future__ import annotations

import math

import qrcode
from reportlab.lib.colors import HexColor
from reportlab.platypus import Flowable

INK = HexColor("#242325")
WINE = HexColor("#8b1e2d")
LINE = HexColor("#c9c2b8")
MUTED = HexColor("#6e6965")


class GlassPanels(Flowable):
    """Gelaagde, half-transparante glaspanelen met fijne lijnen.

    variant bepaalt de compositie; seed verschuift de stapeling zodat elk
    hoofdstuk een eigen, maar familieverwante tekening krijgt.
    """

    def __init__(self, width: float, height: float = 120, variant: int = 0, accent: bool = True):
        super().__init__()
        self.width = width
        self.height = height
        self.variant = variant % 6
        self.accent = accent

    def wrap(self, aw, ah):
        return self.width, self.height

    def _panel(self, c, x, y, w, h, tilt, alpha, stroke_alpha=0.55):
        c.saveState()
        c.translate(x, y)
        c.rotate(tilt)
        c.setFillColor(INK, alpha=alpha)
        c.setStrokeColor(INK, alpha=stroke_alpha)
        c.setLineWidth(0.5)
        c.rect(0, 0, w, h, fill=1, stroke=1)
        c.setStrokeColor(INK, alpha=stroke_alpha * 0.45)
        c.setLineWidth(0.3)
        step = h / 5.0
        for i in range(1, 5):
            c.line(0, i * step, w, i * step)
        c.restoreState()

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        v = self.variant

        if v in (0, 3):
            # Vier panelen in perspectief, oplopend naar rechts.
            base = h * 0.16
            for i in range(4):
                pw = w * (0.17 + i * 0.015)
                ph = h * (0.42 + i * 0.11)
                x = w * 0.10 + i * (w * 0.20)
                self._panel(c, x, base, pw, ph, -4 + i * 2.6, 0.035 + i * 0.022)
        elif v in (1, 4):
            # Concentrische panelen: diepte door herhaling.
            for i in range(5):
                inset = i * (w * 0.055)
                pw = w * 0.62 - inset * 1.4
                ph = h * 0.74 - inset * 1.1
                if pw <= 6 or ph <= 6:
                    break
                x = w * 0.19 + inset * 0.9
                y = h * 0.13 + inset * 0.5
                self._panel(c, x, y, pw, ph, (i - 2) * 1.8, 0.03 + i * 0.018)
        else:
            # Liggende lagen die als glasplaten over elkaar schuiven.
            for i in range(5):
                pw = w * (0.52 - i * 0.04)
                ph = h * 0.16
                x = w * (0.08 + i * 0.075)
                y = h * (0.10 + i * 0.155)
                self._panel(c, x, y, pw, ph, -2.2 + i * 1.1, 0.032 + i * 0.02)

        # Fijne architecturale lijnen die de compositie doorsnijden.
        c.setStrokeColor(LINE)
        c.setLineWidth(0.4)
        c.line(0, h * 0.06, w, h * 0.06)
        c.setStrokeColor(INK, alpha=0.35)
        c.line(w * 0.06, 0, w * 0.06, h)
        if self.accent:
            c.setStrokeColor(WINE)
            c.setLineWidth(1.0)
            c.line(0, h * 0.06, w * 0.14, h * 0.06)


class Fineliner(Flowable):
    """Sober fineliner-motief: lijnen die diepte en transparantie suggereren."""

    def __init__(self, width: float, height: float = 96, variant: int = 0):
        super().__init__()
        self.width, self.height, self.variant = width, height, variant % 3

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setLineWidth(0.35)
        if self.variant == 0:
            # Waaier van lijnen die naar één punt convergeren.
            cx, cy = w * 0.78, h * 0.5
            for i in range(26):
                t = i / 25.0
                c.setStrokeColor(INK, alpha=0.18 + 0.32 * (1 - abs(t - 0.5) * 2))
                c.line(0, h * t, cx, cy)
        elif self.variant == 1:
            # Rasterveld dat naar rechts uitdunt: dichtheid als metafoor.
            cols = 30
            for i in range(cols):
                x = w * i / (cols - 1)
                c.setStrokeColor(INK, alpha=max(0.06, 0.4 - i * 0.012))
                c.line(x, h * 0.08, x, h * 0.92)
            c.setStrokeColor(WINE, alpha=0.7)
            c.setLineWidth(0.8)
            c.line(0, h * 0.5, w * 0.22, h * 0.5)
        else:
            # Zachte golfbanen: het ritme van een gesprek dat wordt gestuurd.
            for k in range(5):
                c.setStrokeColor(INK, alpha=0.14 + k * 0.07)
                path = c.beginPath()
                path.moveTo(0, h * (0.2 + k * 0.13))
                steps = 60
                for i in range(1, steps + 1):
                    x = w * i / steps
                    y = h * (0.2 + k * 0.13) + math.sin(i / steps * math.pi * 2 + k) * h * 0.045
                    path.lineTo(x, y)
                c.drawPath(path)


class QRCode(Flowable):
    """Minimalistische QR-code naar het live register."""

    def __init__(self, data: str, size: float = 62):
        super().__init__()
        self.data = data
        self.size = size

    def wrap(self, aw, ah):
        return self.size, self.size

    def draw(self):
        qr = qrcode.QRCode(version=None, box_size=1, border=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_M)
        qr.add_data(self.data)
        qr.make(fit=True)
        matrix = qr.get_matrix()
        n = len(matrix)
        cell = self.size / n
        c = self.canv
        c.setFillColor(INK)
        for r, row in enumerate(matrix):
            for col, on in enumerate(row):
                if on:
                    c.rect(col * cell, self.size - (r + 1) * cell, cell, cell, fill=1, stroke=0)
