import random

print('So, you call yourself a paddler? Lets see you survive this...')
print(r"Let's play 'Boat, Rocks, River'. Boats conquor rivers, rivers move rocks and rocks destroy boats. Let's see how you fair")

while True:
    print(r"Please choose 'Boat', 'rock' or 'river'.")

    choices = ['boat', 'river', 'rock']

    userChoice = str.lower(input())
    pcChoice = random.choice(choices)

    for choice in choices:
        if choice == userChoice:
            print('The computer chose ' + "'" + pcChoice + "'")
        else:
            break

    if userChoice == pcChoice:
        print(r"It's a tie! We both chose " + userChoice)

    elif userChoice == 'boat':
        if pcChoice == 'river':
            print('Congrats! You conquored the river')
        else:
            print('You wrapped around a rock. Now walk back to civilazation and think about what you did.')

    elif userChoice == 'river':
        if pcChoice == 'boat':
            print('You just got conquored by a scrawny paddler in a piece of fibre glass. How shameful')
        else:
            print('Rocks may be big, but your perserverence puts them in their place. Well done')

    elif userChoice == 'rock':
        if pcChoice == 'boat':
            print('Well done! Those fibreglass boats are no match for your might! Stand Proud!')
        else:
            print('You just got pushed around by some water. I thought you were supposed to be so big and strong. Shame')

    else:
        print('You need to enter a valid option')

    playAgain = input('Play again? (y/n): ')
    if playAgain.lower() != 'y':
        break
