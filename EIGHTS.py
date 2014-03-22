from sys import stdin
test_cases = int(input())
for i in range(test_cases):
    try:
        num = int(stdin.readline())
        print (192 + (num - 1) * 250)        
    except:
        break