"""Animated lesson: SSC Class 10 Science Part 1, Ch 2 - Periodic Classification of Elements.

Render one scene:   manim -ql lesson.py S01Hook
Render everything:  python3 build.py
"""
import random

from common import *  # noqa: F401,F403


def dim(c, k=0.45):
    return interpolate_color(ManimColor(c), ManimColor(BG), k)


# =====================================================================  1. HOOK
class S01Hook(Lesson):
    def construct(self):
        q = B("“Science is hard.”", 84)
        who = T("— your friend", 40, MUTED).next_to(q, DOWN, buff=0.45).align_to(q, RIGHT)
        with self.say("Your friend says science is hard? Let's test that."):
            self.play(Write(q), run_time=1.3)
            self.play(FadeIn(who, shift=LEFT * 0.4), run_time=0.5)
        st = stamp("REALLY?", GOLD, 64).next_to(q, UP, buff=0.2).shift(RIGHT * 3)
        self.play(FadeIn(st, scale=2.5), run_time=0.35)
        self.wait(0.3)
        self.play(FadeOut(VGroup(q, who, st)), run_time=0.5)

        pt = PeriodicTable(cell=0.6, center=UP * 0.2)
        with self.say("This is the periodic table. 118 elements. 118 boxes. Looks scary, right?") as d:
            self.play(LaggedStart(*[FadeIn(b, scale=0.4) for b in pt], lag_ratio=0.025), run_time=3.2)
            self.play(pt.animate.scale(1.04), rate_func=there_and_back, run_time=0.8)

        secret = VGroup(T("The secret?", 40, MUTED), B("You learned it in", 52),
                        B("5th standard.", 64, GOLD)).arrange(DOWN, buff=0.3).to_edge(RIGHT, buff=0.7)
        with self.say("But by the end of this video, you will be able to point at any box and tell its story. "
                      "And the secret? You already learned it in fifth standard."):
            self.play(pt.animate.scale(0.6).to_edge(LEFT, buff=0.4), run_time=1.2)
            z = 11
            b = pt.boxes[z]
            self.play(b.animate.scale(2.4).set_z_index(5), run_time=0.6)
            self.play(b.animate.scale(1 / 2.4), run_time=0.5)
            self.play(pt.animate.set_opacity(0.3), FadeIn(secret, shift=UP * 0.5), run_time=1)
        self.clear_all()

        a = Atom("Na", [2, 8, 1], r0=0.4, step=0.4).scale(0.8).to_edge(LEFT, buff=0.8)
        title = VGroup(T("SSC Class 10 · Science Part 1 · Chapter 2", 32, MUTED),
                       B("Periodic Classification", 70), B("of Elements", 70, GOLD)
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit(title, 8.6).next_to(a, RIGHT, buff=0.7)
        with self.say("Chapter 2. Periodic Classification of Elements. Let's go!"):
            spin(a, 0.8)
            self.play(FadeIn(a, scale=0.5), LaggedStart(*[FadeIn(t, shift=RIGHT * 0.4) for t in title],
                                                         lag_ratio=0.3), run_time=1.5)
        self.wait(0.6)
        unspin(a)
        self.clear_all()


# =====================================================================  2. BASICS
class S02Basics(Lesson):
    def keep(self, *keep):
        self.play(*[FadeOut(m) for m in self.mobjects if m not in keep], run_time=0.6)

    def construct(self):
        h = self.heading("Basics: you already know these")
        self.play(FadeIn(h, shift=DOWN * 0.3))

        # --- nucleus and roll number
        nuc = Circle(radius=0.75, fill_color=NUCLEUS, fill_opacity=1, stroke_width=0)
        plus = VGroup(*[B("+", 34, BG) for _ in range(6)]).arrange_in_grid(2, 3, buff=0.12).move_to(nuc)
        lab = T("nucleus (protons +)", 30, MUTED).next_to(nuc, DOWN, buff=0.3)
        with self.say("Every atom is like a tiny building. In the centre is the nucleus, packed with positive protons."):
            self.play(GrowFromCenter(nuc), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(p, scale=2) for p in plus], lag_ratio=0.15), FadeIn(lab), run_time=1.2)

        with self.doubt("Why don't the electrons just\nfly away from the nucleus?"):
            n = VGroup(Circle(radius=0.7, fill_color=NUCLEUS, fill_opacity=1, stroke_width=0), B("+", 64, BG))
            e = VGroup(Circle(radius=0.32, fill_color=ELECTRON, fill_opacity=1, stroke_width=0), B("\u2212", 50, BG))
            n.move_to(LEFT * 2.6 + DOWN * 0.5)
            e.move_to(RIGHT * 2.6 + DOWN * 0.5)
            a1 = Arrow(e.get_left(), e.get_left() + LEFT * 1.6, color=GOLD, buff=0.1, stroke_width=7)
            a2 = Arrow(n.get_right(), n.get_right() + RIGHT * 1.6, color=GOLD, buff=0.1, stroke_width=7)
            rule = B("+ and \u2212 attract each other", 44, GOLD).move_to(DOWN * 2.1)
            with self.say("Good question! Protons are positive, and electrons are negative. And opposites attract. "
                          "The nucleus keeps pulling the electrons, like a magnet holding iron pins. "
                          "Remember this pull. It explains almost every trend in this chapter."):
                self.play(FadeIn(n, scale=0.5), FadeIn(e, scale=0.5), run_time=0.8)
                self.wait(1.5)
                self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.8)
                self.play(e.animate.shift(LEFT * 1.0), rate_func=there_and_back, run_time=1.2)
                self.play(Write(rule), run_time=1)

        zl = B("Atomic number Z = number of protons", 40, GOLD).next_to(h, DOWN, buff=0.6)
        roll = T("= the element's ROLL NUMBER", 40, INK).next_to(zl, DOWN, buff=0.25)
        cards = VGroup(*[ebox(s, bottom=f"Roll no. {i + 1}", size=1.5)
                         for i, s in enumerate(["H", "He", "Li", "Be", "B", "C"])]).arrange(RIGHT, buff=0.3)
        cards.next_to(roll, DOWN, buff=0.6)
        with self.say("Count the protons, and you get the atomic number, Z. Think of it as the element's roll number. "
                      "Hydrogen is roll number 1, helium 2, lithium 3, and so on. No two elements share a roll number."):
            self.play(FadeOut(VGroup(nuc, plus, lab), shift=LEFT), Write(zl), run_time=1.2)
            self.play(FadeIn(roll, shift=UP * 0.2), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.5) for c in cards], lag_ratio=0.35), run_time=3)
        self.keep(h)

        # --- shells as floors
        atom = Atom("Na", [2, 8, 1], r0=0.42, step=0.5).move_to(LEFT * 3.4 + UP * 0.05)
        caps = VGroup(*[VGroup(B(n, 40, c), T(f"max {m}", 36)).arrange(RIGHT, buff=0.4)
                        for n, m, c in [("K", 2, ELECTRON), ("L", 8, ELECTRON), ("M", 18, ELECTRON),
                                        ("N", 32, ELECTRON)]]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rule = B("= 2n²", 44, GOLD).next_to(caps, DOWN, buff=0.4, aligned_edge=LEFT)
        capbox = VGroup(T("Shells = floors", 40, MUTED), caps, rule).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        capbox.move_to(RIGHT * 3.6 + DOWN * 0.3)
        rule.align_to(caps, LEFT)
        with self.say("Around the nucleus, electrons live on floors called shells: K, L, M and N. "
                      "Each floor has a seat limit: 2, 8, 18 and 32. That's just 2 n squared."):
            self.play(GrowFromCenter(atom.nucleus), FadeIn(atom.label), run_time=0.6)
            self.play(LaggedStart(*[Create(o) for o in atom.orbits], lag_ratio=0.3), FadeIn(capbox[0]), run_time=1.2)
            self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.3) for c in caps], lag_ratio=0.5), run_time=3)
            self.play(Write(rule), run_time=0.6)

        cfg = [B("2", 60, GOLD), B("2, 8", 60, GOLD), B("2, 8, 1", 60, GOLD)]
        for c in cfg:
            c.next_to(atom, DOWN, buff=0.2).shift(UP * 0.1)
        z = T("Z = 11 → 11 electrons", 34, MUTED).next_to(atom, UP, buff=0.15)
        with self.say("Let's fill sodium. Its roll number is 11, so it has 11 electrons. "
                      "2 on the first floor. 8 on the second. And 1 lonely electron on the third. "
                      "Sodium is 2, 8, 1.") as d:
            self.play(FadeOut(capbox), FadeIn(z), run_time=0.6)
            self.wait(d * 0.2)
            cur = None
            for i, sh in enumerate(atom.shells):
                anims = [LaggedStart(*[GrowFromCenter(e) for e in sh], lag_ratio=0.25)]
                anims.append(FadeIn(cfg[i]) if cur is None else ReplacementTransform(cur, cfg[i]))
                self.play(*anims, run_time=1.0 + 0.1 * len(sh))
                cur = cfg[i]
                self.wait(d * 0.08)
            self.play(Indicate(cfg[2], color=GOLD), run_time=0.8)

        val = atom.shells[2][0]
        ring = Circle(radius=0.22, color=GOLD, stroke_width=5).move_to(val)
        vtext = VGroup(B("Valence electron", 44, GOLD), T("= electrons on the TOP floor", 36),
                       T("They decide how the element behaves", 36, MUTED)
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit(vtext, 6.4).move_to(RIGHT * 3.4 + UP * 0.6)
        arr = Arrow(vtext.get_left() + LEFT * 0.2, ring.get_right(), color=GOLD, buff=0.1, stroke_width=6)
        with self.say("That top floor electron is called the valence electron. It is the one at the window, "
                      "the one that meets other atoms. And it decides how the element behaves."):
            self.play(Create(ring), Flash(val, color=GOLD, flash_radius=0.4), run_time=0.8)
            self.play(FadeIn(vtext, shift=LEFT * 0.4), GrowArrow(arr), run_time=1)
        self.play(FadeOut(VGroup(vtext, arr, ring, z, cfg[2])), run_time=0.5)

        # --- give / grab / full
        self.play(atom.animate.scale(0.62).move_to(LEFT * 4.6 + UP * 0.45), run_time=0.8)
        na_lab = VGroup(B("Na  2, 8, 1", 34), B("gives 1 away", 28, S_COL), B("METAL", 30, S_COL)).arrange(DOWN, buff=0.1)
        na_lab.next_to(atom, DOWN, buff=0.3)
        with self.say("Sodium has just one, and it would happily give it away. Elements that give away electrons are metals."):
            self.play(FadeIn(na_lab[0]), run_time=0.5)
            e = atom.shells[2][0]
            self.play(e.animate.move_to(LEFT * 6.8 + UP * 3.2).set_opacity(0), run_time=1.2)
            plus = B("+", 40, GOLD).next_to(atom.nucleus, UR, buff=0.05)
            self.play(FadeIn(plus, scale=2), FadeIn(na_lab[1:], shift=UP * 0.2), run_time=0.7)

        cl = Atom("Cl", [2, 8, 8], r0=0.45, step=0.55).scale(0.62).move_to(UP * 0.45)
        new_e = cl.shells[2][7]
        cl.shells[2].remove(new_e)
        cl_lab = VGroup(B("Cl  2, 8, 7", 34), B("grabs 1", 28, P_COL), B("NON-METAL", 30, P_COL)).arrange(DOWN, buff=0.1)
        cl_lab.next_to(cl, DOWN, buff=0.3)
        with self.say("Chlorine is 2, 8, 7. It needs just one more to fill its top floor, so it grabs one. "
                      "Elements that grab electrons are non-metals."):
            self.play(FadeIn(cl, scale=0.6), FadeIn(cl_lab[0]), run_time=0.8)
            target = new_e.get_center()
            new_e.move_to(UP * 3.6 + RIGHT * 1.5)
            self.add(new_e)
            self.wait(0.8)
            self.play(new_e.animate.move_to(target), run_time=1.1)
            minus = B("−", 40, GOLD).next_to(cl.nucleus, UR, buff=0.05)
            self.play(Flash(new_e, color=GOLD), FadeIn(minus, scale=2), FadeIn(cl_lab[1:], shift=UP * 0.2), run_time=0.7)

        ar = Atom("Ar", [2, 8, 8], r0=0.45, step=0.55).scale(0.62).move_to(RIGHT * 4.6 + UP * 0.45)
        ar_lab = VGroup(B("Ar  2, 8, 8", 34), B("full shell", 28, GOOD), B("NO REACTION", 30, GOOD)).arrange(DOWN, buff=0.1)
        ar_lab.next_to(ar, DOWN, buff=0.3)
        with self.say("And argon, 2, 8, 8, has a full top floor. Totally happy. It does not react at all."):
            self.play(FadeIn(ar, scale=0.6), FadeIn(ar_lab), run_time=1)
            spin(ar, 0.6)
            self.wait(1.5)
        unspin(ar)
        with self.doubt("Why does sodium give away 1 electron?\nWhy not grab 7 more instead?"):
            rows = VGroup()
            for sym, cfg, good, bad in [("Na", "2, 8, 1", "lose 1  \u2192  2, 8", "gain 7  \u2192  2, 8, 8"),
                                        ("Cl", "2, 8, 7", "gain 1  \u2192  2, 8, 8", "lose 7  \u2192  2, 8")]:
                r = VGroup(B(f"{sym}  {cfg}", 40),
                           VGroup(check(size=0.45), T(good, 34), B("easy", 34, GOOD)).arrange(RIGHT, buff=0.25),
                           VGroup(cross(size=0.45), T(bad, 34, MUTED), B("hard", 34, BAD)).arrange(RIGHT, buff=0.25)
                           ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
                rows.add(r)
            rows.arrange(RIGHT, buff=1.4, aligned_edge=UP).move_to(DOWN * 0.45)
            moral = B("Atoms take the EASY way to a full outer shell", 36, GOLD).move_to(DOWN * 2.25)
            with self.say("Think about it. Getting rid of 1 electron is much easier than collecting 7 more. "
                          "Chlorine is the opposite: grabbing 1 is easier than throwing away 7. "
                          "Atoms always take the easy way to a full outer shell. "
                          "That's why metals have few valence electrons, and non-metals have many."):
                self.play(FadeIn(rows[0][0]), run_time=0.5)
                self.play(FadeIn(rows[0][1], shift=RIGHT * 0.2), run_time=0.6)
                self.play(FadeIn(rows[0][2], shift=RIGHT * 0.2), run_time=0.6)
                self.wait(1)
                self.play(FadeIn(rows[1], shift=RIGHT * 0.2), run_time=0.8)
                self.wait(1.5)
                self.play(Write(moral), run_time=1)
        unspin(ar)
        self.keep(h)

        names = [("Roll number", "Atomic number Z"), ("Floors", "Shells & configuration"),
                 ("Top-floor electrons", "Valence electrons")]
        cs = VGroup()
        for i, (a, b) in enumerate(names):
            c = card(4.0, 2.4, stroke=GOLD, sw=4)
            txt = fit(VGroup(B(str(i + 1), 56, GOLD), B(a, 34), T(b, 26, MUTED)).arrange(DOWN, buff=0.18), 3.6).move_to(c)
            cs.add(VGroup(c, txt))
        cs.arrange(RIGHT, buff=0.4).shift(DOWN * 0.1)
        cost = fit(T("Everything else in this chapter = these 3 in different costumes", 34, GOLD), 12.5).next_to(cs, DOWN, buff=0.5)
        with self.say("So remember three things: roll number, floors, and top floor electrons. "
                      "Honestly, the rest of this chapter is just these three, wearing different costumes."):
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.4) for c in cs], lag_ratio=0.5), run_time=2.5)
            self.play(Write(cost), run_time=1.2)
        self.clear_all()


