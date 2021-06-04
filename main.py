import os
from random import randint

from dotenv import load_dotenv
from ogame import OGame
from ogame.constants import buildings, mission, coordinates, speed, ships

load_dotenv(".env")

USER = "{}@{}".format(os.environ.get("EMAIL_USERNAME"), os.environ.get("EMAIL_DOMAIN"))
PASSWORD = os.environ.get("PASSWORD")
UNIVERSE = os.environ.get("UNIVERSE")

empire = OGame(UNIVERSE, USER, PASSWORD)
#
# player_id = empire.player_id
#
# resources = empire.resources(player_id)
#
# print(f"Metal: {resources.metal}, Cristal: {resources.crystal},"
#       f"Deuterium: {resources.deuterium}, Energy: {resources.energy}, Darkmatter: {resources.darkmatter}")

# # Moon
# moon_ids = empire.moon_ids()
# print(moon_ids)
#
# # Fleet
# for fleet in empire.fleet():
#     if fleet.mission == mission.expedition:
#         print(fleet.list)
#         print(
#                 fleet.id,
#                 fleet.mission,
#                 fleet.diplomacy,
#                 fleet.player,
#                 fleet.player_id,
#                 fleet.returns,
#                 fleet.arrival,
#                 fleet.origin,
#                 fleet.destination
#             )
#
#     # Send fleet
#     empire.send_fleet(mission=mission.expedition,
#                       id=id,
#                       where=coordinates(1, 12, 16),
#                       ships=fleet(light_fighter=12, bomber=1, cruiser=100),
#                       resources=[0, 0, 0],  # optional default no resources
#                       speed=speed.max,      # optional default speed.max
#                       holdingtime=2)        # optional default 0 will be needed by expeditions
#
# # send expe
# for expedition in range(4):
#     empire.send_fleet(mission=mission.expedition,
#                       id=empire.id_by_planet_name('Main_Planet'),
#                       where=coordinates(randint(1, 6), randint(1, 499), 16),
#                       ships=[ships.explorer(100), ships.large_transporter(200)],
#                       holdingtime=1)

for empire_id in empire.planet_ids():
    # Ship
    ship = empire.ships(empire_id)
    supply = empire.supply(empire_id)
    res = empire.resources(empire_id)
    if res.energy < 0 and not supply.solar_plant.is_possible:
        print("Build solar_satellite")
        empire.build(buildings.solar_satellite(100), empire_id)
    else:
        print("Build solar_plant")
        empire.build(buildings.solar_plant, empire_id)

    if supply.metal_mine.is_possible:
        print("Build metal_mine")
        empire.build(buildings.metal_mine, empire_id)

    if supply.crystal_mine.is_possible:
        print("Build crystal_mine")
        empire.build(buildings.crystal_mine, empire_id)
