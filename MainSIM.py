from random_word import RandomWords
import random

#pip3 install random-words
r = RandomWords()

all_heroes = ['Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'DIVA', 'Doomfist', 'Echo', 'Genji', 'Hanzo', 'Junkrat', 'Lucio',
 'McCree', 'Mei', 'Mercy', 'Moira', 'Orisa' , 'Pharah', 'Reaper' ,'Reinhardt', 'Roadhog', 'Sigma', 'Soldier', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker',
 'Winston', 'Hammond', 'Zarya', 'Zenyatta']


all_tanks = [5, 16, 19, 20, 21, 28, 29, 30]

all_supports = [0, 2, 4, 11, 14, 15, 31]

all_damage = [1, 3, 6, 7, 8, 9, 10, 12, 13, 17, 18, 22, 23, 24, 25, 26, 27]

# order is tanks 0, damage 1, support 2

brawl_comp = [[19, 30], [12, 18, 22], [15, 11, 4]]

dive_comp = [[5, 28, 29], [6, 7, 8, 17, 23, 26], [0, 11, 14, 31]]

bunker_comp = [[16, 20, 21, 19], [1, 3, 9, 10, 22, 24, 25, 27], [2, 14, 15]]

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

    def __init__(self, rank_start, rank_end, role_variable, player_id):
        self.name = "BigGamer" + str(random.randint(10,500))
        self.rank = random.randint(rank_start, rank_end)
        self.player_id = player_id
        player_average = rank_start + rank_end / 2
        # making sure 2-2-2 is enforced
        self.role_variable = role_variable
        self.mainID = None
        if role_variable == 0:
            self.mainID = random.choice(all_tanks)
        if role_variable == 1:
            self.mainID = random.choice(all_supports)
        if role_variable == 2:
            self.mainID = random.choice(all_damage)
        self.swap_willingness = random.randint(1,100)
        self.char_being_played = self.mainID
        self.last_played = self.mainID
        self.current_value = 1
        self.deaths = 0
        self.eliminations = 0
        self.heroes_played = {self.mainID: {self.mainID: 1, 'value': 1}}
        self.fun_had = 100
        self.personality_type = str(random.choices(
            [1,2,3,4,5],
            weights = [0.1, 0.2, 0.3, ( player_average / 7000), (player_average / 7000)],
            k = 1
        )[0]) # 1-5. with 1 being the most hostile, and 5 being the best teammate you can get
        self.frustration = (5 - int(self.personality_type)) * random.randint(1,8)


    def swapHero(self, new_hero):
        self.last_played = self.char_being_played
        self.char_being_played = new_hero
        if new_hero in self.heroes_played:
            self.heroes_played[new_hero][new_hero] += 1
            self.heroes_played[new_hero]['value'] = self.heroes_played[new_hero]['value'] + self.current_value
        else:
            self.heroes_played[new_hero] = {new_hero : 1, 'value' : self.current_value}
        self.current_value = 0
        print(self.name + " has swapped to " + all_heroes[self.char_being_played])

    def addValue(self):
        if self.char_being_played in self.heroes_played:
            self.heroes_played[self.char_being_played]['value'] += self.current_value
            self.current_value = 0
        else:
            self.heroes_played[self.char_being_played] = {current_hero : 1, 'value' : self.current_value}
            self.current_value = 0

    

# id    role type   play style   map user    map controller    support out     Non vis power   vis power   vis cap   nonvis cap   fun  abilities  ultimate 
# [1 ]  {  2   }   [    3     ]  [  4   ]   [     5       ]    [    6    ]     {    7      }   [    8  ]   [ 9   ]   [   10   ]  [11]  [  12   ]  [ 13   ]

