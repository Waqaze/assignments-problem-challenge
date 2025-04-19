# Problem 1:Reverse a string
print("Problem 1: Reverse a string")
user = input("Enter a Word: ")
print("Reversed string is: ", user[::-1])
print("================================")

# Problem 2:Count Vowels in a string
print("Problem 2: Count Vowels in a string")
user = input("Enter a Word: ")
vowels = 0
for i in user:
    if i in "aeiouAEIOU":
        vowels += 1
print("Number of vowels in the string is: ", vowels)
print("================================")

# Problem 3: Sum of Digits
print("Problem 3: Sum of Digits")
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(int(input("Enter a only number: "))))
print("================================")