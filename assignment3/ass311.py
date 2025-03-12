num = int(input("Enter a number: "))

switch = {
    0: "EVEN",
    1: "ODD"
}

print(switch.get(num % 2))