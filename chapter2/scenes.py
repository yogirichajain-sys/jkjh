"""Lesson content: Maharashtra SSC Class 10, Science & Technology Part 1,
Chapter 2 - Periodic Classification of Elements.

Each scene has a title, a list of narration steps, and a draw(d, k) function
that draws the slide for step k (0-based). Steps reveal things one by one.
"""
from draw import *  # noqa: F401,F403

SCENES = []


def scene(title, steps):
    def wrap_fn(fn):
        SCENES.append({"title": title, "steps": steps, "draw": fn})
        return fn
    return wrap_fn


# ---------------------------------------------------------------- intro
@scene("", [
    "Hi! Today we are doing Chapter 2 of Science Part 1: Periodic Classification of Elements. "
    "Many students think this chapter is just a big table to memorise. It is not. "
    "Once your basics are clear, the whole table makes sense, almost like a story.",
    "Here is our plan. First, we refresh the basics from earlier classes. "
    "Then we see how scientists tried to arrange the elements: Dobereiner, Newlands and Mendeleev. "
    "Then the modern periodic table. Then the trends, which is where most of the marks are. "
    "And finally, some practice questions.",
])
def _intro(d, k):
    if k == 0:
        text(d, (W / 2, 330), "SSC Class 10  ·  Science Part 1  ·  Chapter 2", 44, "Medium", MUTED, "mm")
        text(d, (W / 2, 470), "Periodic Classification", 110, "Bold", TEXT, "mm")
        text(d, (W / 2, 600), "of Elements", 110, "Bold", ACCENT, "mm")
        text(d, (W / 2, 750), "Basics first. Then facts. Then understanding.", 44, "Regular", MUTED, "mm")
    else:
        text(d, (110, 110), "Our plan", 64, "Bold")
        steps = ["Basics refresh", "Dobereiner's triads", "Newlands' octaves",
                 "Mendeleev's table", "Modern periodic table", "Trends", "Practice"]
        for i, s in enumerate(steps):
            x = 110 + (i % 4) * 430
            y = 260 + (i // 4) * 300
            box(d, (x, y, x + 390, y + 240), outline=ACCENT if i in (0, 5) else None)
            text(d, (x + 30, y + 30), str(i + 1), 64, "Bold", ACCENT)
            para(d, x + 30, y + 120, s, 40, 340, "SemiBold")


# ---------------------------------------------------------------- basics
@scene("Basics 1: Element and atom", [
    "Basics first. An element is a pure substance made of only one kind of atom. "
    "Like hydrogen, oxygen, iron or gold. Today we know 118 elements.",
    "Every atom has a nucleus in the centre, which has protons and neutrons. "
    "Around the nucleus, electrons move in shells.",
    "The number of protons is called the atomic number, written as capital Z. "
    "In a neutral atom, the number of electrons is also equal to Z. "
    "Remember this, because the modern periodic table is built on atomic number.",
    "Atomic mass is roughly protons plus neutrons. "
    "The early scientists arranged elements by atomic mass, because the inside of the atom was not yet understood.",
])
def _basics1(d, k):
    items = ["Element: a pure substance made of only one kind of atom (118 known)",
             "Atom: nucleus (protons + neutrons) with electrons in shells",
             "Atomic number Z = number of protons = number of electrons",
             "Atomic mass ≈ protons + neutrons"]
    bullets(d, items, k + 1, maxw=1050)
    if k >= 1:
        atom(d, 1530, 560, [2, 8, 1], "Na")
        text(d, (1530, 900), "Sodium: Z = 11", 40, "SemiBold", MUTED, "mm")


@scene("Basics 2: Shells and electronic configuration", [
    "Shells are named K, L, M and N, starting from the nucleus. "
    "A shell can hold at most 2 n squared electrons. "
    "So K holds 2, L holds 8, M holds 18, and N holds 32.",
    "Writing how the electrons fill the shells is called electronic configuration. "
    "Sodium has 11 electrons: 2, 8, 1. Chlorine has 17: 2, 8, 7. Argon has 18: 2, 8, 8.",
    "Electrons in the outermost shell are called valence electrons. They decide how an element reacts. "
    "Sodium has 1 valence electron and gives it away, so its valency is 1. "
    "Chlorine has 7 and needs 1 more, so its valency is also 1. "
    "Argon's outer shell is full, so it does not react. Its valency is zero.",
    "Keep these three ideas in your pocket: atomic number, electronic configuration, and valence electrons. "
    "With these three, you can explain almost every question in this chapter.",
])
def _basics2(d, k):
    rows = [["Shell", "n", "Max = 2n²"], ["K", "1", "2"], ["L", "2", "8"],
            ["M", "3", "18"], ["N", "4", "32"]]
    table(d, 110, 200, [180, 120, 260], rows, 90, 40)
    if k >= 1:
        rows2 = [["Element", "Z", "K, L, M", "Valence e⁻", "Valency"],
                 ["Sodium (Na)", "11", "2, 8, 1", "1", "1"],
                 ["Chlorine (Cl)", "17", "2, 8, 7", "7", "1"],
                 ["Argon (Ar)", "18", "2, 8, 8", "8", "0"]]
        if k == 1:
            rows2 = [r[:3] for r in rows2]
            colw = [300, 120, 260]
        else:
            colw = [300, 120, 230, 230, 190]
        hl = {(r, 3): ACCENT for r in range(1, 4)} if k == 2 else {}
        table(d, 760, 200, colw, rows2, 90, 38, hl)
    if k == 3:
        for i, s in enumerate(["Atomic number", "Electronic configuration", "Valence electrons"]):
            box(d, (760 + i * 360, 640, 760 + i * 360 + 330, 820), outline=ACCENT)
            para(d, 790 + i * 360, 680, s, 40, 280, "Bold", ACCENT)


@scene("Basics 3: Metals, non-metals, metalloids", [
    "One more basic: metals and non-metals. Metals tend to lose their valence electrons and form positive ions. "
    "That is why we call them electropositive. Sodium, magnesium and iron are metals.",
    "Non-metals tend to gain electrons and form negative ions. They are electronegative. "
    "Chlorine, oxygen and sulphur are non-metals.",
    "And some elements behave a bit like both. These are called metalloids. "
    "For example boron, silicon, germanium and arsenic.",
])
def _basics3(d, k):
    cards = [("Metals", "Lose electrons → positive ions", "Electropositive", "Na, Mg, Fe", S_BLOCK),
             ("Non-metals", "Gain electrons → negative ions", "Electronegative", "Cl, O, S", P_BLOCK),
             ("Metalloids", "Properties of both", "In between", "B, Si, Ge, As", ACCENT)]
    for i, (t, a, b, e, col) in enumerate(cards[:k + 1]):
        x = 110 + i * 580
        box(d, (x, 220, x + 540, 820), outline=col, width=5)
        text(d, (x + 40, 260), t, 60, "Bold", col)
        y = para(d, x + 40, 380, a, 42, 460)
        text(d, (x + 40, y + 30), b, 40, "SemiBold", MUTED)
        text(d, (x + 40, 700), e, 52, "Bold")


# ---------------------------------------------------------------- why classify
@scene("Why classify elements?", [
    "Now the chapter begins. Why classify elements at all? "
    "Imagine a library with thousands of books thrown on the floor. You would never find anything. "
    "Arrange them by subject, and suddenly it is easy.",
    "By the eighteen hundreds, scientists knew many elements, and new ones kept being discovered. "
    "To study them easily, they tried to group elements with similar properties. "
    "Let us see how these attempts improved, step by step.",
])
def _why(d, k):
    para(d, 110, 220, "Many elements, many properties → hard to study one by one.", 48, 1700, "SemiBold")
    para(d, 110, 320, "Classification = putting similar elements together, so we can study them group by group.", 44, 1700, fill=MUTED)
    if k >= 1:
        tl = [("1817", "Dobereiner", "Triads (3)"), ("1866", "Newlands", "Octaves (8)"),
              ("1869", "Mendeleev", "Atomic mass"), ("1913", "Moseley", "Atomic number")]
        d.line((180, 650, 1740, 650), fill=LINE, width=6)
        for i, (y, n, w) in enumerate(tl):
            x = 230 + i * 480
            d.ellipse((x - 22, 628, x + 22, 672), fill=ACCENT)
            text(d, (x, 580), y, 48, "Bold", ACCENT, "mm")
            text(d, (x, 720), n, 44, "SemiBold", TEXT, "mm")
            text(d, (x, 780), w, 38, "Regular", MUTED, "mm")


# ---------------------------------------------------------------- Dobereiner
@scene("Dobereiner's triads (1817)", [
    "First attempt: Dobereiner, a German scientist, in 1817. "
    "He noticed that some elements come in groups of three with similar properties. He called them triads.",
    "Here is the magic. Arrange the three in increasing order of atomic mass. "
    "The atomic mass of the middle element is about the average of the other two. "
    "Lithium is 7 and potassium is 39. 7 plus 39 is 46, divided by 2 is 23. And sodium is 23!",
    "Same for calcium, strontium and barium: 40 plus 137 is 177, half is 88.5, and strontium is about 88. "
    "And chlorine, bromine, iodine: 35.5 plus 127 is 162.5, half is about 81, and bromine is 80.",
    "The limitation: he could find only a few triads among the elements known then. "
    "So this method could not classify all the elements. "
    "But it gave an important idea: properties and atomic mass are connected.",
])
def _dob(d, k):
    triads = [[("Li", 7), ("Na", 23), ("K", 39)],
              [("Ca", 40), ("Sr", 88), ("Ba", 137)],
              [("Cl", 35.5), ("Br", 80), ("I", 127)]]
    n = 1 if k < 2 else 3
    for t in range(n):
        x = 110 + t * 580
        for j, (s, m) in enumerate(triads[t]):
            y = 200 + j * 150
            mid = j == 1 and k >= 1
            box(d, (x, y, x + 520, y + 130), outline=ACCENT if mid else None, width=4)
            text(d, (x + 40, y + 65), s, 64, "Bold", ACCENT if mid else TEXT, "lm")
            text(d, (x + 480, y + 65), f"{m:g}", 52, "SemiBold", MUTED, "rm")
        if k >= 1:
            a, c = triads[t][0][1], triads[t][2][1]
            text(d, (x + 260, 690), f"({a:g} + {c:g}) ÷ 2 = {(a + c) / 2:g}", 40, "SemiBold", GOOD, "mm")
    if k == 0:
        para(d, 750, 260, "Triad = 3 elements with similar properties", 50, 1000, "Bold")
        para(d, 750, 420, "Arranged in increasing order of atomic mass", 44, 1000, fill=MUTED)
    if k == 3:
        box(d, (110, 760, 1810, 890), outline=BAD)
        text(d, (150, 825), "Limitation: only a few triads found → could not classify all elements", 42, "SemiBold", BAD, "lm")


# ---------------------------------------------------------------- Newlands
NEWLANDS = [
    ["sa", "re", "ga", "ma", "pa", "dha", "ni"],
    ["H", "Li", "Be", "B", "C", "N", "O"],
    ["F", "Na", "Mg", "Al", "Si", "P", "S"],
    ["Cl", "K", "Ca", "Cr", "Ti", "Mn", "Fe"],
    ["Co,Ni", "Cu", "Zn", "Y", "In", "As", "Se"],
]


@scene("Newlands' law of octaves (1866)", [
    "Next, John Newlands, an English scientist, in 1866. "
    "He arranged the known elements in increasing order of atomic mass, "
    "starting from hydrogen and ending at thorium, the 56th element.",
    "He noticed that every eighth element had properties similar to the first. "
    "Just like music! Sa, re, ga, ma, pa, dha, ni, and then sa comes again. "
    "So he called it the law of octaves.",
    "Look: lithium, then 7 elements later, sodium. Then 7 more, potassium. "
    "All three are similar, reactive metals. Fluorine and chlorine are also in one column, and they are similar too.",
    "But there were problems. The law worked well only up to calcium. "
    "To fit his pattern, he put two elements, cobalt and nickel, in one place, "
    "in the same column as fluorine and chlorine, which are totally different. "
    "And iron was placed far away from cobalt and nickel, even though they are similar. "
    "He also assumed no new elements would be discovered. So the law failed for heavier elements.",
])
def _newlands(d, k):
    hl = {}
    if k >= 2:
        for r in (1, 2, 3):
            hl[(r, 1)] = GOOD
        hl[(2, 0)] = GOOD
        hl[(3, 0)] = GOOD
    if k == 3:
        hl = {(4, 0): BAD, (3, 6): BAD, (2, 0): (127, 29, 29), (3, 0): (127, 29, 29)}
    rows = NEWLANDS if k >= 1 else NEWLANDS[1:]
    table(d, 110, 200, [190] * 7, rows, 110, 44, hl, header=k >= 1)
    x = 1500
    if k == 0:
        para(d, x, 230, "Increasing atomic mass →", 40, 360, "SemiBold", MUTED)
        para(d, x, 380, "H … Th (56 elements)", 40, 360, "SemiBold")
    elif k in (1, 2):
        para(d, x, 230, "Every 8th element is like the 1st", 42, 360, "Bold", ACCENT)
        para(d, x, 430, "Like musical notes: sa … ni, sa", 40, 360, fill=MUTED)
    else:
        for i, s in enumerate(["Worked only up to calcium", "Two elements in one box (Co, Ni)",
                               "Unlike elements together", "No room for new elements"]):
            text(d, (x, 230 + i * 120), "✗", 44, "Bold", BAD)
            para(d, x + 50, 232 + i * 120, s, 34, 330)


# ---------------------------------------------------------------- Mendeleev
@scene("Mendeleev's periodic table (1869)", [
    "Now the big one: Dmitri Mendeleev, a Russian scientist, in 1869. At that time, 63 elements were known. "
    "He wrote each element and its properties on a card, and kept rearranging the cards like a puzzle.",
    "He used two things: atomic mass, and chemical properties, "
    "especially the formulas of their oxides and hydrides, which means compounds with oxygen and hydrogen.",
    "His law, Mendeleev's periodic law, says: properties of elements are a periodic function of their atomic masses. "
    "Periodic means they repeat after regular intervals. Write this law word for word in the exam.",
    "In his table, the vertical columns are called groups, and the horizontal rows are called periods.",
])
def _mend(d, k):
    items = ["63 elements known; each on a card with its properties",
             "Basis: atomic mass + chemical properties (formulas of oxides and hydrides)"]
    bullets(d, items, min(k + 1, 2))
    if k >= 2:
        box(d, (110, 520, 1810, 700), outline=ACCENT, width=5)
        text(d, (150, 560), "Mendeleev's periodic law", 40, "Bold", ACCENT)
        text(d, (150, 625), "Properties of elements are a periodic function of their atomic masses.", 46, "SemiBold")
    if k == 3:
        text(d, (150, 780), "Columns ↓ = Groups", 50, "Bold", P_BLOCK)
        text(d, (1000, 780), "Rows → = Periods", 50, "Bold", S_BLOCK)


@scene("Mendeleev: merits", [
    "Why was Mendeleev's table so successful? First, he was bold. "
    "Where no known element fitted, he left a gap, and said: an element will be discovered here one day.",
    "He even predicted their properties, and named them using the Sanskrit word eka, which means one. "
    "Eka-boron, eka-aluminium and eka-silicon. Later they were discovered and named scandium, gallium and germanium. "
    "Look how close his predictions for gallium were!",
    "Second, he corrected the wrong atomic masses of some elements. "
    "For example, the atomic mass of beryllium was corrected from 14.09 to 9.4, so it could sit with similar elements.",
    "Third, when the noble gases like helium, neon and argon were discovered later, "
    "they fitted neatly as a separate zero group, without disturbing the rest of the table.",
])
def _merits(d, k):
    if k <= 1:
        rows = [["Group III", "Group IV"], ["B  11", "C  12"], ["Al  27", "Si  28"], ["?  68", "?  72"]]
        table(d, 110, 200, [260, 260], rows, 110, 44, {(3, 0): ACCENT, (3, 1): ACCENT})
        para(d, 110, 690, "Gaps left for undiscovered elements", 40, 560, "SemiBold", ACCENT)
    if k == 0:
        for i, (a, b) in enumerate([("Eka-boron", "Scandium"), ("Eka-aluminium", "Gallium"),
                                    ("Eka-silicon", "Germanium")]):
            y = 230 + i * 140
            text(d, (820, y), a, 48, "Bold", ACCENT)
            text(d, (1300, y), "→  ?", 48, "Bold", MUTED)
    if k == 1:
        rows = [["Property", "Eka-aluminium (predicted)", "Gallium (actual)"],
                ["Atomic mass", "68", "69.7"], ["Density (g/cm³)", "5.9", "5.94"],
                ["Melting point", "Low", "30.2 °C"], ["Oxide", "E₂O₃", "Ga₂O₃"],
                ["Chloride", "ECl₃", "GaCl₃"]]
        table(d, 720, 200, [330, 460, 330], rows, 95, 36)
    if k >= 2:
        merits = ["Left gaps and predicted new elements (Sc, Ga, Ge)",
                  "Corrected atomic masses (Be: 14.09 → 9.4)",
                  "Noble gases fitted as a new zero group"]
        bullets(d, merits, k + 1 if k == 3 else 2, size=48)
        if k == 2:
            text(d, (150, 600), "Be", 120, "Bold", ACCENT)
            text(d, (420, 640), "14.09  →  9.4", 70, "Bold")
        else:
            for i, s in enumerate(["He", "Ne", "Ar", "Kr", "Xe"]):
                cell(d, 150 + i * 160, 640, 140, 140, s, PANEL, ACCENT, 50, outline=ACCENT, width=4)
            text(d, (1000, 710), "Group 0", 60, "Bold", ACCENT, "lm")


@scene("Mendeleev: demerits", [
    "But his table also had some problems. First, the position of hydrogen. "
    "Hydrogen is like the alkali metals in some ways, and like the halogens in other ways. "
    "For example, hydrogen exists as H two, just like chlorine exists as C L two. So its correct place was not fixed.",
    "Second, isotopes. Isotopes are atoms of the same element with different atomic masses, like chlorine 35 and chlorine 37. "
    "If the table is based on atomic mass, where do we put them? Mendeleev's table had no answer.",
    "Third, the order was broken in some places. Cobalt, with atomic mass 58.9, was placed before nickel, 58.7, "
    "just to keep similar elements together.",
    "Fourth, atomic mass does not increase in a regular way from one element to the next. "
    "So it was impossible to say how many elements could exist between two elements.",
])
def _demerits(d, k):
    items = ["Position of hydrogen not fixed (like alkali metals AND like halogens)",
             "Isotopes (Cl-35, Cl-37): different atomic masses - where to put them?",
             "Order broken: Co (58.9) placed before Ni (58.7)",
             "Atomic mass does not increase regularly → can't predict number of elements in between"]
    bullets(d, items, k + 1, size=46)
    if k == 2:
        cell(d, 600, 680, 220, 200, "Co", PANEL, TEXT, 70, outline=BAD, width=5)
        cell(d, 900, 680, 220, 200, "Ni", PANEL, TEXT, 70, outline=BAD, width=5)
        text(d, (710, 850), "58.9", 36, "SemiBold", MUTED, "mm")
        text(d, (1010, 850), "58.7", 36, "SemiBold", MUTED, "mm")


# ---------------------------------------------------------------- modern
@scene("Modern periodic law (Moseley, 1913)", [
    "In 1913, Henry Moseley, an English scientist, did experiments with X-rays. "
    "He showed that the atomic number is the most basic property of an element, more basic than atomic mass.",
    "So the law was changed. The modern periodic law says: "
    "properties of elements are a periodic function of their atomic numbers. "
    "Just one word changed, from mass to number, and many problems disappeared.",
    "Isotopes have the same atomic number, so they now sit in the same place. "
    "And cobalt, atomic number 27, naturally comes before nickel, atomic number 28. No forcing needed.",
])
def _moseley(d, k):
    para(d, 110, 200, "Moseley: atomic number (Z) is the basic property of an element, not atomic mass.", 46, 1700, "SemiBold")
    if k >= 1:
        box(d, (110, 380, 1810, 560), outline=GOOD, width=5)
        text(d, (150, 420), "Modern periodic law", 40, "Bold", GOOD)
        text(d, (150, 485), "Properties of elements are a periodic function of their atomic numbers.", 46, "SemiBold")
    if k == 2:
        for i, (s, z) in enumerate([("Co", "Z = 27"), ("Ni", "Z = 28")]):
            cell(d, 150 + i * 260, 640, 220, 200, s, PANEL, TEXT, 70, outline=GOOD, width=5)
            text(d, (260 + i * 260, 810), z, 34, "SemiBold", MUTED, "mm")
        para(d, 750, 660, "Isotopes: same Z → same place", 48, 1000, "Bold", GOOD)
        para(d, 750, 760, "Co before Ni: correct order", 48, 1000, "Bold", GOOD)


SYMBOLS = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
           "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba "
           "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn "
           "Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og").split()


