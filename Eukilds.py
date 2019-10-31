import math

# Python solution to Eukilds algorithm for Diskrete Mathematics with automated LaTeX code output

# does the computing for Eukilds algorithm
class Eukild:

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
        myTable = TableSetUp()

        if a < b:
            self.update(0, 1, 1, 0, b, a)
            myTable.addLine(-1, self.s0, self.s1, " ", self.r0)
            myTable.addLine( 0, self.t0, self.t1, " ", self.r1)

        else:
            self.update(1, 0, 0, 1, a, b)
            myTable.addLine(-1, self.s0, self.t0, " ", self.r0)
            myTable.addLine(0, self.s1, self.t1, " ", self.r1)

        if addLatex:
            self.tex = Latex()
            self.tex.beginTabluar(self.r0, self.r1)

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

        print(myTable.table)



# give table and returns latex code
class Latex:
    def __init__(self):
        pass

    def beginTabluar(self, a, b):
        name = "LaTeX/Tabular gcd(" + str(a) + ", " + str(b) + ")"
        self.f = open(name, "w")
        startTxt = "gcd(" + str(a) + ", " + str(b) + ")" + """
\\begin{tabular}{c|c c c c} 
    i & $s_i$ & $t_i$ & $q_i$ & $r_i$ \\\\ \\hline \n"""

        self.f.write(startTxt)


    def addLineAsCode(self, i, s, t, q, r):
        line = "    " + str(i) + " & " + str(s) + " & " + str(t) + " & " + str(q) + " & " + str(r) + "\\\\ \n"
        self.f.write(line)

    def endTabular(self):
        self.f.write("\\end{tabular}")
        self.f.close()


# turns values to a tableLine
class Txt:
    def __init__(self):
        pass

    def tableLine(self, i, s, t, q, r):
        line = str(i) + " | " + str(s) + "   " + str(t) + "   " + str(q) + "   "  + str(r)
        return line


# generates table
class TableSetUp:
    def __init__(self):
        self.myTxt = Txt()
        self.table = """i | s   t   q   t
------------------"""

    def addLine(self, i, s, t, q, r):
        line = self.myTxt.tableLine(i, s, t, q, r)
        self.table += "\n" + line

eu = Eukild()


eu.gcd(4, 3, False)

print (" ")

eu.gcd(341, 217, True)


