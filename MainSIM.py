from random_word import RandomWords
import random

#pip3 install random-words
r = RandomWords()

all_heroes = ['Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'DIVA', 'Doomfist', 'Echo', 'Genji', 'Hanzo', 'Junkrat', 'Lucio',
 'Mccree', 'Mei', 'Mercy', 'Moira', 'Orisa' , 'Pharah', 'Reaper' ,'Reinhardt', 'Roadhog', 'Sigma', 'Soldier 76', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker',
 'Winston', 'Hammond', 'Zarya', 'Zenyatta']


all_tanks = [5, 16, 19, 20, 21, 28, 29, 30]

all_supports = [0, 2, 4, 11, 14, 15, 31]

all_damage = [1, 3, 6, 7, 8, 9, 10, 12, 13, 17, 18, 22, 23, 24, 25, 26, 27]

brawl_tanks = [19, 30]

brawl_damage = [12, 18, 22]

brawl_support = [15, 11, 4]

dive_tanks = [5, 28, 29]

dive_damage = [6, 7, 8, 17, 23, 26]

dive_support = [0, 11, 14, 31]

bunker_tanks = [16, 20, 21, 19]

bunker_damage = [1, 3, 9, 10, 22, 24, 25, 27]

bunker_support = [2, 14, 15]

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

    def __init__(self, rank_start, rank_end, role_variable):
        self.name = "BigGamer" + str(random.randint(10,500))
        self.rank = random.randint(rank_start, rank_end)
        player_average = rank_start + rank_end / 2
        # making sure 2-2-2 is enforced
        self.role_variable = role_variable
        if role_variable == 0:
            self.mainID = random.choice(all_tanks)
        if role_variable == 1:
            self.mainID = random.choice(all_supports)
        if role_variable == 2:
            self.mainID = random.choice(all_damage)
        self.swap_willingness = random.randint(1,100)
        self.frustration = 0
        self.char_being_played = self.mainID
        self.last_played = self.mainID
        self.deaths = 0
        self.eliminations = 0
        self.heroes_played = {self.mainID: 1}
        self.fun_had = 100
        self.personality_type = str(random.choices(
            [1,2,3,4,5],
            weights = [0.1, 0.2, 0.3, ( player_average / 7000), (player_average / 7000)],
            k = 1
        )[0]) # 1-5. with 1 being the most hostile, and 5 being the best teammate you can get


    def swapHero(self, new_hero):
        self.last_played = self.char_being_played
        self.char_being_played = new_hero
        if new_hero in self.heroes_played:
            self.heroes_played[new_hero] += 1
        else:
            self.heroes_played[new_hero] = 1
        print(self.name + " has swapped to " + self.char_being_played)


    

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
Hammond = Hero(29, 0, 0, 80, 90, 0, 90, 75, 80, 95, 75, ['Quad Cannons', 'Roll', 'Piledriver'], [1,['Mines']])
Zarya = Hero(30, 0, 1, 10, 20, 0, 45, 45, 65, 55, 70, ['Particle Cannon'], [2,['Graviton Surge']])
Zenyatta = Hero(31, 2, 0, 90, 5, 55, 5, 85, 100, 15, 70, ['Orbs of Destruction'], [0,['Orb of Harmony', 'Transcendence']])

# order is tanks 0, damage 1, support 2
meta_comp = [[31,29], [26, 7, 1, 9], [14, 4, 2]]

# These are all lists of things for players to say in and after the games
choosing_hero_sentences_angriest = ['bro, i f****** hate this hero', 'this s*** is garbage', 'I hate this dogs*** meta', 'F*** THIS F****** GAME', 'im about to f****** throw']
choosing_hero_sentences_upset = ["i guess ill play this guy", 'am i really stuck on this hero', 'i shouldnt have queued']
choosing_hero_random = ['whats up guys?', 'wuz goo', 'whats crackin', 'yo', 'Yo', 'Hey']

end_of_game_angry = ['was i the only one playing?', 'our mercy threw', 'F*** THIS GAME', 'serious question. were our dps throwing?', 'gg. tank diff', 'support diff', 'dps diff']
end_of_game = ['I feel very, very small... please hold me...', "I'm trying to be a nicer person. It's hard, but I'm trying, guys.", "I'm wrestling with some insecurity issues in my life but thank you for playing with me.", 'gg' 'GGs', 'good try', 'gg go next']

# Create a range for the ranks of the players
rank_start = int(input("Enter rank range start: "))
rank_end = int(input("Enter rank range end: "))

