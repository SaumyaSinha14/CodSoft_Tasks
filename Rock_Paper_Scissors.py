import random

def user_choice():
    choices = ['rock', 'paper', 'scissors']
    u_choice = input("Choose rock, paper, or scissors: ").lower()
    
    while u_choice not in choices:
        print("Invalid choice! Please try again.")
        u_choice = input("Choose rock, paper, or scissors: ").lower()
    
    return u_choice

def comp_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "Hurray!!! You won!"
    else:
        return "Oops! You lost!"

def play_game():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    while play_again.lower() == 'yes':
        choice_user = user_choice()
        choice_comp = comp_choice()
        
        print(f"\nYou chose: {choice_user}")
        print(f"Computer chose: {choice_comp}")
        result = winner(choice_user, choice_comp)
        print(f"Result: {result}\n")
        
        if "won" in result:
            user_score += 1
        elif "lost" in result:
            computer_score += 1
        
        print(f"Scores:\n You: {user_score} | Computer: {computer_score}\n")
        
        play_again = input("Do you want to play again? Yes or No: ")

    print("\nThanks for playing!")
    
if __name__ == "__main__":
    play_game()
