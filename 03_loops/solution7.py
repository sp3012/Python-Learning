<<<<<<< HEAD
# validate input
# Keep  asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter any Number to play Guess game: "))

    if 1 <= number <= 10:
        print(f"Congratulations you guessed {number}")
        break
    else:
=======
# validate input
# Keep  asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter any Number to play Guess game: "))

    if 1 <= number <= 10:
        print(f"Congratulations you guessed {number}")
        break
    else:
>>>>>>> 1572a0ca7fbf37fdd673ee612c85c19d878933a9
        print("Sorry, Try again!")