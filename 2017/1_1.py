with open('1_input.txt') as f:
    data = f.read()

data = data.rstrip() # Remove trailing newline

total_sum = 0

# Check all digits to see if they are equal to the digit directly after it
for i in range(len(data)-1):
    if data[i] == data[i+1]:
        total_sum += int(data[i])

# Don't forget to compare the first and last digits
if data[0] == data[-1]:
    total_sum += int(data[0])

print("The sum is: " + str(total_sum))
