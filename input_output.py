name=input("Your name please: ")
print("Hey",name)

age=int(input("Enter Your age :"))
print("You are",age,"years old.")

a=int(input("Enter first number :"))
b=int(input("Enter second number:"))
sum=a+b
print("The sum is:",sum)

a,b,c,d=map(int,input("Enter four numbers:").split())
print("the number are:",a,b,c,d)
sum=a+b-c+d
print("the sum is:",sum)
