from sys import exit

def ruby_room():
	print "\nYou enter a room filled with beautiful rubies and amethysts."
	print "You can take as many shiny gems as you'd like, O wise wizard, but..."
	print "If you take too many you will awaken The Mummy!!!"
	print "But if you take too few, you will live your life in poverty and starve.."
	print "How much do you take, wizard?"

	choice = raw_input(">>> ")
	how_much = int(choice)

	if how_much > 0:
		dead("The thing about the mummy was a lie -- the gems were snakes! bite bite dead!")
	elif how_much == 0:
		print "\nSo you knew that the curse of the Mummy was a lie, eh?"
		print "You also knew that all of the gems were actaully just snakes?"
		print "You are truly the wisest wizard in all the land!"
		print "A large stone door rolls to the side and you walk out into the sunlight"
		print "still the wisest wizard in all the land! HUZZAH! HUZZAH! HUZZAH!"
		exit(0)
	else:
		print "Perhaps the peasants should call you the FOOLISH wizard!"

def dead(why):
	print why, "lol"
	exit(0) 

def start():
	print "======================="
	print "\nWELCOME ADVENTURER TO THE WIZARD'S JOURNEY!"
	print "\nA GAME TO TEST YOUR WIT AND YOUR METTLE!"
	print "\nTRAVEL ALONG CORRIDORS AND THRU DARK AND TREACHEROUS DUNGEONS"
	print "WITH YOUR FAITHFUL TOADIE!"
	print "\nGOODLUCK! (and know that if you die in the game you die in real life!)"
	print "\n======================="


	print "\nYou, the wisest wizard, wake up groggy in a dark room. 'Where am I?' you ask."
	print "Wise question, m'lord."
	print "You are in Hell I believe...I have been assigned your toadie and your guide on"
	print "this journey! But more importantly you are in a dark room with but a single"
	print "door ahead of you!"
	print "\nType ENTER to begin your challenges, m'liege!"

	choice = raw_input(">>> ")

	if choice == "ENTER":
		riddle_room()
	else:
		print "\nI'm sorry m'lord but that is not a room! Perhaps you see something we do not..."
		print "but you must start again ... I'm sorry."
		start()

def riddle_room():
	print "\nYou enter the door and suddenly hear a scary laugh echo in the silence."
	print "HehehehEHEHEHEHE heheh HEH Ehe hHEHEH"
	print "WELCOME TO THE RIDDLE ROOM the foolish voice says"
	print "IT IS I, THE RIVER RIDDLER!!!!"
	print "WHAT DO YOU CALL A WISE WIZARD WHOM SO STUMBLES INTO MY TRAP HAHHEHheheeheh?"
	print "...  . . ... . . .. A (SOON TO BE) PUDDLE (OF BLOOD)! hEHEH HEHeh eheh EHEHE HE!"
	print "ANSWER ME THIS O WIZENED 'ZARD:"
	print "(and remember that if you fail to answer my riddle a large baton will fall from"
	print "the ceiling and bludgeon you 'til you lie in a pool of your own blood!)"
	
	print "\nWHAT RUNS BUT NEVER WALKS, OFTEN MURMURS BUT NEVER TALKS,"
	print "HAS A BED BUT NEVER SLEEPS, HAS A MOUTH BUT NEVER EATS???"
	print "ANSWER QUICK! THE BATON AWAITS!"

	choice = raw_input(">>> ")

	if choice == "RIVER":
		print "\nEEEEEEEeeeeeeEEEEE the river riddler shrieks"
		print "I AM MELTING!!! YOU HAVE SUCCEEDED AND YOU ARE WISE!"
		print "GREAT WEALTH AWAITS YOU!! EEEeeeeeeeee ee e eeeeee e e e!"
		print "You have defeated the most notorious river-themed riddler in all the land!"
		print "Perhaps are truly what the prophecy has predicted!"
		print "O wise wizard, the way is open to you, let us proceed..."
		water_room()
	elif choice == "A RIVER":
		print "\nEEEEEEEeeeeeeEEEEE the river riddler shrieks"
		print "I AM MELTING!!! YOU HAVE SUCCEEDED AND YOU ARE WISE!"
		print "GREAT WEALTH AWAITS YOU!! EEEeeeeeeeee ee e eeeeee e e e!"
		print "You have defeated the most notorious river-themed riddler in all the land!"
		print "Perhaps are truly what the prophecy has predicted!"
		print "O wise wizard, the way is open to you, let us proceed..."
		water_room()
	else:
		print "\nHEHEHEHEEEeeeeHEEE YOU ARE NOT WISE, YOU OLD 'ZARD!"
		dead("a baton falls on your skull and it hurts so bad, alright...")




