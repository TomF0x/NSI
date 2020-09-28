# impérative
def facto(n):
  return 1 if n==1 else n*facto(n-1)
print(facto(5))

# sans impérative
def faction(n):
    for i in range(1,n):
        n*=i
    print(n)

faction(5)
