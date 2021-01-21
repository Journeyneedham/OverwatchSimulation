from random_word import RandomWords
import random

#pip3 install random-words
r = RandomWords()

all_heroes = ['Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'D.va', 'Doomfist', 'Echo', 'Genji', 'Hanzo', 'Junkrat', 'Lucio',
 'Mccree', 'Mei', 'Mercy', 'Moira', 'Orisa' , 'Pharah', 'Reaper' ,'Reinhardt', 'Roadhog', 'Sigma', 'Soldier 76', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker',
 'Winston', 'Wrecking Ball', 'Zarya', 'Zenyatta']


class Hero:

    def __init__(self, id_number, role_type, play_style, map_user, map_controller, support_out, NV_power, V_power, Vpower_CAP, NVpower_CAP, fun, abilities, ultimate):
        self.id_number = id_number
        self.name = all_heroes[id_number]
        self.role_type = role_type #0 is tank, 1 is dps and 2 is support
        self.play_style = play_style #0 is dive, 1 is brawl, 2 is bunker
        self.map_user = map_user #1-100 based on if they need positioning or healthpacks
        self.map_controller = map_controller #1-100 based on how well they control positioning
        self.support_out = support_out #1-100 based on amount of support (healing + utility)
        self.NV_power = NV_power #Non-visible power, based on position control and tanking ability | 1-100
        self.V_power = V_power #Visible power, based on damage output
        self.Vpower_CAP = Vpower_CAP
        self.NVpower_CAP = NVpower_CAP
        self.Support_X_Vpower = Vpower_CAP / V_power
        self.Support_X_NVpower = NVpower_CAP / NV_power
        self.fun = fun
        self.abilities = abilities
        self.ultimate = ultimate[1]
        self.ultimateType = ultimate[0] # either 0 for used on teammates, or 1 for enemies, or 2 for CC


class Player:

    def __init__(self, rank_start, rank_end):
        self.name = "BigGamer" + str(random.randint(10,500))
        self.rank = random.randint(rank_start, rank_end)
        self.mainID = random.randint(0,31)
        self.swap_willingness = random.randint(1,100)
        self.frustration = random.randint(1,40)
        self.char_being_played = self.mainID

    

# id    role type   play style   map user    map controller    support out     Non vis power   vis power   vis cap   nonvis cap   fun  abilities  ultimate 
# [1 ]  {  2   }   [    3     ]  [  4   ]   [     5       ]    [    6    ]     {    7      }   [    8  ]   [ 9   ]   [   10   ]  [11]  [  12   ]  [ 13   ]

