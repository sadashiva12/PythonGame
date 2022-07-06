import random
import pyttsx3
text_speech=pyttsx3.init()
number=random.randrange(1,50)
guess=int(input('Guess the number between 1 and 50 :'))
text_speech.say(guess)
text_speech.runAndWait()

while guess!=number:
    if guess<number:
        print('You need to guess higher ,Try again')
        text_speech.say('You need to guess higher ,Try again')
        text_speech.runAndWait()
        guess=int(input('Guess the number between 1 and 50 :'))
        text_speech.say(guess)
        text_speech.runAndWait()
    else:
        print('You need to guess lower, Try again')
        text_speech.say('You need to guess lower, Try again')
        text_speech.runAndWait()
        guess=int(input('Guess the number between 1 and 50 :'))
        text_speech.say(guess)
        text_speech.runAndWait()
        
print('You guessed the number correctly')
text_speech.say('You guessed the number correctly')
text_speech.runAndWait()