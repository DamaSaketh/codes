# fibanacci is the each number is the sum of two previous numbers
# fin(n)=fib(n-1)+fib(n-2)

num1 ,num2 =0,1
n=15
for i in range(n+1):
    temp=num1+num2
    print(num1)
    num1=num2
    num2=temp