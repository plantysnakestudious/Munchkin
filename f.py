def f():
    import msvcrt
    strr = b''''''
    inp = []
    fl = 1
    print(r"Enter your func below. Remember, that tabs are 4 ' ' and exit is '`'")
    while fl:
        input_char = msvcrt.getch()
        if (not input_char == b"\x08") and (not input_char == b"`") and (not input_char == b"\r") and (not input_char == b"\t"):
            inp.append(input_char)
        elif (input_char == b"\x08"):
            tmp = inp.pop()
        elif (input_char == b"\r"):
            inp.append(b"\n")
            print(flush = True)
        elif (input_char == b"\t"):
            for i in range(4):
                inp.append(b" ")
            print("    ", flush = True, end = "", sep = "")
        print(input_char.decode(), end = "", flush = True)
        if input_char.upper() == b'`':
            print ('OK')
            fl = 0


    strr = b"""""".join(inp)
    strr = strr.decode()
    return strr
    print(strr)
    exec (strr, globals(), locals())
    func()