# =====================================================================  3. TRIADS & OCTAVES
class S03Triads(Lesson):
    def construct(self):
        random.seed(3)
        syms = SYMBOLS[:36]
        mess = VGroup(*[ebox(s, size=0.75) for s in syms])
        for b in mess:
            b.move_to([random.uniform(-6.2, 6.2), random.uniform(-2.4, 2.8), 0]).rotate(random.uniform(-0.6, 0.6))
        with self.say("Now, a puzzle that took 100 years. In the eighteen hundreds, scientists kept discovering new elements, "
                      "but there was no order. Like a cupboard where everything is just thrown in."):
            self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 2, rate_func=rush_from) for b in mess], lag_ratio=0.04), run_time=2.5)
            self.play(mess.animate.scale(1.06).rotate(0.03), rate_func=there_and_back, run_time=1.0)
        self.play(FadeOut(mess, shift=DOWN), run_time=0.6)

        people = [("1817", "Dobereiner"), ("1866", "Newlands"), ("1869", "Mendeleev"), ("1913", "Moseley")]
        tl = Line(LEFT * 6, RIGHT * 6, color=LINE, stroke_width=6).shift(DOWN * 0.2)
        dots, labs = VGroup(), VGroup()
        for i, (y, n) in enumerate(people):
            x = -4.8 + i * 3.2
            dots.add(Dot([x, -0.2, 0], radius=0.16, color=GOLD))
            labs.add(VGroup(B(y, 44, GOLD).move_to([x, 0.6, 0]), B(n, 36).move_to([x, -1.0, 0])))
        with self.say("Four scientists tried to bring order. Let's meet them, one by one."):
            self.play(Create(tl), run_time=0.7)
            self.play(LaggedStart(*[AnimationGroup(GrowFromCenter(d), FadeIn(l, shift=UP * 0.2))
                                    for d, l in zip(dots, labs)], lag_ratio=0.4), run_time=2.2)
        self.play(FadeOut(VGroup(tl, dots, labs)), run_time=0.5)

        # --- Dobereiner
        h = self.heading("1817 · Dobereiner's triads")
        trio = VGroup(*[ebox(s, bottom=m, size=1.6) for s, m in [("Li", 7), ("Na", 23), ("K", 39)]]).arrange(RIGHT, buff=0.5)
        trio.shift(UP * 0.6)
        with self.say("First, Dobereiner, in 1817. He found groups of three similar elements, and called them triads. "
                      "And they had a magic trick hidden inside."):
            self.play(FadeIn(h, shift=DOWN * 0.3), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.5) for b in trio], lag_ratio=0.3), run_time=1.5)
        s1 = B("7 + 39 = 46", 52).next_to(trio, DOWN, buff=0.7)
        s2 = B("46 ÷ 2 = 23", 52, GOLD).move_to(s1)
        with self.say("Take lithium, 7, and potassium, 39. Add them: 46. Half of that: 23. "
                      "And sodium's atomic mass is exactly 23! The middle one is the average of the other two.") as d:
            self.play(Indicate(trio[0], color=GOLD), Indicate(trio[2], color=GOLD), run_time=1)
            self.play(Write(s1), run_time=1)
            self.wait(0.6)
            self.play(ReplacementTransform(s1, s2), run_time=0.8)
            self.play(trio[1].sq.animate.set_stroke(GOLD, 8), Flash(trio[1], color=GOLD, flash_radius=1.1), run_time=0.8)
            tick = check(size=0.9).next_to(trio[1], UP, buff=0.15)
            self.play(FadeIn(tick, scale=2), run_time=0.4)
        more = VGroup(*[VGroup(*[ebox(s, bottom=m, size=1.1) for s, m in t]).arrange(RIGHT, buff=0.2)
                        for t in [[("Ca", 40), ("Sr", 88), ("Ba", 137)], [("Cl", 35.5), ("Br", 80), ("I", 127)]]])
        with self.say("It works for calcium, strontium and barium. And for chlorine, bromine and iodine too. "
                      "But he could find only a few triads. Most elements had no team. So this idea could not classify all elements."):
            g = VGroup(trio, s2, tick)
            self.play(g.animate.scale(0.68).move_to(LEFT * 4.4 + UP * 0.6), run_time=0.8)
            more.arrange(RIGHT, buff=0.6).move_to(RIGHT * 2.2 + UP * 0.9)
            self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.4) for m in more], lag_ratio=0.5), run_time=1.6)
            self.wait(1.5)
            lone = VGroup(*[ebox(s, size=0.7, txt=MUTED) for s in ["Fe", "Cu", "Zn", "Al", "Si", "P", "S", "Mg", "C", "N"]]
                          ).arrange(RIGHT, buff=0.15).shift(DOWN * 1.6)
            qs = T("no team?", 34, BAD).next_to(lone, DOWN, buff=0.25)
            self.play(LaggedStart(*[FadeIn(b, scale=0.5) for b in lone], lag_ratio=0.1), FadeIn(qs), run_time=1.5)
        with self.doubt("Why did they arrange elements by mass?\nWhy not by atomic number?"):
            beam = Line(LEFT * 2.2, RIGHT * 2.2, color=INK, stroke_width=8).shift(UP * 0.2)
            post = Polygon(UP * 0.2, DOWN * 1.6 + LEFT * 0.6, DOWN * 1.6 + RIGHT * 0.6, fill_color=LINE, fill_opacity=1, stroke_width=0)
            pans = VGroup(*[Arc(radius=0.7, start_angle=PI, angle=PI, color=INK, stroke_width=6).move_to(beam.get_end() * k + DOWN * 0.55) for k in (-1, 1)])
            na = ebox("Na", size=0.8).next_to(pans[0], UP, buff=-0.25)
            wt = B("23", 34, GOLD).next_to(pans[1], UP, buff=0.05)
            scale = VGroup(beam, post, pans, na, wt).scale(0.9).move_to(LEFT * 3.4 + DOWN * 0.6)
            facts = VGroup(VGroup(cross(size=0.45), T("Protons, electrons: not discovered yet", 32)).arrange(RIGHT, buff=0.25),
                           VGroup(check(size=0.45), T("Mass: could be measured by weighing", 32)).arrange(RIGHT, buff=0.25),
                           T("Atomic number came only in 1913", 30, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            facts.move_to(RIGHT * 2.6 + DOWN * 0.6)
            with self.say("Because back then, nobody knew about protons or electrons inside the atom! "
                          "The only thing scientists could measure was how heavy an atom is. "
                          "So atomic mass was the best tool they had. Atomic number came much later, in 1913."):
                self.play(FadeIn(scale, shift=UP * 0.3), run_time=0.8)
                self.play(FadeIn(facts[0], shift=LEFT * 0.2), run_time=0.6)
                self.wait(1.2)
                self.play(FadeIn(facts[1], shift=LEFT * 0.2), run_time=0.6)
                self.wait(1.2)
                self.play(FadeIn(facts[2]), run_time=0.6)
        self.clear_all()

        # --- Newlands
        h = self.heading("1866 · Newlands' law of octaves")
        rows = [["H", "Li", "Be", "B", "C", "N", "O"], ["F", "Na", "Mg", "Al", "Si", "P", "S"],
                ["Cl", "K", "Ca", "Cr", "Ti", "Mn", "Fe"]]
        flat = [s for r in rows for s in r]
        boxes = VGroup(*[ebox(s, size=0.56) for s in flat]).arrange(RIGHT, buff=0.04).shift(UP * 0.3)
        arrow_txt = T("increasing atomic mass →", 32, MUTED).next_to(boxes, DOWN, buff=0.35)
        with self.say("Next, Newlands, in 1866. He lined up the elements in increasing order of atomic mass, "
                      "starting from hydrogen, all the way to thorium, 56 elements in all."):
            self.play(FadeIn(h, shift=DOWN * 0.3), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(b, shift=LEFT * 0.6) for b in boxes], lag_ratio=0.06), FadeIn(arrow_txt), run_time=2.5)

        cw = 1.25
        notes = ["sa", "re", "ga", "ma", "pa", "dha", "ni"]
        x0, y0 = -3.75, 1.6
        header = VGroup(*[B(n, 40, GOLD).move_to([x0 + i * cw, y0, 0]) for i, n in enumerate(notes)])
        targets = []
        for r, row in enumerate(rows):
            for c in range(7):
                targets.append([x0 + c * cw, y0 - 1.0 - r * 1.0, 0])
        with self.say("And he noticed something musical. Every eighth element behaves like the first. "
                      "Sa, re, ga, ma, pa, dha, ni, and then sa again! He called it the law of octaves.") as d:
            self.play(FadeOut(arrow_txt), run_time=0.3)
            self.play(*[b.animate.scale(1.6).move_to(t) for b, t in zip(boxes, targets)], run_time=1.6)
            self.play(LaggedStart(*[FadeIn(n, shift=DOWN * 0.3) for n in header], lag_ratio=0.25), run_time=2.2)
            note = T("♪", 70, GOLD).next_to(header, RIGHT, buff=0.4)
            self.play(FadeIn(note, shift=UP * 0.3), Indicate(header[0], color=GOLD), run_time=0.7)
        col_re = VGroup(boxes[1], boxes[8], boxes[15])
        col_sa = VGroup(boxes[7], boxes[14])
        with self.say("Look: lithium, sodium and potassium land in the same column. All three are similar metals. "
                      "Fluorine and chlorine are together too. Beautiful!"):
            self.play(*[b.sq.animate.set_fill(dim(GOOD, 0.35)) for b in col_re], run_time=0.8)
            self.play(Circumscribe(col_re, color=GOOD, buff=0.1), run_time=1.2)
            self.play(*[b.sq.animate.set_fill(dim(GOOD, 0.35)) for b in col_sa], run_time=0.8)

        row4 = VGroup(*[ebox(s, size=0.9, fs=24 if "," in s else None)
                        for s in ["Co,Ni", "Cu", "Zn", "Y", "In", "As", "Se"]])
        for i, b in enumerate(row4):
            b.move_to([x0 + i * cw, y0 - 4.0, 0])
        probs = VGroup(*[VGroup(cross(size=0.45), T(s, 28)).arrange(RIGHT, buff=0.2) for s in
                         ["Worked only up to calcium", "2 elements in 1 box", "Unlike elements together",
                          "No room for new elements"]]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        fit(probs, 4.1).to_edge(RIGHT, buff=0.25)
        probs.shift(DOWN * 0.3)
        with self.say("But after calcium, the music went off-key. He squeezed cobalt and nickel into one box, "
                      "and put them in the same column as fluorine and chlorine. That's like putting a cat in a team of fish! "
                      "And he assumed no new elements would ever be found.") as d:
            grid = VGroup(header, note, boxes)
            self.play(VGroup(grid).animate.shift(LEFT * 2.5), run_time=0.6)
            row4.shift(LEFT * 2.5)
            self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.3) for b in row4], lag_ratio=0.1), run_time=1)
            self.play(row4[0].sq.animate.set_fill(dim(BAD, 0.3)), Wiggle(row4[0]), run_time=1)
            self.play(Circumscribe(VGroup(boxes[7], boxes[14], row4[0]), color=BAD), run_time=1.2)
            self.play(LaggedStart(*[FadeIn(p, shift=LEFT * 0.3) for p in probs], lag_ratio=0.4), run_time=2)
        with self.doubt("Why did the pattern break\nafter calcium?"):
            r8 = VGroup(*[ebox(s, size=0.52) for s in ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]]).arrange(RIGHT, buff=0.04)
            p4 = ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"]
            r18 = VGroup(*[ebox(s, size=0.52, color=dim(D_COL, 0.4) if 2 <= i <= 11 else PANEL) for i, s in enumerate(p4)]).arrange(RIGHT, buff=0.04)
            r8.move_to(UP * 0.6).align_to(r18, LEFT)
            grp = VGroup(r8, r18).arrange(DOWN, buff=0.9, aligned_edge=LEFT).move_to(DOWN * 0.6)
            b8 = Brace(r8, UP, color=GOOD)
            l8 = B("repeats after 8", 30, GOOD).next_to(b8, UP, buff=0.1)
            mid = VGroup(*r18[2:12])
            b10 = Brace(mid, DOWN, color=D_COL)
            l10 = B("10 new elements squeeze in (transition metals)", 30, D_COL).next_to(b10, DOWN, buff=0.1)
            with self.say("Because after calcium, ten new elements squeeze in between: the transition metals, like iron, cobalt, nickel and copper. "
                          "So from there, the pattern repeats after 18, not 8. Newlands forced everything into eights, so it broke. "
                          "The modern table fixes this, as you'll see."):
                self.play(FadeIn(r8), GrowFromCenter(b8), FadeIn(l8), run_time=0.8)
                self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.2) for b in r18], lag_ratio=0.05), run_time=1.5)
                self.play(GrowFromCenter(b10), FadeIn(l10), run_time=0.8)
        self.clear_all()


