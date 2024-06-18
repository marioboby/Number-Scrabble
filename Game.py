''' Purpose: This code is for the game Number Scrabble. 
             Each player takes turns picking a number from 1 to 9. 
             Once a number has been picked, it cannot be picked again.
             If a player has picked three numbers that add up to 15, that player wins the game. 
             If all the numbers are used and no player gets exactly 15, the game is a draw.'''
# Author: Mario Saber Shawqy 

# Function to check if a player has selected three numbers that add up to 15, to check for a win
def check_winner(player_numbers):
    # A Nested Loop, with each loop goes through each number "i" of the player's and the inner loop for each number after "i" 
    for i in range(len(player_numbers)): 
        for j in range(i + 1, len(player_numbers)):
            for k in range(j + 1, len(player_numbers)):
                if player_numbers[i] + player_numbers[j] + player_numbers[k] == 15:
                    return True
    return False

# Main function for the Number Scrabble game
def number_scrabble():
    # Set of numbers available for selection
    numset = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Lists to store numbers selected by each player
    player1_numbers = []
    player2_numbers = []

    print('Welcome to Number Scrabble!')
    print('')
    print('Each player takes turns picking a number from 1 to 9.')
    print('Once a number has been picked, it cannot be picked again.')
    print('If a player has picked three numbers that add up to 15, that player wins the game.')
    print('If all the numbers are used and no player gets exactly 15, the game is a draw.')
    print('')

    # Main game loop
    while numset:


        # Player 1's turn

        # Displays the available numbers for each player before their turn
        print("Available numbers:", numset)  
        while True:
            num1 = input('Player one, please pick a number: ')
            # Checks the validaty of the input
            if num1.isdigit() and int(num1) in numset:  
                # Converts the string input to integer  
                num1 = int(num1)
                # Removes the selected number from numset if valid input
                numset.remove(num1)
                # Adds selected number to the Player's respective set and ends his turn
                player1_numbers.append(num1)
                break
            else:
                print('Please enter a valid or available number.')

        # Check if Player 1 has won
        if check_winner(player1_numbers):
            print("Player 1 wins!")
            return
        # Check for a draw if all numbers are used
        if numset==[]:
            print("Draw!")
            break


        # Player 2's turn

        #The same goes for player 2
        print("Available numbers:", numset)
        while True:
            num2 = input('Player two, please pick a number: ')
            if num2.isdigit() and int(num2) in numset:
                num2 = int(num2)
                numset.remove(num2)
                player2_numbers.append(num2)
                break
            else:
                print('Please enter a valid or available number.')

        # Check if Player 2 has won
        if check_winner(player2_numbers):
            print("Player 2 wins!")
            return
        

# Start the Number Scrabble game
number_scrabble()
