from random_word import RandomWords
from random import seed
from random import randint

#pip3 install random-words
r = RandomWords()
seed(1)

all_heroes = ['Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'D.va', 'Doomfist', 'Echo', 'Genji', 'Hanzo', 'Junkrat', 'Lucio',
 'Mccree', 'Mei', 'Mercy', 'Moira', 'Orisa' , 'Pharah', 'Reaper' ,'Reinhardt', 'Roadhog', 'Sigma', 'Soldier 76', 'Sombra', 'Symmetra', 'Torbjorn', 'Tracer', 'Widowmaker',
 'Winston', 'Wrecking Ball', 'Zarya', 'Zenyatta']


class Hero:

    def __init__(self, id_number, role_type, play_style, map_user, map_controller, support_out, NV_power, V_power, Vpower_CAP, NV_power, fun):
        self.id_number = id_number
        self.name = all_teams[id_number]
        self.role_type = role_type #0 is tank, 1 is dps and 2 is support
        self.play_style = play_style #0 is dive, 1 is brawl, 2 is bunker
        self.map_user = map_user #1-100 based on if they need positioning or healthpacks
        self.map_controller = map_controller #1-100 based on how well they control positioning
        self.support_out = support_out #1-100 based on amount of support (healing + utility)
        self.NV_power = NV_power #Non-visible power, based on position control and tanking ability | 1-100
        self.V_power = V_power #Visible power, based on damage output
        self.Support_X_Vpower = Vpower_CAP / V_power
        self.Support_X_NVpower = NVpower_CAP / NV_power
        self.Vpower_CAP = Vpower_CAP
        self.NVpower_CAP = NVpower_CAP
        self.fun = fun


class Player:

    def __init__(self, rank_start, rank_end, swap_willingness):
        self.name = r.get_random_word() + r.get_random_word() + randint(10,500)
        self.rank = randint(rank_start, rank_end)
        self.mainID = randint(1,32)
        self.swap_willingness = randint
        self.frustration = randint(1,40)
        sefl.char_being_played = self.mainID

    



Ana = Hero(0, 2, 2, 80, 15, 90, 5, 5, 10, 15, 85)
Ashe = Hero(1, 1, )





rank_start = input("Enter rank range start: ")
rank_end = input("Enter rank range end: ")

red_team, blue_team = []

all_teams = [red_team, blue_team]

for team_used in all_teams:
    for player_used in range(6):
        team_used[player_used] = Player()









