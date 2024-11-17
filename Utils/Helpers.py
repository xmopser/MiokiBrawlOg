import json
import string
import random
from datetime import datetime
from colorama import Fore

class Helpers:
    connected_clients = {"ClientsCount": 0, "Clients": {}}

    yellow = Fore.YELLOW
    green = Fore.GREEN
    blue = Fore.LIGHTBLUE_EX
    cyan = Fore.CYAN
    red = Fore.RED

    def timerglobal(self, timer_start, timer_end):
        timer_max = (86400 * timer_end[1]) + (3600 * timer_end[0])
        timer_now = (86400 * int(datetime.today().strftime('%d'))) + (3600 * int(datetime.today().strftime('%H'))) + (60 * int(datetime.today().strftime('%M'))) + int(datetime.today().strftime('%S'))
        print(int(datetime.today().strftime('%d')) < timer_start[1])
        print(int(datetime.today().strftime('%H')) < timer_start[0])
        if (not int(datetime.today().strftime('%d')) < timer_start[1] or not int(datetime.today().strftime('%H')) < timer_start[0]) and not int(datetime.today().strftime('%m')) < timer_start[2]:
            if int(datetime.today().strftime('%m')) == timer_end[2] or int(datetime.today().strftime('%m')) > timer_end[2]:
                print("1")
                timer = timer_max - int(timer_now)
            elif int(datetime.today().strftime('%m')) < timer_end[2]:
                print("2")
                timer = timer_max + (86400 * 28) - int(timer_now)
        else:
            timer = -1
        return timer

    def randomToken(self):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomID(self, length = 8):
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))

    def randomMapID(self):
        return random.randint(1, 2147483647)

    def get_box_type(self, id):
        if id == 5:  # Brawl Box
            return 10
        elif id == 4:  # Big Box
            return 12
        elif id == 3:  # Shop Mega Box
            return 11
        elif id == 1:  # Shop Big Box
            return 12

    def create_config(self):
        settings = {
                "MongoConnectionURL": "",
                "StarPoints": 5000,
                "Gold": 10000,
                "Gems": 100000,
                "Trophies": 0,
                "ExperiencePoints": 999999,
                "BrawlBoxTokens": 99999,
                "BigBoxTokens": 99999,
                "Region": "RO",
                "ThemeID": 0,
                "Maintenance": False,
                "SecondsTillMaintenanceOver": 3600
            }


        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)

    def load_account(self, player_data):
        self.player.name_set = player_data['NameSet']
        self.player.name = player_data['Name']
        self.player.trophies = player_data['Trophies']
        self.player.gems = player_data['Gems']
        self.player.resources = player_data['Resources']
        self.player.token_doubler = player_data['TokenDoubler']
        self.player.high_trophies = player_data['HighestTrophies']
        self.player.trophy_reward = player_data['TrophyRoadReward']
        self.player.exp_points = player_data['ExperiencePoints']
        self.player.profile_icon = player_data['ProfileIcon']
        self.player.name_color = player_data['NameColor']
        self.player.brawlers_unlocked = player_data['UnlockedBrawlers']
        self.player.brawlers_trophies = player_data['BrawlersTrophies']
        self.player.brawlers_high_trophies = player_data['BrawlersHighestTrophies']
        self.player.brawlers_level = player_data['BrawlersLevel']
        self.player.brawlers_powerpoints = player_data['BrawlersPowerPoints']
        self.player.unlocked_skins = player_data['UnlockedSkins2']
        self.player.selected_skins = player_data['SelectedSkins']
        self.player.tickets = player_data['Tickets']
        self.player.home_brawler = player_data['HomeBrawler']
        self.player.region = player_data['Region']
        self.player.content_creator = player_data['SupportedContentCreator']
        self.player.bp_activated = player_data['BrawlPassActivated']
        self.player.starpower = player_data['StarPower']
        self.player.gadget = player_data['Gadget']
        self.player.welcome_msg_viewed = player_data['WelcomeMessageViewed']
        self.player.club_id = player_data['ClubID']
        self.player.club_role = player_data['ClubRole']
        self.player.claimshop = player_data['ClaimShop']
        self.player.season = player_data['Season']
        self.player.day = player_data['Day']
        self.player.dailyskins = player_data['DailySkins']
        self.player.quest = player_data['Quest']


    def load_club(self, club_data):
        try:
            self.player.message_tick = club_data['Messages'][-1]['Tick']
        except:
            pass