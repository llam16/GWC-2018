import sys
import time
end = "GAME OVER YOU LOSE"

print("\n*BOOM!*BAM*BAM*BAM**PEW*PEW*PEW*BA-BAM!*")
time.sleep(1)
print("Dan the Dino: \"What in the Jurassic World was that?!\"")
time.sleep(1.5)
print("T-Swizzle the T-Rex: \"HELP ME DAN THE DINO!!!!\"")
time.sleep(1.5)
print("Dan the Dino: Wait-what? What happened to you??")
time.sleep(1)

print("\n\nWELCOME TO DINO ADVENTURE!\nLET THE GAMES BEGIN...\n\nSTART\n\n")
time.sleep(2)
player = input("Type 1 to begin\n")

if player == "1":
    print("\nT-Swizzle the T-Rex was covered in blood and gunshot wounds to Dan the Dino's surprise")
    time.sleep(1.5)
    print("T-Swizzle: I'm dying. I got shot. I don't know who did it but my dying wish is that you find the killer and don't let me die in vai...")
    time.sleep(1.5)
    print("Dan the Dino: NOOOOOO")
    time.sleep(1)
    print("*sirens*")
    time.sleep(1)
    print("Playtcerotops Police: \"Who goes there? Put yo hands up yo gots the ryyyts to remain syyylint!\"")
    time.sleep(1.5)
    print("Dan the Dino: \"Oh no! What should I do?\"")
    time.sleep(2)
    choice1 = input("\n1: Run\n2: Hide\n")
    if choice1 == "1":
        print("\nThe Playtcerotops Police are chasing after Dan the Dino")
        time.sleep(1)
        print("Oh no! The police have caught up to Dan")
        time.sleep(1)
        print("Playtcerotops Police: \"You're under arrest for the murder of T-Swizzle the T-Rex\"")
        time.sleep(1)
        print("\n", end)
    elif choice1 == "2":
        print("Dan the Dino scours the forest for a hiding spot.")
        time.sleep(1)
        print("He continues in the forest and sees a shack covered in dead vines and leaves and bushes all around.")
        time.sleep(1)
        print("Dan the Dino: \"Where should I hide?\"")
        choice2 = input("\n1: Shack\n2: Bush\n")
        if choice2 == "1":
            print("\nWarwick the Wizard: \"Vho ahre zou?\"")
            time.sleep(1)
            print("Dan the Dino: *panting* \"Come again?\"")
            time.sleep(1)
            print("Warwick the Wizard (louder): \"VhO aHRE zOU?!\"" )
            time.sleep(1)
            print("Dan the Dino: \" uhmmm... \"")
            time.sleep(1)
            print("Warwick the Wizarck: \"Ah mei gud. I seen future. Ju vant a potion.\"")
            time.sleep(2)
            print("Dan the Dino: \"Potion for what? *panting* OK, listen old man, Ihavemnotimeforyourgames-\"")
            time.sleep(2)
            print("         *catches breath and meanwhile realize that he is in a pickle*")
            time.sleep(2)
            print("         WAiT,yousaidyouhaveapotionforme? Willithelpmerightnow? PLEASE PLEASE PLEASE PLEASE!!\"")
            time.sleep(2)
            print("Warwick the Wizard: \"AH SHUSH YOU STUPIDO DINO. I WAS JUST TALKING ABOUT THAT DUMBO.")
            print("         JUST FOR THAT RUDENESS, YOU WILL HAVE TO HOPE YOU PICK THE RIGHT POTION.")
            print("         I DONT HAVE TIME TO EXPLAIN WHAT THE SIDE AFFECTS OF ALL ARE")
            print("         VICH POTION U VANT???\"")
            choice2a = input("\n1: GetOtEt\n2: SiChRr\n")
            if choice2a == "1":
                print("POOF! Dan the Dino reappears next to Kanzata the Khaan in a bush")
                print("Dan the Dino: \"What in the Jurassic Park is this jumbalaya!?!\"")
                print("Dan the Dino: *thinks* Woah I'm in fricking Hawaii! Brroooooo this gon be littttyyyyyyyyyyyyyyy")
                print("Dan the Dino turns around and sees the same old shack he was just in and hears sirens in the background")
                print("Dan the Dino: \"AWWW DANNIT!!\"")
                print("Kanzata the Khaan: \"hey dawg, looks like we both we in a sitch. Wanna help a dino-dawg out man?\"")
                choice2b = input("\n1: HELP\n2: IGNORE\n")
                if choice2b == "1":
                    print("The popos come and arrest for conspiring with Kanzata the Khaan (aka THE KILLER)\n DUN DUN DUUUUUN...")
                    print(end)
                elif choice2b == "2":
                    print(end)

            elif choice2a =="2":
                print("You're safe")
        elif choice2 == "2":
            print("Dan the Dino sees another dinosaur in the bush")
            print("Kanzata the Khaan: \"hey dawg, looks like we both we in a sitch. Wanna help a dino-dawg out man?\"")
            choice2c = input("\n1: HELP\n2: IGNORE\n")
            if choice2c == "1":
                print("The popos come and arrest for conspiring with Kanzata the Khaan (aka THE KILLER)\n DUN DUN DUUUUUN...")
                print(end)
            elif choice2c == "2":
                print(end)

    else:
        sys.exit()
else:
    sys.exit()
