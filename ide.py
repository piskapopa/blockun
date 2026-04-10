import interpreter as i
file = input()
try:
    with open(f"{file}.blcn", "r+") as q:
        qq = q.read()
        strr = 0
        if not qq:
            qq = " "
        qqq = qq.split("\n")
        while True:
            print("\n".join(qqq))
            qqqq = input()
            if qqqq == "@ar":
                strr+=1
            elif qqqq == "@al":
                strr-=1
            elif qqqq == "@pwd":
                print(strr)
            elif qqqq == "@del":
                try:
                    qqq.pop(strr)
                except IndexError:
                    print("Этой строки ещё нет")
            elif qqqq == "@add":
                qqq.insert(strr, " ")
            elif qqqq == "@save":
                q.seek(0)
                q.truncate()
                q.write("\n".join(qqq))
                break
            elif qqqq == "@run":
                i.lex("\n".join(qqq))
            else:
                try:
                    qqq[strr] = qqqq
                except IndexError:
                    qqq.append(qqqq)
except FileNotFoundError:
    with open(f"{file}.blcn", "x") as q:
        pass
    print("Reload")