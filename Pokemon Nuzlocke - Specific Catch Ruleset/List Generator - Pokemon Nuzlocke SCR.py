import random
import os
import ast

#gets the directory for the file no matter where the file is
#Though the file won't do much if you mess with the folders that are needed with the rest of the file
script_dir = os.path.dirname(os.path.abspath(__file__))

#Folder path shortcutes for each game
gen1_path = os.path.join(script_dir,'Games Folders','Generation 1 RBY')
gen3_path = os.path.join(script_dir,'Games Folders','Generation 3 RSE')

#Dictionary for games and their folder paths to prep for proper input from the input statement loop
gameList = {
    "red":os.path.join(gen1_path, "Red"),
    "blue": os.path.join(gen1_path, "Blue"),
    "emerald": os.path.join(gen3_path, "Emerald")
}

#Loop to make sure input is for a valid version, while also making sure whitespace and capitalization is taken care of
print("Please enter the game you would like to play.")
gameChoice = ""
while gameChoice not in gameList:
    print("The current versions available are: Red, Blue and Emerald")
    gameChoice = input("Please enter which version you would like to play: ").strip().lower()
    print("")
    if gameChoice not in gameList:
        print("Please enter a valid version.")

#defining usePath so the file gets the proper text files for the input
usePath = gameList[gameChoice]

#Output path with funny formatting to make the output file match the game choice so a user can have multiple games at the same time
output_path = os.path.join(script_dir,'Output',f'{gameChoice.capitalize()} Version Output.txt')
fo = open(output_path,'w')

startersFilePath = os.path.join(usePath,'starters.txt')
routesFilePath = os.path.join(usePath,'routes.txt')
citiesFilePath = os.path.join(usePath,'cities.txt')
dungeonsFilePath = os.path.join(usePath,'dungeons.txt')

#All the rules of the playthrough, complete with a function to write them all to the top of the output document
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
    f"With all of this out of the way, here's your Pokemon list for {gameChoice.capitalize()} version!\n",
    "\n"
]
for line in rulesText:
    print(line)
    fo.write(line)

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