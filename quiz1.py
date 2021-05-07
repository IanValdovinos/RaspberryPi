# Made by Ian Valdovinos for Coursera Peer-graded Assignemtn on IoT

num_list = []

while len(num_list) < 3:
    num_input = int(input("Enter a number: \n\n"))
    num_list.append(num_input)
    print("\n\n")

num_list.sort()

output_string = ""
for num in num_list:
    output_string += str(num) + ", "

output_string = output_string.strip(', ')
print(output_string)


