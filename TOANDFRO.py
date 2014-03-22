from sys import stdin, exit
while (1):
    num = int(stdin.readline())
    if (num == 0):
        break
    string = stdin.readline()
    
    for j in range (num):
        out = string [j : j+1]
        i = 2
        while (out):
            print(out, end = "")
            tmp1 = string [i * num - 1 - j: i * num - j]
            tmp2 = string [i * num + j: i * num + j + 1]
            if (tmp1 == "\n"):
                tmp1 = ""
            if (tmp2 == "\n"):
                tmp2 = ""
            out = tmp1 + tmp2
            i = i + 2
    print ("\n")

#toioynnkpheleaigshareconhtomesnlewx
#ttyohhieneesiaabss
