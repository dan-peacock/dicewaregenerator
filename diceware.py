# Ask user how many diceware words they will use
length = int(input("How many diceware words do you want to use? "))

# Ask user for diceware input
numberList = []
for x in range(length):
    value = input(f"Enter number combination #{x+1}: ")
    numberList.append(value)

# Search diceware list for the user inputs
files = open('C:/Users/danielpeac/Desktop/diceware/diceware.wordlist.asc', 'r')

password = []
for line in files:
    for x in numberList:
        if x in line:
            word = line[6:-1]
            password.append(word)

# Print the final generated password
for x in password:
    print(x, end=" ")