# =====================================================================  4. MENDELEEV
class S04Mendeleev(Lesson):
    def construct(self):
        h = self.heading("1869 · Mendeleev's periodic table")
        random.seed(5)
        names = [("H", 1), ("Li", 7), ("Be", 9.4), ("B", 11), ("C", 12), ("N", 14), ("O", 16), ("F", 19),
                 ("Na", 23), ("Mg", 24), ("Al", 27), ("Si", 28), ("P", 31), ("S", 32), ("Cl", 35.5), ("K", 39)]
        cards = VGroup(*[ebox(s, bottom=f"{m:g}", size=0.95) for s, m in names])
        grid_pos = [[-3.3 + (i % 8) * 0.95 * 1.05, 0.8 - (i // 8) * 1.1, 0] for i in range(16)]
        for c in cards:
            c.ang = random.uniform(-0.8, 0.8)
            c.move_to([random.uniform(-6, 6), random.uniform(-2.4, 2.6), 0]).rotate(c.ang)
        with self.say("Then came Dmitri Mendeleev, in 1869. 63 elements were known by then. "
                      "He wrote each one on a card with its properties, and kept arranging them, like a game of patience."):
            self.play(FadeIn(h, shift=DOWN * 0.3), run_time=0.5)
            self.play(LaggedStart(*[FadeIn(c, scale=0.3) for c in cards], lag_ratio=0.08), run_time=2)
            self.play(LaggedStart(*[c.animate.rotate(-c.ang).move_to(p)
                                    for c, p in zip(cards, grid_pos)], lag_ratio=0.05), run_time=2.2)
        basis = VGroup(T("Basis:", 34, MUTED), B("atomic mass", 38, GOLD), T("+", 38),
                       B("chemical properties", 38, P_COL)).arrange(RIGHT, buff=0.25).shift(DOWN * 1.6)
        ex = T("(formulas of oxides and hydrides, e.g. Na₂O, MgO, Al₂O₃ · NaH, CH₄)", 28, MUTED
               ).next_to(basis, DOWN, buff=0.25)
        with self.say("He arranged them by atomic mass, and also checked their chemical properties, "
                      "especially the formulas of their oxides and hydrides. That means their compounds with oxygen and hydrogen."):
            self.play(FadeIn(basis, shift=UP * 0.3), run_time=1)
            self.play(FadeIn(ex), run_time=0.8)
        self.play(FadeOut(VGroup(cards, basis, ex)), run_time=0.5)

        law = VGroup(T("Mendeleev's periodic law", 34, GOLD),
                     B("Properties of elements are a periodic", 46),
                     B("function of their atomic masses.", 46)).arrange(DOWN, buff=0.25)
        box = SurroundingRectangle(law, buff=0.4, color=GOLD, corner_radius=0.15, stroke_width=5)
        per = T("periodic = repeating after regular intervals", 32, MUTED).next_to(box, DOWN, buff=0.4)
        with self.say("His law says: properties of elements are a periodic function of their atomic masses. "
                      "Periodic means, repeating after regular intervals. Learn this line exactly, word for word."):
            self.play(Create(box), Write(law), run_time=2.5)
            self.play(FadeIn(per), run_time=0.6)
            self.play(Circumscribe(law[1:], color=GOLD), run_time=1.2)
        self.play(FadeOut(VGroup(law, box, per)), run_time=0.5)

        # --- empty chairs
        heads = VGroup(B("Group III", 24, MUTED), B("Group IV", 24, MUTED)).arrange(RIGHT, buff=0.9)
        col3 = VGroup(ebox("B", bottom=11, size=1.2), ebox("Al", bottom=27, size=1.2))
        col4 = VGroup(ebox("C", bottom=12, size=1.2), ebox("Si", bottom=28, size=1.2))
        col3.arrange(DOWN, buff=0.15)
        col4.arrange(DOWN, buff=0.15)
        g1 = DashedVMobject(RoundedRectangle(corner_radius=0.12, width=1.2, height=1.2, color=GOLD, stroke_width=5), num_dashes=24)
        g2 = g1.copy()
        q1, q2 = B("?", 60, GOLD), B("?", 60, GOLD)
        cols = VGroup(VGroup(col3, g1), VGroup(col4, g2))
        for c, g in ((col3, g1), (col4, g2)):
            g.next_to(c, DOWN, buff=0.15)
        cols.arrange(RIGHT, buff=0.7).move_to(LEFT * 4.0 + DOWN * 0.3)
        heads[0].next_to(cols[0], UP, buff=0.3)
        heads[1].next_to(cols[1], UP, buff=0.3)
        q1.move_to(g1)
        q2.move_to(g2)
        with self.say("Now, his master stroke. Where no known element fitted, he did not force one in. "
                      "He left an empty chair, and said: someone will come and sit here one day."):
            self.play(FadeIn(heads), LaggedStart(*[FadeIn(b, shift=DOWN * 0.3) for b in [*col3, *col4]], lag_ratio=0.2), run_time=1.5)
            self.play(Create(g1), Create(g2), run_time=1)
            self.play(FadeIn(q1, scale=2), FadeIn(q2, scale=2), run_time=0.6)
            self.play(Indicate(VGroup(g1, q1, g2, q2), color=GOLD), run_time=1)
        eka = VGroup(*[VGroup(B(a, 36, GOLD), T("→", 36), B("?", 36, MUTED)).arrange(RIGHT, buff=0.3)
                       for a in ["eka-boron", "eka-aluminium", "eka-silicon"]]).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        eka.move_to(RIGHT * 3.2 + UP * 0.3)
        sk = T("eka = 'one' in Sanskrit", 30, MUTED).next_to(eka, DOWN, buff=0.5)
        with self.say("He even predicted their properties, and gave them names: eka-boron, eka-aluminium and eka-silicon. "
                      "Eka means one, in Sanskrit."):
            self.play(LaggedStart(*[FadeIn(e, shift=LEFT * 0.3) for e in eka], lag_ratio=0.4), run_time=2)
            self.play(FadeIn(sk), run_time=0.6)
        self.play(FadeOut(VGroup(eka, sk)), run_time=0.4)
        with self.doubt("How could he predict an element\nthat nobody had ever seen?"):
            al = ebox("Al", bottom=27, size=1.2)
            gp = DashedVMobject(RoundedRectangle(corner_radius=0.12, width=1.2, height=1.2, color=GOLD, stroke_width=5), num_dashes=24)
            gq = B("?", 56, GOLD)
            inn = ebox("In", bottom=115, size=1.2)
            colm = VGroup(al, gp, inn).arrange(DOWN, buff=0.15).move_to(LEFT * 3.6 + DOWN * 0.7)
            gq.move_to(gp)
            calc = VGroup(T("Neighbours above and below:", 32, MUTED), B("(27 + 115) \u00f7 2 = 71", 44),
                          B("Real gallium: 69.7", 44, GOOD)).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(RIGHT * 2.2 + DOWN * 0.7)
            with self.say("By looking at its neighbours! In the table, properties change step by step. "
                          "Aluminium is above the gap, indium is below it. So the missing element should be somewhere in between. "
                          "The average of 27 and 115 is 71. The real gallium: 69.7. So close! "
                          "That's Dobereiner's averaging idea, used like a pro."):
                self.play(FadeIn(al), FadeIn(inn), Create(gp), FadeIn(gq), run_time=1)
                self.wait(1.5)
                self.play(FadeIn(calc[0]), Indicate(al, color=GOLD), Indicate(inn, color=GOLD), run_time=1)
                self.wait(1)
                self.play(Write(calc[1]), run_time=1)
                self.wait(1)
                self.play(FadeIn(calc[2], shift=UP * 0.2), Flash(gp, color=GOOD, flash_radius=0.9), run_time=0.8)

        rows = [("", "Predicted", "Real Ga"), ("Atomic mass", "68", "69.7"), ("Density", "5.9", "5.94"),
                ("Oxide", "E₂O₃", "Ga₂O₃"), ("Chloride", "ECl₃", "GaCl₃")]
        tab = VGroup()
        for r, (a, b, c) in enumerate(rows):
            wt = BOLD if r == 0 else NORMAL
            row = VGroup(T(a, 32, MUTED, weight=wt), T(b, 34, GOLD, weight=wt), T(c, 34, GOOD, weight=wt))
            for i, m in enumerate(row):
                m.move_to([[-2.3, 0.2, 2.2][i], -r * 0.75, 0])
            tab.add(row)
        fit(tab, 6.2).move_to(RIGHT * 2.9 + DOWN * 0.2)
        ticks = VGroup(*[check(size=0.4).next_to(tab[r][2], RIGHT, buff=0.3) for r in range(1, 5)])
        with self.say("Years later, gallium was discovered. Compare his prediction with the real thing. "
                      "Atomic mass 68, real 69.7. Density 5.9, real 5.94. Oxide formula E2O3, real Ga2O3. "
                      "He nailed it! Scandium and germanium matched his predictions too.") as d:
            self.play(FadeIn(tab[0]), run_time=0.5)
            for r in range(1, 5):
                self.play(FadeIn(tab[r], shift=UP * 0.2), run_time=0.5)
                self.play(FadeIn(ticks[r - 1], scale=2), run_time=0.3)
                self.wait(d * 0.08)
            ga = ebox("Ga", bottom=69.7, size=1.2, stroke=GOOD).move_to(g1)
            ge = ebox("Ge", bottom=72.6, size=1.2, stroke=GOOD).move_to(g2)
            self.play(ReplacementTransform(VGroup(g1, q1), ga), ReplacementTransform(VGroup(g2, q2), ge), run_time=1)
            self.play(Flash(ga, color=GOOD, flash_radius=0.9), Flash(ge, color=GOOD, flash_radius=0.9), run_time=0.7)
        self.clear_all()

        # --- other merits
        h = self.heading("More wins for Mendeleev")
        be = ebox("Be", bottom="14.09", size=2.0).move_to(LEFT * 3.5 + UP * 0.3)
        be2 = ebox("Be", bottom="9.4", size=2.0, stroke=GOOD).move_to(be)
        cap1 = T("corrected atomic mass", 32, MUTED).next_to(be, DOWN, buff=0.35)
        nob = VGroup(*[ebox(s, size=0.85, stroke=GOLD) for s in ["He", "Ne", "Ar", "Kr", "Xe"]]).arrange(DOWN, buff=0.08)
        nob.move_to(RIGHT * 3.8 + DOWN * 0.15)
        stub = VGroup(*[ebox(s, size=0.85) for s in ["F", "Cl", "Br", "I"]]).arrange(DOWN, buff=0.08)
        stub.next_to(nob, LEFT, buff=0.15).align_to(nob, DOWN).shift(UP * 0.0)
        g0 = B("Group 0", 34, GOLD).next_to(nob, UP, buff=0.25)
        with self.say("He also corrected some wrong atomic masses. Beryllium was corrected from 14.09 to 9.4. "
                      "And when noble gases like helium, neon and argon were discovered later, "
                      "they simply joined as a new zero group. Nothing in the table broke."):
            self.play(FadeIn(h), FadeIn(be, scale=0.6), run_time=0.8)
            self.wait(1)
            self.play(ReplacementTransform(be, be2), FadeIn(cap1), run_time=1)
            self.wait(1.2)
            self.play(FadeIn(stub), run_time=0.6)
            nob.shift(RIGHT * 4)
            self.play(nob.animate.shift(LEFT * 4), run_time=1.2)
            self.play(FadeIn(g0, shift=DOWN * 0.2), run_time=0.5)
        self.clear_all()

        # --- cracks
        h = self.heading("But there were cracks", BAD)
        left = VGroup(*[ebox(s, size=0.9) for s in ["Li", "Na", "K"]]).arrange(DOWN, buff=0.08).move_to(LEFT * 4.6 + DOWN * 0.6)
        right = VGroup(*[ebox(s, size=0.9) for s in ["F", "Cl", "Br"]]).arrange(DOWN, buff=0.08).move_to(LEFT * 1.4 + DOWN * 0.6)
        hh = ebox("H", size=0.9, stroke=GOLD).next_to(left, UP, buff=0.1)
        q = B("?", 54, BAD).move_to((left.get_top() + right.get_top()) / 2 + UP * 0.9)
        t1 = T("Hydrogen: like alkali metals AND like halogens", 30).to_edge(DOWN, buff=1.4).shift(LEFT * 2.6)
        with self.say("But his table had a few cracks. Where does hydrogen go? "
                      "In some ways it behaves like the alkali metals, and in other ways, like the halogens."):
            self.play(FadeIn(h), FadeIn(left), FadeIn(right), FadeIn(hh), run_time=0.8)
            for _ in range(2):
                self.play(hh.animate.next_to(right, UP, buff=0.1), run_time=0.7)
                self.play(hh.animate.next_to(left, UP, buff=0.1), run_time=0.7)
            self.play(FadeIn(q, scale=2), FadeIn(t1), run_time=0.6)

        seat = DashedVMobject(RoundedRectangle(corner_radius=0.1, width=1.1, height=1.1, color=MUTED), num_dashes=20)
        seat.move_to(RIGHT * 3.6 + DOWN * 0.3)
        i1 = ebox("Cl-35", size=1.1, fs=26).move_to(RIGHT * 2.0 + UP * 1.3)
        i2 = ebox("Cl-37", size=1.1, fs=26).move_to(RIGHT * 5.2 + UP * 1.3)
        t2 = T("Isotopes: same element, different masses", 30).next_to(seat, DOWN, buff=0.5)
        with self.say("Isotopes, like chlorine 35 and chlorine 37. Same element, but different atomic masses. "
                      "In a table based on mass, which seat do they take?"):
            self.play(Create(seat), FadeIn(i1), FadeIn(i2), run_time=0.8)
            self.play(i1.animate.move_to(seat.get_center() + LEFT * 0.3), i2.animate.move_to(seat.get_center() + RIGHT * 0.3), run_time=0.8)
            self.play(i1.animate.shift(LEFT * 0.9), i2.animate.shift(RIGHT * 0.9), run_time=0.5, rate_func=rush_from)
            self.play(FadeIn(t2), run_time=0.5)
        self.clear_all()

        h = self.heading("Crack 3: heavier before lighter", BAD)
        co = ebox("Co", bottom=58.9, size=1.8).move_to(LEFT * 1.4 + UP * 0.2)
        ni = ebox("Ni", bottom=58.7, size=1.8).move_to(RIGHT * 1.4 + UP * 0.2)
        sign = B(">", 70, BAD).move_to(UP * 0.2)
        t3 = T("Mendeleev placed cobalt (58.9) BEFORE nickel (58.7)", 34).next_to(VGroup(co, ni), DOWN, buff=0.6)
        t4 = T("...breaking his own rule of increasing atomic mass", 32, BAD).next_to(t3, DOWN, buff=0.25)
        with self.say("And cobalt, with atomic mass 58.9, was placed before nickel, 58.7. Heavier before lighter. "
                      "That breaks his own rule! Also, atomic masses don't increase in a regular way, "
                      "so nobody could say how many elements might exist between two elements."):
            self.play(FadeIn(h), FadeIn(co, shift=RIGHT), FadeIn(ni, shift=LEFT), run_time=0.8)
            self.play(FadeIn(sign, scale=2), run_time=0.4)
            self.play(Write(t3), run_time=1.2)
            self.play(FadeIn(t4), Wiggle(VGroup(co, ni)), run_time=1)
        with self.doubt("If his rule was atomic mass,\nwhy did he put cobalt first?"):
            co2 = ebox("Co", size=1.4).move_to(LEFT * 3.2 + DOWN * 0.1)
            ni2 = ebox("Ni", size=1.4).move_to(LEFT * 3.2 + DOWN * 1.8)
            lk1 = VGroup(T("behaves like", 30, MUTED), B("Rh, Ir", 40, GOOD)).arrange(RIGHT, buff=0.3).next_to(co2, RIGHT, buff=1.2)
            lk2 = VGroup(T("behaves like", 30, MUTED), B("Pd, Pt", 40, GOOD)).arrange(RIGHT, buff=0.3).next_to(ni2, RIGHT, buff=1.2)
            ar1 = Arrow(co2.get_right(), lk1.get_left(), color=GOOD, buff=0.15)
            ar2 = Arrow(ni2.get_right(), lk2.get_left(), color=GOOD, buff=0.15)
            moral = B("He trusted PROPERTIES more than mass", 36, GOLD).move_to(DOWN * 2.3)
            with self.say("Because he trusted properties more than mass. Cobalt behaves like rhodium and iridium, "
                          "and nickel behaves like palladium and platinum. So he placed them by their behaviour. "
                          "He was right! He just couldn't explain why. That answer came later, from Moseley."):
                self.play(FadeIn(co2), FadeIn(ni2), run_time=0.6)
                self.wait(0.8)
                self.play(GrowArrow(ar1), FadeIn(lk1), run_time=0.8)
                self.play(GrowArrow(ar2), FadeIn(lk2), run_time=0.8)
                self.wait(1)
                self.play(Write(moral), run_time=1)
        self.clear_all()


# =====================================================================  5. MOSELEY
class S05Moseley(Lesson):
    def construct(self):
        h = self.heading("1913 · Moseley's big fix")
        with self.say("In 1913, a young English scientist, Henry Moseley, fixed all of this with one simple idea."):
            self.play(FadeIn(h, shift=DOWN * 0.3), run_time=0.6)
            idea = B("Use atomic number, not atomic mass.", 52, GOLD)
            self.play(Write(idea), run_time=1.5)
        self.play(FadeOut(idea), run_time=0.4)

        kids = [("Riya", 42, 3, S_COL), ("Aman", 47, 1, D_COL), ("Sara", 41.5, 4, P_COL), ("Om", 42, 2, F_COL)]
        groups = VGroup()
        for n, kg, roll, c in kids:
            s = student(c, 1.2)
            lab = VGroup(B(n, 30), T(f"{kg:g} kg", 26, MUTED), T(f"Roll {roll}", 26, GOLD)).arrange(DOWN, buff=0.08)
            lab.next_to(s, DOWN, buff=0.15)
            groups.add(VGroup(s, lab))
        groups.arrange(RIGHT, buff=1.0).shift(DOWN * 0.1)
        by_w = T("Sort the class by WEIGHT?", 38, BAD).next_to(groups, UP, buff=0.5)
        with self.say("Imagine your teacher arranging the class by weight. Two students weigh 42 kilos each. "
                      "Who comes first? Confusing, right?"):
            self.play(LaggedStart(*[FadeIn(g, shift=UP * 0.3) for g in groups], lag_ratio=0.2), run_time=1.5)
            self.play(FadeIn(by_w), run_time=0.5)
            order = sorted(range(4), key=lambda i: kids[i][1])
            xs = sorted([g.get_x() for g in groups])
            self.play(*[groups[i].animate(path_arc=PI / 2).set_x(xs[k]) for k, i in enumerate(order)], run_time=1.4)
            self.play(Wiggle(VGroup(groups[0], groups[3])), run_time=1)
        by_r = T("Sort by ROLL NUMBER: always clear!", 38, GOOD).move_to(by_w)
        with self.say("Now arrange by roll number. 1, 2, 3, 4. Always clear, never confusing. "
                      "For elements, the roll number is the atomic number."):
            order = sorted(range(4), key=lambda i: kids[i][2])
            xs = sorted([g.get_x() for g in groups])
            self.play(ReplacementTransform(by_w, by_r), *[groups[i].animate(path_arc=PI / 2).set_x(xs[k]) for k, i in enumerate(order)], run_time=1.5)
            self.play(*[Indicate(g[1][2], color=GOLD) for g in groups], run_time=1)
        self.play(FadeOut(VGroup(groups, by_r)), run_time=0.5)

        co = ebox("Co", top=27, bottom=58.9, size=1.8)
        ni = ebox("Ni", top=28, bottom=58.7, size=1.8)
        pair = VGroup(co, ni).arrange(RIGHT, buff=0.5).move_to(LEFT * 3.2 + DOWN * 0.1)
        zs = VGroup(B("Z = 27", 34, GOOD).next_to(co, DOWN, buff=0.25), B("Z = 28", 34, GOOD).next_to(ni, DOWN, buff=0.25))
        seat = RoundedRectangle(corner_radius=0.1, width=1.5, height=1.5, color=GOOD, stroke_width=5).move_to(RIGHT * 3.6 + DOWN * 0.1)
        c35 = ebox("Cl-35", size=1.2, fs=26).move_to(RIGHT * 2.2 + UP * 1.6)
        c37 = ebox("Cl-37", size=1.2, fs=26).move_to(RIGHT * 5.0 + UP * 1.6)
        z17 = B("both Z = 17", 32, GOOD).next_to(seat, DOWN, buff=0.35)
        with self.say("Cobalt's roll number is 27, nickel's is 28. So cobalt comes first, naturally. No rule broken. "
                      "And isotopes? Chlorine 35 and chlorine 37 both have roll number 17. So they share the same seat. Problem solved!"):
            self.play(FadeIn(pair, shift=UP * 0.3), run_time=0.8)
            self.play(Write(zs), Flash(co, color=GOOD, flash_radius=1.3), run_time=1)
            self.wait(1.5)
            self.play(Create(seat), FadeIn(c35), FadeIn(c37), run_time=0.8)
            self.play(c35.animate.move_to(seat).scale(0.95), c37.animate.move_to(seat).scale(0.95), run_time=1)
            self.play(FadeIn(z17), Flash(seat, color=GOOD, flash_radius=1.0), run_time=0.7)
        self.play(FadeOut(VGroup(pair, zs, seat, c35, c37, z17)), run_time=0.5)
        with self.doubt("But why is atomic number better than mass?\nThey both go up together anyway."):
            cols = VGroup()
            for name, n in (("Cl-35", 18), ("Cl-37", 20)):
                nuc = VGroup(Circle(radius=0.75, fill_color=NUCLEUS, fill_opacity=1, stroke_width=0),
                             B(f"17 p\n{n} n", 30, BG))
                cols.add(VGroup(B(name, 38), nuc, T("electrons: 2, 8, 7", 30, GOLD)).arrange(DOWN, buff=0.3))
            cols.arrange(RIGHT, buff=2.2).move_to(LEFT * 1.6 + DOWN * 0.35)
            same = VGroup(B("same electrons", 36, GOOD), B("= same chemistry", 36, GOOD)).arrange(DOWN, buff=0.15).move_to(RIGHT * 4.3 + DOWN * 0.6)
            notes = T("Neutrons add mass but do nothing in chemistry", 32, MUTED).move_to(DOWN * 2.3)
            with self.say("Here's the deep reason. Chemistry is done by electrons. "
                          "And the number of electrons equals the number of protons, the atomic number. "
                          "Neutrons only add mass. They don't change the electrons at all. "
                          "So mass carries extra noise from neutrons, but atomic number tells exactly how an element will behave."):
                self.play(FadeIn(cols[0][:2]), FadeIn(cols[1][:2]), run_time=0.8)
                self.wait(1.5)
                self.play(FadeIn(cols[0][2]), FadeIn(cols[1][2]), run_time=0.7)
                self.wait(1)
                self.play(FadeIn(same, shift=LEFT * 0.2), run_time=0.7)
                self.wait(1)
                self.play(FadeIn(notes), run_time=0.7)

        old = Text("Properties of elements are a periodic function of their atomic masses.", font=FONT,
                   font_size=38, weight=BOLD, color=INK, t2c={"masses": BAD}).scale_to_fit_width(12.6)
        new = Text("Properties of elements are a periodic function of their atomic numbers.", font=FONT,
                   font_size=38, weight=BOLD, color=INK, t2c={"numbers": GOOD}).scale_to_fit_width(12.6)
        lab_old = T("Mendeleev's law", 32, MUTED).next_to(old, UP, buff=0.4)
        lab_new = B("Modern periodic law", 36, GOOD).move_to(lab_old)
        with self.say("So the law changed by just one word. Properties of elements are a periodic function of their atomic numbers. "
                      "Mass became number. That's the modern periodic law."):
            self.play(FadeIn(lab_old), Write(old), run_time=1.5)
            self.wait(0.6)
            self.play(TransformMatchingShapes(old, new), ReplacementTransform(lab_old, lab_new), run_time=1.5)
            box = SurroundingRectangle(VGroup(new, lab_new), buff=0.35, color=GOOD, corner_radius=0.15, stroke_width=5)
            self.play(Create(box), run_time=0.8)
        self.wait(0.5)
        self.clear_all()


# =====================================================================  6. MODERN TABLE
SHORT = {1: (1, 1), 2: (1, 8)}
for _z in range(3, 11):
    SHORT[_z] = (2, _z - 2)
for _z in range(11, 19):
    SHORT[_z] = (3, _z - 10)
SHORT[19] = (4, 1)


def config_of(z):
    out, left = [], z
    for cap in (2, 8, 8, 2):
        if left <= 0:
            break
        out.append(min(cap, left))
        left -= cap
    return out


class S06Modern(Lesson):
    def construct(self):
        h = self.heading("The modern periodic table builds itself")
        cw, chh = 1.35, 1.12
        x0, y0 = -4.75, 2.1

        def spot(r, c):
            return np.array([x0 + (c - 1) * cw, y0 - (r - 1) * chh, 0])

        cells = {}
        for z, (r, c) in SHORT.items():
            cfg = ", ".join(map(str, config_of(z)))
            b = ebox(SYMBOLS[z - 1], top=z, bottom=cfg, size=1.05, fs=34)
            b.move_to(spot(r, c))
            cells[z] = b
        plabs = VGroup(*[T(f"Period {r}", 26, MUTED).next_to(spot(r, 1), LEFT, buff=0.75) for r in (1, 2, 3)])
        with self.say("Now watch the modern periodic table build itself, using only our three basics. "
                      "Hydrogen has 1 electron, helium has 2. Both use just one floor, so they make period 1."):
            self.play(FadeIn(h, shift=DOWN * 0.3), run_time=0.5)
            self.wait(2)
            self.play(FadeIn(cells[1], scale=0.5), FadeIn(cells[2], scale=0.5), FadeIn(plabs[0]), run_time=1)
        with self.say("Lithium to neon need two floors. That's period 2. Sodium to argon need three floors: period 3. "
                      "So the period number is simply the number of floors!") as d:
            self.play(LaggedStart(*[FadeIn(cells[z], shift=RIGHT * 0.3) for z in range(3, 11)], lag_ratio=0.15),
                      FadeIn(plabs[1]), run_time=2)
            self.play(LaggedStart(*[FadeIn(cells[z], shift=RIGHT * 0.3) for z in range(11, 19)], lag_ratio=0.15),
                      FadeIn(plabs[2]), run_time=2)
            rule = B("Period number = number of shells", 36, GOLD).to_edge(DOWN, buff=1.25)
            self.play(Write(rule), run_time=1)
        k = cells[19]
        col = VGroup(cells[3], cells[11], k)
        with self.say("Now look down a column. Lithium 2, 1. Sodium 2, 8, 1. Potassium 2, 8, 8, 1. "
                      "All have one top-floor electron. Same valence electrons, same group, similar behaviour."):
            self.play(FadeOut(rule), FadeIn(k, shift=DOWN * 0.3), run_time=0.7)
            self.play(*[b.sq.animate.set_stroke(GOLD, 6) for b in col], run_time=0.8)
            self.play(Circumscribe(col, color=GOLD, buff=0.08), run_time=1.5)
            g = B("Same group = same valence electrons", 36, GOLD).to_edge(DOWN, buff=1.25)
            self.play(Write(g), run_time=1)
        with self.doubt("Wait! The M shell can hold 18.\nSo why is potassium 2, 8, 8, 1 and not 2, 8, 9?"):
            wrong = VGroup(B("2, 8, 9", 60, MUTED), cross(size=0.8)).arrange(RIGHT, buff=0.4)
            right = VGroup(B("2, 8, 8, 1", 60, GOOD), check(size=0.8)).arrange(RIGHT, buff=0.4)
            VGroup(wrong, right).arrange(RIGHT, buff=1.6).move_to(DOWN * 0.3)
            rt = B("The OUTERMOST shell can't hold more than 8 electrons", 34, GOLD)
            rule = VGroup(card(rt.width + 0.8, 1.1, stroke=GOLD, sw=4), rt)
            rt.move_to(rule[0])
            rule.move_to(DOWN * 2.0)
            with self.say("Brilliant doubt! There's one more rule: the outermost shell cannot hold more than 8 electrons. "
                          "So once the M shell has 8, the next electron moves up to the N shell. "
                          "That's why potassium starts a new period: period 4."):
                self.play(FadeIn(wrong), run_time=0.6)
                self.wait(1.5)
                self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.8)
                self.wait(1.5)
                self.play(FadeIn(right, shift=LEFT * 0.2), run_time=0.8)
        clb = cells[17]
        with self.say("Quick trick, for chlorine, 2, 8, 7. Three floors, so period 3. "
                      "Seven valence electrons, plus 10, gives group 17. "
                      "For groups 1 and 2, the group number is just the number of valence electrons."):
            self.play(FadeOut(g), *[b.sq.animate.set_stroke(LINE, 2) for b in col], run_time=0.5)
            self.play(clb.animate.scale(1.25), clb.sq.animate.set_stroke(P_COL, 7), run_time=0.6)
            t1 = B("3 shells → Period 3", 34, GOLD)
            t2 = B("7 valence e⁻ + 10 → Group 17", 34, GOLD)
            VGroup(t1, t2).arrange(RIGHT, buff=0.8).to_edge(DOWN, buff=1.25)
            self.play(FadeIn(t1, shift=UP * 0.2), run_time=0.6)
            self.wait(1.2)
            self.play(FadeIn(t2, shift=UP * 0.2), run_time=0.6)
        with self.doubt("Helium has 2 valence electrons.\nWhy is it in group 18, not group 2?"):
            he = Atom("He", [2], r0=0.45, step=0.6).move_to(LEFT * 4 + DOWN * 0.6)
            pts = VGroup(B("Its only shell (K) holds 2 \u2192 FULL", 36),
                         B("Full outer shell = noble gas, like Ne, Ar", 36, GOOD),
                         T("Groups are about behaviour", 32, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(RIGHT * 1.6 + DOWN * 0.6)
            with self.say("Because helium's only shell, K, can hold just 2. So it's already full. "
                          "All group 18 elements have a full outer shell, and none of them react. "
                          "Helium behaves exactly like them, so it belongs in group 18. Groups are really about behaviour."):
                self.play(FadeIn(he, scale=0.6), run_time=0.8)
                for p_ in pts:
                    self.play(FadeIn(p_, shift=LEFT * 0.2), run_time=0.6)
                    self.wait(1.2)
            self.play(FadeOut(VGroup(he, pts)), run_time=0.4)
            hh = ebox("H", top=1, bottom="1", size=1.5).move_to(LEFT * 4 + DOWN * 0.6)
            hp = VGroup(B("1 valence electron \u2192 placed in group 1", 36),
                        B("but it's a non-metal gas!", 36, BAD),
                        T("so hydrogen's position is still special", 32, MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(RIGHT * 1.6 + DOWN * 0.6)
            with self.say("And hydrogen? It has 1 valence electron, so it's placed in group 1. "
                          "But it's a non-metal gas, not a metal. That's why hydrogen's position is still a special case."):
                self.play(FadeIn(hh, scale=0.6), run_time=0.6)
                for p_ in hp:
                    self.play(FadeIn(p_, shift=LEFT * 0.2), run_time=0.6)
                    self.wait(0.8)
        self.play(FadeOut(VGroup(t1, t2, plabs)), clb.animate.scale(1 / 1.25), run_time=0.5)

        pt = PeriodicTable(cell=0.58, center=UP * 0.3)
        fz = [z for z in pt.boxes if POS[z][0] >= 8]
        main = [z for z in pt.boxes if POS[z][0] < 8 and z > 19]
        ph = VGroup()
        for r, s in ((6, "57-71"), (7, "89-103")):
            p = ebox("", size=0.54).move_to(pt.point(r, 3))
            p.add(T(s, 13, MUTED).move_to(p))
            ph.add(p)
        with self.say("Keep going, and you get the full table: 7 periods, and 18 groups."):
            self.play(FadeOut(h), *[ReplacementTransform(cells[z], pt.boxes[z]) for z in range(1, 20)], run_time=1.5)
            self.play(LaggedStart(*[FadeIn(pt.boxes[z], scale=0.5) for z in main], lag_ratio=0.02), FadeIn(ph), run_time=2.5)
            gl = VGroup(*[T(str(c), 18, MUTED).move_to(pt.point(1, c) + UP * 0.45) for c in range(1, 19)])
            plb = VGroup(*[T(str(r), 22, MUTED).move_to(pt.point(r, 1) + LEFT * 0.5) for r in range(1, 8)])
            self.play(FadeIn(gl), FadeIn(plb), run_time=0.6)

        def paint(block):
            return [pt.boxes[z].sq.animate.set_fill(dim(BLOCK_COL[block], 0.4))
                    for z in pt.boxes if block_of(z) == block and z not in fz]
        legend = VGroup()
        with self.say("It has four blocks. Groups 1 and 2 are the s-block. Groups 13 to 18 are the p-block. "
                      "And groups 3 to 12 in the middle are the d-block, the transition elements.") as d:
            for blk, name in (("s", "s-block"), ("p", "p-block"), ("d", "d-block")):
                self.play(*paint(blk), run_time=0.8)
                item = VGroup(Square(0.3, fill_color=BLOCK_COL[blk], fill_opacity=1, stroke_width=0), T(name, 26))
                item.arrange(RIGHT, buff=0.15)
                legend.add(item)
                legend.arrange(RIGHT, buff=0.5).move_to(UP * 3.6)
                self.add(item)
                self.wait(d * 0.15)
        with self.doubt("Why does the table suddenly get\nwider from period 4?"):
            mini = PeriodicTable(cell=0.42, center=DOWN * 0.55, numbers=False)
            for z in mini.boxes:
                if block_of(z) == "d" and POS[z][0] < 8:
                    mini.boxes[z].sq.set_fill(dim(D_COL, 0.4))
            mini.remove(*[mini.boxes[z] for z in fz])
            dgrp = VGroup(*[mini.boxes[z] for z in mini.boxes if block_of(z) == "d" and POS[z][0] < 8])
            br = Brace(dgrp, DOWN, color=D_COL)
            bl = B("10 extra elements per period", 28, D_COL).next_to(br, DOWN, buff=0.1)
            with self.say("From period 4, ten extra elements, the d-block, fit in between group 2 and group 13. "
                          "That's the same reason Newlands' octaves broke! "
                          "These elements put their new electrons into an inner shell, not the outer one. "
                          "So their outer shells look alike, and that's why transition metals are so similar to each other."):
                self.play(FadeIn(mini), run_time=1)
                self.play(Circumscribe(dgrp, color=D_COL), GrowFromCenter(br), FadeIn(bl), run_time=1.5)
        for z in fz:
            pt.boxes[z].sq.set_fill(dim(F_COL, 0.4))
        with self.say("The f-block, the lanthanides and actinides, is pulled out and kept at the bottom, "
                      "just so the table doesn't become too wide."):
            starts = [ph[0].get_center() if POS[z][0] == 8 else ph[1].get_center() for z in fz]
            targets = [pt.boxes[z].get_center() for z in fz]
            for z, s in zip(fz, starts):
                pt.boxes[z].move_to(s).scale(0.2)
            self.add(*[pt.boxes[z] for z in fz])
            self.play(LaggedStart(*[pt.boxes[z].animate.scale(5).move_to(t) for z, t in zip(fz, targets)],
                                  lag_ratio=0.04), run_time=2.5)
            item = VGroup(Square(0.3, fill_color=F_COL, fill_opacity=1, stroke_width=0), T("f-block", 26)).arrange(RIGHT, buff=0.15)
            old = legend.copy()
            legend.add(item)
            legend.arrange(RIGHT, buff=0.5).move_to(UP * 3.6)
            self.play(*[Transform(o, n) for o, n in zip(old, legend[:-1])], FadeIn(item), run_time=0.6)
            self.remove(*old)
            self.add(legend)

        stair = pt.staircase(GOLD, 8)
        met = VGroup(*[pt.boxes[z] for z in pt.boxes if SYMBOLS[z - 1] in METALLOIDS])
        ml = B("Metals", 34, S_COL).move_to(pt.point(2, 6) + DOWN * 0.1)
        nl = B("Non-metals", 28, P_COL).move_to(pt.point(1, 15) + UP * 0.05)
        with self.say("And this zig-zag line separates metals on the left from non-metals on the right. "
                      "The metalloids sit right along the line. And see? Most elements are metals."):
            self.play(Create(stair), run_time=1.5)
            self.play(*[b.sq.animate.set_stroke(GOLD, 5) for b in met], run_time=0.8)
            self.play(FadeIn(ml, shift=RIGHT * 0.2), FadeIn(nl, shift=LEFT * 0.2), run_time=0.8)
        counts = VGroup(*[B(str(n), 26, GOLD).move_to(pt.point(r, 18) + RIGHT * 0.65)
                          for r, n in zip(range(1, 8), [2, 8, 8, 18, 18, 32, 32])])
        with self.say("And the number of elements in each period: 2, 8, 8, 18, 18, 32, 32."):
            self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.2) for c in counts], lag_ratio=0.4), run_time=3)
        self.wait(0.5)
        self.clear_all()


# =====================================================================  7. TRENDS
class S07Trends(Lesson):
    def construct(self):
        h = self.heading("Trends: just TWO reasons")
        r1 = VGroup(card(5.8, 2.6, stroke=GOLD, sw=4))
        r1.add(VGroup(B("Reason 1 →", 40, GOLD), T("Across a period:", 32, MUTED),
                      B("same floors, more protons", 34)).arrange(DOWN, buff=0.2).scale_to_fit_width(5.2).move_to(r1[0]))
        r2 = VGroup(card(5.8, 2.6, stroke=P_COL, sw=4))
        r2.add(VGroup(B("Reason 2 ↓", 40, P_COL), T("Down a group:", 32, MUTED),
                      B("a new floor is added", 34)).arrange(DOWN, buff=0.2).move_to(r2[0]))
        VGroup(r1, r2).arrange(RIGHT, buff=0.6).shift(DOWN * 0.2)
        with self.say("Now the trends. Many students try to memorise lots of arrows, and then forget them in the exam. "
                      "Don't. You only need two reasons."):
            self.play(FadeIn(h, shift=DOWN * 0.3), run_time=0.6)
            self.wait(2.5)
            self.play(FadeIn(r1, shift=UP * 0.3), run_time=0.8)
            self.play(FadeIn(r2, shift=UP * 0.3), run_time=0.8)
        self.play(FadeOut(VGroup(r1, r2)), run_time=0.5)

        # --- across: shrink
        data = [("Li", 3, 152), ("Be", 4, 111), ("B", 5, 88), ("C", 6, 77), ("N", 7, 74), ("O", 8, 66)]

        def atom_for(sym, z, pm):
            k = pm / 152
            a = Atom(sym, config_of(z), r0=0.42, step=0.75 * k + 0.05)
            return a.move_to(LEFT * 3.3 + DOWN * 0.1)

        cur = atom_for(*data[0])
        info = VGroup(B("Li", 48), T("protons: +3", 34, NUCLEUS), B("152 pm", 44, GOLD)).arrange(DOWN, buff=0.3)
        info.move_to(RIGHT * 2.0 + UP * 0.4)
        row = VGroup()
        with self.say("Reason one. Across a period, the floors stay the same, but the nucleus gets more and more protons. "
                      "So it pulls harder, the electrons come closer, and the atom shrinks. "
                      "Lithium is 152 picometres. Oxygen is only 66.") as d:
            self.play(FadeIn(cur, scale=0.6), FadeIn(info), run_time=0.8)
            for sym, z, pm in data[1:]:
                nxt = atom_for(sym, z, pm)
                ni = VGroup(B(sym, 48), T(f"protons: +{z}", 34, NUCLEUS), B(f"{pm} pm", 44, GOLD)).arrange(DOWN, buff=0.3).move_to(info)
                self.play(ReplacementTransform(cur, nxt), ReplacementTransform(info, ni), run_time=0.9)
                cur, info = nxt, ni
                self.wait(max(0.1, d * 0.06))
            dots = VGroup(*[VGroup(Circle(radius=pm / 152 * 0.4, fill_color=D_COL, fill_opacity=0.6, stroke_color=D_COL),
                                   T(s, 22)) for s, _, pm in data])
            for c in dots:
                c[1].move_to(c[0])
            dots.arrange(RIGHT, buff=0.3).move_to(RIGHT * 2.4 + DOWN * 1.9)
            self.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in dots], lag_ratio=0.15), run_time=1.2)
            arr = Arrow(dots.get_left() + DOWN * 0.6, dots.get_right() + DOWN * 0.6, color=GOLD, buff=0, stroke_width=5)
            tx = T("radius DECREASES", 28, GOLD).next_to(arr, DOWN, buff=0.1)
            self.play(GrowArrow(arr), FadeIn(tx), run_time=0.7)
        with self.doubt("More protons AND more electrons...\nshouldn't the atom get BIGGER?"):
            def ring(z, r):
                g = VGroup(Circle(radius=r, stroke_color=GOLD, stroke_width=4),
                           Circle(radius=0.38, fill_color=NUCLEUS, fill_opacity=1, stroke_width=0), B(f"+{z}", 28, BG))
                for k in range(4):
                    a_ = TAU * k / 4 + PI / 4
                    g.add(Arrow(np.array([np.cos(a_), np.sin(a_), 0]) * (r - 0.05), np.array([np.cos(a_), np.sin(a_), 0]) * 0.55,
                                color=NUCLEUS, buff=0, stroke_width=2 + z * 0.9, max_tip_length_to_length_ratio=0.2))
                return g
            left_ = ring(3, 1.6).move_to(LEFT * 3.2 + DOWN * 0.7)
            right_ = ring(8, 1.0).move_to(RIGHT * 1.0 + DOWN * 0.7)
            lab = VGroup(B("same floor", 34, GOLD), B("stronger pull", 34, NUCLEUS), B("\u2192 smaller atom", 34, GOOD)
                         ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(RIGHT * 4.7 + DOWN * 0.7)
            with self.say("It feels like it, right? But the new electrons go to the same floor. No new floor is added. "
                          "Meanwhile, the nucleus gets stronger with every proton, and pulls that whole floor inward. "
                          "Same floor, stronger pull: smaller atom."):
                self.play(FadeIn(left_), run_time=0.8)
                self.wait(2)
                self.play(TransformFromCopy(left_, right_), run_time=1.5)
                self.play(LaggedStart(*[FadeIn(l_, shift=LEFT * 0.2) for l_ in lab], lag_ratio=0.5), run_time=1.5)
        self.play(FadeOut(VGroup(cur, info, dots, arr, tx)), run_time=0.5)

        # --- down: grow
        gdata = [("Li", [2, 1], 152), ("Na", [2, 8, 1], 186), ("K", [2, 8, 8, 1], 231)]
        atoms = VGroup(*[Atom(s, sh, r0=0.3, step=0.3, e_radius=0.06) for s, sh, _ in gdata]).arrange(RIGHT, buff=0.8)
        atoms.move_to(LEFT * 2.0 + UP * 0.25)
        pms = VGroup(*[B(f"{pm} pm", 34, GOLD).next_to(a, DOWN, buff=0.25) for a, (_, _, pm) in zip(atoms, gdata)])
        for p in pms:
            p.set_y(atoms.get_bottom()[1] - 0.4)
        extra = VGroup(*[VGroup(Circle(radius=pm / 262 * 0.95, fill_color=S_COL, fill_opacity=0.35, stroke_color=S_COL),
                                B(s, 30)) for s, pm in [("Rb", 244), ("Cs", 262)]])
        for e in extra:
            e[1].move_to(e[0])
        extra.arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.1)
        epm = VGroup(T("244 pm", 26, GOLD).next_to(extra[0], LEFT, buff=0.15), T("262 pm", 26, GOLD).next_to(extra[1], LEFT, buff=0.15))
        unit = T("1 picometre (pm) = 10⁻¹² m", 30, MUTED).to_edge(DOWN, buff=1.25)
        with self.say("Reason two. Down a group, a new floor is added each time, so the atom gets bigger. "
                      "Lithium 152, sodium 186, potassium 231 picometres. "
                      "And one picometre is ten to the power minus twelve metre. Super tiny!"):
            for a, p in zip(atoms, pms):
                self.play(FadeIn(a, scale=0.5), FadeIn(p), run_time=0.8)
                self.wait(0.4)
            self.play(FadeIn(extra, shift=LEFT * 0.3), FadeIn(epm), run_time=0.8)
            self.play(FadeIn(unit), run_time=0.6)
        with self.doubt("But protons increase down a group too!\nSo why does the atom grow there?"):
            k_ = Atom("K", [2, 8, 8, 1], r0=0.33, step=0.38, e_radius=0.06).move_to(LEFT * 4.5 + DOWN * 0.75)
            crowd = Annulus(inner_radius=0.34, outer_radius=0.33 + 0.38 * 3 + 0.1, fill_color=ELECTRON, fill_opacity=0.25, stroke_width=0).move_to(k_.nucleus)
            pts = VGroup(B("1. A whole new floor, far out", 34),
                         B("2. Inner electrons block the pull", 34, ELECTRON),
                         T("(like a crowd between you and the stage)", 30, MUTED),
                         B("\u2192 weak pull on the outer electron \u2192 bigger atom", 32, GOOD)
                         ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            fit(pts, 7.6).next_to(k_, RIGHT, buff=0.5)
            with self.say("Because the new floor wins. Each new floor sits much farther out. "
                          "And the inner floors of electrons stand in between, blocking part of the nucleus's pull, "
                          "like a crowd between you and the stage. "
                          "So the outer electron feels only a weak pull, and the atom gets bigger."):
                self.play(FadeIn(k_), run_time=0.8)
                self.play(FadeIn(pts[0]), Indicate(k_.orbits[3], color=GOLD), run_time=1)
                self.wait(1)
                self.play(FadeIn(crowd), FadeIn(pts[1]), run_time=0.8)
                self.play(FadeIn(pts[2]), run_time=0.6)
                self.wait(1.5)
                self.play(FadeIn(pts[3], shift=UP * 0.2), run_time=0.8)
        self.play(FadeOut(VGroup(atoms, pms, extra, epm, unit)), run_time=0.5)

        # --- metallic character
        mdef = fit(VGroup(B("Metallic character", 40, S_COL), T("= how easily an atom GIVES AWAY electrons", 34)).arrange(RIGHT, buff=0.3), 12.8)
        mdef.next_to(h, DOWN, buff=0.4)
        p3 = [("Na", S_COL), ("Mg", S_COL), ("Al", S_COL), ("Si", GOLD), ("P", P_COL), ("S", P_COL), ("Cl", P_COL)]
        prow = VGroup(*[ebox(s, size=1.0, stroke=c, txt=c) for s, c in p3]).arrange(RIGHT, buff=0.1).move_to(LEFT * 2.2 + UP * 0.6)
        tags = VGroup(T("metals", 26, S_COL).next_to(prow[0:3], DOWN, buff=0.15),
                      T("metalloid", 26, GOLD).next_to(prow[3], DOWN, buff=0.15),
                      T("non-metals", 26, P_COL).next_to(prow[4:], DOWN, buff=0.15))
        a1 = Arrow(prow.get_left() + DOWN * 1.05, prow.get_right() + DOWN * 1.05, color=BAD, buff=0, stroke_width=6)
        a1t = B("metallic character decreases", 28, BAD).next_to(a1, DOWN, buff=0.1)
        with self.say("Now, metallic character. It simply means: how easily an atom gives away electrons. "
                      "Across a period, the nucleus holds tighter, so giving away gets harder. Metallic character decreases. "
                      "Sodium and magnesium are metals, silicon is a metalloid, and phosphorus, sulphur and chlorine are non-metals."):
            self.play(FadeIn(mdef), run_time=0.8)
            self.wait(2)
            self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.2) for b in prow], lag_ratio=0.12), run_time=1.5)
            self.play(GrowArrow(a1), FadeIn(a1t), run_time=0.8)
            self.wait(1)
            self.play(FadeIn(tags), run_time=0.8)
        gcol = VGroup(*[ebox(s, size=0.64, stroke=S_COL, txt=S_COL) for s in ["Li", "Na", "K", "Rb", "Cs"]]).arrange(DOWN, buff=0.05)
        gcol.move_to(RIGHT * 4.0 + UP * 0.35)
        a2 = Arrow(gcol.get_top() + RIGHT * 0.75, gcol.get_bottom() + RIGHT * 0.75, color=GOOD, buff=0, stroke_width=6)
        a2t = B("metallic\ncharacter\nincreases", 24, GOOD).next_to(a2, RIGHT, buff=0.15)
        with self.say("Down a group, the top floor electrons are far from the nucleus, and loosely held. Easy to give away. "
                      "So metallic character increases. That's why potassium is more reactive than sodium."):
            self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.2) for b in gcol], lag_ratio=0.15), run_time=1.2)
            self.play(GrowArrow(a2), FadeIn(a2t), run_time=0.8)
            self.play(Indicate(gcol[2], color=GOLD, scale_factor=1.3), run_time=1)
        nm = VGroup(B("Non-metallic character = the exact opposite", 32, P_COL),
                    T("increases across a period, decreases down a group · halogens: F > Cl > Br > I", 28)
                    ).arrange(DOWN, buff=0.15)
        fit(nm, 12.6).move_to(DOWN * 2.2)
        with self.say("Non-metallic character is the exact opposite. It increases across a period, and decreases down a group. "
                      "Among the halogens, fluorine is the strongest electron grabber."):
            self.play(FadeIn(nm, shift=UP * 0.2), run_time=1)
        with self.doubt("Why is fluorine the best\nelectron grabber?"):
            f_ = Atom("F", [2, 7], r0=0.35, step=0.4, e_radius=0.06).move_to(LEFT * 3.6 + DOWN * 0.7)
            i_ = Atom("I", [2, 8, 18, 18, 7], r0=0.35, step=0.3, e_radius=0.045).move_to(RIGHT * 2.2 + DOWN * 0.7)
            e1 = Dot(radius=0.09, color=GOOD).move_to(f_.get_center() + UP * 2.0 + LEFT * 1.6)
            e2 = Dot(radius=0.09, color=GOOD).move_to(i_.get_center() + UP * 2.0 + RIGHT * 2.6)
            l1 = B("small: strong grip", 32, GOOD).next_to(f_, DOWN, buff=0.25)
            l2 = B("big: weaker grip", 32, MUTED).next_to(i_, RIGHT, buff=0.3)
            with self.say("Because fluorine is the smallest in its group. Its outer floor is very close to the nucleus, "
                          "so an incoming electron feels a strong pull. Small atom, strong grip. "
                          "Iodine is big, so its grip is weaker."):
                self.play(FadeIn(f_), FadeIn(i_), FadeIn(e1), FadeIn(e2), run_time=0.8)
                self.wait(1.5)
                self.play(e1.animate.move_to(f_.get_center() + UR * 0.78), run_time=0.6, rate_func=rush_into)
                self.play(FadeIn(l1), run_time=0.5)
                self.wait(1.5)
                self.play(e2.animate.move_to(i_.get_center() + UR * 1.45), run_time=2.0, rate_func=smooth)
                self.play(FadeIn(l2), run_time=0.5)
        self.clear_all()

        # --- valency
        h2 = self.heading("Valency follows the valence electrons")
        els = ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]
        val = [1, 2, 3, 4, 3, 2, 1, 0]
        boxes = VGroup(*[ebox(s, size=1.0) for s in els]).arrange(RIGHT, buff=0.25).shift(UP * 1.6)
        ve = VGroup(*[T(f"{i + 1} e⁻", 26, MUTED).next_to(b, DOWN, buff=0.15) for i, b in enumerate(boxes)])
        base_y = -2.2
        pts = [np.array([b.get_x(), base_y + v * 0.6, 0]) for b, v in zip(boxes, val)]
        dots = VGroup(*[Dot(p, radius=0.09, color=GOLD) for p in pts])
        nums = VGroup(*[B(str(v), 34, GOLD).next_to(p, UP, buff=0.15) for p, v in zip(pts, val)])
        line = VMobject(stroke_color=GOLD, stroke_width=6).set_points_as_corners(pts)
        with self.say("Valency comes from the valence electrons. Across period 3: 1, 2, 3, 4, then 3, 2, 1, and 0. "
                      "Up to four, then back down. And down a group, it stays the same.") as d:
            self.play(FadeIn(h2), LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.08), FadeIn(ve), run_time=1.2)
            self.wait(1)
            self.play(Create(line), LaggedStart(*[AnimationGroup(FadeIn(dt, scale=2), FadeIn(n)) for dt, n in zip(dots, nums)],
                                                lag_ratio=0.3), run_time=4)
        with self.doubt("Why does valency go back DOWN after 4?"):
            rows = VGroup()
            for sym, ve_, lose, gain, v in [("P", 5, "lose 5", "gain 3", 3), ("S", 6, "lose 6", "gain 2", 2), ("Cl", 7, "lose 7", "gain 1", 1)]:
                rows.add(VGroup(B(f"{sym}: {ve_} valence e\u207b", 34).set_width(3.6),
                                VGroup(cross(size=0.4), T(lose, 32, MUTED)).arrange(RIGHT, buff=0.2),
                                VGroup(check(size=0.4), T(gain, 32)).arrange(RIGHT, buff=0.2),
                                B(f"valency {v}", 34, GOLD)).arrange(RIGHT, buff=0.7))
            rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(DOWN * 0.6)
            with self.say("Remember the easy way? Phosphorus has 5 valence electrons. Losing 5 is hard, gaining 3 is easier. "
                          "So its valency is 3. Sulphur needs 2, chlorine needs 1. And argon is already full, so zero."):
                self.wait(0.8)
                self.play(FadeIn(rows[0][0]), run_time=0.5)
                self.play(FadeIn(rows[0][1]), run_time=0.5)
                self.play(FadeIn(rows[0][2]), run_time=0.5)
                self.play(FadeIn(rows[0][3], scale=1.5), run_time=0.5)
                self.wait(0.8)
                self.play(FadeIn(rows[1], shift=UP * 0.2), run_time=0.6)
                self.play(FadeIn(rows[2], shift=UP * 0.2), run_time=0.6)
        self.clear_all()

        # --- summary
        h3 = self.heading("All trends on one screen")
        rows = [("Property", "Across a period →", "Down a group ↓"),
                ("Shells", "same", "increase"), ("Valence electrons", "1 → 8", "same"),
                ("Valency", "1 → 4 → 0", "same"), ("Atomic radius", "decreases", "increases"),
                ("Metallic character", "decreases", "increases"), ("Non-metallic character", "increases", "decreases")]
        tab = VGroup()
        xs = [-3.6, 0.9, 4.3]
        for r, row in enumerate(rows):
            cells = VGroup()
            for i, s in enumerate(row):
                col = MUTED if r == 0 else (INK if i == 0 else (GOLD if i == 1 else P_COL))
                t = T(s, 30, col, weight=BOLD if r == 0 or i else NORMAL).move_to([xs[i], 2.3 - r * 0.62, 0])
                cells.add(t)
            tab.add(cells)
        lines = VGroup(*[Line([-6.2, 2.0 - r * 0.62, 0], [6.2, 2.0 - r * 0.62, 0], color=LINE, stroke_width=1.5) for r in range(6)])
        why = VGroup(B("→ more protons, same floors", 28, GOLD), B("↓ new floor added", 28, P_COL)).arrange(RIGHT, buff=1.0)
        why.next_to(tab, DOWN, buff=0.35)
        with self.say("Here is every trend on one screen. And every single arrow comes from those two reasons: "
                      "more protons across, a new floor down. Pause the video and take a screenshot."):
            self.play(FadeIn(h3), FadeIn(tab[0]), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.15) for r in tab[1:]], lag_ratio=0.3), Create(lines), run_time=3)
            self.play(FadeIn(why, shift=UP * 0.2), run_time=0.8)
        self.wait(2.5)
        self.clear_all()


