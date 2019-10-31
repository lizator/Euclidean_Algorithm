# give table and returns latex code
class Latex:
    def __init__(self):
        pass

    def beginTabluar(self, a, b):
        name = "LaTeX/Tabular gcd(" + str(a) + ", " + str(b) + ")"
        self.f = open(name, "w")
        startTxt = "% gcd(" + str(a) + ", " + str(b) + ")" + """
\\begin{tabular}{c|c c c c} 
    $i$ & $s_i$ & $t_i$ & $q_i$ & $r_i$ \\\\ \\hline \n"""

        self.f.write(startTxt)


    def addLineAsCode(self, i, s, t, q, r):
        line = "    " + str(i) + " & " + str(s) + " & " + str(t) + " & " + str(q) + " & " + str(r) + " \\\\ \n"
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