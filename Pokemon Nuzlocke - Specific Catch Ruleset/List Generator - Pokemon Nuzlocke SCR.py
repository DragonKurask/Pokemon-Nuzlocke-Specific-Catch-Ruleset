#Project Goals:
#Have the user be able to enter what game they want a list for (ex Red, Emerald, Scarlet, etc)
#Based on a case statement, the program should read from different documents throughout the folder structure
#Then for "Route","Cities", and "Dungeons" it should iterate through those documents and generate a random Pokemon from each locations values
#It should then output a txt file in the "Output" folder

#Extra goals
#Potentially make a way that the output file doesn't overwrite the old one when running the program again or
#Have the user be able to specify what they want the file to be named each time


import random
import os
import ast
import re

#gets the directory for the file no matter where the file is
#Though the file won't do much if you mess with the folders that are needed with the rest of the file
script_dir = os.path.dirname(os.path.abspath(__file__))

#Folder path shortcutes for each game
gen1_path = os.path.join(script_dir,'Games Folders','Generation 1')
gen3_path = os.path.join(script_dir,'Games Folders','Generation 3')
gen9_path = os.path.join(script_dir,'Games Folders','Generation 9')

#Dictionary for games and their folder paths to prep for proper input from the input statement loop
gamePaths = {
    "red":os.path.join(gen1_path, "Red"),
    "blue": os.path.join(gen1_path, "Blue"),
    "yellow": os.path.join(gen1_path, "Yellow"),
    "ruby": os.path.join(gen3_path, "Ruby"),
    "sapphire": os.path.join(gen3_path, "Sapphire"),
    "emerald": os.path.join(gen3_path, "Emerald"),
    "fr": os.path.join(gen3_path, "Fire Red"),
    "lg": os.path.join(gen3_path, "Leaf Green"),
    "scarlet": os.path.join(gen9_path, "Scarlet"),
    "violet": os.path.join(gen9_path, "Violet")
}

#Might change this list at some point so it can properly grab the name of the game instead of matching the input code
print("Please enter the game you would like to play.")
print("The games and their codes are as follows:\n")
gamesList = [
    ["Game Name", "Input Code\n"],
    ["Red Version", "red"],
    ["Blue Version", "blue"],
    ["Yellow Version", "yellow"],
    ["Ruby Version", "ruby"],
    ["Sapphire Version", "sapphire"],
    ["Emerald Version", "emerald"],
    ["Fire Red Version", "fr"],
    ["Leaf Green Version", "lg"],
    ["Scarlet Version", "scarlet"],
    ["Violet Version", "violet"]
]

#Makes a table out of gamesList with the input code for the input showing up next to it
#input codes are helpful for remakes that have extra words on their names, like Fire Red being FR or Brilliant Diamond being BD
for row in gamesList:
    print(f"{row[0]:<20} {row[1]:<10}")
print("")

#Loop to make sure input is for a valid version, while also making sure whitespace and capitalization is taken care of
gameChoice = ""
while gameChoice not in gamePaths:
    # print("The current versions available are: Red, Blue, Yellow, and Emerald")
    gameChoice = input("Please enter the code for the version you would like to play: ").strip().lower()
    print("")
    if gameChoice not in gamePaths:
        print("Please enter a valid version. Make sure you're looking at the 'Input Code' column above")

#defining usePath so the file gets the proper text files for the input
usePath = gamePaths[gameChoice]

#File Name Input, lets the user name their files
while True:
    fileNameInput = input("Please name your file (Max 35 characters, alphanumeric only): ")
    fileName = re.sub(r'[^a-zA-Z0-9\s]', '', fileNameInput)
    if len(fileName) <= 35 and len(fileName) > 0:
        break
    else:
        print("That file name is invalid.")


#Output path takes the string from fileName and makes it the name of the file in the correct spot
output_path = os.path.join(script_dir,'Output',f'{fileName}.txt')
fo = open(output_path,'w')

#Some files will need to be redone for formatting to make it look nicer
# ("Pokemon Name (% chance floor, % chance floor/floor2)") putting commas inbetween the different percentages instead of more slashes
startersFilePath = os.path.join(usePath,'starters.txt')
routesFilePath = os.path.join(usePath,'routes.txt')
citiesFilePath = os.path.join(usePath,'cities.txt')
dungeonsFilePath = os.path.join(usePath,'dungeons.txt')