def positions():
    """Return {Z: (row, col)}; rows 1-7 main table, rows 8-9 for f-block."""
    pos = {1: (1, 1), 2: (1, 18)}
    z = 3
    for period in (2, 3):
        for c in (1, 2, 13, 14, 15, 16, 17, 18):
            pos[z] = (period, c); z += 1
    for period in (4, 5):
        for c in range(1, 19):
            pos[z] = (period, c); z += 1
    for period, frow in ((6, 8), (7, 9)):
        pos[z] = (period, 1); pos[z + 1] = (period, 2); z += 2
        for i in range(15):
            pos[z] = (frow, 3 + i); z += 1
        for c in range(4, 19):
            pos[z] = (period, c); z += 1
    return pos


def block_colour(z, row, col):
    if row >= 8:
        return F_BLOCK
    if col <= 2:
        return S_BLOCK
    if col >= 13:
        return P_BLOCK
    return D_BLOCK


METALLOIDS = {"B", "Si", "Ge", "As", "Sb", "Te", "Po"}


def periodic_table(d, k, x0=210, y0=190, cw=84, ch=72, hl_group=None, hl_period=None):
    pos = positions()

    def xy(row, col):
        y = y0 + (row - 1) * ch + (25 if row >= 8 else 0)
        return x0 + (col - 1) * cw, y
    for z, (row, col) in pos.items():
        x, y = xy(row, col)
        s = SYMBOLS[z - 1]
        fill = PANEL
        if k >= 1:
            c = block_colour(z, row, col)
            fill = tuple(int(v * 0.55) for v in c)
            if k == 1 and row >= 8:
                fill = PANEL
        if hl_group and col == hl_group and row <= 7:
            fill = (161, 98, 7)
        if hl_period and row == hl_period:
            fill = (161, 98, 7)
        outline = ACCENT if (k >= 3 and s in METALLOIDS) else BG
        d.rectangle((x + 2, y + 2, x + cw - 2, y + ch - 2), fill=fill, outline=outline,
                    width=4 if outline == ACCENT else 1)
        text(d, (x + cw / 2, y + ch / 2 + 4), s, 28, "SemiBold", TEXT, "mm")
        text(d, (x + 6, y + 4), str(z), 14, "Regular", MUTED)
    # placeholders for La-Lu and Ac-Lr in group 3
    for row, s in ((6, "57-71"), (7, "89-103")):
        x, y = xy(row, 3)
        d.rectangle((x + 2, y + 2, x + cw - 2, y + ch - 2), fill=PANEL)
        text(d, (x + cw / 2, y + ch / 2), s, 18, "Regular", MUTED, "mm")
    # labels
    for c in range(1, 19):
        x, _ = xy(1, c)
        text(d, (x + cw / 2, y0 - 22), str(c), 22, "SemiBold", MUTED, "mm")
    for r in range(1, 8):
        x, y = xy(r, 1)
        text(d, (x - 30, y + ch / 2), str(r), 26, "SemiBold", MUTED, "mm")
    if k >= 3:
        pts = []
        for i, c in enumerate(range(13, 18)):
            px, py = xy(2 + i, c)
            pts += [(px, py), (px, py + ch)]
        d.line(pts, fill=ACCENT, width=7, joint="curve")
    return xy


