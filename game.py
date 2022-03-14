from gladiators import Gladiator
import time


player_name = input("What should we call you?  >> ")

player = Gladiator(player_name, 40, 5)
rat = Gladiator("Tetraites 🐀", 5, 2)
wolf = Gladiator("Lycan 🐺", 10, 4)
t_rex = Gladiator("Crixus 🦖", 15, 4)

opponents = [rat, wolf, t_rex]
num_opponents = len(opponents)

time.sleep(2)
print(f"\nWelcome to the arena {player_name}! 🏛\nTo become Champion of Gladiators you must defeat 3 worthy opponents...")
print(f"Slay them all and live, and your name, ✨{player_name}✨, will go down in history along side legends! 📜")
time.sleep(3)
print(f"Should you lose, you will be forgotten... ")
time.sleep(3)
print("\n~ you enter the arena ~\n~ the crowd is cheering ~\n~ and your opponent enters from the other side ~")
time.sleep(2)

for opponent in opponents:
    print(f"\n{opponent.name} is now attacking you.\nTheir health is {opponent.hp} and max damage is {opponent.max_dmg}")
    while opponent.hp > 0:
        # player choose to attack or defend
        def chooseCommand():
            """player chooses a command"""
            command = ""
            while command != "1" and command != "2":
                command = input("\nWhat do you want to do?\n" + "1. ATTACK!!!\n" + "2. Defend\n" + "use 1 or 2 to select your command  >> ")

            return command

        command = chooseCommand()
        # print(command)

        if command == "1":
            opponent.hp = opponent.hp - player.attack()
            player.hp = player.hp - opponent.attack()
            if opponent.hp <= 0:
                print("\nYour opponent has been slain! 👏👏👏")
                if opponents.index(opponent) + 1 == num_opponents:
                    print("🌿✨ You are the arena's new champion!!! ✨🕊")
                    print(f"~ the crowd chanting; '{player_name}! {player_name}! {player_name}!'")
                else:
                    print("Your next opponent is approaching... ")
                    time.sleep(2)
            else:
                print(f"\n{opponent.name} HP: {opponent.hp}")
                print(f"{player.name} HP: {player.hp}")

        else:
            dmg = opponent.defend()
            player.hp = player.hp - dmg
            print(f"\n{opponent.name} dealt {dmg} damage")
            print(f"{player.name} HP: {player.hp}")

        if player.hp <= 0:
            print("\n💀 You have been defeated! 💀\nGAME OVER 👎")
            break

    if player.hp <= 0:
        break
