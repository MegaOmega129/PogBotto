import os, json
from nextcord.ext import commands
from colorama import Fore

# Options File
with open('Config.json', 'r') as rawOptions: Options:dict = json.load(rawOptions)

# Bot Object
bot = commands.Bot(
    command_prefix = Options['Prefix']
)

# Loading Commands
def load(module:str) -> None:
    if module.endswith('.py'):
        Module = f"Commands.{module.replace('.py', '')}"
        try: 
            bot.load_extension(Module)
            print(Fore.LIGHTGREEN_EX + f"[ {module} ] was loaded sucessfully." + Fore.RESET)
        except Exception as error: 
            print(Fore.LIGHTRED_EX + f"[ {module} ] could not be loaded." + Fore.RESET)
            print(Fore.RED + error[:50] + Fore.RESET)
            
for module in os.listdir('Commands/'): load(module)

# Logging into discord
bot.run(Options['Token'])