Ana = Hero(0, 2, 2, 80, 15, 85, 5, 5, 10, 15, 65, ['Sleep Dart', 'Biotic Grenade', 'Biotic Rifle'], [0,['Nanoboost', 'Biotic Rifle', 'Biotic Grenade']])
Ashe = Hero(1, 1, 2, 60, 20, 0, 15, 90, 130, 15, 80, ['Dynamite', 'Coach Gun'], [1,['Bob']])
Baptiste = Hero(2, 2, 2, 5, 10, 95, 5, 80, 85, 15, 60, ['Biotic Launcher'], [0,['Amplification Matrix']])
Bastion = Hero(3, 1, 2, 70, 75, 5, 25, 60, 90, 35, 60, ['Sentry Mode', 'Recon Mode'], [1,['Tank Mode']])
Brigitte = Hero(4, 2, 1, 20, 75, 80, 25, 35, 40, 35, 10, ['Flail', 'Shield Bash', 'Whip'], [0,['Inspire', 'Rally', 'Repair Throw']])
DIVA = Hero(5, 0, 0, 5, 80, 0, 40, 30, 35, 50, 40, ['Rockets', 'Fusion Cannons', 'Self-Destruct'], [0,['Defense Matrix']])
Doomfist = Hero(6, 1, 0, 90, 20, 0, 25, 65, 75, 30, 55, ['Slam', 'Upper Cut', 'Punch'], [1,['Meteor Strike']])
Echo = Hero(7, 1, 0, 30, 70, 0, 15, 95, 180, 25, 90, ['Tri-Shot', 'Sticky Bombs', 'Focusing Beam'], [1,['Duplicated Hero']])
Genji = Hero(8, 1, 0, 50, 10, 0, 10, 70, 90, 15, 90, ['Shuriken', 'Deflect'], [1,['Dragonblade']])
Hanzo = Hero(9, 1, 2, 30, 40, 0, 15, 90, 140, 25, 85, ['Storm Bow', 'Storm Arrow'], [1,['Dragonstrike']])
Junkrat = Hero(10, 1, 2, 30, 25, 0, 15, 50, 70, 20, 80, ['Frag Launcher', 'Mine', 'Trap'], [1,['Riptire']])
Lucio = Hero(11, 2, 0, 40, 5, 40, 5, 10, 10, 25, 80, ['Sonic Amplifier', 'Boop'], [0,['Crossfade', 'Sound Barrier']])
McCree = Hero(12, 1, 1, 70, 70, 0, 25, 80, 110, 30, 80, ['Revolver', 'Fan the Hammer'], [2,['Flash']])
Mei = Hero(13, 1, 1, 30, 60, 0, 25, 80, 90, 35, 65, ['Ice-cicle', 'Freeze'], [2,['Blizzard', 'Freeze']])
Mercy = Hero(14, 2, 0, 5, 10, 90, 5, 5, 10, 30, 80, ['Blaster'], [0,['Healing Beam', 'Resurrection']])
Moira = Hero(15, 2, 1, 5, 40, 75, 5, 20, 25, 15, 40, ['Biotic Grasp', 'Biotic Orb', 'Coalescence'], [0,['Coalescence', 'Biotic Orb', 'Biotic Grasp']])
Orisa = Hero(16, 0, 2, 40, 65, 0, 55, 30, 35, 75, 5, ['Fusion Driver', 'Pull'], [0,['Supercharger', 'Barrier']])
Pharah = Hero(17, 1, 0, 20, 10, 0, 10, 40, 90, 40, 70, ['Rocket Launcher'], [1,['Barrage']])
Reaper = Hero(18, 1, 1, 50, 10, 0, 20, 60, 65, 25, 75, ['Shotguns'], [1,['Death Blossom']])
Reinhardt = Hero(19, 0, 1, 20, 35, 0, 55, 30, 50, 65, 30, ['Hammer', 'Firestrike', 'Charge'], [2,['Earthshatter']])
Roadhog = Hero(20, 0, 2, 20, 70, 0, 45, 65, 80, 65, 80, ['Scrap Gun', 'Hook'], [1,['Whole Hog']])
Sigma = Hero(21, 0, 2, 10, 40, 0, 65, 60, 80, 85, 70, ['Hyperspheres', 'Rock', 'Gravitic Flux'], [2,['Rock']])
Soldier = Hero(22, 1, 1, 35, 20, 10, 20, 65, 80, 25, 75, ['Pulse Rifle', 'Helix Missile', 'Tactical Visor'], [0,['Biotic Field']])
Sombra = Hero(23, 1, 0, 30, 90, 15, 25, 60, 70, 20, 60, ['Machine Pistol'], [2,['EMP', 'Hack']])
Symmetra = Hero(24, 1, 2, 20, 50, 0, 5, 55, 70, 20, 40, ['Photon Beam', 'Sentry Turret'], [0,['Photon Barrier']])
Torbjorn = Hero(25, 1, 2, 10, 40, 0, 15, 65, 75, 25, 75, ['Rivet Gun', 'Hammer', 'Turret'], [1,['Molten Core']])
Tracer = Hero(26, 1, 0, 80, 35, 0, 35, 95, 110, 35, 85, ['Pulse Pistols'], [1,['Pulse Bomb']])
Widowmaker = Hero(27, 1, 2, 80, 40, 0, 5, 40, 80, 15, 75, ['Sniper'], [1,['Venom Mine']])
Winston = Hero(28, 0, 0, 50, 35, 0, 55, 20, 35, 65, 40, ['Tesla Cannon', 'Jump Pack'], [1,['Primal Rage']])
Hammond = Hero(29, 0, 0, 80, 90, 0, 90, 65, 70, 95, 75, ['Quad Cannons', 'Roll', 'Piledriver'], [1,['Mines']])
Zarya = Hero(30, 0, 1, 10, 20, 0, 45, 65, 75, 55, 70, ['Particle Cannon'], [2,['Graviton Surge']])
Zenyatta = Hero(31, 2, 0, 90, 5, 55, 5, 85, 100, 15, 70, ['Orbs of Destruction'], [0,['Orb of Harmony', 'Transcendence']])

# order is tanks 0, damage 1, support 2
meta_comp = [[31,29], [26, 7, 1, 9], [14, 4, 2]]

# These are all lists of things for players to say in and after the games
choosing_hero_sentences_angriest = ['bro, i f****** hate this hero', 'this s*** is garbage', 'I hate this dogs*** meta', 'F*** THIS F****** GAME', 'im about to f****** throw']
choosing_hero_sentences_upset = ["i guess ill play this guy", 'am i really stuck on this hero', 'i shouldnt have queued']
not_playing_synergy = ['i dont really like this comp, im just gonna go ', 'not a fan of this comp, im gonna play ', 'dont feel like playing that comp, imma play ']
not_playing_synergy_angry = ['bro f*** that dumba** comp, im playin ', 'nah that comp is dumb as f***, im goin ', 'F*** THAT S*** IM GOING ']
choosing_hero_random = ['whats up guys?', 'wuz goo', 'whats crackin', 'yo', 'Yo', 'Hey']

unhappy_with_supports = ['can out supports swap?', 'yo, supports. you there?', 'hey supports, can one of you swap?']
angry_with_supports = ['our supports are dogs***', 'WHY THE F*** CANT THE SUPPORTS HEAL ME????', 'our supports are absolutely braindead', 'zzz supports WTF ARE YOU DOING???', 'support diff']

unhappy_with_tanks = ['can our tanks swap?', 'yo, tanks. you there?', 'tanks, can one of you swap?']
angry_with_tanks = ['our tanks are dogs***', 'TANKS PRESS W KEY', 'our tanks are F****** braindead', 'gg. tanks are dogs***']

unhappy_with_damage = ['can our dps swap?', 'yo, dps. you there?', 'dps, can one of you swap?']
angry_with_damage = ['our dps are dogs***', 'DPS TURN ON YOUR MONITORS', 'our dps are F****** braindead', 'pretty sure our dps are throwing']

end_of_game_angry = ['was i the only one playing?', 'our team actually hard threw', 'F*** THIS GAME', 'serious question. was out team throwing?', 'pretty sure the rest of my team didnt have their monitors on', 'wish i had 5 avoid slots']
end_of_game = ['I feel very, very small... please hold me...', "I'm trying to be a nicer person. It's hard, but I'm trying, guys.", "I'm wrestling with some insecurity issues in my life but thank you for playing with me.", 'gg' 'GGs', 'good try', 'gg go next']

# Create a range for the ranks of the players
rank_start = int(input("Enter rank range start: "))
rank_end = int(input("Enter rank range end: "))
games = int(input('Enter amount of matches to play: '))

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
        team_used.append(Player(rank_start, rank_end, role_type, (str([red_team, blue_team].index(team_used)) + str(player_used))))


for x in red_team:
    print(x.name + "'s main is " + all_heroes[x.mainID] + ", they're on red team, and their personality type is: " + x.personality_type)

for x in blue_team:
    print(x.name + "'s main is " + all_heroes[x.mainID] + ", they're on blue team, and their personality type is: " + x.personality_type)


# ---------------------- First game ---------------------------------


# First hero pick

#setting global team vars to keep track of
red_team_support = 0
red_team_damage = 0
red_team_tanking = 0
red_team_damage_amplified = 0
red_team_tanking_amplified = 0
red_team_team_swap_num = 0

