# it is a natural number and have only two factors one and itself
# 2,3,5,7.11,13,17,19,23


def check_prime(num):
    if num<=1:
        return('not a prime')
    for i in range(2,num):
        if num%i==0:
          return('not a prime ')
    return('prime')

res=check_prime(7)
print(res)