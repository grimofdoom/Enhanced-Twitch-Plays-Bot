from TwitchPlays_KeyCodes import *
from CommandsDef import *



class ExampleGame(GameDef):
    def __init__(self): # Use the constructor class
        super().__init__() # Required for initializing base
        self.name = "Example Game" # Give the game a name
        self.AddCommand(ExampleCmd1()) # Added the first example command 
        self.AddCommand(ExampleCmd2()) # added the second example command
        self.AddCommand(TaskManager()) # added the task manager command

class ExampleCmd1(CommandDef):
    def __init__(self):
        self.name = "Example Command 1" # give the command a name, ONLY used by 1 error call currently
        self.call = "!example1" # Give the command a call, this is what users will send in chat to call the command
    def Perform(self): # Override the Perform() function, to do what will happen when someone calls this command 
        PressKey(K) # This will hold the keyboard key 'K' for 0.25 seconds

class ExampleCmd2(CommandDef):
    def __init__(self):
        self.name = "Example Command 2"
        self.call = "!example2"
    def Perform(self):
        PressKey(H)

class TaskManager(CommandDef):
    def __init__(self):
        self.name = "Bring up task manager"
        self.call = "!task"
    def Perform(self):
        ComboKeysPress([LEFT_CONTROL, LEFT_SHIFT, ESC])