#All the rules of the playthrough, complete with a function to write them all to the top of the output document
#This potentially will be consolidated to an external document rather than being in the code itself but it's not guaranteed
rulesText = [
    "Welcome to the Pokemon Nuzlocke - Specific Catch Ruleset!\n",
    "\n",
    "While the traditional Nuzlocke rules apply, there are some changes so here's all the rules including traditional ones:\n",
    "1) All Pokemon must be nicknamed.\n",
    "2) Any Pokemon that faints is considered \"dead\" and must be released (or kept in your box if you prefer).\n",
    "3) You can only catch the Pokemon listed here for each location. For example if Route 1 has Pidgey next to it, you can only catch Pidgey there.\n",
    "\n",
    "Optional Rules\n",
    "1) The list also has a random starter listed, along with a \"Wildcard\" option which lets you pick yours if you roll it.\n",
    "2) If you get a duplicate rolled, whether by catching it earlier or evolving an already caught one, you can either:\n",
    "    - Catch the first non-duplicate Pokemon you encounter.\n",
    "    OR\n",
    "    - Treat the location as a \"Wildcard\" and pick whichever Pokemon you want.\n",
    "3) If you roll a Pokemon that has a 10% or lower spawn rate (Which is stated next to the mon)\n",
    "    you can choose to do that route in normal Nuzlocke style or treated it as a \"Wildcard\".\n",
    "4) You also have access to any other optional rules, such as the Wobuffet Clause or the Shiny Clause.\n",
    "5) Water on routes with both land and water encounters are special (for now). You can either:\n",
    "    - Treat each as a separate location (so you can get two encounters).\n",
    "    OR\n",
    "    - Catch either one or the other.\n"
    "6) Unique encounters such as static Pokemon (like Kecleon in Gen 3 or Sudowoodo in Gen 2) and trades can be gotten in addition to Pokemon already caught\n"
    "    in the location\n"
    "\n",
    f"With all of this out of the way, here's your Pokemon list for this playthrough!\n",
    "\n"
]
for line in rulesText:
    print(line)
    fo.write(line)

if gameChoice == "scarlet" or gameChoice == "violet":
    print("IMPORTANT INFO FOR SCARLET AND VIOLET")
    print("The data the internet has for Scarlet and Violet is lacking in a lot of ways, so rather than try and put a specific percentage")
    print("If you spend too long trying to find a Pokemon (subjective), then consider the area a Wildcard\n")
    fo.write("IMPORTANT INFO FOR SCARLET AND VIOLET\n")
    fo.write("The data the internet has for Scarlet and Violet is lacking in a lot of ways, so rather than try and put a specific percentage\n")
    fo.write("If you spend too long trying to find a Pokemon (subjective), then consider the area a Wildcard\n")
    fo.write("\n")

#The headers have extra new lines and print statements to properly format it on the output on the document and in the terminal
#That way its easier to read
print("STARTER CHOICE")
fo.write("STARTER CHOICE\n")
print("")
fo.write("\n")

#Starter Loop Here
with open(startersFilePath, 'r') as f:
    for line in f:
        starterParts = line.strip().split(":")
        starterName = starterParts[0]
        starterTuple = ast.literal_eval(starterParts[1])
        randomStarter = random.choice(starterTuple)
        starterChoice = (f"{starterName} - {randomStarter}")
        print(starterChoice)
        fo.write(f"{starterChoice}\n")

print("")
fo.write("\n")
print("ROUTES LIST")
fo.write("ROUTES LIST\n")
print("")
fo.write("\n")

#Route Loop Here
with open(routesFilePath,'r') as f:
    for line in f:
        routeParts = line.strip().split(":")
        routeName = routeParts[0]
        routeTuple = ast.literal_eval(routeParts[1])
        randomRoute = random.choice(routeTuple)
        routeChoice = (f"{routeName} - {randomRoute}")
        print(routeChoice)
        fo.write(f"{routeChoice}\n")

print("")
fo.write("\n")
print("CITIES LIST")
fo.write("CITIES LIST\n")
print("")
fo.write("\n")

#Cities Loop Here
with open(citiesFilePath,'r') as f:
    for line in f:
        cityParts = line.strip().split(":")
        cityName = cityParts[0]
        cityTuple = ast.literal_eval(cityParts[1])
        randomCity = random.choice(cityTuple)
        cityChoice = (f"{cityName} - {randomCity}")
        print(cityChoice)
        fo.write(f"{cityChoice}\n")

print("")
fo.write("\n")
print("DUNGEONS LIST")
fo.write("DUNGEONS LIST\n")
print("")
fo.write("\n")

#Dungeons Loop Here
with open(dungeonsFilePath,'r') as f:
    for line in f:
        dungeonParts = line.strip().split(":")
        dungeonName = dungeonParts[0]
        dungeonTuple = ast.literal_eval(dungeonParts[1])
        randomDungeon = random.choice(dungeonTuple)
        dungeonChoice = (f"{dungeonName} - {randomDungeon}")
        print(dungeonChoice)
        fo.write(f"{dungeonChoice}\n")

print("")
fo.write("\n")
print("")
fo.write("\n")

#Shameless self plug
print("Enjoy your playthrough! If you have any questions or wish to support me,")
print("you can find DragonKurask on Discord, at @DragonKurask on X/Twitter, or @dragonkurask.bsky.social on Bluesky.")
print("You can also find me streaming on either on Twitch at https://www.twitch.tv/dragonkurask or")
print("on Youtube at https://www.youtube.com/@dragonkurask")
fo.write("Enjoy your playthrough! If you have any questions or wish to support me,\n")
fo.write("you can find DragonKurask on Discord, at @DragonKurask on X/Twitter, or @dragonkurask.bsky.social on Bluesky.\n")
fo.write("You can also find me streaming on either on Twitch at https://www.twitch.tv/dragonkurask or\n")
fo.write("on Youtube at https://www.youtube.com/@dragonkurask\n")

#input statement to keep the terminal window opening at the end so the user can look at it without having to look in their folder
print("")
end = input("Input anything and press Enter to close the window. Your file has been saved to the \"Output\" in this directory.\n")
fo.close()