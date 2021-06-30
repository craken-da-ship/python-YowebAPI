##This will be a future interation to make for easier selection from API
##and possiblibly future use as a discord bot.

import base

OCEAN_NAME = 'Emerald'
PIRATE_NAME = 'Ritok'
CREW_ID = 5031339

OCEAN = base.Ocean(OCEAN_NAME)
PIRATE = OCEAN.getpirate(PIRATE_NAME)
CREW = OCEAN.getcrew(CREW_ID)


print(PIRATE.affiliations.crew.rank)
