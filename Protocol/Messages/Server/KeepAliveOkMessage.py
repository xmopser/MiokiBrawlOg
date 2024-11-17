from ByteStream.Writer import Writer
from DataBase.MongoDB import MongoDB
from datetime import datetime
import random
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage

class KeepAliveOkMessage(Writer):

    def __init__(self, client, player, db: MongoDB):
        super().__init__(client)
        self.id = 20108
        self.player = player
        self.db = db

    def encode(self):

        if int(datetime.today().strftime('%d')) != self.player.day:
            self.player.day = int(datetime.today().strftime('%d'))
            try:
                self.player.claimshop.remove("dailygift")
            except:
                print("Okbuyhsabuy")

            if len(sorted(set([3, 15, 27, 29, 176]) - set(self.player.unlocked_skins))) != 0:
                self.player.dailyskins[0] = random.choice(sorted(set([3, 15, 27, 29, 176]) - set(self.player.unlocked_skins)))
                self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
                try:
                    self.player.claimshop.remove("skin1")
                except:
                    print("Okbuyhsabuy")

            if len(sorted(set([20, 11, 47, 45, 5]) - set(self.player.unlocked_skins))) != 0:
                self.player.dailyskins[1] = random.choice(sorted(set([20, 11, 47, 45, 5]) - set(self.player.unlocked_skins)))
                self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
                try:
                    self.player.claimshop.remove("skin2")
                except:
                    print("Okbuyhsabuy")

            if len(sorted(set([44, 68, 90]) - set(self.player.unlocked_skins))) != 0:
                self.player.dailyskins[2] = random.choice(sorted(set([44, 68, 90]) - set(self.player.unlocked_skins)))
                self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
                try:
                    self.player.claimshop.remove("skin3")
                except:
                    print("Okbuyhsabuy")

            if len(sorted(set([49]) - set(self.player.unlocked_skins))) != 0:
                self.player.dailyskins[3] = random.choice(sorted(set([49]) - set(self.player.unlocked_skins)))
                self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
                try:
                    self.player.claimshop.remove("skin4")
                except:
                    print("Okbuyhsabuy")

            self.db.update_player_account(self.player.token, 'ClaimShop',  self.player.claimshop)
            self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
            self.db.update_player_account(self.player.token, 'Day',  self.player.day)

        if len(sorted(set([3, 15, 27, 29, 176]) - set(self.player.unlocked_skins))) != 0 and self.player.dailyskins[0] == 0:
            self.player.dailyskins[0] = random.choice(sorted(set([3, 15, 27, 29, 176]) - set(self.player.unlocked_skins)))
            self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
            try:
                self.player.claimshop.remove("skin1")
            except:
                print("Okbuyhsabuy")

        if len(sorted(set([20, 11, 47, 45, 5]) - set(self.player.unlocked_skins))) != 0 and self.player.dailyskins[1] == 0:
            self.player.dailyskins[1] = random.choice(sorted(set([20, 11, 47, 45, 5]) - set(self.player.unlocked_skins)))
            self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
            try:
                self.player.claimshop.remove("skin2")
            except:
                print("Okbuyhsabuy")

        if len(sorted(set([44, 68, 90]) - set(self.player.unlocked_skins))) != 0 and self.player.dailyskins[2] == 0:
            self.player.dailyskins[2] = random.choice(sorted(set([44, 68, 90]) - set(self.player.unlocked_skins)))
            self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
            try:
                self.player.claimshop.remove("skin3")
            except:
                print("Okbuyhsabuy")

        if len(sorted(set([49]) - set(self.player.unlocked_skins))) != 0 and self.player.dailyskins[3] == 0:
            self.player.dailyskins[3] = random.choice(sorted(set([49]) - set(self.player.unlocked_skins)))
            self.db.update_player_account(self.player.token, 'DailySkins',  self.player.dailyskins)
            try:
                self.player.claimshop.remove("skin4")
            except:
                print("Okbuyhsabuy")

        if self.player.season < 2:
            self.player.resources[1]['Amount'] = (self.player.resources[1]['Amount'] // 10)
            self.db.update_player_account(self.player.token, 'Resources', self.player.resources)

        if not self.player.season == 2:
            if not self.player.gems_remove:
                self.player.gems_remove = True
                self.player.gems = 0
                self.db.update_player_account(self.player.token, 'GemsRemove', self.player.gems_remove)
                self.db.update_player_account(self.player.token, 'Gems', self.player.gems)
            trophies_old = self.player.trophies
            self.player.trophies = 0
            for x in self.player.brawlers_id:
                print(self.player.brawlers_id)
                if self.player.brawlers_trophies[str(x)] > 1250:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 100) - 1) * 100
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 100) - 1) * 100
                    self.player.gems = self.player.gems + ((self.player.brawlers_trophies[str(x)] // 100) - 1) * 100
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                if self.player.brawlers_trophies[str(x)] > 1000:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 75) - 1) * 75
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 75) - 1) * 75
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                if self.player.brawlers_trophies[str(x)] > 500:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                if self.player.brawlers_trophies[str(x)] > 300:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 15) - 1) * 15
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 15) - 1) * 15
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                if self.player.brawlers_trophies[str(x)] > 100:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 10) - 1) * 10
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 10) - 1) * 10
                    self.player.gems = self.player.gems + self.player.brawlers_trophies[str(x)] // 50
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                else:
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
            if self.player.resources[0]['Amount'] < 0:
                self.player.resources[0]['Amount'] = 500
            self.player.season = 2
            self.db.update_player_account(self.player.token, 'Resources', self.player.resources)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies',  self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'Gems',  self.player.gems)
            self.db.update_player_account(self.player.token, 'Season',  self.player.season)
            self.db.update_player_account(self.player.token, 'Trophies',  self.player.trophies)
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Сброс сезона! Снято " + str(trophies_old - self.player.trophies) + " кубков! Начислено " + str(self.player.trophies) + " старпоинтов, " + str(self.player.trophies // 10) + " кристаллов!").send()
        self.player.trophies = 0
        for x in self.player.brawlers_id:
            self.player.trophies += self.player.brawlers_trophies[str(x)]
        self.db.update_player_account(self.player.token, 'Trophies',  self.player.trophies)
        if not self.player.gems_remove:
            self.player.gems_remove = True
            self.player.gems = 0
            self.db.update_player_account(self.player.token, 'GemsRemove', self.player.gems_remove)
            self.db.update_player_account(self.player.token, 'Gems', self.player.gems)
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Перерасчёт гемов...").send()
        pass

