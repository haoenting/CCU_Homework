import time   
import random 
random.seed(20) 

def printSlow(text):
    lines = text.split('\n')
    for line in lines:
        print(line)
        time.sleep(1) 

def win():
    print("You have successfully completed the training. Now, you are ready for the real challenges.")
    print("Do you want to play again?")
    while True:
        replay = input("Enter 'yes/y' to replay, 'no/n' to exit: ")
        time.sleep(1) 
        if replay.lower().strip() in ["yes","y"]:
            print("\nRestarting the game...")
            time.sleep(1) 
            return play_game()
        elif replay.lower().strip() in ["no","n"]:
            print("\nGoodbye!")
            return 
        else: 
            print("Enter the wrong thing! Try again.\n")

def fail():
    print("Do you want to play again?")
    while True:
        replay = input("Enter 'yes/y' to replay, 'no/n' to exit: ")
        time.sleep(1) 
        if replay.lower().strip() in ["yes","y"]:
            print("\nRestarting the game...")
            time.sleep(1) 
            return play_game()
        elif replay.lower().strip() in ["no","n"]:
            print("\nGoodbye!")
            return 
        else: 
            print("Enter the wrong thing! Try again.\n")

    
def play_game():
    # Introduction
    text = """You are a 13-year-old child who has lived behind a high wall town for as long as you can remember. 
People have been living inside the walls for thousands of years because of the Titans that devour people outside the walls..\n"""
    printSlow(text)
    
    # Scenario 1
    text ="""One day, a Colossal Titan (taller than the wall) suddenly appeared behind the wall. 
He kicked a hole in the wall and instantly people screaming and running, while many giants rushed into the wall. 
Your father was practicing medicine, and your mother didn't manage to escape... 
After a week of living in the shelter, you opened your eyes saw your father carrying you towards the woods, 
giving you an injection, and the key to the family basement, telling you the secret of the world inside. 
Then you suddenly woke up and realized that your dad was gone.\n"""
    printSlow(text)
    
    # Scenario 2
    print("Two years later, with the order of the country's recruitment, you join the training corps to train ...\n")
    time.sleep(1)  # Pause for dramatic effect
    text="""Following an extensive training period, you emerge as one of the top ten recruits in the 104th Regiment.
Now, you must decide which regiment to join: 
the Scout Regiment (Outside exploration), the Garrison Regiment(Protects and maintains the Walls), or 
the Military Police Regiment(Personal guard of the Monarch).\n
Your options are..."""
    printSlow(text) 

    regiments = ["Scout Regiment", "Garrison Regiment", "Military Police Regiment\n"]
    for i, regiment in enumerate(regiments):
        print(i+1, regiment)
        time.sleep(1) 
        
        
    attempts = 2
    
    # Player makes a choice
    while True:
        choice = input("Enter the number or words corresponding to your chosen regiment : ")
        time.sleep(1)  
        # Explanation of regiments
        if 'scout' in choice.lower().strip() or choice == '1':
            text ="""You have chosen the Scout Regiment.
Your mission is to explore beyond the walls and uncover the secrets of the world.
Prepare for an adventurous journey filled with mysteries and dangers.\n"""
            printSlow(text)
            break
        elif 'garrison' in choice.lower().strip() or choice == '2':
            text ="""You have chosen the Garrison Regiment.
Your duty is to become one of the guardians of the wall, take care of all defenses for the Walls whether it be patrols, repairs, or improvements.
Your commitment is crucial to the town's defense.\n"""
            printSlow(text)
            break
        elif 'military' in choice.lower().strip() or choice == '3' or 'police' in choice.lower().strip():
            text ="""You have chosen the Military Police Regiment.
Your role is to enter the capital maintain order within and personal guard of the Monarch.
Enjoy the relative comfort and safety.\n"""
            printSlow(text)
            break
        elif attempts > 0:
            print(f"Enter the wrong thing, your answer is {choice}, You have {attempts}!more  attempts.")
            print("Try enter number (i.e: 1) or words(i.e:Garrison Regiment).\n")
            attempts -= 1
            
        else: 
            print("You've reached the maximum number of attempts. so I have selected one for you:",random.choice(regiments))
            time.sleep(1)
            print("Warning: Please follow the rule next time or you will get punish!\n")
            break
                
    random.seed(20) 
    
    
    # Scenario 3
    text="""Before your official graduation, you are given your first assignment as a trainer.
You're guarding the city wall with everyone else when suddenly a giant appears and the wall is kicked down again.
With everyone scrambling, you are accidentally eaten by a giant.\n"""
    printSlow(text)

    # Player makes a choice
    text = """However, you realize that you have the power of a giant. You became a Titan! This is when you...
1. Defeat the other giants in one fell swoop.\n
2. Run around in a panic.\n"""
    printSlow(text)
    
    attempts = 2
    
    while True:
        choice = input("Enter the number or words corresponding to your decision : ")
        
        if 'fight' in choice.lower().strip() or 'defeat' in choice.lower().strip() or 'battle' in choice.lower().strip() or choice == '1':
            time.sleep(1)  
            print("After you beat the giants, you ran out of the back of your neck, and the area you had just injured grew back.")
            time.sleep(1)  
            print("But they think you and your friends are enemies, and the commander orders fire on you guys.")
            break
        elif 'run' in choice.lower().strip()or 'scream' in choice.lower().strip() or choice == '2':
            time.sleep(1)  
            print("You panicked running attracts more giants.")
            time.sleep(1)   
            print("Because you ran around without resistance, you were eaten by the other giants..")  
            return fail()
        elif attempts > 0:
            print(f"Enter the wrong thing,your answer is {choice}, you have one more chance ! Try enter number or words.\n")
            attempts -= 1
            
        else:
                print("You've reached the maximum number of attempts. You are not allowed by the rule.")
                time.sleep(1) 
                print("Therefore, System Punish: You were eaten by giants...😢.\n")
                time.sleep(1) 
                return fail()
                    
    # Scenario 4
    text="""At this point, you will..."
1. Bite yorself, become a giant again to deflect the fire.\n
2. Convince the commander, along with your friends, that you can block the walls with rocks and you have the key to the basement to see the secrets of the world.\n
3. You don't know what to do...\n"""
    printSlow(text)
    
    attempts = 2    
    while True:
        choice = input("Enter the number or words corresponding to your decision: ")
        time.sleep(1)  
        if 'giant' in choice.lower().strip() or 'bite' in choice.lower().strip() or choice == '1':
            print("\nYou become a giant again and manage to deflect the incoming fire.\n")
            time.sleep(1)  
            print("Your actions save you and your friends. The commander, realizing the mistake, stops the attack.\n")
            break
        elif 'convince' in choice.lower().strip() or choice == '2' or 'talk to commander' in choice.lower().strip()  :
            print("\nYou and your friends start convincing the commander about your plan.\n")
            time.sleep(1)
            print("The commander is persuaded and orders the troops to stand down.\n")
            break
        elif "don't know" in choice.lower().strip() or choice == '3' or 'not knowing'in choice.lower().strip():
            print("\nNot knowing what to do? Time waits for no one! You are killed by the cannon fire.")
            time.sleep(1)  
            return fail()
        elif attempts > 0:
            print(f"Enter the wrong thing,your answer is {choice}, you have one more chance ! Try enter number or words.\n")
            attempts -= 1
            
        else:
            print("You've reached the maximum number of attempts. You are not allowed by the rule.")
            time.sleep(1) 
            print("Therefore, System Punish: You were eaten by giants...😢.\n")
            time.sleep(1) 
            return fail()

    # Scenario 5
    text="""After successfully blocking the wall, you're taken to jail.
The leader of the Scout Regiment comes in and asks if you want to join them.
Your choice?
1. Join?
2. Decline?\n"""
    printSlow(text)

    while True:
        choice = input("\nEnter the number or words corresponding to your decision: ")
        time.sleep(1)  
        if 'join' in choice.lower().strip() or choice == "1":
            print("\nYou choose to join the Investigators.")
            time.sleep(1)  # Pause for dramatic effect
            print("You're about to go off the wall to discover the secrets of the world, and you've got a long and dangerous journey ahead of you!")
            print("You're about to set off to explore the secrets of the world beyond the wall.")
            return win()
        elif 'decline' in choice.lower().strip() or choice == "2":
            print("\nYou decline the offer.")
            time.sleep(1)  # Pause for dramatic effect
            print("Capture and forced research on giants await you, leading to a life shrouded in darkness.")
            return fail()
        else:
            print(f"Enter the wrong thing,your answer is {choice}, you don't have one more chance !\n")
            time.sleep(1)
            return fail()


def main():
    print("Hello! What is your name?")
    player_name = input("Enter your name : ").title()
    print("Hello", player_name, "!")
    time.sleep(1)  
    play_game()
            

if __name__ == "__main__":
    main()