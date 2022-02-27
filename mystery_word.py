import random


def play_game():
        #what is the next step after connecting to iTerm2
        #this line of code allows it to display text
    with open("test-word.txt") as test_word:
        words = test_word.read()
        test_word = list(map(str, words.split()))
        random_word = random.choice(test_word)
        print(test_word)
        print(random_word)
        #add input 
        # what line of code would help me tell the user how many turns they have to guess the word
        intro = input("would you like to play a game? y/n ").lower()
        if intro == "y":
            intro2 = input("which level would you like to play? 1,2,3 ")
            print("Your word is", len(random_word), "letters")
        if intro == "n":
            print("Have a nice day!")
            exit()
        count = 8
        letter_placement = len(random_word) * "_"
        while count > 0:
            answer = input("please only input one letter per spot ").casefold()
            #check if the input is in random_word
            #for letter  in random_word:
            if len(answer) > 1:
                print("you can't do that!!")
            if answer in random_word:
                print("your guess is correct")
            if answer not in random_word:
                print("incorrect")
    
            
            
                
            
        
        print(random_word)
        
        
        
    
    
    pass


if __name__ == "__main__":
    play_game()