@scene("The modern periodic table", [
    "This is the modern periodic table. It has seven horizontal rows, called periods, "
    "and eighteen vertical columns, called groups.",
    "The table is divided into blocks. Groups 1 and 2 form the s-block. Groups 13 to 18 form the p-block. "
    "Groups 3 to 12 in the middle form the d-block. These are called transition elements.",
    "The two rows kept separately at the bottom are the f-block: the lanthanides and the actinides, "
    "also called inner transition elements. They are kept below only so the table does not become too wide.",
    "And see this zig-zag line in the p-block? Metals are on its left side, non-metals on its right side, "
    "and the metalloids lie along this line. Most elements are metals.",
])
def _modern(d, k):
    periodic_table(d, k)
    lx = 210
    legend = [("7 periods (rows)", TEXT), ("18 groups (columns)", TEXT)]
    if k >= 1:
        legend = [("s-block", S_BLOCK), ("p-block", P_BLOCK), ("d-block", D_BLOCK)]
    if k >= 2:
        legend.append(("f-block", F_BLOCK))
    if k >= 3:
        legend.append(("metalloids / zig-zag line", ACCENT))
    for i, (s, c) in enumerate(legend):
        d.rectangle((lx, 900, lx + 34, 934), fill=c)
        text(d, (lx + 46, 917), s, 32, "SemiBold", TEXT, "lm")
        lx += 90 + text_w(s, 32, "SemiBold")


