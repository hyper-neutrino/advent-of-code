with open("input.txt", "r") as f:
    src = data = f.read()

if data and data[-1] == "\n":
    data = data[:-1]

py_input = input

def input():
    global data
    if data:
        try:
            line, data = data.split("\n", 1)
        except:
            line = data
            data = ""
        return line
    return py_input()
