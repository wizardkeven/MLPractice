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

    def __init__(self,name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off."
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self,value):
        self._desc = value

# hit goblin with one point harm
def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health -= 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
        else:
            msg = "I'm not strong enough, I can only hit goblin."
    else:
        msg = "There is no {} here.".format(noun)
    return msg

# help the wounded goblin get one point energy
def help(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            if thing.health+1<= 3:
                thing.health+=1
                msg = "You just help the {} get 1 health!".format(noun)
            else:
                msg = "The {} is quite healthy!".format(noun)
    return msg
            
            

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
    "hit":hit,
    "help":help,
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
