from manim import *
from pyrr.rectangle import height
from math import sin, cos
# config.media_width = "75%"
config.verbosity = "WARNING"


class CircleOfFifths(Scene):
    def construct(self):
        # Notes creation:
        notes = []
        self.wait(2)
        for each in range(12):
            c = Circle(radius=0.1, color=YELLOW)
            c.move_to((-5.5, 2, 0))
            self.add(c)
            notes.append(c)

        # Notes translation in line:
        animations = []
        for each in range(len(notes)):
            animations.append(notes[each].animate.shift(RIGHT * each))
        self.play(*animations)
        self.wait(1)

        # Notes playing (filling circles and creating arcs):
        notes[0].set_fill(YELLOW, opacity=1)
        arcs = []
        for each in range(11):
            a, b = notes[each: each + 2]
            arc = ArcBetweenPoints(a.get_center(), b.get_center())
            arcs.append(arc)
            self.add(arc)
            self.play(Create(arc, run_time=0.5))
            notes[each+1].set_fill(YELLOW, opacity=1)

        # Wait time, clearing notes:
        self.wait(2)
        for note in notes:
            note.set_fill(YELLOW, opacity=0)

        # Stretching arcs:
        animations = []
        for each in range(11):
            a, b = notes[each: each + 2]
            new_arc = ArcBetweenPoints(a.get_center(), b.get_center(), angle=0.01)
            animations.append(Transform(arcs[each], new_arc))
        self.play(*animations)
        self.wait(1)

        notes[10].move_to((-5.5, 0, 0))
        # Rearranging them in the circle of fifths

        # Painting notes and arcs
        self.wait(3)
