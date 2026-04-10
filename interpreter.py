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
                        val = int(file.read())
                elif valb == "stdout":
                    val = stdout
                elif valb == "inp":
                    val = int(input())
                elif valb.isdecimal():
                    val = int(valb)
                else:
                    raise BlockunError(f"SyntaxError: incorrect to syntax in string {num}")
                for i in dela:
                    if i[0] == "b":
                        if int(i[1::]) in blocks.keys():
                            match blocks[int(i[1::])]:
                                case "+":
                                    blocks[int(i[1::])][0]+=val
                                case "-":
                                    blocks[int(i[1::])][0]-=val
                                case "/":
                                    blocks[int(i[1::])][0]//=val
                                case "*":
                                    blocks[int(i[1::])][0]*=val
                                case "%":
                                    blocks[int(i[1::])][0]%=val
                                case "or":
                                    blocks[int(i[1::])][0] = int(int(i[1::]) != 0 or val != 0)
                                case "and":
                                    blocks[int(i[1::])][0] = int(int(i[1::]) != 0 and val != 0)
                                case "not":
                                    blocks[int(i[1::])][0] = int(int(i[1::]) == 0)   
                                case _:
                                    raise BlockunError(f"BlockCorruptedError: uncorrect operation in block {int(i[1::])} and str {num}")
                        else:
                            blocks[int(i[1::])] = val
                    if i[0] == "f":
                        with open(i[1::], "a", encoding="utf-8") as opn:
                            opn.write(val)
                    if i == "stdout":
                        print(val)
                        stdout = val
                    if i == "charout":
                        print(chr(val))
                        stdout = val
                if valb[0] == "b":
                    blocks[int(valb[1::])][0] = 0
                if valb == "stdout":
                    stdout = 0
        except IndexError:
            break