@scene("Groups, periods and electronic configuration", [
    "Now connect this to our basics. Elements in the same group have the same number of valence electrons. "
    "Lithium is 2, 1. Sodium is 2, 8, 1. Potassium is 2, 8, 8, 1. All have 1 valence electron. "
    "That is why they behave alike.",
    "Elements in the same period have the same number of shells. Everything in period 2, from lithium to neon, has 2 shells. "
    "So, the period number equals the number of shells. "
    "As we go from left to right in a period, the valence electrons increase by one each time.",
    "Here is a quick trick to find an element's position. Write its electronic configuration. "
    "The number of shells gives the period. For groups 1 and 2, the valence electrons give the group. "
    "For the p-block, add 10. For example, chlorine is 2, 8, 7. Three shells, so period 3. "
    "Seven valence electrons, plus 10, so group 17.",
    "The number of elements in the periods is 2, 8, 8, 18, 18, 32 and 32. "
    "This comes from how many electrons the shells can hold.",
])
def _groups(d, k):
    if k == 0:
        rows = [["Group 1", "Configuration", "Valence e⁻"], ["Li", "2, 1", "1"],
                ["Na", "2, 8, 1", "1"], ["K", "2, 8, 8, 1", "1"]]
        table(d, 110, 200, [260, 420, 300], rows, 110, 46, {(r, 2): ACCENT for r in (1, 2, 3)})
        para(d, 1250, 260, "Same group → same valence electrons → similar properties", 48, 560, "Bold", ACCENT)
    if k == 1:
        els = [("Li", "2,1"), ("Be", "2,2"), ("B", "2,3"), ("C", "2,4"), ("N", "2,5"),
               ("O", "2,6"), ("F", "2,7"), ("Ne", "2,8")]
        for i, (s, c) in enumerate(els):
            cell(d, 110 + i * 212, 220, 200, 160, s, PANEL, TEXT, 60, outline=LINE)
            text(d, (210 + i * 212, 430), c, 40, "SemiBold", ACCENT, "mm")
        para(d, 110, 540, "Period 2: all have 2 shells.", 50, 1700, "Bold")
        para(d, 110, 630, "Period number = number of shells", 50, 1700, "Bold", ACCENT)
        para(d, 110, 720, "Left → right: valence electrons 1 → 8", 46, 1700, fill=MUTED)
    if k == 2:
        atom(d, 420, 520, [2, 8, 7], "Cl", r0=50, step=60)
        y = 230
        for s, c in [("Chlorine: 2, 8, 7", TEXT), ("3 shells → Period 3", ACCENT),
                     ("7 valence e⁻ + 10 → Group 17", ACCENT)]:
            text(d, (850, y), s, 54, "Bold", c)
            y += 130
        para(d, 850, y + 30, "Groups 1, 2: group = valence electrons. Groups 13-18: group = valence electrons + 10", 36, 950, fill=MUTED)
    if k == 3:
        rows = [["Period", "1", "2", "3", "4", "5", "6", "7"],
                ["Elements", "2", "8", "8", "18", "18", "32", "32"]]
        table(d, 110, 280, [260] + [190] * 7, rows, 130, 54)


