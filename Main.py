import PySimpleGUI as sg
import os
import Euklids

# Source of RepresentsInt:
# https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def latexDir():
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "LaTeX")
    if not os.path.exists(path):
        os.mkdir(path)
        sg.Popup("Made LaTeX-folder at " + path)


layout = [
    [sg.Text("s * a + t * b = r")],
    [sg.Text("Input value a"), sg.Input()],
    [sg.Text("Input value b"), sg.Input()],
    [sg.Checkbox("Output the LaTeX-code")],
    [sg.Button("GCD!")]
]

eu = Euklids.Euklid()

window = sg.Window("GCD()").Layout(layout)

while True:

    button, values = window.Read()
    if RepresentsInt(values[0]) and RepresentsInt(values[1]):
        if values[2]:
            latexDir()
        tablePreview = eu.gcd(int(values[0]), int(values[1]), values[2])
        sg.Popup(tablePreview, title="GCD(" + str(values[0]) + ", " + str(values[1]) + ") - Preview")
    else:
        sg.Popup("Make sure all values are integers!")
