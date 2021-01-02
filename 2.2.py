a = list(input())
a[::2], a[1::2] = a[1::2], a[::2]
print(' '.join([str(i) for i in a]))