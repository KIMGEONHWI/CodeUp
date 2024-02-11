a, b, c = map(int, input().split())
if(a<=b<=c):
    print(a)
elif(b<=a<=c):
    print(b)
elif(c<=b<=a):
    print(c)
elif(b<=c<=a):
    print(b)
elif(c<=a<=b):
    print(c)
elif(a<=c<=b):
    print(a)