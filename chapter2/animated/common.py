"""Shared look, building blocks and narration sync for the animated lesson."""
import json
import os
import sys
from contextlib import contextmanager

import numpy as np
from manim import *  # noqa: F401,F403

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from voice import speak  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- colours
BG = "#0f172a"
PANEL = "#1e293b"
LINE = "#475569"
INK = "#f1f5f9"
MUTED = "#94a3b8"
GOLD = "#facc15"
GOOD = "#4ade80"
BAD = "#f87171"
S_COL = "#f97316"
P_COL = "#14b8a6"
D_COL = "#3b82f6"
F_COL = "#a855f7"
ELECTRON = "#60a5fa"
NUCLEUS = "#ef4444"
FONT = "Inter"

config.background_color = BG
PAUSE = 0.35          # breathing space after each narration line
CAPTION_SAFE_Y = -2.9  # keep content above this; captions live below


def T(s, size=36, color=INK, weight=NORMAL, **kw):
    return Text(s, font=FONT, font_size=size, color=color, weight=weight, **kw)


def fit(m, width):
    """Shrink a mobject to `width` if it is wider."""
    if m.width > width:
        m.scale_to_fit_width(width)
    return m


def B(s, size=36, color=INK, **kw):
    return T(s, size, color, BOLD, **kw)


# ---------------------------------------------------------------- lesson base
class Lesson(Scene):
    """Scene with narration: `with self.say(text) as d:` plays the voice line,
    lets you animate during it, then waits until the line has finished."""

    def setup(self):
        self.cues = []

    @contextmanager
    def say(self, text, who="teacher"):
        path, dur = speak(text, who)
        start = self.renderer.time
        self.add_sound(path)
        self.cues.append({"start": start, "dur": dur, "text": text, "who": who})
        yield dur
        left = dur + PAUSE - (self.renderer.time - start)
        if left > 0.01:
            self.wait(left)

    @contextmanager
    def doubt(self, question):
        """A student asks a doubt (second voice). Current content steps aside,
        the body of the `with` answers it, then the content comes back."""
        saved = list(self.mobjects)
        if saved:
            self.play(*[FadeOut(m) for m in saved], run_time=0.5)
        kid = student(F_COL, 0.85).move_to([-5.9, 2.55, 0])
        q = B(question, 34)
        bub = RoundedRectangle(corner_radius=0.25, width=q.width + 0.7, height=q.height + 0.55,
                               fill_color=PANEL, fill_opacity=1, stroke_color=F_COL, stroke_width=4)
        q.move_to(bub)
        bubble = VGroup(bub, q).next_to(kid, RIGHT, buff=0.55).align_to(kid, UP).shift(UP * 0.15)
        tail = Polygon(bub.get_left() + UP * 0.12, bub.get_left() + DOWN * 0.22, kid.get_right() + RIGHT * 0.08 + UP * 0.1,
                       fill_color=F_COL, fill_opacity=1, stroke_width=0)
        tag = B("DOUBT!", 24, F_COL).next_to(kid, DOWN, buff=0.12)
        with self.say(question.replace("\n", " "), who="student"):
            self.play(FadeIn(kid, shift=UP * 0.4), FadeIn(tag), run_time=0.4)
            self.play(GrowFromPoint(bubble, kid.get_right()), FadeIn(tail), run_time=0.5)
        yield bubble.get_bottom()[1]
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
        if saved:
            self.play(*[FadeIn(m) for m in saved], run_time=0.5)

    def line(self, text, *anims, run_time=None):
        """Narrate one line while playing anims at its start."""
        with self.say(text) as d:
            if anims:
                self.play(*anims, run_time=run_time or min(1.5, max(0.5, d * 0.5)))

    def tear_down(self):
        out = os.path.join(HERE, "build", "cues")
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, type(self).__name__ + ".json"), "w") as f:
            json.dump(self.cues, f, indent=1)

    def clear_all(self, run_time=0.6):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=run_time)

    def heading(self, s, color=GOLD):
        h = B(s, 44, color).to_edge(UP, buff=0.45)
        return h


def student(color, h=1.0):
    head = Circle(radius=0.22 * h, fill_color=color, fill_opacity=1, stroke_width=0)
    body = RoundedRectangle(corner_radius=0.18 * h, width=0.6 * h, height=0.8 * h, fill_color=color,
                            fill_opacity=1, stroke_width=0)
    head.next_to(body, UP, buff=0.06)
    return VGroup(body, head)


# ---------------------------------------------------------------- atom
class Atom(VGroup):
    def __init__(self, symbol, shells, r0=0.42, step=0.42, e_radius=0.075,
                 show_label=True, outer_gold=True, **kw):
        super().__init__(**kw)
        self.r0, self.step = r0, step
        self.nucleus = Circle(radius=r0, fill_color=NUCLEUS, fill_opacity=1, stroke_width=0)
        self.label = B(symbol, int(r0 * 70), BG).move_to(self.nucleus)
        self.orbits = VGroup()
        self.shells = VGroup()
        for i, n in enumerate(shells):
            r = r0 + step * (i + 1)
            self.orbits.add(Circle(radius=r, stroke_color=LINE, stroke_width=2.5))
            outer = i == len(shells) - 1
            dots = VGroup()
            for k in range(n):
                a = TAU * k / max(n, 1) + PI / 2
                dots.add(Dot([r * np.cos(a), r * np.sin(a), 0], radius=e_radius,
                             color=GOLD if (outer and outer_gold) else ELECTRON))
            self.shells.add(dots)
        self.add(self.orbits, self.nucleus)
        if show_label:
            self.add(self.label)
        self.add(self.shells)

    @property
    def electrons(self):
        return VGroup(*[d for s in self.shells for d in s])

    def outer_radius(self):
        return self.r0 + self.step * len(self.shells)


