from os import getcwd, open, close, O_CREAT
from sys import stdin


def manager (cmd, src, dst = ""):
    if (cmd == "touch"):
        f = open (src, O_CREAT)
        close(f)
    
print (getcwd())
inp = stdin.readline()
inp = inp.split()
print (inp)
manager (inp [0], inp [1])
