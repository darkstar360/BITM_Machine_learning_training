names = []


def take_names():
    '''funtion to take names'''
    while True:
        inp = input('Enter a name (enter "*" to go next step): ')
        if inp == '*':
            break
        names.append(inp)


def greetings(name):
    '''return greetings'''
    return 'Greetings {}'.format(name)


take_names()
for name in names:
    print(greetings(name))
