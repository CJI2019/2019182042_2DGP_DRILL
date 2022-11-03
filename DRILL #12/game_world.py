#game world

objects = [[], [], []]

def add_object(o,depth):
    objects[depth].append(o)

def remove_object(o,depth):
    objects[depth].remove(o)
    del o

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        del layer

