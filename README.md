# Enhanced_Twitch_Plays_Bot
 An enhanced version of DougDoug & ddarknut's Twitch Play's Bot.  
 I do not know which license to use; but this bot is considered a generic open source project that you are not allowed to sell or claim as 100% your own  
 This version of the bot is not for those fresh to programming or python- but with basic pattern matching, can be easy to understood


# Changes
 - Added 'press' and 'combo' inputs for keyboard commands and SHORTEST_KEY_TIME variable in TwitchPlays_KeyCodes.py 
   - Press' will perform Hold and Release with the shortest time in between  
   - Combo's will accept an array of hex keys and perform the appropriate action  
   - SHORTEST_KEY_TIME is used to define the shortest time a key can be held down and released, used for Press'
 - Added GameManager, GameDef, CommandDef in CommandsDef.py 
   - GameManager - The core that handles being able to select from multiple games
   - GameDef - Defines a single game that you can select on bot boot & contains all the game's commands
   - CommandDef - Defines a single command to add to your game/s  
 - Twitch_Plays_Bot.py
   - Added in the GameManager and adjusted the handle_messages command to use GameManager.PerformCommand alternatively
 - Games/ExampleGame.py
   - This is an example of how to set up a game and its commands


# Future Coming Features
 - Swap out the Twitch connection for a different method so that more data can be aggregated from each message
   - With this change, each command can be defined to only run if X points were spent, or only ran for subscribers
