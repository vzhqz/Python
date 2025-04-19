from manim import *

class Series(Scene):
    def construct(self):
        main_problem = MathTex(r"M = \frac{1}{\sqrt{2} + \sqrt{1}} + \frac{1}{\sqrt{3} + \sqrt{2}} + \frac{1}{\sqrt{4} + \sqrt{3}} + \frac{1}{\sqrt{5} + \sqrt{4}} + \cdots + \frac{1}{\sqrt{441} + \sqrt{440}}", font_size=36)
        required = MathTex("2.5M^2 = ?").to_edge(UP)
        
        self.play(AnimationGroup(
                  Write(main_problem, run_time=2),
                  Write(required, run_time=1),
                  lag_ratio=0
        ))
        self.wait(2)

        self.play(main_problem.animate.move_to(UP),
                  FadeOut(required))
        txt1 = Tex("We see here that theres a pattern in the denominator:")
        self.play(Write(txt1))
        
        self.wait()

        pattern = MathTex("\sqrt{n} + \sqrt{n - 1}").next_to(txt1, DOWN)
        self.play(Write(pattern))

        self.wait()

        self.play(FadeOut(main_problem, txt1, pattern))
        self.wait()

        txt2 = Tex("So M becomes:").to_edge(UP)
        main_pattern = MathTex(r"M = \frac{1}{\sqrt{n} + \sqrt{n - 1}}")

        self.play(Write(txt2),
                  Write(main_pattern))
        
        self.wait(2)

        self.play(FadeOut(txt2))
        self.wait(2)

        step1 = MathTex(r"M = \frac{1}{\sqrt{n} + \sqrt{n - 1}} \cdot \frac{\sqrt{n} - {n - 1}}{\sqrt{n} - {n - 1}}")

        self.play(Transform(main_pattern, step1))
        self.wait()

        txt3 = Tex("Multiply the numerator by the numerator and the denominator by the denominator.", font_size=36).to_edge(UP)
        step2 = MathTex(r"M = \frac{\sqrt{n}-\sqrt{n-1}} {(\sqrt{n}+\sqrt{n-1})(\sqrt{n}-\sqrt{n-1})}")

        self.play(Write(txt3))
        self.play(Transform(main_pattern, step2))
        self.wait()

        box1 = SurroundingRectangle(step2[0][12:], color=RED)
        rule1 = MathTex("(a+b)(a-b) = a^2 - b^2", color=RED).next_to(step2, DOWN)

        self.play(FadeOut(txt3),
                  Create(box1),
                  Write(rule1))
        self.wait()

        step3 = MathTex(r"M = \frac{\sqrt{n}-\sqrt{n-1}} {(\sqrt{n})^2 - (\sqrt{n-1})^2}")

        self.play(Transform(main_pattern, step3),
                  Transform(box1, SurroundingRectangle(step3[0][12:], color=RED)))
        self.wait()

        step4 = MathTex(r"M = \frac{\sqrt{n}-\sqrt{n-1}} {n-(n-1)}")

        self.play(FadeOut(rule1),
                  FadeOut(box1),
                  Transform(main_pattern, step4))
        self.wait()

        step5 = MathTex(r"M = \frac{\sqrt{n}-\sqrt{n-1}}{1}")

        self.play(Transform(main_pattern, step5))
        self.wait()

        step6 = MathTex(r"M = \sqrt{n} - \sqrt{n - 1}")
        self.play(Transform(main_pattern, step6))
        self.wait()

        txt4 = Tex("Let's get back to the series.")
        self.play(FadeOut(main_pattern),
                  Write(txt4))
        self.wait()

        series = MathTex(r"M = (\sqrt{2} - 1) + (\sqrt{3} - \sqrt{2}) + (\sqrt{4} - \sqrt{3}) + (\sqrt{5} - \sqrt{4}) + \cdots + (\sqrt{441} - \sqrt{440})", font_size=36)

        self.play(txt4.animate.to_edge(UP),
                  Write(series))
        self.wait()

        txt5 = Tex("Now we eliminate the square root with the square root in the next bracket.", font_size=36).to_edge(UP)
        box2 = SurroundingRectangle(series[0][5], color=RED)
        box3 = SurroundingRectangle(series[0][17], color=RED)

        self.play(Transform(txt4, txt5),
                  Create(box2),
                  Create(box3))
        
        self.wait(0.5)

        self.play(Transform(box2, SurroundingRectangle(series[0][13], color=BLUE)))
        self.play(Transform(box3, SurroundingRectangle(series[0][27], color=BLUE)))
        
        self.wait(0.5)

        self.play(Transform(box2, SurroundingRectangle(series[0][23], color=PURPLE)))
        self.play(Transform(box3, SurroundingRectangle(series[0][37], color=PURPLE)))

        self.wait()

        txt6 = Tex("After eliminating, you'll be remained with:").to_edge(UP)
        step7 = MathTex("M = -1 + \sqrt{441}")

        self.play(FadeOut(box2),
                  FadeOut(box3),
                  Transform(txt4, txt6),
                  Transform(series, step7))
        self.wait()

        step8 = MathTex("M = - 1 + 21")
        
        self.play(Transform(series, step8))
        
        self.wait()

        txt7 = Tex("So we found out that:").to_edge(UP)
        step9 = MathTex("M = 20")

        self.play(Transform(txt4, txt7),
                  Transform(series, step9))
        
        self.wait()

        txt8_0 = Tex("Now subtitute ")
        txt8_1 = MathTex("20")
        txt8_2 = Tex("Into ")
        txt8_3 = MathTex("2.5M^2")

        txt8 = VGroup(txt8_0, txt8_1, txt8_2, txt8_3).arrange(RIGHT).to_edge(UP)
        step10 = MathTex("2.5M^2")

        self.play(Transform(txt4, txt8),
                  Transform(series, step10))
        
        self.wait()

        box4 = SurroundingRectangle(step10[0][3], color=RED)

        self.play(Create(box4))

        step11 = MathTex("2.5(20)^2")

        self.play(Transform(series, step11),
                  Transform(box4, SurroundingRectangle(step11[0][3:], color=RED)))
        
        self.wait()

        step12 = MathTex("2.5 \cdot 400")

        self.play(Transform(series, step12),
                  Transform(box4, SurroundingRectangle(step12, color=RED)))
        
        self.wait()

        txt9 = Tex("So...").to_edge(UP)
        step13 = MathTex("2.5M^2 = 1,000")

        self.play(Transform(txt4, txt9),
                  Transform(series, step13),
                  Transform(box4, SurroundingRectangle(step13, color=RED)))
        
        self.wait(3)