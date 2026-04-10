import interpreter_repl as ir
app = ""
while True:
    irir = input()
    if irir.startswith("@run "):
        with open(irir[5::], "r") as failik:
            ir.lex(failik.read())
    elif irir.startswith("~"):
        app+=f"\n{irir[1::]}"
    elif irir == "$":
        ir.lex(app)
        app = ""
    elif irir == "@quit":
        break
    else:
        ir.lex(irir)