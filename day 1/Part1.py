import re;
# read a text file 

list1 = []
list2 = []

# open the file
with open("data.txt", "r") as file:
     # Process the file line by line
    for line in file:
        # Clean the line and split it by whitespace
        numbers = line.split()
        
        # Check if the line contains exactly two elements
        if len(numbers) == 2:
                # Append the numbers (converted to integers) to the respective lists
                list1.append(int(numbers[0]))
                list2.append(int(numbers[1]))


# calculate the sum of the absolute difference between the two lists
total_diff = 0
for i in range(len(list1)):
    total_diff += abs(list1[i] - list2[i])

print(total_diff)