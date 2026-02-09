# the sum each digit raised to the power of the 
# number of digits is equal to original number
# 153=1*3+5*3+3*3


num=153
temp=num
sum=0
digits=len(str(num))

while temp>0:
    digit= temp%10
    sum += digit**digits
    temp//=10

if sum==num:
    print('armstrong')
else:
    print('not a armstron number')