blue_team_support = 0
blue_team_damage = 0
blue_team_tanking = 0
blue_team_damage_amplified = 0
blue_team_tanking_amplified = 0
blue_team_team_swap_num = 0

num_iter = -1

for current_team in [red_team, blue_team]:
    num_iter += 1
    sr_average = (rank_start + rank_end) / 2
    swap_said = False
    comp_synergy = {}
    meta_synergy = []
    used_char_list = []
    synergy_use_list = None
    
    
    person_to_suggest = None
    # these numbers are for flat support, visible power and non visible

    if num_iter == 0:
        team_support = red_team_support
        team_damage = red_team_damage
        team_tanking = red_team_tanking
        team_damage_amplified = red_team_damage_amplified
        team_tanking_amplified = red_team_tanking_amplified
        team_swap_num = red_team_team_swap_num
    else: 
        team_support = blue_team_support
        team_damage = blue_team_damage
        team_tanking = blue_team_tanking
        team_damage_amplified = blue_team_damage_amplified
        team_tanking_amplified = blue_team_tanking_amplified
        team_swap_num = blue_team_team_swap_num
    
    # Creating lists to see how close the teams are to synergy or meta comp
    for i in current_team:
        player_style = eval(all_heroes[i.mainID]).play_style
        if player_style in comp_synergy:
            comp_synergy[player_style] += 1
        else:
            comp_synergy[player_style] = 1

        if player_style in meta_comp:
            meta_synergy += player_style

    comp_synergy_key = max(comp_synergy, key=comp_synergy.get)

    # Check if their team is closer to meta comp, or a certain synergy

    if len(meta_synergy) > comp_synergy[comp_synergy_key]:
        team_swap_num = 3
        synergy_use_list = meta_comp.copy()
        #this means meta comp
    else:
        team_swap_num = comp_synergy_key
        if comp_synergy_key == 0:
            synergy_use_list = [dive_comp[0].copy(), dive_comp[1].copy(), dive_comp[2].copy()]
        elif comp_synergy_key == 1:
            synergy_use_list = [brawl_comp[0].copy(), brawl_comp[1].copy(), brawl_comp[2].copy()]
        else:
            synergy_use_list = [bunker_comp[0].copy(), bunker_comp[1].copy(), bunker_comp[2].copy()]
        #this will swap to the number. ex 0 means dive 1 is brawl and 2 is bunker
    
    chars_picked = []
    for x in current_team:

        # if elect to swap to a comp with synergy
        #if the synergy comp is dive
        type_string = None
        if team_swap_num == 0:
            type_string = 'dive_comp'
        elif team_swap_num == 1:
            type_string = 'brawl_comp'
        elif team_swap_num == 2:
            type_string = 'bunker_comp'
        else:
            type_string = 'meta_comp'

        if swap_said == False:
            print(x.name + ": Lets go " + type_string[0 : (len(type_string) - 5)] + ' ' + type_string[(len(type_string) - 4) : (len(type_string))])
            person_to_suggest = x.name
            swap_said = True
        # 0 in role is tank
        # synergy order is tank 0, damage 1, support 2
        swap_var = None
        hero_type_temp = None
        if x.role_variable == 0:
            hero_type_temp = eval(type_string + '[0]')
        elif x.role_variable == 1:
            hero_type_temp = eval(type_string + '[1]')
        else:
            hero_type_temp = eval(type_string + '[2]')
        compar_chars = []
        synergy_delete = None
        for f in hero_type_temp:
            if f in synergy_use_list[x.role_variable]:
                compar_chars.append(f)

        random_sr_int = random.randint(200, 350)


        pick_list = []
        options_pick_list = []
        
        for l in range(len(synergy_use_list[x.role_variable])):

            loop_tank = eval(all_heroes[synergy_use_list[x.role_variable][l]])

            # order is tank 0, damage 1, support 2
            #create chances the hero will get picked based on the team's support, damage, rank and how fun the hero is
            if x.role_variable == 0: #tank
                chance_primary_pick = (loop_tank.NVpower_CAP * (max(1, (team_support/50)))) + loop_tank.NV_power #Primary is tanking / map control ability
                chance_secondary_pick = (loop_tank.Vpower_CAP * (max(1, ((team_damage + team_tanking)/190)))) + loop_tank.V_power #secondary is damage
                chance_fun_pick = loop_tank.fun * ((5350 - sr_average) / 1000) #fun
            elif x.role_variable == 1: #damage
                chance_primary_pick = (loop_tank.V_power * max(1, (team_damage/50))) + loop_tank.NV_power #Primary is damage and cc
                chance_secondary_pick = (loop_tank.V_power * max(1, ((team_support + loop_tank.Vpower_CAP)/90))) #secondary is damage with support
                chance_fun_pick = loop_tank.fun * ((5650 - sr_average) / 1000) #fun
            else:
                chance_primary_pick = (loop_tank.V_power * max(1, (team_tanking_amplified/50)) + loop_tank.NV_power) #Primary healing out
                chance_secondary_pick = (loop_tank.V_power * max(1, ((team_damage_amplified + loop_tank.Vpower_CAP)/70))) #secondary is utility
                chance_fun_pick = loop_tank.fun * ((5450 - sr_average) / 1000) #fun

            pick_list.append(chance_fun_pick + chance_primary_pick + chance_secondary_pick)
            options_pick_list.append(loop_tank.id_number)
            
                #add some past picks here
        
        high_sr_var = random.choices(
            options_pick_list,
            weights = pick_list,
            k=1
        )[0]

        add_random_char = random.choices(
            [1,2,3],
            weights=[9000 + (sr_average * 3), max(1000, ((4600 - sr_average) * (6 - int(x.personality_type)))), (4600 - sr_average) * (6 - int(x.personality_type))],
            k=1

        )[0]
        first_check = False
        if add_random_char == 2:
            def random_char_func():
                global high_sr_var
               
                first_check = True
                if x.role_variable == 0:
                    high_sr_var = eval(all_heroes[random.choice(all_tanks)]).id_number
                elif x.role_variable == 1:
                    high_sr_var = eval(all_heroes[random.choice(all_damage)]).id_number
                else:
                    high_sr_var = eval(all_heroes[random.choice(all_supports)]).id_number
                if high_sr_var in used_char_list:
                    random_char_func()
                elif high_sr_var not in synergy_use_list[x.role_variable]:
                    swapping_quote = random.choices(
                        [1,2],
                        weights = [350, ((6 - int(x.personality_type)) * x.frustration)],
                        k=1

                    )[0]
                    if swapping_quote == 1:
                        print(x.name + ': ' + random.choice(not_playing_synergy) + all_heroes[high_sr_var])
                    else:
                        print(x.name + ': ' + random.choice(not_playing_synergy_angry) + all_heroes[high_sr_var])
                
                    
            if first_check == False:
                random_char_func()
        high_sr_var = eval(all_heroes[high_sr_var])
        used_char_list.append(high_sr_var.id_number)
        team_support += high_sr_var.support_out
        team_damage += high_sr_var.V_power
        team_tanking += high_sr_var.NV_power
        team_damage_amplified += high_sr_var.Vpower_CAP
        team_tanking_amplified += (high_sr_var.NVpower_CAP + high_sr_var.map_controller)
        if num_iter == 0:
            red_team_support = team_support
            red_team_damage = team_damage
            red_team_tanking = team_tanking
            red_team_damage_amplified = team_damage_amplified
            red_team_tanking_amplified = team_tanking_amplified
            red_team_team_swap_num = team_swap_num
        else: 
            blue_team_support = team_support
            blue_team_damage = team_damage
            blue_team_tanking = team_tanking
            blue_team_damage_amplified = team_damage_amplified
            blue_team_tanking_amplified = team_tanking_amplified
            blue_team_team_swap_num = team_swap_num
        x.swapHero(high_sr_var.id_number)
        if high_sr_var.id_number in synergy_use_list[x.role_variable]:
            synergy_use_list[x.role_variable].remove(high_sr_var.id_number)


           # eval(compar_chars[f])

