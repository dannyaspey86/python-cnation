#import libraries
import time
import random

answer = input("Would you like to play? (yes/no)")
​
#greeting and name
if answer.lower().strip() == "yes":
    answer = input("Great!Lets go!")
​
    player_name =  input("What's your name? ")
    print("Hello ", player_name)
    print("Welcome to:")
    
    print(r".___          __      __                  .___           .__                     .___._.")
    time.sleep(1)
    print(r"|   | ____   /  \    /  \____   ____    __| _/___________|  | _____    ____    __| _/| |")
    time.sleep(1)
    print(r"|   |/    \  \   \/\/   /  _ \ /    \  / __ |/ __ \_  __ \  | \__  \  /    \  / __ | | |") 
    time.sleep(1)
    print(r"|   |   |  \  \        (  <_> )   |  \/ /_/ \  ___/|  | \/  |__/ __ \|   |  \/ /_/ |  \|")
    time.sleep(1)
    print(r"|___|___|  /   \__/\  / \____/|___|  /\____ |\___  >__|  |____(____  /___|  /\____ |  __")
    time.sleep(1)
    print(r"         \/         \/             \/      \/    \/                \/     \/      \/  \/")
    print("\n")
    # story and first 4 optins
    print("Is dark around...You woke up in the middle of the forrest...Shocked!")
    print("A lot of noise around, you are scared and dont now what to do!")
    print("you think hard about options and come up with 4:")
    print("A - you lie down and wait till you wake up!Must be a deam!")
    print("B - you get up, look around and see the rabbit! You follow it !")
    print("C - you see the leprechaun and decide to follow him! ")
    print("D - you see the quin and decide to follow that chic!")  
else:
    print("That's a shame!")
    # no_choice()
​
 #take user input
  # choices functions 
#users possible response
# answer_A = ["A", "a"]
# answer_B = ["B", "b"]
# answer_C = ["C", "c"]
# answer_D = ["D", "d"]
yes = ["yes", "YES"]
no = ["no", "No"]
  
#choice = ["a","A", "b", "B", "c", "C", "d", "D"]
#print(input_choices)
choice = input("What do you choose?A/B/C/D: ")
print("\n")
​
def drink_it():
    print("Congratulations on rolling 6.")
    print("\n")
    #take user input yes/no
    print("Now you are presented with an elixir.") 
    
    answer = input("Do you want to drink it? (yes/no)")
​
    print("\n")
    if answer == "yes":
        print("Awesome! you get smaller ans smaller so rabbit takes you through a tiny door!")
        print("There are forrest animal -Pig, Elephant, Fox, Kangaroo having a dance off! They invite you to join")
        input("You need to dance for 3h not repeating the same style to win the prize. Do you try? (yes/no)")
        
​
    elif answer == "no":
        print("You worry that rabbit is tryint to kill you and dont want to drink the elixir.")
        print("You wait for a while not knowing what to do...Knight with big sword comes in...")
        print("He doesnt like your face and kills you! GAME OVER")
​
​
if choice == 'a' or choice =='A':
    print("You wait and wait and wait ... and die waiting!")
​
elif choice == "B" or choice == "b":
     def dice_roll():
        dice = random.randint(1,6)
        if dice != 6:
            print(dice)
            hit_enter = input("Try again. Hit enter")
            if hit_enter == "":
                dice_roll()
        elif dice == 6:
            print("good")
            drink_it()
​
        else:
            print("Try again")
     print("You speak to rabbit which gives you a task!You play dice with him. You get 6 you can go with him...keep rolling until you do!")
        #function randit
     dice_roll()
   
​
elif choice == "C" or choice == "c":
    print("You folowed the Lepreachaun and got to the end of a rainbow. There is a pot of gold!Do you take it?")
                #function yes/no
    choice2 =input("Do you take it? yes/no ")
    if choice2 in yes:
            print("You take Leprachun gold, he sees you you and kills you with his laser eyes!GAME OVER")
    else:
            print("You are scared to take it and run away! You run too fast and are stopped by police horse who takes you to jail. You die in jail!")
​
​
elif choice == "d" or choice == "D" :
    print("Queen sees you following her! Screams! Guards chop your head of!")
else:
    print("")