#Magic 8 ball
import random
answers = ['It is certain', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Yes-Signs point to yes', 'The gods have refused', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is NO', 'The gods are working on it', 'Outlook not so good', 'Very doubtful']

print('Hello There, I am the Magic 8 Ball, What is your name?')
name = input()
print('Hi ' + name + '...')

def Magic8Ball():
    print('Ask me a question.')
    input()
    print (answers[random.randint(0, len(answers)-1)] )
    print('I hope that helped!')
    Replay()
    

def Replay():
    print ('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('I apologize, I did not get that. Please repeat.')
        Replay()

		
Magic8Ball()
