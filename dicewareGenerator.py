import math
import requests
import os

class DicewarePasswordGenerator:
    def __init__(self):
        self.number_of_words = 0
        self.generated_numbers = []
        self.generated_password = []
        self.path = os.path.dirname(__file__)
    
    def take_user_input(self):
        self.number_of_words = int(input("How many diceware words do you want to use? ")) 
        for x in range(self.number_of_words):
            diceware_number = input(f"Enter dice number sequence #{x+1}: ")
            if len(diceware_number)>5:
                print("Please enter a 5 digit number.")
                diceware_number = input(f"Enter dice number sequence #{x+1}: ")
            else:
                self.generated_numbers.append(diceware_number)

    def download_diceware_list(self):
        url = 'http://world.std.com/~reinhold/diceware.wordlist.asc'
        r = requests.get(url, allow_redirects=True)
        open('diceware2.wordlist.asc', 'wb').write(r.content)

    def find_diceware_words(self):
        self.finalpath = self.path+'/diceware2.wordlist.asc'
        wordlist = open(self.finalpath, 'r')
        for line in wordlist:
            for x in self.generated_numbers:
                if x in line:
                    diceware_word = line[6:-1]
                    self.generated_password.append(diceware_word)

    def print_password(self):
        print("Your password is:", end=" ")
        for x in self.generated_password:
            print(x, end=" ")

    def calculate_entropy(self):
        sum = 0
        for x in range(len(self.generated_password)):   
            sum += len(self.generated_password[x])
        password_length = sum + (len(self.generated_password) - 1)
        password_entropy = math.log2(7776**password_length)
        print(f"\nThe entropy of your password is {password_entropy}")