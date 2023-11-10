import random
import sys

def main():
    # Get a random word.
    answer = getRandomWord()
    attempts = 0
    max_attempts = 6  # Set the maximum number of attempts.
    
    while attempts < max_attempts:
        guess = input('Enter a 5 letter guess?\n')
        
        if len(guess) != 5:
            print("Invalid input. Please enter a 5 letter guess.")
            continue
        
        result = printGuessColors(guess, answer)
        #print(result)
        attempts += 1

        if guess == answer:
            print(f'You Won! That took {attempts} guess(es).')
            break

    if attempts >= max_attempts:
        print(f"You lost. The answer was {answer}.")

def printGuessColors(guess, answer):
    guess_s = ''
    for i in range(len(guess)):
        g = guess[i]
        a = answer[i]

        if g == a:
            guess_s += g
            print(g + ' - Green')
        elif g in answer and g != a and g not in guess_s:
            guess_s += g
            print(g + ' - Yellow')
        elif g not in answer and g not in guess_s:
            guess_s += g
            print(g + ' - Red')
    return 
# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()
