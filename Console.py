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
        self.server_choice = input("Choice server: Prod (1), Dev (2), Stage (3): ")
        if self.server_choice == "1":
            self.database = self.client['Classic-Brawl']
        if self.server_choice == "2":
            self.database = self.client['Classic-Brawl-Test']
        if self.server_choice == "3":
            self.database = self.client['Classic-Brawl-Stage']
        self.players = self.database['Players']
        self.clubs = self.database['Clubs']
        self.mongo_utils = MongoUtils()

        self.data = { # 11395778
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
        MongoDB.data_set(self, self.token, "Trophies", -1)
        MongoDB.data_set(self, self.token, "Name", "Account Banned")
        MongoDB.input_c(self)

    def pardon(self):
        MongoDB.data_set(self, self.token, "Ban", False)
        MongoDB.input_c(self)

    def brawler_add(self):
        brawler_id = int(input("Brawler ID: "))
        player_account = MongoDB.load_player_account_by_id(self, self.token)
        player_token = player_account['Token']
        player_item = player_account['UnlockedBrawlers']
        if brawler_id not in player_item:
            player_item.append(brawler_id)
        MongoDB.update_player_account(self, player_token, 'UnlockedBrawlers', player_item)
        MongoDB.input_c(self)

    def account_recovery(self): # 51623226
        player_id_old = int(input("Player ID OLD: "))
        player_id = int(input("Player ID: "))
        player_account_old = MongoDB.load_player_account_by_id(self, player_id_old)
        player_account = MongoDB.load_player_account_by_id(self, player_id)
        player_token_old = player_account_old['Token']
        player_token = player_account['Token']
        for x in ['Name', 'NameSet', 'Gems', 'Trophies', 'Resources', 'UnlockedBrawlers', 'BrawlersLevel', 'UnlockedSkins2', 'BrawlPassActivated', 'Season']:
            MongoDB.update_player_account(self, player_token, x, player_account_old[x])
            input(x + ": " + str(player_account_old[x]))
        b = player_account['BrawlersTrophies']
        b['8'] = 760
        b['2'] = 740
        b['6'] = 730
        b['0'] = 730
        b['3'] = 690
        b['10'] = 610
        b['39'] = 610
        b['27'] = 590
        b['26'] = 570
        b['13'] = 430
        b['22'] = 420
        b['18'] = 360
        b['19'] = 340
        b['5'] = 340
        b['15'] = 320
        b['20'] = 310
        b['4'] = 300
        b['16'] = 210
        b['31'] = 200
        b['7'] = 120
        b['9'] = 120
        b['1'] = 120
        bh = player_account['BrawlersHighestTrophies']
        bh['8'] = 760
        bh['2'] = 740
        bh['6'] = 730
        bh['0'] = 730
        bh['3'] = 690
        bh['10'] = 610
        bh['39'] = 610
        bh['27'] = 590
        bh['26'] = 570
        bh['13'] = 430
        bh['22'] = 420
        bh['18'] = 360
        bh['19'] = 340
        bh['5'] = 340
        bh['15'] = 320
        bh['20'] = 310
        bh['4'] = 300
        bh['16'] = 210
        bh['31'] = 200
        bh['7'] = 120
        bh['9'] = 120
        bh['1'] = 120
        MongoDB.update_player_account(self, player_token, 'Gems', 4000)
        MongoDB.update_player_account(self, player_token, 'BrawlersTrophies', b)
        MongoDB.update_player_account(self, player_token, 'BrawlersHighestTrophies', bh)
        MongoDB.update_player_account(self, player_token_old, 'Trophies', 0)
        MongoDB.input_c(self)

    def account_recoverygf(self): # 51623226
        player_id = int(input("Player ID: "))
        player_account = MongoDB.load_player_account_by_id(self, player_id)
        player_token = player_account['Token']
        b = player_account['BrawlersTrophies']
        b['22'] = 0
        MongoDB.update_player_account(self, player_token, 'BrawlersTrophies', b)
        MongoDB.input_c(self)


    def hui(self):
        player_account = MongoDB.load_player_account_by_id(self, self.token)
        file = open('log.txt', "w")
        file.write(str(player_account)) 
        file.close()
        MongoDB.input_c(self)

    def skin_add(self):
        brawler_id = int(input("Skin ID: "))
        player_account = MongoDB.load_player_account_by_id(self, self.token)
        player_token = player_account['Token']
        player_item = player_account['UnlockedSkins2']
        player_item.append(brawler_id)
        MongoDB.update_player_account(self, player_token, 'UnlockedSkins2', player_item)
        MongoDB.input_c(self)

    def guest_delete(self):
        print("Начало очистки...")
        self.mongo_utils.delete_all_documents(self.players, {'Name': "Guest"})
        print("Очистка учпешно завершена!")

    def all_delete(self):
        input("Ты блять уверен что случайно не стерёшь все данные с проды? Ты выбрал " + self.server_choice + " сервер!!! Предупреждение 1")
        input("Ты блять уверен что случайно не стерёшь все данные с проды? Ты выбрал " + self.server_choice + " сервер!!! Предупреждение 2")
        input("Ты блять уверен что случайно не стерёшь все данные с проды? Ты выбрал " + self.server_choice + " сервер!!! Предупреждение 3")
        input("Ты блять уверен что случайно не стерёшь все данные с проды? Ты выбрал " + self.server_choice + " сервер!!! Предупреждение 4")
        input("Ты блять уверен что случайно не стерёшь все данные с проды? Ты выбрал " + self.server_choice + " сервер!!! Предупреждение 5")
        self.mongo_utils.delete_all_documents(self.players, {})
        print("Очистка учпешно завершена!")

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
Set Token (9)
Brawler Add (10)
Skin Add (11)
??? (12)
Guest Clear (13)
Account Recovery (14)
Account Recovery GF (15)
All Clear (16)
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
        if choice == "10":
            MongoDB.brawler_add(self)
        if choice == "11":
            MongoDB.skin_add(self)
        if choice == "12":
            MongoDB.hui(self)
        if choice == "13":
            MongoDB.guest_delete(self)
        if choice == "14":
            MongoDB.account_recovery(self)
        if choice == "15":
            MongoDB.account_recoverygf(self)
        if choice == "16":
            MongoDB.all_delete(self)

    def set_token(self):
        self.token = int(input("Token: "))
        MongoDB.input_c(self)

if __name__ == "__main__":
    console = MongoDB()
    console.set_token()