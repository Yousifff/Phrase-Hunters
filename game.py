# Create your Game class logic in here.


import phrase

import random
class Game:
    
    def __init__(self) -> None:
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
    
        self.guesses = []
        
        
    def create_phrases(self):
        return [phrase.Phrase('hello world'),
                phrase.Phrase('there is no trying'),
                phrase.Phrase('may the force be with you'),
                phrase.Phrase('you have to see the matrix for yourself'),
                phrase.Phrase('life is like a box of chocolates')]
        
    def get_random_phrase(self):
        
        return random.choice(self.phrases)
        
    def reset_the_game(self):
        self.missed = 0
        self.guesses = [" "]
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        
    def get_guess(self):
        get_letter = input("Enter a character : ").lower()
        if len(get_letter) > 1:
            raise Exception("one character is allowed!\n")
        
        if get_letter.isnumeric():
            raise ValueError("Numbers aren't allowed, please enter letter from a - z\n")
        
        return get_letter
    
 
    def welcome(self):
        print("="*20)
        print("   Phrase Hunter    ")
        print("="*20)
        
    def start(self):
        
        user_guess = ""
        while True:
           
            self.welcome()
            try:
                user_guess = self.get_guess()
                self.guesses.append(user_guess)
            except Exception as err:
                print(f'{err}')
            except ValueError as vr:
                print(f'{vr}')
           
       
            
         
            self.active_phrase.display(self.guesses)
            if not self.active_phrase.check_phrase(user_guess):
                self.missed = self.missed + 1
            print(f'\n\nNumber Missed: {self.missed}')
            if self.game_over():
                get_input = input("Would you like to start a new game?(y,n) : ")
                if get_input.lower() == 'y':
                    self.reset_the_game()
                else:
                    print("Hope you enjoy the game, buy buy!!")
                    break
    
    def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            print("You win the game")
            return True
        elif self.missed == 5:
            print("You lost the game.")
            return True
        else:
            return False        