# =====================================================================  8. QUIZ & OUTRO
class S08Quiz(Lesson):
    def countdown(self, secs=5):
        ring = Circle(radius=0.55, color=GOLD, stroke_width=8).move_to(RIGHT * 5.6 + DOWN * 1.2)
        num = B(str(secs), 50, GOLD).move_to(ring)
        self.play(Create(ring), FadeIn(num), run_time=0.4)
        for s in range(secs - 1, -1, -1):
            new = B(str(s), 50, GOLD).move_to(ring)
            self.play(ReplacementTransform(num, new), run_time=1)
            num = new
        self.play(FadeOut(ring), FadeOut(num), run_time=0.3)

    def construct(self):
        h = self.heading("Quick test: beat the timer!")
        with self.say("Quick test! Three questions. Try to answer before the timer runs out."):
            self.play(FadeIn(h, shift=DOWN * 0.3), run_time=0.6)
        qs = [
            ("An element is 2, 8, 2.\nWhich period and group? Metal or non-metal?",
             "An element is 2, 8, 2. Which period and which group? And is it a metal?",
             "3 shells → Period 3 · 2 valence e⁻ → Group 2\nIt's magnesium, a metal.",
             "Three floors, so period 3. Two valence electrons, so group 2. It's magnesium, a metal."),
            ("Who left empty spaces in his table?\nWhat was eka-aluminium later called?",
             "Who left empty spaces in his table? And what was eka-aluminium later called?",
             "Mendeleev · Gallium",
             "Mendeleev. And eka-aluminium is gallium."),
            ("Which atom is bigger: sodium or potassium?\nWhy?",
             "Which atom is bigger, sodium or potassium? And why?",
             "Potassium: it has one more shell (new floor down the group).",
             "Potassium. Going down the group, a new floor is added."),
        ]
        for i, (qt, qs_, at, as_) in enumerate(qs):
            num = B(f"Q{i + 1}", 60, GOLD).to_edge(LEFT, buff=0.8).shift(UP * 1.6)
            q = fit(B(qt, 40), 10.6).next_to(num, RIGHT, buff=0.5).align_to(num, UP)
            with self.say(qs_):
                self.play(FadeIn(num), Write(q), run_time=1.5)
            self.countdown(5)
            ans = fit(VGroup(T("Answer", 30, GOOD), B(at, 36)).arrange(DOWN, aligned_edge=LEFT, buff=0.2), 9.0)
            box = SurroundingRectangle(ans, buff=0.35, color=GOOD, corner_radius=0.15, stroke_width=4)
            VGroup(ans, box).next_to(q, DOWN, buff=0.8).align_to(num, LEFT)
            with self.say(as_):
                self.play(Create(box), FadeIn(ans, shift=UP * 0.2), run_time=0.8)
            self.wait(0.8)
            self.play(FadeOut(VGroup(num, q, ans, box)), run_time=0.5)
        self.clear_all()

        recap = VGroup(*[VGroup(B(a, 64, GOLD), B(b, 40)).arrange(RIGHT, buff=0.4)
                         for a, b in [("3", "basics: roll number, floors, top-floor electrons"),
                                      ("1", "story: triads → octaves → Mendeleev → Moseley"),
                                      ("2", "reasons: more protons across, new floor down")]]
                       ).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        fit(recap, 12.4).shift(UP * 0.4)
        with self.say("So, was it hard? Three basics. One story. Two reasons. That is the whole chapter."):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.4) for r in recap], lag_ratio=0.6), run_time=3.5)
        st = stamp("MYTH BUSTED", GOOD, 80).move_to(DOWN * 0.2)
        share = T("Send this to the friend who said science is hard.", 36, INK).to_edge(DOWN, buff=1.3)
        with self.say("Myth busted! Now send this video to the friend who said science is hard. All the best for your exams!"):
            self.play(recap.animate.set_opacity(0.25), run_time=0.5)
            self.play(FadeIn(st, scale=3), run_time=0.4)
            self.play(FadeIn(share, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.clear_all()


SCENE_ORDER = ["S01Hook", "S02Basics", "S03Triads", "S04Mendeleev", "S05Moseley", "S06Modern", "S07Trends", "S08Quiz"]