#----------------------------------------------------------------------------------------
#------------------ Function for swapping after fights-----------------------------------
#----------------------------------------------------------------------------------------


def losing_team_swap(team, team_id):
    if team_id == 'red':
        global red_team_support
        global red_team_damage
        global red_team_tanking
        global red_team_damage_amplified
        global red_team_tanking_amplified
        global red_team_team_swap_num
    elif team_id == 'blue':
        global blue_team_support
        global blue_team_damage
        global blue_team_tanking
        global blue_team_damage_amplified
        global blue_team_tanking_amplified
        global blue_team_team_swap_num

    for current_team in range(1):
        sr_average = (rank_start + rank_end) / 2
        swap_said = False
        comp_synergy = {}
        meta_synergy = []
        used_char_list = []
        synergy_use_list = None
        
        
        person_to_suggest = None
        # these numbers are for flat support, visible power and non visible

        if team_id == 'red':
            team_support = red_team_support
            team_damage = red_team_damage
            team_tanking = red_team_tanking
            team_damage_amplified = red_team_damage_amplified
            team_tanking_amplified = red_team_tanking_amplified
            team_swap_num = red_team_team_swap_num
        elif team_id == 'blue':
            team_support = blue_team_support
            team_damage = blue_team_damage
            team_tanking = blue_team_tanking
            team_damage_amplified = blue_team_damage_amplified
            team_tanking_amplified = blue_team_tanking_amplified
            team_swap_num = blue_team_team_swap_num

        meta_chance = 0
        bunker_chance = 0
        brawl_chance = 0
        dive_chance = 0
        for i in range(len(team)):
            #if tank
            if team[i].role_variable == 0:
                #check for meta comp
                for l in range(len(meta_comp[0])):
                    #check if initial dict key matches
                    if meta_comp[0][l] in team[i].heroes_played:
                        #then subtract valu
                        meta_chance += (team[i].heroes_played[meta_comp[0][l]]['value'] - team[i].heroes_played[meta_comp[0][l]][meta_comp[0][l]])
                #check for buner
                for l in range(len(bunker_comp[0])):
                    if bunker_comp[0][l] in team[i].heroes_played:
                        bunker_chance += (team[i].heroes_played[bunker_comp[0][l]]['value'] - team[i].heroes_played[bunker_comp[0][l]][bunker_comp[0][l]])
                for l in range(len(brawl_comp[0])):
                    if brawl_comp[0][l] in team[i].heroes_played:
                        brawl_chance += (team[i].heroes_played[brawl_comp[0][l]]['value'] - team[i].heroes_played[brawl_comp[0][l]][brawl_comp[0][l]])
                for l in range(len(dive_comp[0])):
                    if dive_comp[0][l] in team[i].heroes_played:
                        dive_chance += (team[i].heroes_played[dive_comp[0][l]]['value'] - team[i].heroes_played[dive_comp[0][l]][dive_comp[0][l]])
            #if support
            if team[i].role_variable == 1:
                #check for meta comp
                for l in range(len(meta_comp[2])):
                    #check if initial dict key matches
                    if meta_comp[2][l] in team[i].heroes_played:
                        #then subtract valu
                        meta_chance += (team[i].heroes_played[meta_comp[2][l]]['value'] - team[i].heroes_played[meta_comp[2][l]][meta_comp[2][l]])
                #check for buner
                for l in range(len(bunker_comp[2])):
                    if bunker_comp[2][l] in team[i].heroes_played:
                        bunker_chance += (team[i].heroes_played[bunker_comp[2][l]]['value'] - team[i].heroes_played[bunker_comp[2][l]][bunker_comp[2][l]])
                for l in range(len(brawl_comp[2])):
                    if brawl_comp[2][l] in team[i].heroes_played:
                        brawl_chance += (team[i].heroes_played[brawl_comp[2][l]]['value'] - team[i].heroes_played[brawl_comp[2][l]][brawl_comp[2][l]])
                for l in range(len(dive_comp[2])):
                    if dive_comp[2][l] in team[i].heroes_played:
                        dive_chance += (team[i].heroes_played[dive_comp[2][l]]['value'] - team[i].heroes_played[dive_comp[2][l]][dive_comp[2][l]])
            if team[i].role_variable == 2:
                #check for meta comp
                for l in range(len(meta_comp[1])):
                    #check if initial dict key matches
                    if meta_comp[1][l] in team[i].heroes_played:
                        #then subtract valu
                        meta_chance += (team[i].heroes_played[meta_comp[1][l]]['value'] - team[i].heroes_played[meta_comp[1][l]][meta_comp[1][l]])
                #check for buner
                for l in range(len(bunker_comp[1])):
                    if bunker_comp[1][l] in team[i].heroes_played:
                        bunker_chance += (team[i].heroes_played[bunker_comp[1][l]]['value'] - team[i].heroes_played[bunker_comp[1][l]][bunker_comp[1][l]])
                for l in range(len(brawl_comp[1])):
                    if brawl_comp[1][l] in team[i].heroes_played:
                        brawl_chance += (team[i].heroes_played[brawl_comp[1][l]]['value'] - team[i].heroes_played[brawl_comp[1][l]][brawl_comp[1][l]])
                for l in range(len(dive_comp[1])):
                    if dive_comp[1][l] in team[i].heroes_played:
                        dive_chance += (team[i].heroes_played[dive_comp[1][l]]['value'] - team[i].heroes_played[dive_comp[1][l]][dive_comp[1][l]])
        
        print('meta chance: ' + str(meta_chance) + ' dive chance: ' + str(dive_chance) + ' brawl chance: ' + str(brawl_chance) + ' bunker chance: ' + str(bunker_chance))

        # Creating lists to see how close the teams are to synergy or meta comp
        for i in team:
            player_style = eval(all_heroes[i.mainID]).play_style
            if player_style in comp_synergy:
                comp_synergy[player_style] += 1
            else:
                comp_synergy[player_style] = 1

            if player_style in meta_comp:
                meta_synergy += player_style

        comp_synergy_key = max(comp_synergy, key=comp_synergy.get)

        # Check if their team is closer to meta comp, or a certain synergy


        #adding some randomness and main priority for comp  synergy swaps
        added_weighting = random.choices(
            [1,2,3,4,5],
            weights= [10, meta_chance, dive_chance, brawl_chance, bunker_chance],
            k=1

        )[0]

        meta_count = len(meta_synergy)
        if added_weighting == 2:
            meta_count += meta_chance
            team_swap_num = 3
            synergy_use_list = meta_comp.copy()
        elif added_weighting == 3 or added_weighting == 4 or added_weighting == 5: 
            # 3 is dive, 4 is brawl, and 5 is bunker
            if added_weighting == 3:
                synergy_use_list = [dive_comp[0].copy(), dive_comp[1].copy(), dive_comp[2].copy()]
                team_swap_num = 0
            elif added_weighting == 4:
                synergy_use_list = [brawl_comp[0].copy(), brawl_comp[1].copy(), brawl_comp[2].copy()]
                team_swap_num = 1
            else:
                synergy_use_list = [bunker_comp[0].copy(), bunker_comp[1].copy(), bunker_comp[2].copy()]
                team_swap_num = 2
        
        elif added_weighting == 1: 

            if meta_count > comp_synergy[comp_synergy_key]:
                team_swap_num = 3
                synergy_use_list = meta_comp.copy()
                #this means meta comp
            else:
                team_swap_num = comp_synergy_key
                if comp_synergy_key == 0:
                    synergy_use_list = [dive_comp[0].copy(), dive_comp[1].copy(), dive_comp[2].copy()]
                elif comp_synergy_key == 1:
                    synergy_use_list = [brawl_comp[0].copy(), brawl_comp[1].copy(), brawl_comp[2].copy()]
                else:
                    synergy_use_list = [bunker_comp[0].copy(), bunker_comp[1].copy(), bunker_comp[2].copy()]
                #this will swap to the number. ex 0 means dive 1 is brawl and 2 is bunker
        
        chars_picked = []
        for x in team:

            # if elect to swap to a comp with synergy
            #if the synergy comp is dive
            type_string = None
            if team_swap_num == 0:
                type_string = 'dive_comp'
            elif team_swap_num == 1:
                type_string = 'brawl_comp'
            elif team_swap_num == 2:
                type_string = 'bunker_comp'
            else:
                type_string = 'meta_comp'

            if swap_said == False:
                print(x.name + ": Lets swap to " + type_string[0 : (len(type_string) - 5)] + ' ' + type_string[(len(type_string) - 4) : (len(type_string))])
                person_to_suggest = x.name
                swap_said = True
            # 0 in role is tank
            # synergy order is tank 0, damage 1, support 2
            swap_var = None
            hero_type_temp = None
            if x.role_variable == 0:
                hero_type_temp = eval(type_string + '[0]')
            elif x.role_variable == 1:
                hero_type_temp = eval(type_string + '[1]')
            else:
                hero_type_temp = eval(type_string + '[2]')
            compar_chars = []
            synergy_delete = None
            for f in hero_type_temp:
                if f in synergy_use_list[x.role_variable]:
                    compar_chars.append(f)

            random_sr_int = random.randint(200, 350)


            pick_list = []
            options_pick_list = []
            
            for l in range(len(synergy_use_list[x.role_variable])):

                loop_tank = eval(all_heroes[synergy_use_list[x.role_variable][l]])

                # order is tank 0, damage 1, support 2
                #create chances the hero will get picked based on the team's support, damage, rank and how fun the hero is
                if x.role_variable == 0: #tank
                    chance_primary_pick = (loop_tank.NVpower_CAP * (max(1, (team_support/50)))) + loop_tank.NV_power #Primary is tanking / map control ability
                    chance_secondary_pick = (loop_tank.Vpower_CAP * (max(1, ((team_damage + team_tanking)/190)))) + loop_tank.V_power #secondary is damage
                    chance_fun_pick = loop_tank.fun * ((5350 - sr_average) / 1000) #fun
                elif x.role_variable == 1: #damage
                    chance_primary_pick = (loop_tank.V_power * max(1, (team_damage/50))) + loop_tank.NV_power #Primary is damage and cc
                    chance_secondary_pick = (loop_tank.V_power * max(1, ((team_support + loop_tank.Vpower_CAP)/90))) #secondary is damage with support
                    chance_fun_pick = loop_tank.fun * ((5650 - sr_average) / 1000) #fun
                else:
                    chance_primary_pick = (loop_tank.V_power * max(1, (team_tanking_amplified/50)) + loop_tank.NV_power) #Primary healing out
                    chance_secondary_pick = (loop_tank.V_power * max(1, ((team_damage_amplified + loop_tank.Vpower_CAP)/70))) #secondary is utility
                    chance_fun_pick = loop_tank.fun * ((5450 - sr_average) / 1000) #fun

                pick_list.append(chance_fun_pick + chance_primary_pick + chance_secondary_pick)
                options_pick_list.append(loop_tank.id_number)
                
                    #add some past picks here
            
            high_sr_var = random.choices(
                options_pick_list,
                weights = pick_list,
                k=1
            )[0]

            add_random_char = random.choices(
                [1,2,3],
                weights=[9000 + (sr_average * 3), max(1000, ((4600 - sr_average) * (6 - int(x.personality_type)))), (4600 - sr_average) * (6 - int(x.personality_type))],
                k=1

            )[0]
            first_check = False
            if add_random_char == 2:
                def random_char_func():
                    global high_sr_var
                
                    first_check = True
                    if x.role_variable == 0:
                        high_sr_var = eval(all_heroes[random.choice(all_tanks)]).id_number
                    elif x.role_variable == 1:
                        high_sr_var = eval(all_heroes[random.choice(all_damage)]).id_number
                    else:
                        high_sr_var = eval(all_heroes[random.choice(all_supports)]).id_number
                    if high_sr_var in used_char_list:
                        random_char_func()
                    elif high_sr_var not in synergy_use_list[x.role_variable]:
                        swapping_quote = random.choices(
                            [1,2],
                            weights = [350, ((6 - int(x.personality_type)) * x.frustration)],
                            k=1

                        )[0]
                        if swapping_quote == 1:
                            print(x.name + ': ' + random.choice(not_playing_synergy) + all_heroes[high_sr_var])
                        else:
                            print(x.name + ': ' + random.choice(not_playing_synergy_angry) + all_heroes[high_sr_var])
                    
                        
                if first_check == False:
                    random_char_func()
            high_sr_var = eval(all_heroes[high_sr_var])
            used_char_list.append(high_sr_var.id_number)
            team_support += high_sr_var.support_out
            team_damage += high_sr_var.V_power
            team_tanking += high_sr_var.NV_power
            team_damage_amplified += high_sr_var.Vpower_CAP
            team_tanking_amplified += (high_sr_var.NVpower_CAP + high_sr_var.map_controller)
            if team_id == 'red':
                red_team_support = team_support
                red_team_damage = team_damage
                red_team_tanking = team_tanking
                red_team_damage_amplified = team_damage_amplified
                red_team_tanking_amplified = team_tanking_amplified
                red_team_team_swap_num = team_swap_num
            elif team_id == 'blue': 
                blue_team_support = team_support
                blue_team_damage = team_damage
                blue_team_tanking = team_tanking
                blue_team_damage_amplified = team_damage_amplified
                blue_team_tanking_amplified = team_tanking_amplified
                blue_team_team_swap_num = team_swap_num
            x.swapHero(high_sr_var.id_number)
            if high_sr_var.id_number in synergy_use_list[x.role_variable]:
                synergy_use_list[x.role_variable].remove(high_sr_var.id_number)
