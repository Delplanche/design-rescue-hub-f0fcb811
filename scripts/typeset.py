"""Zetwerk-engine voor de publicaties van De Marktplaats van de Ziel.

Doel: dichte, doorlopende boekbladspiegel zonder kunstmatige witruimte.
Platypus zorgt voor uitgevulde tekst, automatische paginabreuk en registers.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public/publicaties"
ASSETS = ROOT / "src/assets"

PAPER = HexColor("#fcfbf9")
INK = HexColor("#242325")
WINE = HexColor("#8b1e2d")
MUTED = HexColor("#6e6965")
LINE = HexColor("#c9c2b8")


def _font_file(spec: str) -> str:
    return subprocess.check_output(["fc-match", "-f", "%{file}", spec], text=True).strip()


def register_fonts() -> None:
    pairs = [
        ("Serif", "DejaVu Serif"),
        ("SerifBold", "DejaVu Serif:style=Bold"),
        ("SerifItalic", "DejaVu Serif:style=Italic"),
        ("SerifBoldItalic", "DejaVu Serif:style=Bold Italic"),
        ("Sans", "DejaVu Sans"),
        ("SansBold", "DejaVu Sans:style=Bold"),
        ("SansItalic", "DejaVu Sans:style=Oblique"),
        ("Mono", "DejaVu Sans Mono"),
        ("MonoBold", "DejaVu Sans Mono:style=Bold"),
    ]
    for name, spec in pairs:
        pdfmetrics.registerFont(TTFont(name, _font_file(spec)))
    pdfmetrics.registerFontFamily(
        "Serif", normal="Serif", bold="SerifBold", italic="SerifItalic", boldItalic="SerifBoldItalic"
    )
    pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="SansBold", italic="SansItalic")


def styles(body_size: float = 9.3, leading: float = 13.6) -> dict[str, ParagraphStyle]:
    s: dict[str, ParagraphStyle] = {}
    s["body"] = ParagraphStyle(
        "body",
        fontName="Serif",
        fontSize=body_size,
        leading=leading,
        alignment=TA_JUSTIFY,
        textColor=INK,
        spaceAfter=0,
        firstLineIndent=0,
    )
    s["body_indent"] = ParagraphStyle("body_indent", parent=s["body"], firstLineIndent=12)
    s["lead"] = ParagraphStyle(
        "lead", parent=s["body"], fontName="SerifItalic", fontSize=body_size + 1.4,
        leading=leading + 2.4, textColor=MUTED, spaceAfter=7,
    )
    s["chapter_num"] = ParagraphStyle(
        "chapter_num", fontName="Mono", fontSize=7, leading=9, textColor=WINE, spaceAfter=5
    )
    s["chapter_title"] = ParagraphStyle(
        "chapter_title", fontName="Serif", fontSize=20, leading=23, textColor=INK, spaceAfter=4
    )
    s["h2"] = ParagraphStyle(
        "h2", fontName="SansBold", fontSize=9.4, leading=12.5, textColor=INK,
        spaceBefore=11, spaceAfter=3.5,
    )
    s["h3"] = ParagraphStyle(
        "h3", fontName="Mono", fontSize=6.8, leading=9, textColor=WINE,
        spaceBefore=9, spaceAfter=2.5,
    )
    s["quote"] = ParagraphStyle(
        "quote", fontName="SerifItalic", fontSize=body_size + 0.3, leading=leading + 1.2,
        leftIndent=16, rightIndent=10, textColor=INK, alignment=TA_LEFT,
    )
    s["quote_src"] = ParagraphStyle(
        "quote_src", fontName="Mono", fontSize=6.3, leading=8.6, leftIndent=16,
        textColor=MUTED, spaceBefore=3, spaceAfter=8,
    )
    s["bullet"] = ParagraphStyle(
        "bullet", parent=s["body"], leftIndent=13, bulletIndent=2, spaceAfter=2.5,
    )
    s["note"] = ParagraphStyle(
        "note", fontName="Sans", fontSize=6.9, leading=9.6, textColor=MUTED,
        alignment=TA_JUSTIFY, spaceAfter=2.5, leftIndent=15, firstLineIndent=-15,
    )
    s["cell"] = ParagraphStyle("cell", fontName="Sans", fontSize=7.2, leading=9.8, textColor=INK)
    s["cell_head"] = ParagraphStyle(
        "cell_head", fontName="MonoBold", fontSize=6.3, leading=8.6, textColor=PAPER
    )
    s["cell_mono"] = ParagraphStyle("cell_mono", fontName="Mono", fontSize=6.6, leading=9, textColor=WINE)
    s["box_title"] = ParagraphStyle(
        "box_title", fontName="MonoBold", fontSize=6.6, leading=9, textColor=WINE, spaceAfter=3.5
    )
    s["box_body"] = ParagraphStyle(
        "box_body", fontName="Sans", fontSize=7.8, leading=11.2, textColor=INK, alignment=TA_JUSTIFY
    )
    s["cover_title"] = ParagraphStyle(
        "cover_title", fontName="Serif", fontSize=33, leading=36, textColor=INK
    )
    s["cover_sub"] = ParagraphStyle(
        "cover_sub", fontName="Mono", fontSize=8, leading=13, textColor=WINE
    )
    s["caption"] = ParagraphStyle(
        "caption", fontName="Mono", fontSize=6.2, leading=8.8, textColor=MUTED, spaceBefore=3
    )
    return s


class Rule(Flowable):
    def __init__(self, width: float, thickness: float = 0.6, color=LINE, space: float = 6):
        super().__init__()
        self.width, self.thickness, self.color, self.space = width, thickness, color, space
        self.height = thickness + space

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.space, self.width, self.space)


class SideBar(Flowable):
    """Vertical accent used before a chapter opener."""

    def __init__(self, width: float, height: float = 3, color=WINE):
        super().__init__()
        self.width, self.height, self.color = width, height, color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)


class Box(Flowable):
    """Bordered callout that draws itself around pre-built flowables."""

    def __init__(self, flowables, width, tint=HexColor("#f2eee7"), border=LINE, pad=9):
        super().__init__()
        self.flowables = flowables
        self.width = width
        self.tint = tint
        self.border = border
        self.pad = pad
        self._h = 0.0

    def wrap(self, aw, ah):
        inner = self.width - 2 * self.pad
        total = 0.0
        for f in self.flowables:
            _, h = f.wrap(inner, ah)
            total += h + getattr(f, "spaceAfter", 0)
        self._h = total + 2 * self.pad
        return self.width, self._h

    def draw(self):
        c = self.canv
        c.setFillColor(self.tint)
        c.setStrokeColor(self.border)
        c.setLineWidth(0.6)
        c.rect(0, 0, self.width, self._h, fill=1, stroke=1)
        c.setFillColor(WINE)
        c.rect(0, 0, 2.2, self._h, fill=1, stroke=0)
        y = self._h - self.pad
        inner = self.width - 2 * self.pad
        for f in self.flowables:
            _, h = f.wrap(inner, self._h)
            f.drawOn(c, self.pad, y - h)
            y -= h + getattr(f, "spaceAfter", 0)


def data_table(rows, widths, st, head=True):
    body = []
    for i, row in enumerate(rows):
        style = st["cell_head"] if (head and i == 0) else st["cell"]
        body.append([Paragraph(cell, style) for cell in row])
    t = Table(body, colWidths=widths, repeatRows=1 if head else 0, hAlign="LEFT")
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -2), 0.35, LINE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PAPER, HexColor("#f4f1eb")]),
    ]
    if head:
        cmds.append(("BACKGROUND", (0, 0), (-1, 0), INK))
    t.setStyle(TableStyle(cmds))
    return t


class Book(BaseDocTemplate):
    """Document with running heads, folios and a live chapter title."""

    def __init__(self, path: str, pagesize, label: str, margins=(42, 42, 46, 40), **kw):
        left, right, top, bottom = margins
        super().__init__(
            path, pagesize=pagesize, leftMargin=left, rightMargin=right,
            topMargin=top, bottomMargin=bottom, pageCompression=1, **kw
        )
        self.label = label
        self.running = ""
        frame = Frame(
            left, bottom, pagesize[0] - left - right, pagesize[1] - top - bottom,
            id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        blank = Frame(0, 0, pagesize[0], pagesize[1], id="full",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="body", frames=[frame], onPage=self._decorate),
            PageTemplate(id="plain", frames=[blank], onPage=self._paint),
        ])

    def _paint(self, canv, doc):
        canv.setFillColor(PAPER)
        canv.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=1, stroke=0)

    def _decorate(self, canv, doc):
        w, h = doc.pagesize
        self._paint(canv, doc)
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.5)
        canv.line(38, 30, w - 38, 30)
        canv.line(38, h - 34, w - 38, h - 34)
        canv.setFillColor(MUTED)
        canv.setFont("Mono", 6.2)
        canv.drawString(38, h - 44, "DE MARKTPLAATS VAN DE ZIEL")
        canv.drawRightString(w - 38, h - 44, self.running.upper()[:62])
        canv.drawString(38, 19, self.label)
        canv.drawRightString(w - 38, 19, f"{doc.page:02d}")

    def afterFlowable(self, flowable):
        if getattr(flowable, "_running", None):
            self.running = flowable._running


def mark(flowable, running: str):
    flowable._running = running
    return flowable
