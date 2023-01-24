"""
with open("todos.txt",'w') as file:
    file.writelines("")
"""
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    # doc strings je opis funkcije koje se pojavljuje na kmandu help (funkcija)
    """ Read a text file and return list of
    to-do items"""
    with open(filepath, 'r') as file_local:
          todos_local = file_local.readlines()
    return todos_local

print(help(get_todos))

# Donja funkcija se ponaša kao procedura, jer ne vraća vrijednost
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list in text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)

# donji set naredbi definise izvrsenje samo unutar functions2 modula
if __name__ == "__main__":
    print("Hello from functions2.")
    print(get_todos())