#numbers = [1, 3, 3, 4, 5, 6, 8]
#print(50 in numbers)
#print(numbers.index(5))
#print(numbers.count(3))
#print(numbers.sort())
#numbers.sort()
#numbers.reverse()
#print(number)


prog = [1, 3, 3, 4, 5, 5, 7]
unique = []
for number in prog:
    if number not in unique:
        unique.append(number)
print(unique)

name = input("Enter your name: ")
game = input(name + " are you down for a quick game: ")
if game.lower() == "yes":

    secret_number = 9
    i = 0
    while i < 3:
       guess = int(input("Guess the lucky digit: "))
       i += 1
       if guess == secret_number:
           print("You win this game! ")
           break
    else:
    print("Sorry, You failed better Luck next time")
else:
    print("Game quited")
    











