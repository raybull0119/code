while True:
    try:
        a=int(input())
        b=input().split()
        # b = [99,77,66,44,11]
        for i in  range(0, a):
            # print(b) # b = [99,77,66,44,11]
            print(' '.join(b))
            b.reverse()
            # print(numbers)
            b.pop()
            # b = [11,44,66,77]
        print('')
        # print(a)
        # print(b)
    except EOFError:
        break
