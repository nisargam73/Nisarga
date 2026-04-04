num=int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)



n=int(input("Enter a number: "))
total=0
for i in range(1, n + 1):
    total += i
print("Sum:", total)


num=int(input("Enter a number: "))
rev=0
while num > 0:
    digit=num % 10
    rev=rev * 10 + digit
    num=num // 10
print("Reversed number:", rev)