# ---------------------------------------------------------------- trends
@scene("Trend 1: Valency", [
    "Now the trends. These are asked a lot in the exam. First, valency. Valency depends on valence electrons.",
    "Across period 3: sodium 1, magnesium 2, aluminium 3, silicon 4, then phosphorus 3, sulphur 2, chlorine 1, and argon 0. "
    "So in a period, valency first increases from 1 to 4, and then decreases to 0.",
    "Down a group, valence electrons stay the same, so valency stays the same. All group 1 elements have valency 1.",
])
def _valency(d, k):
    els = ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]
    ve = [1, 2, 3, 4, 5, 6, 7, 8]
    val = [1, 2, 3, 4, 3, 2, 1, 0]
    rows = [["Period 3"] + els, ["Valence e⁻"] + [str(v) for v in ve]]
    if k >= 1:
        rows.append(["Valency"] + [str(v) for v in val])
    table(d, 110, 200, [300] + [175] * 8, rows, 100, 44,
          {(2, c): ACCENT for c in range(1, 9)} if k >= 1 else {})
    if k >= 1:
        base = 780
        pts = [(410 + 87 + i * 175, base - v * 60) for i, v in enumerate(val)]
        d.line(pts, fill=ACCENT, width=6)
        for p in pts:
            d.ellipse((p[0] - 10, p[1] - 10, p[0] + 10, p[1] + 10), fill=ACCENT)
        text(d, (110, 640), "1 → 4 → 0", 54, "Bold", ACCENT)
    if k == 2:
        text(d, (110, 860), "Down a group: valency stays the same", 48, "Bold", GOOD)


