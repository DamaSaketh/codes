num=12345
print(int(str(num)[::-1]))

num=int(input('enter a number'))
rev=0

while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10

print('reversed number:',rev)