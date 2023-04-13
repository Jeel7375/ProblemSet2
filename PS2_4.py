def collatz(n):
    # Perform x/2 operation for even number
    if n % 2 == 0:
        print(n // 2)
        return n // 2

    # Perform 3x + 1 operation for odd number
    elif n % 2 == 1:
        result = 3 * n + 1
        print(result)
        return result

# Take number inout from the user
n = input("Enter the number: ")
while n != 1:
    n = collatz(int(n))