RAD_P = [("Li", 152), ("Be", 111), ("B", 88), ("C", 77), ("N", 74), ("O", 66)]
RAD_G = [("Li", 152), ("Na", 186), ("K", 231), ("Rb", 244), ("Cs", 262)]


@scene("Trend 2: Atomic size (atomic radius)", [
    "Second, atomic size, measured as atomic radius: the distance from the nucleus to the outermost shell. "
    "It is tiny, so we measure it in picometres. One picometre is ten to the power minus twelve metre.",
    "Across a period, from left to right, atomic radius decreases. Why? "
    "The number of shells stays the same, but the atomic number increases, so the positive charge on the nucleus increases. "
    "A stronger nucleus pulls the electrons closer. Lithium is 152 picometres, but oxygen is only 66.",
    "Down a group, atomic radius increases. That is because a new shell is added at every step. "
    "More shells means a bigger atom, even though the nuclear charge also increases. "
    "Lithium 152, sodium 186, potassium 231.",
])
def _radius(d, k):
    if k == 0:
        atom(d, 500, 540, [2, 8, 1], "Na", r0=50, step=70)
        arrow(d, (500, 540), (500 + 50 + 70 * 3, 540), col=GOOD, width=6)
        text(d, (650, 470), "radius", 40, "Bold", GOOD, "mm")
        para(d, 950, 300, "Atomic radius = distance from nucleus to outermost shell", 48, 850, "Bold")
        para(d, 950, 480, "Unit: picometre (pm)", 46, 850, fill=ACCENT, weight="SemiBold")
        para(d, 950, 560, "1 pm = 10⁻¹² m", 46, 850, fill=MUTED)
    if k == 1:
        for i, (s, r) in enumerate(RAD_P):
            cx = 230 + i * 290
            rr = r * 0.75
            d.ellipse((cx - rr, 480 - rr, cx + rr, 480 + rr), fill=(30, 64, 175), outline=D_BLOCK, width=3)
            text(d, (cx, 480), s, 46, "Bold", TEXT, "mm")
            text(d, (cx, 640), f"{r} pm", 36, "SemiBold", MUTED, "mm")
        arrow(d, (230, 750), (1680, 750), col=ACCENT)
        text(d, (230, 800), "Across a period → radius DECREASES (more nuclear charge, same shells)", 40, "Bold", ACCENT)
    if k == 2:
        for i, (s, r) in enumerate(RAD_G):
            cx = 220 + i * 330
            rr = r * 0.55
            cy = 520
            d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=(124, 45, 18), outline=S_BLOCK, width=3)
            text(d, (cx, cy), s, 46, "Bold", TEXT, "mm")
            text(d, (cx, 720), f"{r} pm", 36, "SemiBold", MUTED, "mm")
        text(d, (110, 800), "Down a group → radius INCREASES (new shell added each time)", 40, "Bold", ACCENT)


