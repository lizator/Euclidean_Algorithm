import math
import tabula

# Python solution to Eukilds algorithm for Diskrete Mathematics with automated LaTeX code output

# does the computing for Eukilds algorithm
class Euklid:

    def __init__(self):
        self.s0 = 0; self.s1 = 0
        self.t0 = 0; self.t1 = 0
        self.r0 = 0; self.r1 = 0
        pass

    def update(self, s1, s2, t1, t2, r1, r2):
        self.s0 = s1; self.s1 = s2
        self.t0 = t1; self.t1 = t2
        self.r0 = r1; self.r1 = r2
        pass


    def gcd(self, a, b, addLatex):
        myTable = tabula.TableSetUp()

        if a < b:
            self.update(0, 1, 1, 0, b, a)
            myTable.addLine(-1, self.s0, self.s1, " ", self.r0)
            myTable.addLine( 0, self.t0, self.t1, " ", self.r1)

        else:
            self.update(1, 0, 0, 1, a, b)
            myTable.addLine(-1, self.s0, self.t0, " ", self.r0)
            myTable.addLine(0, self.s1, self.t1, " ", self.r1)

        if addLatex:
            self.tex = tabula.Latex()
            self.tex.beginTabluar(self.r0, self.r1)
            self.tex.addLineAsCode(-1, self.s0, self.t0, " ", self.r0)
            self.tex.addLineAsCode(0, self.s1, self.t1, " ", self.r1)

        i = 1
        while (self.r1 != 0):
            q = math.floor(self.r0 / self.r1)
            s2 = self.s0 - (self.s1 * q)
            t2 = self.t0 - (self.t1 * q)
            r2 = self.r0 - (self.r1 * q)

            myTable.addLine(i, s2, t2, q, r2)

            if addLatex:
                self.tex.addLineAsCode(i, s2, t2, q, r2)

            self.update(self.s1, s2, self.t1, t2, self.r1, r2)
            i += 1

        if addLatex:
            self.tex.endTabular()

        return myTable.table


# testing
#eu = Eukild()

#eu.gcd(4, 3, False)

#print (" ")

#eu.gcd(341, 217, True)



