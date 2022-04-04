#Qn 2b from Wk01 in python
#Switch cases
switch = {
    "CSC1006": "Mathematics 2",
    "CSC1007": "Operating Systems",
    "CSC1008": "Data Structures and Algorithms",
    "CSC1009": "Object Oriented Programming",
    "CSC1010": "Computer Networks"
}

#Prompts the user to input a  module code
module = input("Enter a module code: ")

#Prints the input the user entered and obtains the value from the switch case block
print(switch.get(module))

#Qn 2c from Wk01 in python
#odd number in descending order starting from 102 and ending with 66
for x in range(102, 65, -1):
	if(x%2 != 0):
		print(f'Value of x: {x}')
