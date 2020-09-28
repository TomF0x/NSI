# impérative
def facto(n):
  if n==0:
    return 1
  else:
    return n*facto(n-1)
print(facto(5))

# sans impérative
def faction(n):
    for i in range(1,n):
        n*=i
    print(n)

faction(5)
