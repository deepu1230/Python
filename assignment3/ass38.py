num = int(input("Enter a number: "))
original_num = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** len(str(original_num))
    num //= 10

if sum == original_num:
    print(original_num, "is an Armstrong number.")
else:
    print(original_num, "is not an Armstrong number.")