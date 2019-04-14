import random
import emoji
from tkinter import *
from tkinter import messagebox

print('Hello new user what is your name?')
name = input('')
print('well hey there ' + name)
print('do you want to play a game that I created?? \nyes/no')

list_no = ['no', 'n', 'nope', 'never', 'na', 'nah', 'nawt', 'no way']
list_yes = ['yes', 'sure', 'y', 'ok', 'k', 'ya', 'yup', 'yeah', 'okey dokey', 'mmhmm', 'for sure']

want_to_play = input('')

if want_to_play in list_no:
    print('you stink and I dont care you are playing')
elif want_to_play in list_yes:
    print('yay, lets start a simple number game where you will guess what number I am thinking of')
elif want_to_play not in list_yes or list_no:
    print('that wasnt appropriate and you should quit now, but you will play anyways')

print('before we go any further I would like to ask you another question \nHow old are you ' + name + '?')

while True:
    try:
        age = int(input())
    except ValueError:
        print('thats not a number')
        continue
    else:
        break

if int(age) >= 25:
    print('your getting pretty old to be playing with computers')
    print(emoji.emojize('lol :thumbs_up:'))
if int(age) <= 25:
    print('you should be at work or doing something better with your time')
    print(emoji.emojize('lol :thumbs_up:'))

num = random.randint(1,int(age))
print('so I think we should make this game range all the way up to your age')

tries = len(name)
print('we will also use the number of letters in your name for your guessing limit: ' + str(tries))

print('I am thinking of a number between 1 - ' + str(age))
print('take any guess you want')

counter = 1

play = True
while play:

    guess = input('')
    guess = int(guess)

    if tries == counter - 1:
        print('youve taken up all the guesses you could use: ' + str(tries))
        print('the number was ' + str(num))
        break

    if guess < num:
        counter += 1
        print('no, please try again and guess higher')

    if guess > num:
        counter += 1
        print('no, please try again and guess lower')

    if guess == num:
        print('that is correct')
        print('the number was ' + str(num))
        print('and it took you ' + str(counter) + ' tries to get it!')
        window = Tk()
        window.lift()
        window.attributes('-topmost', True)
        window.title('THE WINNING NUMBER ' + str(num))
        btn = Button(window, text='winner winner chicken dinner', font=('Bold, 63'))
        btn.grid(row=0, column=0)
        messagebox.askyesno('Questionaire', name + ' did you enjoy the game?')
        window.destroy()
        break

print('keep it up')


