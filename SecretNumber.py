# HW82: Guess the secret number
secret = 6  # Number to guess
guess = input("Enter a number (between 1 and 20) ? ")  # Benutzereingabe
if int(guess) == secret:
    print("Congratulations !!! You guessed the secret number !!!")
elif int(guess) < secret:
    print("The number you entered is too small!!!")
elif int(guess) > secret:
    print("The number you entered is too large!!!")
