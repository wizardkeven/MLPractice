def get_input():
    command = input(":").split()
    verbo_word = command[0]
    if verbo_word in verb_dict:
        verb = verb_dict[verbo_word]
    else:
        print("Unknown verb: {}".format(''.join(str(e)+' ' for e in command)))
        return

    if len(command) >= 2:
        noun_word = ''.join(str(e)+' ' for e in command[1:])
        print(verb(noun_word))
    elif len(command)==1 and command[0]!='say':
        verb(command[0])
    else:
        print(verb("nothing"))


# action

def say(noun):
    return "You said {}".format(noun)

class Quit_Loop(Exception):
    pass
# quit
def exit(exitComm):
    print('I will {} !'.format(exitComm))
    raise Quit_Loop

# link verb with action

verb_dict = {
    "say": say,
    "exit":exit,
    }

try:
    while True:
        get_input()
except Quit_Loop:
    pass
