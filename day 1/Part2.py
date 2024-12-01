import re;
# read a text file 

list1 = []
list2 = []

# open the file
with open("data.txt", "r") as file:
    for line in file:
        # Clean the line and split by whitespace
        numbers = line.split()
        
        # Check if the line contains exactly two elements
        if len(numbers) == 2:
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))


# calculate the sum of the absolute difference between the two lists
similarity = []
for num1 in list1:
    number_of_similar_by_number = 0
    for num2 in list2:
        if num1 == num2:
            number_of_similar_by_number+=1
    similarity.append(number_of_similar_by_number*num1)

          
        

print(sum(similarity))