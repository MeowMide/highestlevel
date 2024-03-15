def pprint(linecode):
    line = linecode
    z = list(line)
    z.pop()
    w = ""
    string = ''
    for i in z:
        w += i
        if w == "print:":
            w = ''
            y = z[6:]
            for i in y:
                string += str(i)
                try:
                    string = int(string)
                except:
                    string = str(string)
            return f'print({string})'

def pnd(linecode):
    line = linecode
    z = list(line)
    z.pop()
    w = ""
    string = ''
    for i in z:
        w += i
        if w == "pnd:":
            return f'print("Punks not dead!")'

