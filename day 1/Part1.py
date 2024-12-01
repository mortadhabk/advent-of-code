import re;
# read a text file 

list1 = []
list2 = []

# open the file
with open("data.txt", "r") as file:
        # read the file
        data = file.read()
        # split the file into lines
        lines = data.split("\n")
        # split by space 
        for line in lines:
            # Delete all the white space between the words
            # The \s is a shorthand character class in regular expressions that matches any whitespace character, including spaces, tabs, and newline characters. The + quantifier means "one or more" of the preceding element, so \s+ matches one or more consecutive whitespace characters.
            numbers = re.split(r'\s+', line)
            if len(numbers) == 2:
                    list1.append(numbers[0])
                    list2.append(numbers[1])

        # trier les deux listes 
        list1.sort()
        list2.sort()
        # close the file
        file.close()


# calculate the sum of the absolute difference between the two lists
total_diff = 0
for i in range(len(list1)):
    total_diff += abs(int(list1[i]) - int(list2[i]))

print(total_diff)