#---------------------------- End function for later swapping--------------------------------

#---------------------------- fighting ------------------------------------------------------
 
print('red team support is: ' + str(red_team_support))  
print('blue team support is: ' + str(blue_team_support))     

#During round
#this will swap to the number. ex 0 means dive 1 is brawl and 2 is bunker, 3 is meta

red_games_won = 0
blue_games_won = 0
games_tied = 0




for x in range(games):
    red_match_total = 0
    blue_match_total = 0
    for q in range(8):

        def fun_calculation(team):
            overall_return = 0
            if team == 'red':
                for i in red_team:
                    overall_return += i.fun_had * (1 + int(i.personality_type))
            elif team == 'blue':
                for i in blue_team:
                    overall_return += i.fun_had * (1 + int(i.personality_type))
            print(overall_return)
            return overall_return
            

        overall_red = (red_team_damage * (200 - red_team_support)) + (red_team_damage_amplified * red_team_support) + (red_team_tanking * max(10, (80 - red_team_support))) + (red_team_tanking_amplified * red_team_support) + fun_calculation('red')
        overall_blue = (blue_team_damage * (200 - blue_team_support)) + (blue_team_damage_amplified * blue_team_support) + (blue_team_tanking * max(10, (80 - blue_team_support))) + (blue_team_tanking_amplified * blue_team_support) + fun_calculation('blue')

        advantage = random.choices(
            [1,2],
            weights= [overall_red, overall_blue],
            k=1

        )
        # advantage 1 is red, and 2 is blue





        red_stats = []
        blue_stats = []

        for i in red_team:
            red_char_playing = eval(all_heroes[i.char_being_played])
            red_stats.append([i, (red_char_playing.V_power * (200 - red_team_support)) + (red_char_playing.Vpower_CAP * red_team_support) + (red_char_playing.NV_power * max(1, (80 - red_team_support))) + (red_char_playing.NVpower_CAP * red_team_support) + ((red_char_playing.fun - i.frustration) * 3)])
        for i in blue_team:
            blue_char_playing = eval(all_heroes[i.char_being_played])
            blue_stats.append([i, (blue_char_playing.V_power * (200 - blue_team_support)) + (blue_char_playing.Vpower_CAP * blue_team_support) + (blue_char_playing.NV_power * max(1, (80 - blue_team_support))) + (blue_char_playing.NVpower_CAP * blue_team_support) + ((blue_char_playing.fun - i.frustration) * 3)])

        red_dead = 0
        blue_dead = 0
        living_red_team = red_team.copy()
        living_blue_team = blue_team.copy()
        dead_people = []
        dead_people_ids = []
        temp_red_stats = red_stats.copy()
        temp_blue_stats = blue_stats.copy()
        for w in range(6):
            
            range_options = random.choice([0,1,2,3,4,5])
            winner_single = random.choices(
                [1,2],
                weights= [red_stats[w][1], blue_stats[w][1]],
                k=1
            )[0]
            loser_id = 0
            # if red wins the fight
            if winner_single == 1:
                loser_var = blue_stats[w][0]
                loser_var.frustration += 2
                loser_var.fun_had += -2
                blue_list = []
                blue_id_list = []
                for o in temp_blue_stats:
                    if o[0] not in dead_people:
                        blue_list.append(o[1])
                        blue_id_list.append(o[0])


                person_killed = random.choices(
                    blue_id_list,
                    weights = blue_list,
                    k=1
                )[0]


                #if the person killed was a tank
                mean_comment = random.choices(
                    [1,2],
                    weights= [700, person_killed.frustration * (5 - int(person_killed.personality_type))],
                    k=1

                )
                
                #when they die  
                for u in temp_blue_stats:
                    if u[0] == person_killed:
                        temp_blue_stats.remove(u)
           
                dead_people.append(person_killed)
                blue_dead += 1
                random_killer = random.choice(red_team)
                random_killer.addValue()
                random_killer.eliminations += 1
                print(person_killed.name + ' was killed by ' + random_killer.name + "'s " + str(random.choice(eval(all_heroes[random_killer.char_being_played]).abilities)))
                living_blue_team.remove(person_killed)

                if mean_comment == 2:
                    # if person killed was a tank
                    if person_killed.role_variable == 0:
                        if random.choice([1,2]) == 1:
                            random_comment = random.choice(angry_with_supports)
                            for q in blue_team:
                                if blue_team[q].role_variable == 1:
                                    blue_team[q].frustration += 10
                                    blue_team[q].fun_had += -10
                        else:
                            random_comment = random.choice(angry_with_damage)
                            for q in blue_team:
                                if blue_team[q].role_variable == 2:
                                    blue_team[q].frustration += 10
                                    blue_team[q].fun_had += -10
                    # if person killed was a support 
                    if person_killed.role_variable == 1:
                        if random.choice([1,2]) == 1:
                            random_comment = random.choice(angry_with_tanks)
                            for q in blue_team:
                                if blue_team[q].role_variable == 0:
                                    blue_team[q].frustration += 10
                                    blue_team[q].fun_had += -10
                        else:
                            random_comment = random.choice(angry_with_damage)
                            for q in blue_team:
                                if blue_team[q].role_variable == 2:
                                    blue_team[q].frustration += 10
                                    blue_team[q].fun_had += -10
                    # if person killed was a dps
                    if person_killed.role_variable == 2:
                        if random.choice([1,2]) == 1:
                            random_comment = random.choice(angry_with_supports)
                            for q in blue_team:
                                if blue_team[q].role_variable == 1:
                                    blue_team[q].frustration += 10
                                    blue_team[q].fun_had += -10
                        else:
                            random_comment = random.choice(angry_with_tanks)
                            for q in blue_team:
                                if blue_team[q].role_variable == 0:
                                    blue_team[q].frustration += 10
                                    blue_team[q].fun_had += -10
                    print(person_killed.name + ': ' + random_comment)
                else:
                    regular_comment = random.choices(
                        [1,2],
                        weights= [20000, (int(person_killed.personality_type) * sr_average)],
                        k=1
                    )
                    if regular_comment == 2:
                        if person_killed.role_variable == 0:

                            if random.choice([1,2]) == 1:
                                random_comment = random.choice(unhappy_with_supports)
                            else:
                                random_comment = random.choice(unhappy_with_damage)

                        elif person_killed.role_variable == 1:

                            if random.choice([1,2]) == 1:
                                random_comment = random.choice(unhappy_with_tanks)
                            else:
                                random_comment = random.choice(unhappy_with_damage)

                        elif person_killed.role_variable == 2:

                            if random.choice([1,2]) == 1:
                                random_comment = random.choice(unhappy_with_tanks)
                            else:
                                random_comment = random.choice(unhappy_with_supports)

                        print(person_killed.name + ': ' + random_comment)

                person_killed.deaths += 1
                person_killed.frustration += 5
                person_killed.fun_had += -5

            elif winner_single == 2:
                loser_var = red_stats[w][0]
                loser_var.frustration += 2
                loser_var.fun_had += -2
                red_list = []
                red_id_list = []
                for o in temp_red_stats:
                    if o[0] not in dead_people:
                        red_list.append(o[1])
                        red_id_list.append(o[0])


                person_killed = random.choices(
                    red_id_list,
                    weights = red_list,
                    k=1
                )[0]


                #if the person killed was a tank
                mean_comment = random.choices(
                    [1,2],
                    weights= [700, person_killed.frustration * (5 - int(person_killed.personality_type))],
                    k=1

                )
                

                
                #when they die
                hero_player_killed = eval(all_heroes[person_killed.char_being_played])
                for u in temp_red_stats:
                    if u[0] == person_killed:
                        temp_red_stats.remove(u)
                dead_people.append(person_killed)
                red_dead += 1
                random_killer = random.choice(blue_team)
                random_killer.current_value += 1
                random_killer.addValue()
                living_red_team = red_team.copy()
                random_killer.eliminations += 1
                print(person_killed.name + ' was killed by ' + random_killer.name + "'s " + str(random.choice(eval(all_heroes[random_killer.char_being_played]).abilities)))

                if mean_comment == 2:
                    # if person killed was a tank
                    if person_killed.role_variable == 0:
                        if random.choice([1,2]) == 1:
                            random_comment = random.choice(angry_with_supports)
                            for q in red_team:
                                if red_team[q].role_variable == 1:
                                    red_team[q].frustration += 10
                                    red_team[q].fun_had += -10
                        else:
                            random_comment = random.choice(angry_with_damage)
                            for q in red_team:
                                if red_team[q].role_variable == 2:
                                    red_team[q].frustration += 10
                                    red_team[q].fun_had += -10
                    # if person killed was a support 
                    if person_killed.role_variable == 1:
                        if random.choice([1,2]) == 1:
                            random_comment = random.choice(angry_with_tanks)
                            for q in red_team:
                                if red_team[q].role_variable == 0:
                                    red_team[q].frustration += 10
                                    red_team[q].fun_had += -10
                        else:
                            random_comment = random.choice(angry_with_damage)
                            for q in red_team:
                                if red_team[q].role_variable == 2:
                                    red_team[q].frustration += 10
                                    red_team[q].fun_had += -10
                    # if person killed was a dps
                    if person_killed.role_variable == 2:
                        if random.choice([1,2]) == 1:
                            random_comment = random.choice(angry_with_supports)
                            for q in red_team:
                                if red_team[q].role_variable == 1:
                                    red_team[q].frustration += 10
                                    red_team[q].fun_had += -10
                        else:
                            random_comment = random.choice(angry_with_tanks)
                            for q in red_team:
                                if red_team[q].role_variable == 0:
                                    red_team[q].frustration += 10
                                    red_team[q].fun_had += -10
                    print(person_killed.name + ': ' + random_comment)
                else:
                    regular_comment = random.choices(
                        [1,2],
                        weights= [20000, (int(person_killed.personality_type) * sr_average)],
                        k=1
                    )
                    if regular_comment == 2:
                        if person_killed.role_variable == 0:

                            if random.choice([1,2]) == 1:
                                random_comment = random.choice(unhappy_with_supports)
                            else:
                                random_comment = random.choice(unhappy_with_damage)

                        elif person_killed.role_variable == 1:

                            if random.choice([1,2]) == 1:
                                random_comment = random.choice(unhappy_with_tanks)
                            else:
                                random_comment = random.choice(unhappy_with_damage)

                        elif person_killed.role_variable == 2:

                            if random.choice([1,2]) == 1:
                                random_comment = random.choice(unhappy_with_tanks)
                            else:
                                random_comment = random.choice(unhappy_with_supports)
                        print(person_killed.name + ': ' + random_comment)
                        


                person_killed.deaths += 1
                person_killed.frustration += 5
                person_killed.fun_had += -5





                # 0 tank, 1 support, 2dps

        if red_dead > blue_dead: 
            for i in living_red_team:
                random_killer = random.choice(blue_team)
                print(i.name + ' was killed by ' + random_killer.name + "'s " + str(random.choice(eval(all_heroes[random_killer.char_being_played]).abilities)))
                random_killer.current_value += 1
                random_killer.addValue()
                random_killer.eliminations += 1
                random_killer.frustration -= 5
                random_killer.fun_had += 5
                blue_match_total += 1
            losing_team_swap(red_team, 'red')
        elif red_dead < blue_dead: 
            for i in living_blue_team:
                random_killer = random.choice(red_team)
                print(i.name + ' was killed by ' + random_killer.name + "'s " + str(random.choice(eval(all_heroes[random_killer.char_being_played]).abilities)))
                random_killer.current_value += 1
                random_killer.addValue()
                random_killer.eliminations += 1
                random_killer.frustration -= 5
                random_killer.fun_had += 5
                red_match_total += 1
            losing_team_swap(blue_team, 'blue')

    if red_match_total > blue_match_total:
        red_games_won += 1
        for l in range(len(red_team)):
            red_team[l].current_value += 1
            red_team[l].addValue()
            red_team[l].fun_had += 10
            red_team[l].frustration -= 5
            end_choice = random.choices(
                [1,2],
                weights= [2,4],
                k=1

            )[0]
            if end_choice == 1:
                what_to_say = random.choices(
                    [1,2],
                    weights = [900000, (red_team[l].frustration * (6 - int(red_team[l].personality_type)) * (4800 - sr_average))]

                )[0]
                if what_to_say == 1:
                    print('(Red Team)' + red_team[l].name + ': ' + random.choice(end_of_game))
                elif what_to_say == 2:
                    print('(Red Team)' + red_team[l].name + ': ' + random.choice(end_of_game_angry))
        for l in range(len(blue_team)):
            blue_team[l].fun_had -= 35
            blue_team[l].frustration += 15
            end_choice = random.choices(
                [1,2],
                weights= [2,4],
                k=1

            )[0]
            if end_choice == 1:
                what_to_say = random.choices(
                    [1,2],
                    weights = [900000, (blue_team[l].frustration * (6 - int(blue_team[l].personality_type)) * (4800 - sr_average))]

                )[0]
                if what_to_say == 1:
                    print('(Blue Team)' + blue_team[l].name + ': ' + random.choice(end_of_game))
                elif what_to_say == 2:
                    print('(Blue Team)' + blue_team[l].name + ': ' + random.choice(end_of_game_angry))
            
    elif blue_match_total > red_match_total:
        blue_games_won += 1
        for l in range(len(red_team)):
            red_team[l].fun_had -= 35
            red_team[l].frustration -= 5
            end_choice = random.choices(
                [1,2],
                weights= [2,4],
                k=1

            )[0]
            if end_choice == 1:
                what_to_say = random.choices(
                    [1,2],
                    weights = [900000, (red_team[l].frustration * (6 - int(red_team[l].personality_type)) * (4800 - sr_average))]

                )[0]
                if what_to_say == 1:
                    print('(Red Team)' + red_team[l].name + ': ' + random.choice(end_of_game))
                elif what_to_say == 2:
                    print('(Red Team)' + red_team[l].name + ': ' + random.choice(end_of_game_angry))
        for l in range(len(blue_team)):
            blue_team[l].current_value += 1
            blue_team[l].addValue()
            blue_team[l].fun_had += 10
            blue_team[l].frustration += 15
            end_choice = random.choices(
                [1,2],
                weights= [2,4],
                k=1

            )[0]
            if end_choice == 1:
                what_to_say = random.choices(
                    [1,2],
                    weights = [900000, (blue_team[l].frustration * (6 - int(blue_team[l].personality_type)) * (4800 - sr_average))]

                )[0]
                if what_to_say == 1:
                    print('(Blue Team)' + blue_team[l].name + ': ' + random.choice(end_of_game))
                elif what_to_say == 2:
                    print('(Blue Team)' + blue_team[l].name + ': ' + random.choice(end_of_game_angry))
    else:
        games_tied += 1
        for l in range(len(red_team)):
            red_team[l].fun_had -= 10
            red_team[l].frustration += 5
            end_choice = random.choices(
                [1,2],
                weights= [2,4],
                k=1

            )[0]
            if end_choice == 1:
                what_to_say = random.choices(
                    [1,2],
                    weights = [900000, (red_team[l].frustration * (6 - int(red_team[l].personality_type)) * (4800 - sr_average))]

                )[0]
                if what_to_say == 1:
                    print('(Red Team)' + red_team[l].name + ': ' + random.choice(end_of_game))
                elif what_to_say == 2:
                    print('(Red Team)' + red_team[l].name + ': ' + random.choice(end_of_game_angry))
        for l in range(len(blue_team)):
            blue_team[l].fun_had -= 10
            blue_team[l].frustration += 5
            end_choice = random.choices(
                [1,2],
                weights= [2,4],
                k=1

            )[0]
            if end_choice == 1:
                what_to_say = random.choices(
                    [1,2],
                    weights = [900000, (blue_team[l].frustration * (6 - int(blue_team[l].personality_type)) * (4800 - sr_average))]

                )[0]
                if what_to_say == 1:
                    print('(Blue Team)' + blue_team[l].name + ': ' + random.choice(end_of_game))
                elif what_to_say == 2:
                    print('(Blue Team)' + blue_team[l].name + ': ' + random.choice(end_of_game_angry))

print('red matches won = ' + str(red_games_won))
print('blue matches won = ' + str(blue_games_won))
print('matches tied = ' + str(games_tied))


# End of round
#------------------------------------
# For each player, update the heroes played with the current one
#for current_team in [red_team, blue_team]:
    #for x in current_team:
        # Check to see if they swapped that round
       # if x.last_played != x.char_being_played:
        #    if x.char_being_played in x.heroes_played:
        #        x.heroes_played[x.char_being_played] += 1
       #     else: 
       #         x.heroes_played[x.char_being_played] = 1
     #   x.last_played = x.char_being_played





# ----------------------- End of Game -----------------------------------

