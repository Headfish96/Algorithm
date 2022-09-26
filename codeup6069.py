letter = str(input())
sentence = str()

def lettertosentence():
    if letter == 'A':
        sentence = 'best!!!'
    elif letter == 'B':
        sentence = 'good!!'
    elif letter == 'C':
        sentence = 'run!'
    elif letter == 'D':
        sentence = 'slowly~'
    else:
        sentence = 'what?'
    print(sentence)

lettertosentence()