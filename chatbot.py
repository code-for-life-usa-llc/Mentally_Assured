#Game bot
def main():
    name = input("Hello I am game bot! Whats your name?")
    print (f"Hello {name}")
    question1 = input("What are some game genres you are looking for ? ")
    question2 = input("Are you hoping for a short and easy game or a Long and hard game?")
    question3 = input("Are you looking for a single player game or a multiplayer game?")
    print(f"{question1}")
    print(f"{question2}")
    print(f"{question3}")
    greeting = input (" Great! now that I know what you're looking for let me show you some suggestions. Please choose one of the following choices")
    print (greeting)
    Horror = input('Here are some single player horror games')
    print(Horror)
    choice1 = input(" Choice one: Resident Evil")
    choice2 = input(" Choice two: Silent Hill")
    choice3 = input("Choice three: Five Nights At Freddy's")
    print(f"{choice1}")
    print(f"{choice2}")
    print(f"{choice3}")
    if choice1:
        print (" Link to Resident Evil")
        

    

main()