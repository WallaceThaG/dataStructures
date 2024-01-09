# read 6 numbers into an array and output them in reverse order, then output total and average
# array array[6]
array = [0,0,0,0,0,0]
for i in range(6):
    array[i] = input("Enter number: ")
# iterate backwards through the array
for j in range((len(array)-1), -1, -1):
    print(array[j])
    