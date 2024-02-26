## allows us to use random numbers
import random


## function called guess with paramter x
def guess(x):

  
  ## creates a random number between 1 and x (the paramter taken in from
  ## the function)
  random_number = random.randint(1, x)

  
  ## variable that will store the users guess
  guess_value = 0

  
  ## while the guess is not the random number, follow the set of
  ## instructions in the loop
  
  ## when the condition is false the set of instructions will not run
  while guess_value != random_number:

    
    ## cast the input as an integer because that is the response we want   
    ##from the user
    guess_value = int(input(f'Guess a number between 1 and {x}:'))

    
    ## if the user's guess is less than the random number, print the
    ##message
    if guess_value < random_number:
      print('Sorry, guess again. Too low.')

    
    ## if the user's guess is greater than the random number, print the
    ##message
    elif guess_value > random_number:
      print('Sorry, guess again. Too high.')

  
  ## if the user's guess is equal to the random number, print the message
  
  ## another if statement is not needed because the while loop will stop  
  ## when the guess is equal to the random number
  
  ## the f in front of the '' allows the {number} to be printed as the
  ## actual integer value
  print(f'Yay, congrats. You have guessed the number {random_number} correctly!')




## main function is how the console can output the results of your code
if __name__ == "__main__":
  guess(10)