Ana = Hero(0, 2, 2, 80, 15, 85, 5, 5, 10, 15, 65, ['Sleep Dart', 'Biotic Grenade', 'Biotic Rifle'], [0,['Nanoboost', 'Biotic Rifle', 'Biotic Grenade']])
Ashe = Hero(1, 1, 2, 60, 20, 0, 15, 90, 130, 15, 80, ['Dynamite', 'Coach Gun'], [1,['Bob']])
Baptiste = Hero(2, 2, 2, 5, 10, 95, 5, 80, 85, 15, 60, ['Biotic Launcher'], [0,['Amplification Matrix']])
Bastion = Hero(3, 1, 2, 70, 75, 5, 35, 60, 90, 55, 60, ['Sentry Mode', 'Recon Mode'], [1,['Tank Mode']])
Brigitte = Hero(4, 2, 1, 20, 75, 80, 60, 35, 40, 80, 10, ['Flail', 'Shield Bash', 'Whip'], [0,['Inspire', 'Rally', 'Repair Throw']])
DIVA = Hero(5, 0, 0, 5, 80, 0, 40, 30, 35, 50, 40, ['Rockets', 'Fusion Cannons', 'Self-Destruct'], [0,['Defense Matrix']])
Doomfist = Hero(6, 1, 0, 90, 20, 0, 35, 65, 75, 40, 55, ['Slam', 'Upper Cut', 'Punch'], [1,['Meteor Strike']])
Echo = Hero(7, 1, 0, 30, 70, 0, 65, 95, 180, 105, 90, ['Tri-Shot', 'Sticky Bombs', 'Focusing Beam'], [1,['Duplicated Hero']])
Genji = Hero(8, 1, 0, 50, 10, 0, 10, 70, 90, 15, 90, ['Shuriken', 'Deflect'], [1,['Dragonblade']])
Hanzo = Hero(9, 1, 2, 30, 40, 0, 25, 90, 140, 35, 85, ['Storm Bow', 'Storm Arrow'], [1,['Dragonstrike']])
Junkrat = Hero(10, 1, 2, 30, 25, 0, 35, 50, 70, 40, 80, ['Frag Launcher', 'Mine', 'Trap'], [1,['Riptire']])
Lucio = Hero(11, 2, 0, 40, 5, 40, 5, 10, 10, 50, 80, ['Sonic Amplifier', 'Boop'], [0,['Crossfade', 'Sound Barrier']])
McCree = Hero(12, 1, 1, 70, 70, 0, 25, 80, 110, 30, 80, ['Revolver', 'Fan the Hammer'], [2,['Flash']])
Mei = Hero(13, 1, 1, 30, 60, 0, 45, 80, 90, 50, 65, ['Ice-cicle', 'Freeze'], [2,['Blizzard', 'Freeze']])
Mercy = Hero(14, 2, 0, 5, 10, 90, 5, 5, 10, 50, 80, ['Blaster'], [0,['Healing Beam', 'Resurrection']])
Moira = Hero(15, 2, 1, 5, 40, 75, 5, 20, 25, 15, 40, ['Biotic Grasp', 'Biotic Orb', 'Coalescence'], [0,['Coalescence', 'Biotic Orb', 'Biotic Grasp']])
Orisa = Hero(16, 0, 2, 40, 65, 0, 55, 30, 35, 60, 5, ['Fusion Driver', 'Pull'], [0,['Supercharger', 'Barrier']])
Pharah = Hero(17, 1, 0, 20, 10, 0, 15, 40, 90, 50, 70, ['Rocket Launcher'], [1,['Barrage']])
Reaper = Hero(18, 1, 1, 50, 10, 0, 20, 60, 65, 25, 75, ['Shotguns'], [1,['Death Blossom']])
Reinhardt = Hero(19, 0, 1, 20, 35, 0, 55, 30, 50, 65, 30, ['Hammer', 'Firestrike', 'Charge'], [2,['Earthshatter']])
Roadhog = Hero(20, 0, 2, 20, 70, 0, 45, 65, 80, 65, 80, ['Scrap Gun', 'Hook'], [1,['Whole Hog']])
Sigma = Hero(21, 0, 2, 10, 40, 0, 75, 70, 80, 85, 70, ['Hyperspheres', 'Rock', 'Gravitic Flux'], [2,['Rock']])
Soldier = Hero(22, 1, 1, 35, 20, 10, 20, 75, 95, 35, 75, ['Pulse Rifle', 'Helix Missile', 'Tactical Visor'], [0,['Biotic Field']])
Sombra = Hero(23, 1, 0, 30, 90, 15, 25, 60, 70, 30, 60, ['Machine Pistol'], [2,['EMP', 'Hack']])
Symmetra = Hero(24, 1, 2, 20, 50, 0, 45, 55, 70, 70, 40, ['Photon Beam', 'Sentry Turret'], [0,['Photon Barrier']])
Torbjorn = Hero(25, 1, 2, 10, 40, 0, 55, 65, 75, 65, 75, ['Rivet Gun', 'Hammer', 'Turret'], [1,['Molten Core']])
Tracer = Hero(26, 1, 0, 80, 35, 0, 35, 90, 100, 55, 85, ['Pulse Pistols'], [1,['Pulse Bomb']])
Widowmaker = Hero(27, 1, 2, 80, 40, 0, 65, 70, 100, 75, 75, ['Sniper'], [1,['Venom Mine']])
Winston = Hero(28, 0, 0, 50, 35, 0, 55, 30, 45, 65, 40, ['Tesla Cannon', 'Jump Pack'], [1,['Primal Rage']])
WreckingBall = Hero(29, 0, 0, 80, 90, 0, 90, 75, 80, 95, 75, ['Quad Cannons', 'Roll', 'Piledriver'], [1,['Mines']])
Zarya = Hero(30, 0, 1, 10, 20, 0, 45, 45, 65, 55, 70, ['Particle Cannon'], [2,['Graviton Surge']])
Zenyatta = Hero(31, 2, 0, 90, 5, 55, 5, 85, 100, 15, 70, ['Orbs of Destruction'], [0,['Orb of Harmony', 'Transcendence']])






rank_start = int(input("Enter rank range start: "))
rank_end = int(input("Enter rank range end: "))

red_team = []
blue_team = []

all_teams = [red_team, blue_team]

for team_used in all_teams:
    for player_used in range(6):
        team_used.append(Player(rank_start, rank_end))


for x in red_team:
    print(x.name + ' and their main is ' + all_heroes[x.mainID] + ' and theyre on red team')

for x in blue_team:
    print(x.name + ' and their main is ' + all_heroes[x.mainID] + ' and theyre on blue team')

