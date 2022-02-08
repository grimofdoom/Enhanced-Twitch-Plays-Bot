from os import system, name
from TwitchPlays_KeyCodes import *

###############################
#             OVERVIEW
# -GameManager
#   -Manages the games and commands, should only ever need 1
# -GameDef
#   -Defines a single game, and holds all of its possible commands
# -CommandDef
#   -Defines a single command



class GameManager:
    def __init__(self):
        # The games with their commands added to list
        self.games = []
        # The selected final game
        self.finalGame = None

    # Ask the user which game should be used
    def GrabGame(self):
        # INFINITELY run until user selects an actual game in the list or closes program
        while True:
            try:
                # Clear screen, didn't want to add an extra class, so bear with me
                if name == 'nt':
                    _ = system('cls')
                else:
                    _ = system('clear')
                # Print the games out in order w/ their indices
                print("Select Game:")
                for i in range(len(self.games)):
                    print(f"[{i}] {self.games[i].name}")
                # Ask for input of which game the user wants to play
                selectedGame = int(input("Enter the game number you wish to run: "))
            except ValueError:
                # The input was not even a number, error, retry
                print("That was not even a number")
                continue
            if selectedGame not in range(len(self.games)):
                # The input WAS a number, but it was not actually within the listed games
                print("Select a number posted above!!")
            else: 
                # Everything was all good, lets goooooo
                break
        self.finalGame = self.games[selectedGame]


    # Add a game to the game list
    def AddGame(self, game):
        self.games.append(game);

    # Place the message from twitch and check if it exists, perform if so
    def PerformCommand(self, cmd):
        if cmd in self.finalGame.commands:
            self.finalGame.commands[cmd].Perform()




# Defines a single game, that can hold multiple commands
class GameDef:
    def __init__(self):
        # The name of the game, visual detail
        self.name = "Game Name"
        # The commands that the game hosts
        self.commands = {}

    # Add a new command to GameDef
    def AddCommand(self, command):
        if command.call in self.commands:
            print(f"[{command.call}] command already exists in game:{self.name} ")
        else:
            self.commands[command.call] = command
        print(f"command count: {len(self.commands)}")





# Defines a single command for [GameDef] to hold
class CommandDef:
    def __init__(self):
        # Name of the command, not really used outside of error
        self.name = "Command Name"
        # This is the actual command that will be sent by chat
        self.call = "!call"

    # This lets you disable a command for whatever reason, programmatically or manually
    enabled = True 
    # The action performed when the [call] name is used by chat
    def Perform(self):
        pass