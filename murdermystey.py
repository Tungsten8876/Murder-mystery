clues = []

A = True
B = False
suspects = ["penny", "jason", "atticus", "jacobs dad"]

wake_up = input("You wake up in a trap house, needles spread all over the ground. Someone is pinned up against the wall with a upsidown cross nailed into there stomach, do you want to explore further into the house A, or (B)try to find out whos body it is?")

while True:
    if wake_up == "A":
        walk = input("You open the door and walk into the hall, once you step into the hall two steel doors enclosing you one of the doors has a key hole, a speaker plays over head, it seems you fell for my trap now I have hidden a key in this room you are in which will open the door. You may ask for a hint but then the timer will begin, (A) search the room for the key, or (B) ask for the hint")
        if walk == "A":
            wka = input("You searched the room and found nothing, (A) ask for the hint")
            if wka == "A":
                wkh = input("The timer will begin, 30 mins, I see let me feed you this hint look at the back of your calf, (A) look at the back of your calf,(b)wait for timer to finish")
                if wkh == "A":
                    pensil = input("Hou look at the back of your calf and see a key imprent in your leg, (A) dig it out to open the door, (B)  wait for the timer to finsih")
                    if pensil =="A":
                        gpa = input("As you dug it out you have the key and opened the door you are now in a room with one window and a trap door, (A) jump out the window without thinking,(B)crawl into the trap door")
                        if gpa =="A":
                            WSP = input("Uh oh you should think before you do something!, you died, the neigbor got it on their ring camera and reported the person that was playing with you to the police. sacrafice well served Atticus McKennon Petersons is now in jail for life ")
                            break 


 
                        elif gpa == "B":
                            GGG = input ("Uhh ohh when you entered the trap door a huge weight dropped on your neck which several fractures while paralizing you, then the rats in the vents ate you alive starting with your eyes.")
                    elif pensil == "B":
                        asf = input("The room filled with water and you died :( ")
                        break
                elif wkh == "B":     
                      auf = input("The room filled with water and you died :( ")
                      break
            elif wka == "B":
                fjs = input ("HEY! NO AWNSER FOR (B)  NOT COOL MAN NOW I HAVE TURN OFF THE COMPUTER")    
                break    
        elif walk == "B": 
            bbb = input("The timer will begin, 30 mins, I see let me feed you this hint look at the back of your calf, A look at the back of your calf,(B)wait for timer to finish")         
    elif wake_up == "B":
        walk = input("As you further investigate the body you move it and see a trap door in bellow it. A crawl into the trap door ")
        if walk == "A":
            ufk = input("As you crawl your hit with a problem do you want to A turn right or(B)turn left")
            if ufk == "A":
                BBB = input("You turn left and see two vents that you can look into A vent left, you see a person sleeping on a desk that has cameras all over the house choose A if you want to jump in.(B)Go into the right its a open room with nothing in it.")
                if BBB == "A":
                    gdsf = input("Now you have on option kill the person please click A")
                    if gdsf =="A":
                        lllll = input("You have WON bu killing the game creator")

                elif BBB == "B":
                    UUU = input("You are now in a room with no doors and the vent got slammed close by metal trap doors. You starved to death :( game over")
            elif ufk == "B":
                hsdf = input("Wrong you fell through the vent onto spikes.")
