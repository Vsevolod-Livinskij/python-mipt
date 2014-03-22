from sys import stdin

def count (num):
    if (num == 1):
        return str (1) + "/" + str (1)
    diag = 1
    s_n = 1
    s_prev = 1
    while (s_n < num):
        s_prev = s_n
        s_n = int ((1 + diag) * diag / 2)
        diag += 1
    diag -= 1
    s_prev += 1
    up = 1
    down = 1
    if (diag % 2 == 0):
        down = diag
        while (s_prev < num):
            up += 1
            down -= 1
            s_prev += 1
    else:
        up = diag
        while (s_prev < num):
            up -= 1
            down += 1
            s_prev += 1
    return str(up) + "/" + str (down)
    
test_cases = int(stdin.readline())
for x in range(test_cases):
    try:
        num = int(stdin.readline())
        print ("TERM " + str(num) + " IS " + str (count (num)))
    except:
        break

