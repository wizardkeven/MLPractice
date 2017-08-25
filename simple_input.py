# class definition zone

class Quit_Loop(Exception):
    pass

# binding action 
def exit(exitComm):
    print('I will {}!'.format(exitComm))
    raise Quit_Loop

class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self,name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n"+self.desc


class Goblin(GameObject):
    class_name = "goblin"
    desc= "A fool creature"

# instantiate class
goblin = Goblin("Gobbly")

# binding action

def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        print(noun)
        print(GameObject.objects)
        return "There is no {} here.".format(noun)
# action
def say(noun):
    return "You said {}".format(noun)


# link verb with action
verb_dict = {
    "say": say,
    "exit":exit,
    "examine": examine,
    }


def get_input():
    command = input(":").split()
    verbo_word = command[0]
    if verbo_word in verb_dict:
        verb = verb_dict[verbo_word]
    else:
        print("Unknown verb: {}".format(''.join(str(e)+' ' for e in command)))
        return

    if len(command) >= 2:
        noun_word = ''.join(str(e)+' ' for e in command[1:-1])+command[-1]
        #noun_word = noun_word.rstrip() #strip the last whitespace as the loop above
                                        #will add  an extra whitespece ate the end of the string
        print(verb(noun_word))
    elif len(command)==1 and command[0]!='say':
        verb(command[0])
    else:
        print(verb("nothing"))

#main loop
try:
    while True:
        get_input()
except Quit_Loop:
    pass