@scene("Trend 3: Metallic and non-metallic character", [
    "Third, metallic character. A metal easily loses its valence electrons. "
    "So metallic character means: how easily an atom gives away electrons.",
    "Across a period, metallic character decreases. The atom gets smaller and the nucleus holds the electrons more tightly, "
    "so giving them away is harder. In period 3, sodium and magnesium are metals, silicon is a metalloid, "
    "and phosphorus, sulphur and chlorine are non-metals.",
    "Down a group, metallic character increases. The outer electrons are farther from the nucleus, so they are easier to remove. "
    "That is why potassium is more reactive than sodium.",
    "Non-metallic character is the exact opposite: it increases across a period and decreases down a group. "
    "Among the halogens, fluorine is the most reactive, and reactivity decreases down to iodine.",
])
def _metallic(d, k):
    para(d, 110, 190, "Metallic character = tendency to LOSE valence electrons", 46, 1700, "Bold")
    if k >= 1:
        els = [("Na", S_BLOCK), ("Mg", S_BLOCK), ("Al", S_BLOCK), ("Si", ACCENT),
               ("P", P_BLOCK), ("S", P_BLOCK), ("Cl", P_BLOCK)]
        for i, (s, c) in enumerate(els):
            cell(d, 110 + i * 170, 300, 155, 130, s, PANEL, c, 54, outline=c, width=4)
        text(d, (110, 480), "metals", 34, "SemiBold", S_BLOCK)
        text(d, (620, 480), "metalloid", 34, "SemiBold", ACCENT)
        text(d, (790, 480), "non-metals", 34, "SemiBold", P_BLOCK)
        arrow(d, (110, 560), (1290, 560), col=BAD)
        text(d, (110, 590), "Metallic character decreases →", 38, "Bold", BAD)
    if k >= 2:
        for i, s in enumerate(["Li", "Na", "K"]):
            cell(d, 1450, 300 + i * 150, 150, 130, s, PANEL, S_BLOCK, 54, outline=S_BLOCK, width=4)
        arrow(d, (1650, 300), (1650, 730), col=GOOD)
        para(d, 1690, 380, "Metallic character increases", 34, 200, "Bold", GOOD)
    if k == 3:
        box(d, (110, 700, 1380, 900), outline=P_BLOCK, width=4)
        para(d, 140, 720, "Non-metallic character: opposite!", 42, 1200, "Bold", P_BLOCK)
        para(d, 140, 790, "Increases across a period, decreases down a group. Halogens: F > Cl > Br > I", 38, 1200)


