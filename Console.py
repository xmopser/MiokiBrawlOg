import sys
import pymongo
import datetime
from DataBase.MongoUtils import MongoUtils
from Logic.Player import Player
import json
import bson
from Utils.Helpers import Helpers

class MongoDB:
    def __init__(self):
        self.player = Player
        self.client = pymongo.MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS = 5000)
        try:
            print(f"{Helpers.cyan}[DEBUG] Connecting to Mongo DataBase...")
            self.client.server_info()
        except Exception:
            print(f"{Helpers.red}[ERROR] Unable to connect to Mongo server!")
            sys.exit()

        self.database = self.client['Classic-Brawl']
        self.players = self.database['Players']
        self.clubs = self.database['Clubs']
        self.mongo_utils = MongoUtils()

        self.data = { #11395778
            'Name': 'Guest',
            'NameSet': False,
            'Gems': Player.gems,
            'Trophies': Player.trophies,
            'Tickets': Player.tickets,
            'Resources': Player.resources,
            'TokenDoubler': 0,
            'HighestTrophies': 0,
            'HomeBrawler': 0,
            'TrophyRoadReward': 300,
            'ExperiencePoints': Player.exp_points,
            'ProfileIcon': 0,
            'NameColor': 0,
            'UnlockedBrawlers': Player.brawlers_unlocked,
            'BrawlersTrophies': Player.brawlers_trophies,
            'BrawlersHighestTrophies': Player.brawlers_high_trophies,
            'BrawlersLevel': Player.brawlers_level,
            'BrawlersPowerPoints': Player.brawlers_powerpoints,
            'UnlockedSkins2': Player.unlocked_skins,
            'UnlockedPins': Player.emotes_id,
            'SelectedSkins': Player.selected_skins,
            'SelectedBrawler': 0,
            'Region': Player.region,
            'SupportedContentCreator': "MiokiBrawl",
            'StarPower': Player.starpower,
            'Gadget': Player.gadget,
            'BrawlPassActivated': False,
            'WelcomeMessageViewed': False,
            'ClubID': 0,
            'ClubRole': 1,
            'ClaimShop': Player.claimshop,
            'Season': Player.season,
            'Wins': Player.wins,
            'Day': Player.day,
            'DailySkins': Player.dailyskins,
            'Quest': Player.quest,
            'BrawlerRare': Player.brawler_rare,
            'BrawlerSuperRare': Player.brawler_superrare,
            'BrawlerEpic': Player.brawler_epic,
            'BrawlerMegaEpic': Player.brawler_megaepic,
            'BrawlerLegendary': Player.brawler_legendary,
            'Ban': Player.ban,
            'BanReason': Player.ban_reason,
            'AccountType': Player.account_type,
            'TestState': Player.test_state,
            'Maintenance': Player.maintenance,
            'MaintenanceTime': Player.maintenance_time,
            'TimeStamp': str(datetime.datetime.now())
        }

        self.club_data = {
            'Name': '',
            'Description': '',
            'Region': '',
            'BadgeID': 0,
            'Type': 0,
            'Trophies': 0,
            'RequiredTrophies': 0,
            'FamilyFriendly': 0,
            'Members': [],
            'Messages': [],
            'Inbox': []
        }

    def merge(self, dict1, dict2):
        return (dict1.update(dict2))


    def create_player_account(self, id, token):
        auth = {
            'ID': id,
            'Token': token,
        }

        auth.update(self.data)

        self.mongo_utils.insert_data(self.players, auth)


    def load_player_account(self, id, token):
        query = {"Token": token}
        result = self.mongo_utils.load_document(self.players, query)

        if result:
            for x in self.data:
                if x not in result:
                    self.update_player_account(token, x, self.data[x])

            query = {"Token": token}
            result = self.mongo_utils.load_document(self.players, query)

            return result


    def load_player_account_by_id(self, id):
        query = {"ID": id}
        result = self.mongo_utils.load_document(self.players, query)

        if result:
            return result


    def update_player_account(self, token, item, value):
        query = {"Token": token}
        self.mongo_utils.update_document(self.players, query, item, value)


    def update_all_players(self, query, item, value):
        self.mongo_utils.update_all_documents(self.players, query, item, value)


    def delete_all_players(self, args):
        self.mongo_utils.delete_all_documents(self.players, args)


    def delete_player(self, token):
        query = {"Token": token}
        self.mongo_utils.delete_document(self.players, query)


    def load_all_players(self, args):
        result = self.mongo_utils.load_all_documents(self.players, args)

        return result


    def load_all_players_sorted(self, args, element):
        result = self.mongo_utils.load_all_documents_sorted(self.players, args, element)

        return result


    def create_club(self, id, data):
        auth = {
            'ID': id,
        }

        auth.update(data)

        self.mongo_utils.insert_data(self.clubs, auth)


    def update_club(self, id, item, value):
        query = {"ID": id}
        self.mongo_utils.update_document(self.clubs, query, item, value)


    def load_club(self, id):
        query = {"ID": id}
        result = self.mongo_utils.load_document(self.clubs, query)

        if result:
            for x in self.club_data:
                if x not in result:
                    self.update_club(id, x, self.club_data[x])

            query = {"ID": id}
            result = self.mongo_utils.load_document(self.clubs, query)

            return result


    def load_all_clubs_sorted(self, args, element):
        result = self.mongo_utils.load_all_documents_sorted(self.clubs, args, element)

        return result

    def load_all_clubs(self, args):
        result = self.mongo_utils.load_all_documents(self.clubs, args)

        return result

    def delete_club(self, id):
        query = {"ID": id}
        self.mongo_utils.delete_document(self.clubs, query)

    def data_add(self, token, item, value):
        player_account = MongoDB.load_player_account_by_id(self, token)
        player_token = player_account['Token']
        player_item = player_account[item]
        MongoDB.update_player_account(self, player_token, item, player_item + value)

    def data_set(self, token, item, value):
        player_account = MongoDB.load_player_account_by_id(self, token)
        player_token = player_account['Token']
        MongoDB.update_player_account(self, player_token, item, value)

    def resources_data_set(self, token, item, value, id):
        player_account = MongoDB.load_player_account_by_id(self, token)
        player_token = player_account['Token']
        player_item = player_account[item]
        player_item[id]['Amount'] = value
        MongoDB.update_player_account(self, player_token, item, player_item)

    def resources_data_add(self, token, item, value, id):
        player_account = MongoDB.load_player_account_by_id(self, token)
        player_token = player_account['Token']
        player_item = player_account[item]
        player_item[id]['Amount'] = player_item[id]['Amount'] + value
        MongoDB.update_player_account(self, player_token, item, player_item)

    def gempack_add(self):
        item = "Gems"
        value = int(input("Value: "))
        MongoDB.data_add(self, self.token, item, value)
        MongoDB.input_c(self)

    def resources_edit(self):
        item = "Resources"
        value = int(input("Value: "))
        id = int(input("ID: "))
        MongoDB.resources_data_set(self, self.token, item, value, id)
        MongoDB.input_c(self)

    def resources_add(self):
        item = "Resources"
        value = int(input("Value: "))
        id = int(input("ID: "))
        MongoDB.resources_data_add(self, self.token, item, value, id)
        MongoDB.input_c(self)

    def value_edit(self):
        item = input("Item: ")
        value = int(input("Value: "))
        MongoDB.data_set(self, self.token, item, value)
        MongoDB.input_c(self)

    def value_add(self):
        item = input("Item: ")
        value = int(input("Value: "))
        MongoDB.data_add(self, self.token, item, value)
        MongoDB.input_c(self)

    def text_edit(self):
        item = input("Item: ")
        value = input("Value: ")
        MongoDB.data_set(self, self.token, item, value)
        MongoDB.input_c(self)

    def ban(self):
        ban_reason = input("Ban reason: ")
        MongoDB.data_set(self, self.token, "Ban", True)
        MongoDB.data_set(self, self.token, "BanReason", ban_reason)
        MongoDB.input_c(self)

    def pardon(self):
        MongoDB.data_set(self, self.token, "Ban", False)
        MongoDB.input_c(self)

    def input_c(self):
        choice = input("""___MiokiBrawlConsoleMenu___
Gems Add (1)
Value edit (2)
Value add (3)
Ban (4)
Text edit (5)
Resources edit (6)
Resources add (7)
Pardon (8)
Set Token(9)
Enter: """)
        print("___MiokiBrawlConsoleCommand___")
        if choice == "1":
            MongoDB.gempack_add(self)
        if choice == "2":
            MongoDB.value_edit(self)
        if choice == "3":
            MongoDB.value_add(self)
        if choice == "4":
            MongoDB.ban(self)
        if choice == "5":
            MongoDB.text_edit(self)
        if choice == "6":
            MongoDB.resources_edit(self)
        if choice == "7":
            MongoDB.resources_add(self)
        if choice == "8":
            MongoDB.pardon(self)
        if choice == "9":
            MongoDB.set_token(self)

    def set_token(self):
        self.token = int(input("Token: "))
        MongoDB.input_c(self)

if __name__ == "__main__":
    console = MongoDB()
    console.set_token()