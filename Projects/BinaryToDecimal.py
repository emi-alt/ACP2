num = int(input("Enter a binary number: "))
decimal = 0
for i in range(1, len(str(num)) + 1):
    num_ryt = num % 10
    decimal += num_ryt * 2**(i - 1)
    num //= 10
print("Decimal equivalent:", decimal)