def spin(atom, speed=0.35):
    """Slowly rotate each shell of an atom (alternating directions)."""
    for i, sh in enumerate(atom.shells):
        sgn = 1 if i % 2 == 0 else -1
        sh.add_updater(lambda m, dt, s=sgn * speed / (i + 1) ** 0.5, a=atom:
                       m.rotate(s * dt, about_point=a.nucleus.get_center()))


def unspin(atom):
    for sh in atom.shells:
        sh.clear_updaters()


# ---------------------------------------------------------------- element boxes
def ebox(sym, top=None, bottom=None, color=PANEL, size=0.9, fs=None, stroke=LINE, txt=INK):
    sq = RoundedRectangle(corner_radius=size * 0.1, width=size, height=size,
                          fill_color=color, fill_opacity=1, stroke_color=stroke, stroke_width=2)
    g = VGroup(sq)
    s = B(sym, fs or int(size * 34), txt).move_to(sq)
    g.add(s)
    if top is not None:
        g.add(T(str(top), int(size * 15), MUTED).move_to(sq.get_corner(UL) + np.array([0.18, -0.13, 0]) * size))
    if bottom is not None:
        s.shift(UP * size * 0.1)
        g.add(T(str(bottom), int(size * 17), MUTED).next_to(s, DOWN, buff=size * 0.06))
    g.sq, g.sym = sq, s
    return g


def card(width, height, color=PANEL, stroke=LINE, sw=2):
    return RoundedRectangle(corner_radius=0.15, width=width, height=height,
                            fill_color=color, fill_opacity=1, stroke_color=stroke, stroke_width=sw)


def stamp(word, color=BAD, size=72):
    t = B(word, size, color)
    r = SurroundingRectangle(t, buff=0.2, color=color, stroke_width=8, corner_radius=0.1)
    return VGroup(r, t).rotate(-12 * DEGREES)


def check(color=GOOD, size=0.5):
    return T("✓", int(size * 80), color, weight=BOLD)


def cross(color=BAD, size=0.5):
    return T("✗", int(size * 80), color, weight=BOLD)


# ---------------------------------------------------------------- periodic table
SYMBOLS = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
           "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba "
           "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn "
           "Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og").split()
METALLOIDS = {"B", "Si", "Ge", "As", "Sb", "Te", "Po"}


def table_positions():
    """{Z: (row, col)}; rows 1-7 main table, 8-9 the f-block rows."""
    pos = {1: (1, 1), 2: (1, 18)}
    z = 3
    for period in (2, 3):
        for c in (1, 2, 13, 14, 15, 16, 17, 18):
            pos[z] = (period, c)
            z += 1
    for period in (4, 5):
        for c in range(1, 19):
            pos[z] = (period, c)
            z += 1
    for period, frow in ((6, 8), (7, 9)):
        pos[z], pos[z + 1] = (period, 1), (period, 2)
        z += 2
        for i in range(15):
            pos[z] = (frow, 3 + i)
            z += 1
        for c in range(4, 19):
            pos[z] = (period, c)
            z += 1
    return pos


POS = table_positions()


def block_of(z):
    row, col = POS[z]
    if row >= 8:
        return "f"
    if col <= 2:
        return "s"
    if col >= 13:
        return "p"
    return "d"


BLOCK_COL = {"s": S_COL, "p": P_COL, "d": D_COL, "f": F_COL}


class PeriodicTable(VGroup):
    def __init__(self, cell=0.6, gap=0.04, center=ORIGIN + UP * 0.25, numbers=True, **kw):
        super().__init__(**kw)
        self.cell, self.gap = cell, gap
        self.boxes = {}
        self.origin = center + np.array([-8.5 * cell, 4.0 * cell, 0])
        for z, (row, col) in POS.items():
            b = ebox(SYMBOLS[z - 1], z if numbers else None, size=cell - gap, fs=int(cell * 30))
            b.move_to(self.point(row, col))
            self.boxes[z] = b
            self.add(b)

    def point(self, row, col):
        y = -(row - 1) * self.cell - (0.3 * self.cell if row >= 8 else 0)
        return self.origin + np.array([(col - 1) * self.cell, y, 0])

    def zs(self, cond):
        return [z for z in self.boxes if cond(z)]

    def group_of(self, zlist):
        return VGroup(*[self.boxes[z] for z in zlist])

    def staircase(self, color=GOLD, width=7):
        c = self.cell
        pts = []
        for i, col in enumerate(range(13, 18)):
            p = self.point(2 + i, col) + np.array([-c / 2, c / 2, 0])
            pts += [p, p + DOWN * c]
            if col < 17:
                pts.append(p + DOWN * c + RIGHT * c)
        return VMobject(stroke_color=color, stroke_width=width).set_points_as_corners(pts)
