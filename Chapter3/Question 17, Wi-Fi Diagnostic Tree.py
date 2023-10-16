#Question 17, Wi-Fi Diagnostic Tree

#This is a rudimentary tool to diagnose Wi-Fi issues and problems

print("This is a guide to fixing your router's Wi-Fi connection.")
print("Please follow the steps below to ensure the best results.")

#Step 1, Reboot the computer
print("Step 1: Reset the Computer.")
computer_reset = input("Did resetting your computer work? (yes/no)").lower()

if computer_reset == "yes":
    print("Thanks for using our manual!")
else:
    print("Reboot the router")
#Step 2, Reboot the router    
    reboot = input("Did rebooting the router work? (yes/no)").lower()
if reboot == "yes":
    print("Thanks for using our manual!")
else:
    print("Try checking the cables and reconnecting them into the router.")
#Step 3, Connect the cables    
    cables = input("Did re-connecting the cables work? (yes/no)").lower()
if cables == "yes":
    print("Thank you for using our manual.")
else:
    print("Move the router to a different location")
#Step 4, Move the router    
    router = input("Did moving the router work? (yes/no)")
if router == "yes":
    print("Thank you for using our manual!")
else:
    print("Sorry, looks like you will need a new router!")



