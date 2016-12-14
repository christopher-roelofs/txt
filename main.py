from TxtInterface import *

input = True




while input:
    response = getInput('')
    if response == 'quit':
        quitresponse = getInput('Are you sure you want to quit?')
        if quitresponse.lower() == 'yes':
            input = False
