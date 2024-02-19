string = input("Enter string: ")
numChars = len(string)
stack = [""] * numChars

for i in range(numChars, 0, -1):
    stack[i - 1] = string[numChars - (i)]
    print(stack)
if stack == list(string):
    print("Palindrome")
else:
    print("Not palindrome")