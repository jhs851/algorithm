while True:
    try:
        n = int(input())
        i = 1

        while True:
            if str(n * i).replace("1", "") == "":
                print(len(str(n * i)))
                break
            else:
                i += 1
    except:
        exit()
