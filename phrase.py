# Create your Phrase class logic here.
class Phrase:
    def __init__(self,phrases) -> None:
        self.phrases = phrases
        
    def __str__(self) -> str:
        return f'{self.phrases}'
    
    def display(self,guesses):
        for letter in self.phrases:
            if letter in guesses:
                print(letter,end=" ")
            elif letter == " ":
                print(" ",end=" ")
            else:
                print("_",end=" ")  
        
        print()
    
                
    def check_phrase(self,guess):
        if guess not in self.phrases:
            return False
     
        return True
    
    def check_complete(self,guesses):
        
        for letter in self.phrases:
            if letter not in guesses:
                return False
            
        return True
        
                
                