# Both team lists
red_team = []
blue_team = []

# Generate the players, and make it 2-2-2
for team_used in [red_team, blue_team]:
    for player_used in range(6):
        role_type = None
        if player_used == 0 or player_used == 1:
            role_type = 0
        elif player_used == 2 or player_used == 3:
            role_type = 1
        else:
            role_type = 2
        team_used.append(Player(rank_start, rank_end, role_type))


for x in red_team:
    print(x.name + "'s main is " + all_heroes[x.mainID] + ", they're on red team, and their personality type is: " + x.personality_type)

for x in blue_team:
    print(x.name + "'s main is " + all_heroes[x.mainID] + ", they're on blue team, and their personality type is: " + x.personality_type)


# ---------------------- First game ---------------------------------


# First hero pick

#try to pick their main

for current_team in [red_team, blue_team]:
    sr_average = (rank_start + rank_end) / 2
    swap_said = False
    comp_synergy = {}
    meta_synergy = []
    synergy_use_list = None
    team_swap_num = 0
    person_on_main = 0
    # these numbers are for flat support, visible power and non visible
    team_support = 0
    team_damage = 0
    team_tanking = 0
    # these are for the visible and non visible cap
    team_damage_amplified = 0
    team_tanking_amplified = 0
    
    # Creating lists to see how close the teams are to synergy or meta comp
    for i in current_team:
        if i.play_style in comp_synergy:
            comp_synergy[i.play_style] += 1
        else:
            comp_synergy[i.play_style] = 1

        if i.play_style in meta_comp:
            meta_synergy += i.play_style

    comp_synergy_key = max(comp_synergy, key=comp_synergy.get())

    # Check if their team is closer to meta comp, or a certain synergy

    if len(meta_synergy) > comp_synergy[comp_synergy_key]:
        team_swap_num = 3
        synergy_use_list = meta_comp
        #this means meta comp
    else:
        team_swap_num = comp_synergy_key
        if comp_synergy_key == 0:
            synergy_use_list = [dive_tanks, dive_damage, dive_support]
        elif comp_synergy_key == 1:
            synergy_use_list = [brawl_tanks, brawl_damage, brawl_support]
        else:
            synergy_use_list = [bunker_tanks, bunker_damage, bunker_support]
        #this will swap to the number. ex 0 means dive 1 is brawl and 2 is bunker
    
    chars_picked = []
    for x in current_team:

        if swap_said == False:
            swap_options = random.choices(
                [1,2,3],
                # 1 is swapping to a comp with synergy/meta, 2 is their main, and 3 is random
                weights = [((sr_average * x.swap_willingness) / (250,000 / int(x.personality_type))), 0.7, 0.2],
                k=1
            )

            # if elect to swap to a comp with synergy
            if swap_options = 1:
                #if the synergy comp is dive
                if team_swap_num == 0:
                    print(x.name + ": Lets go dive")
                    # 0 in role is tank
                    # synergy order is tank 0, damage 1, support 2
                    swap_var = None
                    if x.role_variable == 0:
                        compar_chars = {}
                        for f in dive_tanks:
                            if f in synergy_use_list[0]:
                                compar_chars[f] = 0
                        for f in compar_chars:
                            eval(compar_chars[f])
                        
                                

                    elif x.role_variable == 1:
                        swap_var = dive_damage
                    else:
                        swap_var = dive_support
                    
                    x.swapHero(swap_var)
                        x.char_being_played = x.role_variable
                swap_said = True

        if x.mainID not in chars_picked:
            x.char_being_played = x.mainID
            chars_picked.append(x.mainID)
            person_on_main = [x.name, x.char_being_played]
        else: 
            #change here to look in their history for a hero that can be picked
            if 
                        
            #put the possibility of leaving here
            if random.random() < 0.2:
                print(x.name + ": " + choosing_hero_sentences_angriest)



for i in range(4):
    for current_team in [red_team, blue_team]:

        for x in current_team:
            if i == 3 and random.choices(
                [True, False],
                weights = [],
                k = 1
            )
            



#During round



# End of round
#------------------------------------
# For each player, update the heroes played with the current one
for current_team in [red_team, blue_team]:
    for x in current_team:
        # Check to see if they swapped that round
        if x.last_played != x.char_being_played:
            if x.char_being_played in x.heroes_played:
                x.heroes_played[x.char_being_played] += 1
            else: 
                x.heroes_played[x.char_being_played] = 1
        x.last_played = x.char_being_played





# ----------------------- End of Game -----------------------------------

