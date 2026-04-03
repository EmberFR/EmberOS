import os
import random
os.system("cls")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()
# Sigma Login/Signup func
print("Welcome To EmberOS")

print("-" * 26)
print("SIGN UP")
print("-" * 26)

username = input("Create Your Username ")
password = input("Create Your Password ")

print("-" * 26)
print("LOG IN")
print("-" * 26)

while True:
    username_attempt = input("Enter Your Username ")
    password_attempt = input("Enter Your Password ")

    if username == username_attempt and password == password_attempt:
        print("Username Correct!")
        print("Password Correct!")
        break
    else:
        print("Username or Password Incorrect, Try Again")

print("-" * 26)
print(f"LOGGED IN {username}")
print("-" * 26)

# Admin Menu
if username == "ember_admin":
    print(f"Welcome {username} You Are An Admin")

# Main Menu
while True:
    clear()
    print("--------------------------")
    print("1. View Username")
    print("2. Change Username")
    print("3. Change Password")
    print("4. Logout")
    print("5. Exit")
    print("6. Calculator")
    print("7. Account Info")
    print("8. Github")
    print("9. Dice")
    print("10. Guess The Number")
    print("11. Magic 8 Ball")
    print("67.67 Kid")
    if username == "ember_admin":
        print("99. (admin only) custom print")
    print("--------------------------")

    # Main Menu Options
    option = int(input("Choose 1,2,3,4,5,6,7,8,9,10,10,67 "))

    if option == 1:
        print(username)
        input("Press Enter To Continue")

    elif option == 2:
        old_username = username
        username = input("Enter Your New Username ")
        print(f"Username Changed from {old_username} to {username}")
        input("Press Enter To Continue")

    elif option == 3:
        old_password = password
        password = input("Enter Your New Password ")
        print(f"Password Changed from {old_password} to {password}")
        input("Press Enter To Continue")

    elif option == 4:
        print("Logging Out...")
        break

    elif option == 5:
        print("Exiting Program...")
        break

    elif option == 6:
        first_number = int(input("Choose The First Number "))
        multiplication = input("*,+,/ or - ")
        second_number = int(input("Choose The Second Number "))

        if multiplication == "*":
            print(f"The Answer Is {first_number * second_number}")
        elif multiplication == "+":
            print(f"The Answer Is {first_number + second_number}")
        elif multiplication == "/":
            print(f"The Answer Is {first_number / second_number}")
        elif multiplication == "-":
            print(f"The Answer Is {first_number - second_number}")
        else:
            print("Invalid operation")

        input("Press Enter To Continue")

    elif option == 7:
        print("----- ACCOUNT INFO -----")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print("Account Status: Active")
        print("Login Status: Logged In")
        print("------------------------")
        input("Press Enter To Continue")

    elif option == 8:
        print("https://github.com/EmberFR/ember")
        input("Press Enter To Continue")

    elif option == 99:
        if username == "ember_admin":
            admin_print = input("Type What You Want To Print ")
            print(admin_print)
            input("Press Enter To Continue")
        else:
            print("Admin only option")
            input("Press Enter To Continue")

    elif option == 67:
        print("Squint Your Eyes")
        print("""
****#%%@@%%%%%%%%##%%@%%%%%%%%%%%%%%%####%@%#%%%%@@@@%%%#%%##**#%#++*%%%#**%%%%+
####%%@@%%%%%%%%%##%@@@%%%%%%%%%%%##**#***##%%@@@@@@@@%%@%%%#=-=%%*+%@@@@%@@#*+=
%%%%%@@@%%%%%%%%%##%%@@%%%%%####**+*=+****+++*##%@@@@@@@@@%%%*=#%#+=+**+++***+=-
%%%%%@@@%%%%%%%%%##%%@@%%%%%##***++****++**=+++**#%@@@%#*+==%%*#+:--==+====+++=-
%%%%%@@@%%%%%%%%%#*#%@@%%%%##****+=+#******++****+*%#++=====++=====-=+=+*++***++
%%%%%@@@%%%%%%%%%##%@@@@%%#*#*++*+=*#++*****##*++++*#+++===--------::-=+#*+==..:
%%%%%@@@%#%%%%@@%#%%*++*##*#**+**+**+++*++++++=====+#*+=-:-+-::..:.-+#@@#*+=....
%%%%%%@@%@@@@@#%%*#%*=-=+**+++===+++++***+=-------==++*+-=+++*+-==-=##+=-:::::..
%%%%%@@@@#=--===+*#####****+++++++==++*#*===-----=-:--+*=**###**+=:-++=:.:::..
%%%#**###*=-:.===-=*++**+==--==-=::=+*#%#+===::====:::=++++***++*-.--=--:::..
==:::::-=-=+-:===--==+++=----+****+**##%#*****+****=.:-=**#*+++*#=.---::....
--:.:=+=::+*+=++++=--=++-=--=#%%#%%%#####*+*######*=. :-=******###=-::.....
=+=-=++=:=+=---=+++===++==--=#%%%%###+-+=:-+#####**+. .:-=+***##%%%=:......
----+++====--..--=++###*+=-=-####*+*#****++**++**++=:..:=++*######*:......
.  .-=--==-:.....:+*#***+++-=##**=+#%%#######*=++===:.::-+**######+ ..
...:--=+=:..-+=:.:=+***++==--=#**=+====+===---=+++=-..---==+*#####=
...:=+*-:.:++====-=+**+++=-:-:=**++. .::.... .+*+=-.:.-==++**#****:
 .:::.....:---+++++****+=:-:::.=***+.-===-=-:=+*==. .:-==+*****++=..
=++-..   .  .:+++++6++++=:-::...+###+=+++++=++*+=-:.:-==-+*##*+++-7.
++=:..       .=+==++++===+*+=:. :*###**++++=+++====:--=-=++++**++: .
===:..       .-=++++===+*%#**+-.-**##**++++++*==-=--==-=++==+*#**: .
---:.      .. -========#%##***+--+**###*****+===---====+=-=+****+.
-::...        :----===*####**+++==**+*****++===---==++=--=++*+++=.
::::...       ::----*%%#******+++++++++======-----===-:==++++=++-.
""")
        input("Press Enter To Continue")

    elif option == 9:
        dice = random.randint(1, 6)
        print(f"The Dice Has Landed On {dice}")
        input("Press Enter To Continue")

    elif option == 10:
        guess_number = random.randint(1, 20)

        while True:
            guessed_number = int(input("Guess The Number From 1 To 20 "))

            if guessed_number == guess_number:
                print("You Guessed It Well Done")
                input("Press Enter To Continue")
                break
            elif guessed_number > guess_number:
                print(f"{guessed_number} Is Bigger")
                input("Press Enter To Try Again")
            elif guessed_number < guess_number:
                print(f"{guessed_number} Is Smaller")
                input("Press Enter To Try Again")
            else:
                print("You Got It Wrong")
                input("Press Enter To Try Again")
    elif option == 11:
        ball = random.randint(1, 10)

        while True:
            question = input("Ask A Question ")
            if ball == 1:
                print("No")
                input("Press Enter To Continue")
                break
            elif ball == 2:
                print("Yes")
                input("Press Enter To Continue")
                break
            elif ball == 3:
                print("Go For It!")
                input("Press Enter To Continue")
                break
            elif ball == 4:
                print("Hell No!")
                input("Press Enter To Continue")
                break
            elif ball == 5:
                print("Nah")
                input("Press Enter To Continue")
                break
            elif ball == 6:
                print("Dont Trust Me")
                input("Press Enter To Continue")
                break
            elif ball == 7:
                print("Maybe")
                input("Press Enter To Continue")
                break
            elif ball == 8:
                print("Definitely")
                input("Press Enter To Continue")
                break
            elif ball == 9:
                print("Never")
                input("Press Enter To Continue")
                break
            elif ball == 10:
                print("Probably")
                input("Press Enter To Continue")
                break
            else:
                print("Invalid Option")
    else:
        print("Invalid option")
        input("Press Enter To Continue")
