import os

from dotenv import load_dotenv
from ogame import OGame
from ogame.constants import buildings

load_dotenv(".env")

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
UNIVERSE = os.environ.get("UNIVERSE")

empire = OGame(UNI, USER, PASSWORD)
#
# player_id = empire.player_id
#
# resources = empire.resources(player_id)
#
# print(f"Metal: {resources.metal}, Cristal: {resources.crystal},"
#       f"Deuterium: {resources.deuterium}, Energy: {resources.energy}, Darkmatter: {resources.darkmatter}")


for id in empire.planet_ids():
    supply = empire.supply(id)
    res = empire.resources(id)
    if res.energy < 0 and not supply.solar_plant.is_possible:
        print("Build solar_satellite")
        empire.build(buildings.solar_satellite(100), id)
    else:
        print("Build solar_plant")
        empire.build(buildings.solar_plant, id)

    if supply.metal_mine.is_possible:
        print("Build metal_mine")
        empire.build(buildings.metal_mine, id)

    if supply.crystal_mine.is_possible:
        print("Build crystal_mine")
        empire.build(buildings.crystal_mine, id)
