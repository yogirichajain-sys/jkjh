"""Small drawing helpers for the lesson slides (1920x1080)."""
from PIL import ImageDraw, ImageFont

W, H = 1920, 1080
FONT_DIR = "/usr/share/fonts/opentype/inter/"

# Colours
BG = (15, 23, 42)
PANEL = (30, 41, 59)
LINE = (71, 85, 105)
TEXT = (241, 245, 249)
MUTED = (148, 163, 184)
ACCENT = (250, 204, 21)   # yellow highlight
GOOD = (74, 222, 128)
BAD = (248, 113, 113)
S_BLOCK = (249, 115, 22)
P_BLOCK = (20, 184, 166)
D_BLOCK = (59, 130, 246)
F_BLOCK = (168, 85, 247)

_cache = {}


def font(size, weight="Regular"):
    key = (size, weight)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(f"{FONT_DIR}Inter-{weight}.otf", size)
    return _cache[key]


def text(d, xy, s, size=40, weight="Regular", fill=TEXT, anchor="la"):
    d.text(xy, s, font=font(size, weight), fill=fill, anchor=anchor)


def text_w(s, size=40, weight="Regular"):
    return font(size, weight).getlength(s)


def wrap(s, size, maxw, weight="Regular"):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(t, size, weight) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, s, size=40, maxw=800, weight="Regular", fill=TEXT, gap=1.3):
    """Draw wrapped text, return y after it."""
    for line in wrap(s, size, maxw, weight):
        text(d, (x, y), line, size, weight, fill)
        y += int(size * gap)
    return y


def box(d, xy, fill=PANEL, outline=None, r=18, width=3):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def bullets(d, items, shown, x=110, y=200, maxw=1700, size=44, gap=34):
    """Show the first `shown` items; the newest one is highlighted."""
    for i, it in enumerate(items[:shown]):
        new = i == shown - 1
        col = TEXT if new else MUTED
        d.ellipse((x, y + size * 0.35, x + 16, y + size * 0.35 + 16),
                  fill=ACCENT if new else LINE)
        y = para(d, x + 40, y, it, size, maxw - 40, "SemiBold" if new else "Regular", col)
        y += gap
    return y


def cell(d, x, y, w, h, s, fill=PANEL, fg=TEXT, size=36, weight="SemiBold",
         outline=LINE, width=2):
    d.rectangle((x, y, x + w, y + h), fill=fill, outline=outline, width=width)
    if s:
        text(d, (x + w / 2, y + h / 2), s, size, weight, fg, anchor="mm")


def table(d, x, y, colw, rows, rowh=70, size=34, hl=None, header=True):
    """rows: list of lists of strings. hl: dict {(r,c): colour} for fills."""
    hl = hl or {}
    for r, row in enumerate(rows):
        cx = x
        for c, s in enumerate(row):
            fill = hl.get((r, c), (51, 65, 85) if (header and r == 0) else PANEL)
            fg = BG if (r, c) in hl and hl[(r, c)] in (ACCENT, GOOD) else TEXT
            cell(d, cx, y + r * rowh, colw[c], rowh, s, fill, fg, size,
                 "Bold" if header and r == 0 else "SemiBold")
            cx += colw[c]
    return y + len(rows) * rowh


def atom(d, cx, cy, shells, symbol, r0=55, step=55, label=True):
    """Bohr-style atom: nucleus + shells with electrons."""
    import math
    for i, n in enumerate(shells):
        r = r0 + step * (i + 1)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=LINE, width=3)
        outer = i == len(shells) - 1
        for k in range(n):
            a = 2 * math.pi * k / n - math.pi / 2
            ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
            col = ACCENT if outer else (96, 165, 250)
            d.ellipse((ex - 11, ey - 11, ex + 11, ey + 11), fill=col)
    d.ellipse((cx - r0, cy - r0, cx + r0, cy + r0), fill=BAD)
    if label:
        text(d, (cx, cy), symbol, 44, "Bold", BG, anchor="mm")


def arrow(d, p1, p2, col=ACCENT, width=8, head=26):
    import math
    d.line((p1, p2), fill=col, width=width)
    a = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    l, rt = a + math.radians(150), a - math.radians(150)
    d.polygon([p2,
               (p2[0] + head * math.cos(l), p2[1] + head * math.sin(l)),
               (p2[0] + head * math.cos(rt), p2[1] + head * math.sin(rt))],
              fill=col)
