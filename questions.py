""" Porque usar funções? """
def welcome():
    print("Welcome to test..")
    input("When you are ready press enter..")

def ask_questions(ask_collor=False):
    name = input("name:")
    print(f"It is nice to meet you {name}")
    color = input("What is your favorite color?")
    print(f"{color} is a great color!")
    input("Describe yourself")
    print("admirable!")

def goodbye():
    print("Goodbye.")

welcome()
ask_questions(ask_collor=True)
goodbye()
