class BlockunError(PythonFinalizationError):
    pass
def lex(c):
    c = c.split("\n")
    num = -1
    blocks = {}
    stdout = 0
    while True:
        try:
            num+=1
            d = c[num]
            if d.find(" to ") != -1:
                d = d.split(" to ")
                dela = d[1].split(" ")
                valb = d[0]
                if valb[0] == "b":
                    val = blocks[int(valb[1::])][0]
                elif valb[0] == "f":
                    with open(valb[1::], "r", encoding="utf-8") as file:
                        val = file.read()
                elif valb == "stdout":
                    val = stdout
                elif valb == "inp":
                    val = int(input())
                elif valb.isdecimal():
                    val = int(d)
                else:
                    raise  BlockunError(f"SyntaxError: incorrect to syntax in string {num}")
        except IndexError:
            break