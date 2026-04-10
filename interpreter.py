class BlockunError(PythonFinalizationError):
    pass
def lex(c):
    c = c.split("\n")
    num = -1
    blocks = {}
    stdout = 0
    koshschi_metki = {}
    while True:
        try:
            num+=1
            d = c[num]
            if d.find(" to ") != -1:
                dd = d.split(" to ")
                dela = dd[1].split(" ")
                valb = dd[0]
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
                            match blocks[int(i[1::])][1]:
                                case "+"|" +"|"+ "|" + ":
                                    blocks[int(i[1::])][0]+=val
                                case "-"|" -"|"- "|" - ":
                                    blocks[int(i[1::])][0]-=val
                                case "/"|" /"|"/ "|" / ":
                                    blocks[int(i[1::])][0]//=val
                                case "*"|" *"|"* "|" * ":
                                    blocks[int(i[1::])][0]*=val
                                case "%"|" %"|"% "|" % ":
                                    blocks[int(i[1::])][0]%=val
                                case "or"|" or"|"or "|" or ":
                                    blocks[int(i[1::])][0] = int(int(i[1::]) != 0 or val != 0)
                                case "and"|" and"|"and "|" and ":
                                    blocks[int(i[1::])][0] = int(int(i[1::]) != 0 and val != 0)
                                case "not"|" not"|"not "|" not ":
                                    blocks[int(i[1::])][0] = int(int(i[1::]) == 0)   
                                case _:
                                    raise BlockunError(f"BlockCorruptedError: uncorrect operation in block {int(i[1::])} and str {num}")
                        else:
                            blocks[int(i[1::])] = [val, "+"]
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
            if d.startswith("null "):
                obnulaemoe = d[5::]
                if obnulaemoe[0] == "b":
                    blocks[int(obnulaemoe[1::])][0] = 0
                elif obnulaemoe[0] == "f":
                    with open(obnulaemoe[1::], "w") as file:
                        file.truncate()
            if d.startswith("crt "):
                koshschi_metki[d[4::]] = num
            if d.startswith("goto "):
                num = koshschi_metki[d[5::]]
                continue
            if d.startswith("coto "):
                dela = d[5::].split(";")
                match dela[2]:
                    case "=":
                        if blocks[int(dela[0])][0] == blocks[int(dela[1])][0]:
                            num = koshschi_metki[dela[3]]
                            continue
                    case ">":
                        if blocks[int(dela[0])][0] > blocks[int(dela[1])][0]:
                            num = koshschi_metki[dela[3]]
                            continue
                    case "<":
                        if blocks[int(dela[0])][0] < blocks[int(dela[1])][0]:
                            num = koshschi_metki[dela[3]]
                            continue
                    case _:
                        raise BlockunError("IncorrectCotoError")
            if d.startswith("mount "):
                mount_block = d[6::].split(" ")[0]
                mount_operation = d[6::].split(" ")[1]
                blocks[int(mount_block)][1] = mount_operation
        except IndexError:
            break
lex("""
crt label
inp to b0
mount 0 *
2 to b0
b0 to stdout charout
goto label
""")