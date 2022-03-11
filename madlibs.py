noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
pnoun = input("Enter a plural noun: ")
bodypart = input("Enter a body part: ")
number = int(input("Enter a whole number: "))
place = input("Enter a place: ")
ingverb = input("Enter a verb ending with ing: ")

def madlib1():
    print ("I love " + noun + " because it is " + adjective + 
    ". I do not love " + pnoun + " because they never provide me with peace of " 
    + bodypart + ". I hate " + pnoun + " " + str(number) + " times more than fishing." +
    " I like to fish at " + place + ". Fishing is like " + ingverb + ".")

def madlib2():
    print ("It was a " + adjective + " March day. I woke up to the sound of my "
    + noun + ". I got up to see where it was coming from, when I heard about some "
    + pnoun + " attacking " + place + ". It was " + ingverb + " seeing them attack. "
    + " The " + pnoun + " were the size of " + str(number) + " skyscrapers" + "! " +
    "Oh well, it's not my problem. Now i'll itch my " + bodypart + ".")

def madlib3():
    print ("I was playing with my " + noun + " when I suddenly heard the " + adjective
    + " sound. I went to explore the sound, and figured out that it was coming from "
    + place + ". On the way there, I saw some " + pnoun + ". They ran up to me and chopped off my "
    + bodypart + "! This pain hurt " + str(number) + " times more than an ACL tear. I shook off the pain, and started " +
    ingverb + " with some of my friends.")

storynumber = input(" Which story would you like to play? (1, 2, 3, or q): ")

if storynumber == "1":
    madlib1()
elif storynumber == "2":
    madlib2()
elif storynumber == "3":
    madlib3()
elif storynumber == "q":
    print("You have succesfully quit")
else:
    print("Invalid input. Click run and choose again")
