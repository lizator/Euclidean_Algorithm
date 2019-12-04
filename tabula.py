# give table and returns latex code
class Latex:
    def __init__(self):
        pass

    def beginTabluar(self, a, b):
        name = "LaTeX/Tabular gcd(" + str(a) + ", " + str(b) + ").txt"
        self.f = open(name, "w")
        startTxt = "% gcd(" + str(a) + ", " + str(b) + ")" + """
\\begin{tabular}{c|c c c c} 
\t$i$\t& $s_i$\t& $t_i$\t& $q_i$\t& $r_i$\t\\\\ \\hline \n"""

        self.f.write(startTxt)


    def addLineAsCode(self, i, s, t, q, r):
        line = "\t" + str(i) + "\t& " + str(s) + "\t& " + str(t) + "\t& " + str(q) + "\t& " + str(r) + "\t\\\\ \n"
        self.f.write(line)

    def endTabular(self):
        self.f.write("\\end{tabular}")
        self.f.close()


# turns values to a tableLine
class Txt:
    def __init__(self):
        pass

    def tableLine(self, i, s, t, q, r):
        line = str(i) + "\t| " + str(s) + "\t" + str(t) + "\t" + str(q) + "\t" + str(r)
        return line


# generates table
class TableSetUp:
    def __init__(self):
        self.myTxt = Txt()
        self.table = """i\t| s\tt\tq\tr
--------------------------------------------------------------------"""

    def addLine(self, i, s, t, q, r):
        line = self.myTxt.tableLine(i, s, t, q, r)
        self.table += "\n" + line