@scene("All trends in one table", [
    "Here is everything in one table. Take a screenshot of this. "
    "If you understand why each arrow goes the way it does, you do not need to memorise it. "
    "Just remember two reasons. Across a period, the nuclear charge increases but the shells stay the same. "
    "Down a group, a new shell is added each time.",
])
def _summary(d, k):
    rows = [["Property", "Across a period →", "Down a group ↓"],
            ["Number of shells", "Same", "Increases"],
            ["Valence electrons", "1 → 8", "Same"],
            ["Valency", "1 → 4 → 0", "Same"],
            ["Atomic radius", "Decreases", "Increases"],
            ["Metallic character", "Decreases", "Increases"],
            ["Non-metallic character", "Increases", "Decreases"]]
    table(d, 110, 170, [620, 540, 540], rows, 92, 42)
    text(d, (110, 840), "Reason →  more nuclear charge, same shells", 36, "SemiBold", ACCENT)
    text(d, (1000, 840), "Reason ↓  new shell added", 36, "SemiBold", ACCENT)


@scene("Memory tricks", [
    "Some memory tricks. For the history, remember: 3, 8, mass, number. "
    "Dobereiner's triads had 3 elements. Newlands' octaves had 8. Mendeleev used atomic mass. Moseley used atomic number.",
    "For group 2: beryllium, magnesium, calcium, strontium, barium, radium. "
    "Remember it as: Beta Mange Car, Scooter Baap Raazi. "
    "And for the halogens, fluorine, chlorine, bromine, iodine: Fat Cats Bring Ice.",
])
def _tricks(d, k):
    if k == 0:
        for i, (a, b) in enumerate([("3", "Dobereiner: triads"), ("8", "Newlands: octaves"),
                                    ("Mass", "Mendeleev"), ("Number", "Moseley (modern)")]):
            x = 110 + i * 430
            box(d, (x, 260, x + 400, 640), outline=ACCENT)
            text(d, (x + 200, 380), a, 90, "Bold", ACCENT, "mm")
            para(d, x + 30, 500, b, 38, 340, "SemiBold")
    else:
        y = 220
        for sym, phrase in [("Be  Mg  Ca  Sr  Ba  Ra", "Beta Mange Car, Scooter Baap Raazi"),
                            ("F  Cl  Br  I", "Fat Cats Bring Ice")]:
            box(d, (110, y, 1810, y + 270))
            text(d, (150, y + 50), sym, 64, "Bold", ACCENT)
            text(d, (150, y + 160), phrase, 50, "SemiBold")
            y += 320


QUESTIONS = [
    ("Name the law: “Properties of elements are a periodic function of their atomic numbers.”",
     "Modern periodic law (given after Moseley's work)."),
    ("An element has electronic configuration 2, 8, 2. Find its period, group and type.",
     "3 shells → period 3. 2 valence electrons → group 2. It is magnesium, a metal, valency 2."),
    ("Why does atomic radius decrease from left to right in a period?",
     "Atomic number (nuclear charge) increases but the electrons are added to the same shell, so they are pulled closer to the nucleus."),
    ("Which elements did Mendeleev call eka-boron, eka-aluminium and eka-silicon?",
     "Scandium, gallium and germanium."),
]

_qsteps = []
for q, a in QUESTIONS:
    _qsteps.append("Question. " + q.replace("“", "").replace("”", "") + " Pause the video and try it.")
    _qsteps.append("Answer. " + a.replace(" → ", ", so "))


@scene("Practice questions", _qsteps)
def _practice(d, k):
    qi, show = k // 2, k % 2 == 1
    q, a = QUESTIONS[qi]
    text(d, (110, 200), f"Q{qi + 1}", 70, "Bold", ACCENT)
    para(d, 300, 205, q, 52, 1500, "SemiBold")
    if show:
        box(d, (110, 560, 1810, 860), outline=GOOD, width=5)
        text(d, (150, 590), "Answer", 40, "Bold", GOOD)
        para(d, 150, 660, a, 46, 1620)
    else:
        text(d, (W / 2, 700), "Pause and try", 56, "Bold", MUTED, "mm")


@scene("", [
    "That is the whole chapter. Remember the three basics: atomic number, electronic configuration and valence electrons. "
    "Then the story: triads, octaves, Mendeleev, and Moseley. "
    "Then the trends, with just two reasons behind them. "
    "Revise the summary table once tomorrow and once before the exam. All the best!",
])
def _outro(d, k):
    text(d, (W / 2, 300), "Remember", 64, "Bold", ACCENT, "mm")
    lines = ["Basics: Z, electronic configuration, valence electrons",
             "Story: Triads → Octaves → Mendeleev → Moseley",
             "Trends: two reasons (nuclear charge across, new shell down)"]
    for i, s in enumerate(lines):
        text(d, (W / 2, 450 + i * 110), s, 46, "SemiBold", TEXT, "mm")
    text(d, (W / 2, 830), "All the best!", 60, "Bold", GOOD, "mm")
