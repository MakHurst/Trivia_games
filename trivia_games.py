
import random


def game():
    print('Hello, Welcome to the game!')

    name = input('What is your name?:\n')

    print(f'Hello {name}, nice to meet you!\n')

    play = int(input('Which game would you like to play?:\n' '1: US Geography Trivia\n' '2: The Office Trivia\n' '3: Naruto Trivia\n'))
    if play == 1:
        geo()
    elif play == 2:
        the_office()
    elif play == 3:
        quit()





def geo(): # Geography game 
    user_points = 0
    user_strikes = 0
    max_strikes = 5
    print('Welcome to the US Geography Quiz Game!\n')

    print('In order to win, you need to get an 80% or greater\n')
    
    while user_strikes < max_strikes:
        q_1 = input('What is the capital of Massachusetts?\n').lower()
        if q_1 == 'boston':
            user_points += 1
            print(f"Correct! Nice Job. You now have {user_points} point(s).")
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).')

        q_2 = input('What is that capital of California?:\n').lower()
        if q_2 == 'sacramento':
            user_points += 1
            print(f"Correct! Nice Job. You now have {user_points} point(s).")
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).')
    
        q_3 = input('What region of the country is Georgia in?:\n' 'A: NorthWest\n' 'B: SouthWest\n' 'C: SouthEast\n' 'D: NorthEast\n').lower()
        if q_3 == 'southeast' or 'c':
            user_points += 1
            print(f"Correct! Nice Job. You now have {user_points} point(s).")
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).')

        q_4 = input("What is the smallest U.S. state?\n").lower()
        if q_4 == 'rhode island':
            user_points += 1
            print(f"Correct! Nice Job. You now have {user_points} point(s).")
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).')

        q_5 = input('What is the LARGEST state in the US?:\n' 'A: Texas\n' 'B: California\n' 'C: Alaska\n' 'D: New York\n').lower()
        if q_5 == 'c' or 'alaska':
            user_points += 1
            print(f'Correct! Nice Job. You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).')

        q_6 = input('Where is Mount Rushmore located":\n').lower()
        if q_6 == 'south dakota':
            user_points += 1
            print(f'Correct! Nice Job. You now have {user_points} point(s).')
        else:
            user_strikes += 1
            print(f'WRONG! You now have {user_strikes} strike(s).')
        q_7 = input('What is the largest lake in the United States?:\n').lower()
        if q_7 == 'lake superior':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f"WRONG! You now have {user_strikes} strike(s).\n")
        q_8 = input('How many states share a boarder with Mexico?:\n')
        if q_8 == '4' or 4:
            user_points += 1
            print(f'Correct! great Job. You now have {user_points} point(s).')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).')
        q_9 = input("Which U.S. state only baorders 1 other?;\n").lower()
        if q_9 == 'maine':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s)')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q_10 = input('Which is the least populated U.S. state?:\n').lower()
        if q_10 == 'wyoming':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s)')
        q_11 = input('What is that capital of Texas?:\n').lower()
        if q_11 == 'austin':
            user_points += 1 
            print(f'Great Job! You now have {user_points} point(s).\n')
            break
        else:
            user_strikes += 1
            print(f'Yikes! You now have {user_strikes} strike(s).\n')
            break
            
    
    if user_strikes >= max_strikes:
        print('You exceeded the number of strikes!\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points < 7:
        print(f' You scored a {user_points}/11.\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points > 7:
        print(f'You scored a {user_points}/11.\n')
        print('Y O U  W I N!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()


    
    
def the_office(): #the office trivia

    print('Hello! Welcome to The Office themed fun!\n')

    difficulty = int(input('Which difficulty would you like to play?\n' '1. Easy\n' '2. Medium\n' '3. Hard\n'))
    if difficulty == 1:
        the_office_easy()
    elif difficulty == 2:
        the_office_medium()
    elif difficulty == 3:
        the_office_hard()
    
    
def the_office_easy(): # easy mode
        
    user_points = 0
    user_strikes = 0
    max_strikes = 5

    print("Let's get started!!!\n")

    while user_strikes < max_strikes:
        q_1 = input('Who started the fire in the office in season 1?:\n').lower()
        if q_1 == 'ryan':
            user_points += 1
            print(f"That's correct!! You now have {user_points} point(s).\n")
        else:
            user_strikes += 1
            print(f'Incorrect!! You now have {user_strikes} strike(s).\n')
        q_2 = input('What season did Michael leave the show?:\n')
        if q_2 == '7' or 7:
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'WRONG!! You now have {user_strikes} strike(s).\n')
        q_3 = input('Who is "Big Tuna"?:\n').lower()
        if q_3 == 'jim':
            user_points += 1
            print(f'Nice Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'SORRY You now have {user_strikes} strike(s).\n')
        q_4 = input('Who does Dwight have an office fling with?').lower()
        if q_4 == 'angela':
            user_points += 1
            print(f'Nice Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q_5 = input('Where does Jim propose to Pam?\n' 'A: Parking lot\n' 'B: Dunder Miflin\n' 'C: a Park\n' 'D: a Gas Station\n').lower()
        if q_5 == 'd' or 'a gas station' or 'gas station':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'YIKES! Incorrect! You now have {user_strikes} strikes.\n')
        q_6 = input('WHat Ivy league school did Andy go to?\n').lower()
        if q_6 == 'cornell':
            user_points += 1
            print(f'You are killin it! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q_7 = input('How many seasons are there of The Office?\n').lower()
        if q_7 == '9' or 9:
            user_points += 1
            print(f'Wonderful job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q_8 = input("What is the name of Angela's favorite cat?\n" 'A: Sprinkles\n' 'B: Kitty\n' 'C: Sweetie\n' 'D: Minnie\n').lower()
        if q_8 == 'a' or 'sprinkles':
            user_points += 1
            print(f'Amazing job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q_9 = input("Which character did Michael go to high school with?\n").lower()
        if q_9 == 'phyllis':
            user_points += 1
            print(f'Nice Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q_10 = input('What was the name of the company everyone worked for?\n')
        if q_10 == 'dunder miflin':
            user_points += 1
            print(f'Nice Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
   
    
    if user_strikes >= max_strikes:
        print('You exceeded the number of strikes!\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points < 7:
        print(f' You scored a {user_points}/10.\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points > 7:
        print(f'You scored a {user_points}/10.\n')
        print('Y O U  W I N!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()

        
    
def the_office_medium(): # medium mode
        user_points = 0
        user_strikes = 0
        max_strikes = 5
        
        print("Let's get started!!!")

        while user_strikes < max_strikes:
            q_1 = input('Who was the first person to be cast?\n').lower()
            if q_1 == 'bj novak':
                user_points += 1
                print(f'Nice Job!!! You now have {user_points} point(s).\n')
            else:
                user_strikes += 1
                print('Incorrect! You now have {user_strikes) strike(s).\n')
            q_2 = input('Who does Kevin get for secret santa in the christmas party episode?\n').lower()
            if q_2 == 'himself':
                user_points += 1
                print(f'Nice Job! You now have {user_points} point(s).\n')
            else:
                user_strikes += 1
                print(f'SORRY You now have {user_strikes} strike(s).\n')
            q_3 = input('Who says the quote: "Guess what, I have flaws. What are they? Oh, I dont know. I sing in the shower.\nSometimes I spend too much time volunteering. Occasionally Ill hit somebody with my car.\nSo sue me... No, dont sue me. That is the opposite of the point that Im trying to make.?"\n').lower()
            if q_3 == 'Michael' or 'michael scott':
                user_points += 1
                print(f'You are doing great! You now have {user_points} point(s).\n')
            else:
                user_strikes += 1 
                print(f'Incorrect! you now have {user_strikes} strike(s)!\n')
            q_4 = input('Where does Michael Scott move to start his new life with Holly?\n').lower()
            if q_4 == 'denver' or 'colorado':
                user_points += 1
                print(f'Correct! You now have {user_points} point(s).\n')
            else:
                user_strikes += 1
                print(f'WRONG!! You now have {user_strikes} strike(s).\n')
            q_5 = input("What is Michael Scott's middle name?").lower()
            if q_5 == 'gary':
                user_points += 1
                print(f'You are doing great! Yoou now have {user_points} point(s)')
            else:
                user_strikes += 1
                print(f'Incorrect! You now have {user_strikes} strike(s).')
            q_6 = input('Who gave Michael the Worlds Best Boss mug?\n').lower()
            if q_6 == 'himself' or 'michael':
                user_points += 1
                print(f'Correct! You now have {user_points} point(s).\n')
            else:
                user_strikes += 1
                print(f'WRONG!!! You now have {user_strikes} strike(s).\n')
            q_7 = input("Who dates Pam's mother?:\n"'A; Michael\n' 'B; Creed\n' 'C: Dwight\n').lower()
            if q_7 == 'michael' or 'a':
                user_points += 1
                print(f'Great Job! You now have {user_points} point(s)\n.')
            else:
                user_strikes += 1
                print(f'Yikes! that is incorrect! You now have {user_strikes} strike(s).\n')
            q_8 = input('How many brothers does Jim Halpert have?:\n').lower()
            if q_8 == '2' or 2 or 'two':
                user_points += 1
                print(f'You are correct! You now have {user_points} points.\n')
            else:
                user_strikes += 1
                print(f'WRONG! You now have {user_strikes} strike(s).\n')
            q_9 = input("What is Plop's actual name? (The intern):\n" ).lower()
            if q_9 == 'pete':
                user_points += 1
                print(f'Correct! You now have {user_points} point(s).\n')
            else:
                user_strikes += 1
                print(f'Wrong! Yiu now gave {user_strikes} strike(s).\n')
            q_10 = input("Who did Michael take with him to Jamaica?\n").lower()
            if q_10 == 'jan':
                user_points += 1
                print(f'Nice Job! You now have {user_points} point(s).\n')
                break
            else:
                user_strikes += 1
                print(f'That is incorrect! You now have {user_strikes} strike(s).\n')
                break
        
        if user_strikes >= max_strikes:
            print('You exceeded the number of strikes!\n')
            print('Y O U  L O S E!!!\n')
            play_again = int(input('Do you want to play again?' '1: Yes\n' '2: No\n'))
            if play_again == 1:
                game()
            elif play_again == 2:
                quit()
        if user_points < 7:
            print(f' You scored a {user_points}/10.\n')
            print('Y O U  L O S E!!!\n')
            play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
            if play_again == 1:
                game()
            elif play_again == 2:
                quit()
        if user_points > 7:
            print(f'You scored a {user_points}/10.\n')
            print('Y O U  W I N!!!\n')
            play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
            if play_again == 1:
                game()
            elif play_again == 2:
                quit()



def the_office_hard(): # hard mode 
    user_points = 0
    user_strikes = 0
    max_strikes = 5

    while user_strikes <= max_strikes:
        q_1 = input('Who created the game "suck it" that was eventually purchased by the military?:' 'A: Robert Californa\n' 'B: Toby\n' 'C: Todd Packer\n' 'D: David Wallace\n').lower()
        if q_1 == 'd':
            user_points += 1
            print(f'Great Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You have {user_strikes} strike(s).\n')
        q_2 = int(input('Schrute boys must learn how many rules by the age of 5?:\n'))
        if q_2 == 40:
            user_points += 1
            print(f'Nice! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Not quite! You now have {user_strikes} strike(s).\n')
        q_3 = input("What is the name of Michael's old boss?:\n").lower()
        if q_3 == 'ed truck' or 'ed':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q_4 = int(input('How much does Bob Vance bid on a hug from his wife Phyllis?:\n'))
        if q_4 == 1000:
            user_points += 1
            print(f'You are Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Nope! You now have {user_strikes} strikes.\n')
        q_5 = input("What is Pam's favorite yogurt flavor?\n").lower()
        if q_5 == 'mixed berry':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strikes.\n')
        q_6 = input('Michael likes waking up to the smell of what?:\n').lower()
        if q_6 == 'bacon':
            user_points += 1
            print(f'Great job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'You are wrong! You now have {user_strikes} strike(s).\n')
        q_7 = input('Who does Kevin get for secret santa?:\n')
        if q_7 == 'kevin' or 'himself':
            user_points += 1
            print(f'You are right! You now have {user_points} point(s).\n')    
        else:
            user_strikes += 1
            print(f'You guessed incorrectly! You now have {user_strikes} strike(s).\n')
        q_8 = input("What was the name of Pam's ex fiance?\n").lower()
        if q_8 == 'roy':
            user_points += 1
            print(f'You are correct! You now have {user_points} point)s_.\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q_9 = input('What billionare appeared in the season finale?\n').lower()
        if q_9 == 'warren buffett' or 'buffett':
            user_points += 1
            print(f'Great Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q_10 = input('What was the name of the character Will Ferrell play?\n').lower()
        if q_10 == 'deangelo vickers':
            user_points += 1
            print(f'Nice Job! You now have {user_points} points.\n')
            break
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
            break
    
    if user_strikes >= max_strikes:
        print('You exceeded the number of strikes!\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points < 7:
        print(f' You scored a {user_points}/10.\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points > 7:
        print(f'You scored a {user_points}/10.\n')
        print('Y O U  W I N!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()

        
    
def naruto():
    print('Hello, Welcome to the Naruto Trivia Game!\n')
    difficulty = int(input('Which difficulty would you like to play on?\n' '1: Easy\n' '2: Medium\n' '3: Hard\n'))
    if difficulty == 1:
        naruto_easy()
    elif difficulty == 2:
        naruto_medium()
    elif difficulty == 3:
        pass

def naruto_easy():
    user_points = 0
    user_strikes = 0
    max_strikes = 5
    print("OK! Let's begin!\n")
    while user_strikes <= max_strikes:
        q1 = input("Who is Naruto's father?:\n" 'A: Kakashi\n' 'B: Gara\n' 'C: Donzo\n' 'D: Minato\n').lower()
        if q1 == 'minato' or 'a':
            user_points += 1
            print(f'Great Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'IOncorrect! You now have {user_strikes} strike(s).\n')
        q2 = input("What is Sasuke's brother's name?:").lower()
        if q2 == 'itachi':
            user_points += 1
            print(f'You are correct! You now have {user_points} pint(s)\n.')
        else:
            user_strikes += 1
            print(f'WRONG!! You now have {user_strikes} strike(s).\n')
        q3 = input('What does Naruto have inside him?\n' 'A; a dragon\n' 'B; The 9 Tails\n' 'C: Love\n' 'D: The 8 Tails\n').lower()
        if q3 == 'b' or 'the 9 tails':
            user_points += 1
            print(f'You are correct! You have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q4 = input("What is Naruto's favorite food?\n").lower()
        if q4 == 'ramen':
            user_points += 1
            print(f'Youre doing great! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Not quite! You now have {user_strikes} strike(s).\n')
        q5 = input("Who is Naruto's first love?\n").lower()
        if q5 == 'sakura':
            user_points += 1 
            print(f'Great Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'WRONG! You now have {user_strikes} strike(s).\n')
        q6 = input('Who is the 6th Hokage?\n').lower()
        if q6 == 'kakashi':
            user_points += 1
            print(f'Nice Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q7 = input(f'Who does Naruto want to bring back to the Leaf Village?\n').lower()
        if q7 == 'sasuke':
            user_points += 1
            print(f'You are correct! You nmow ahve {user_points} strike(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrct! You now have {user_strikes} strike(s)')
        q8 = input('How many times did Naruto fail the garduation test at the academy?\n').lower()
        if q8 == '3' or 'three':
            user_points += 1
            print(f'Amazing! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Nope! You now have {user_strikes} strike(s).\n')
        q9 = input('Who did Kakashi get his eye from?\n' 'A: Donzo\n' 'B: Obito\n' 'C: Itachi\n' 'D: Madara\n').lower()
        if q9 == 'obito' or 'b':
            user_points += 1
            print(f'You are doing amazing! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q10 = input('What does Naruto wear before he becomes a Genin?\n').lower()
        if q10 == 'goggles':
            user_points += 1
            print(f'Good Job! You now have {user_points} ppoint(s).\n')
        else:
            user_strikes += 1
            print(f'Almost! You now have {user_strikes} strike(s).\n')
        

    if user_strikes >= max_strikes:
        print('You exceeded the number of strikes!\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points < 7:
        print(f' You scored a {user_points}/10.\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points > 7:
        print(f'You scored a {user_points}/10.\n')
        print('Y O U  W I N!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()

def naruto_medium():
    user_points = 0
    user_strikes = 0
    max_strikes = 5
    print('Okay! Lets Begin!')
    while user_strikes <= max_strikes:
        q1 = input('Who held Naruto hostage when he was born?\n').lower()
        if q1 == 'madara':
            user_points += 1
            print(f'That is correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q2 = input('Who does NOT have Kekkei Genkai?\n').lower()
        if q2 == 'naruto':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q3 = input('Who killed Donzo?\n').lower()
        if q3 == 'sasuke':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} stike(s).\n')
        q4 = input("What is Sasuke's Kekkei Genkai?\n").lower()
        if q4 == 'sharingan':
            user_points += 1
            print(f'Great Job! You now have {user_points} point(s).')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q5 = input('Who summoned the five kage for the five kage summit?\n').lower()
        if q5 == 'raikage':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q6 = input("Who was the Sannin's sensei?\n").lower()
        if q6 == 'sarutobi' or 'the 3rd hokage':
            user_points += 1
            print(f'Nice Job! You now have {user_points} point(s).')
        else:
            user_strikes += 1
            print(f'Incorrect! You now have {user_strikes} strike(s).\n')
        q7 = input('Which legendary Sannin became Hokage?\n').lower()
        if q7 == 'tsunade' or 'lady tsunade':
            user_points += 1
            print(f'You are correct! You now ahve {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q8 = input('How many ninja made it to the third stage of the Chunin Exam').lower()
        if q8 == '5' or 'five':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        q9 = input("Who is Naruto's biggest enemy?\n").lower()
        if q9 == 'sasuke':
            user_points += 1
            print(f'Correct! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Wrong! You now have {user_strikes} strike(s).\n')
        q10 = input('Are there two types of Jounin?\n' 'A: Yes\n' 'B: No\n').lower()
        if q10 == 'yes' or 'a':
            user_points += 1
            print(f'Nice Job! You now have {user_points} point(s).\n')
        else:
            user_strikes += 1
            print(f'Incorrect! you now have {user_strikes} strike(s).\n')
        
    
    if user_strikes >= max_strikes:
        print('You exceeded the number of strikes!\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points < 7:
        print(f' You scored a {user_points}/10.\n')
        print('Y O U  L O S E!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 2:
            quit()
    if user_points > 7:
        print(f'You scored a {user_points}/10.\n')
        print('Y O U  W I N!!!\n')
        play_again = int(input('Do you want to play again?\n' '1: Yes\n' '2: No\n'))
        if play_again == 1:
            game()
        elif play_again == 3:
            quit()

        



game()