print('Hello, Django girls!')
if 3 > 2:
    print('It works!')
    if 5 > 2:
        print('5 is indeed greater than 2')
    else:
        print('5 is not greater than 2')
name = 'Vanessa'
if name == 'Nina':
    print('Hey Nina!')
elif name == 'Vanessa':
    print('Hey Vanessa!')
else:
    print('Hey anonymous!')
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")# What's going on?
if volume < 20 or volume > 80:
    volume = 50
    print("That's better!")
def hi(name):
    print ("hallo " + name)
    print ("i am ready")
hi("sybil")
hi("anna")
hi("bill")
def Treffpunkt(location):
    print ("let's meet in " + location)
Treffpunkt("Bern")
Treffpunkt("Solothurn")
Treffpunkt("Basel")
