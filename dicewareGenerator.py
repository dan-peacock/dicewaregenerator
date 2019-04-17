import math

class DicewarePasswordGenerator:
    def __init__(self):
        self.number_of_words = 0
        self.generated_numbers = []
        self.generated_password = []
    
    def take_user_input(self):
        self.number_of_words = int(input("How many diceware words do you want to use? ")) 
        for x in range(self.number_of_words):
            diceware_number = input(f"Enter dice number sequence #{x+1}: ")
            self.generated_numbers.append(diceware_number)

    def find_diceware_words(self):
        wordlist = open('C:/Users/danielpeac/Desktop/diceware/diceware.wordlist.asc', 'r')
        for line in wordlist:
            for x in self.generated_numbers:
                if x in line:
                    diceware_word = line[6:-1]
                    self.generated_password.append(diceware_word)

    def print_password(self):
        for x in self.generated_password:
            print(x, end=" ")

    def calculate_entropy(self):
        length = len(self.generated_password)
        possible = 7776^length
        password_entropy = math.log2(possible)
        total = password_entropy*self.number_of_words
        print()
        print(f"The entropy of your password is {total}")

DicewarePasswordGenerator = DicewarePasswordGenerator()
DicewarePasswordGenerator.take_user_input()
DicewarePasswordGenerator.find_diceware_words()
DicewarePasswordGenerator.print_password()
DicewarePasswordGenerator.calculate_entropy()