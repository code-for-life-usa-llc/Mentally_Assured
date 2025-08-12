#Chat Bot

def main():
    name = input("Hello I'm Chat bot! Whats your name?")
    print (f"Hello!{name}")
    question1 = input(" would you care to join me in a conversation (Y/N):").upper()
    if question1 != 'Y':
     print ("..........")
    print("Proceeding!")
    print ("..........")

    question0= input ("lets start of with some simple questions")
    print ({question0})
    print ("..........")

    print ("..........")
    question2 = input("whats your favorite color?")
    print ({question2})
    print ("..........")

    print ("..........")
    question3 = input("whats your favorite animal?")
    print(question3)
    print ("..........")

    print ("..........")
    question4 = ("What do you wanna be when your older?")
    print(question4)
    print ("..........")

    print ("..........")
    question5 = ("Do you have any siblings?")
    print(question5)
    print ("..........")

    print ("..........")
    question6 = ("How many friends do you have?")
    print (question6)
    print ("..........")
 
main()