def water_room():
	print "\n*SPLASH*! o my, o wizard, it would appear we have stumbled upon a Wet Room!"
	print "The water appears to be steadily rising! It may kill us! oh no!"
	print "What do you want to do, o wise wise wise wizard? Cast a spell perhaps?"
	print "Perhaps drink all of this water (several hundred gallons it would seem)?"
	print "Perhaps you have a wet-vac with you? Someone truly wise would never be without"
	print "one!"

	print "\n choose: CAST, DRINK, VAC"

	choice = raw_input(">>> ")

	if choice == "CAST":
		print "\nyou cast your 'water drain' spell"
		print "godammn that was smart (wise)! the room drains instantly and you notice"
		print "a door in the floor where the water had previously been"
		print "My liege let us proceed to the Booty Rooom! I am sure it must be behind this"
		print "door in the floor!"
		print "*you enter*"
		laundry_room()
	elif choice == "DRINK":
		dead("Really too much water to drink, but you made a good dent and then drowned...")
	elif choice == "VAC":
		print "\nO fuck, you think, I forgot my wet vac! but you're too embarassed to admit it"
		dead("you act like you are wet-vaccing something until you drown...")
	else:
		print "\nAh, quite a wise choice!"
		dead("not a wise choice bro .. you drown...")
	

def laundry_room():
	print "\n*sniff sniff* mmmm do you smell that smell, o bearded one?"
	print "It smells like ... like the smell of fresh laundry drying on the line in the"
	print "sun .. You look around and see that this is the case -- you are in a labyrinth"
	print "of clothes lines and drying laundry."
	print "\nO m'lord look at all this laundry! We will never find our way out of here!"
	print "Surely you must have a Wise Idea on how we may escape!"
	print "\nPerhaps we may fold all this laundry so that we may see the way."
	print "Can you cast a clairvoyancy spell to show us the way?"
	print "Perhaps we can leave a treat for the laundry goblin and he may show us the way!"
	print "So what will it be, o wise one? FOLD, SPELL, or TREAT FOR THE LAUNDRY GOBLIN?"

	choice = raw_input(">>> ")

	if choice == "FOLD":
		print "\nM'lord we have been folding laundry for hours and hours and still our way is"
		print "blocked by fresh clothes! I believe that the dry clothes are sucking the"
		print "Moisture out of my body!"
		dead("You continue to fold and the laundry dehydrates you and you die!")
	elif choice == "SPELL":
		print "\nO wizard you spell has been cast straight and true, but it would seem that"
		print "spells do not have any effect on laundry (the only thing in the multiverse"
		print "that is uneffected by wise spells). As your toadie I suggest you continue"
		print "Casting it until it works maybe!"
		dead("You continue casting unsuccessfully until you die amongst the laundry!")
	elif choice == "TREAT FOR THE LAUNDRY GOBLIN":
		print "\nAh look! The goblin smells your treat and approaches!"
		print "Please do not be shy o hideous goblin! Come closer so that we may grab you!"
		print "'grllr ggerhg hl lrgegergg grgllrllgrg gl!'"
		print "The goblin accepts your treat, he says, so long as he can give your toadie"
		print "a sloppy wet kiss on the lips"
		print "\nDo you accept the goblin's proposition? [Y/N]"
		
		kiss = raw_input(">>> ")

		if kiss == "Y":
			print "\n'grgrgtlgl! hlr! hlkrhghrll hrh grgrgrgrgrgrgGRGRGRGRGR!'"
			print "Huzzah! he will show us the way! This way to the booty room he says!"
			ruby_room()
		else:
			print "Oh no the laundry goblin is mauling my face!"
			dead("You are unable to survive even an hour without your toadie.")
	else:
		print "\nAha! going off the script again are you? I love it!"
		dead("Your toadie kills you in your sleep.")

start()