from ByteStream.Writer import Writer
from DataBase.MongoDB import MongoDB
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage

class KeepAliveOkMessage(Writer):

    def __init__(self, client, player, db: MongoDB):
        super().__init__(client)
        self.id = 20108
        self.player = player
        self.db = db

    def encode(self):
        if not self.player.season == 1:
            trophies_old = self.player.trophies
            self.player.trophies = 0
            for x in self.player.brawlers_id:
                print(self.player.brawlers_id)
                if self.player.brawlers_trophies[str(x)] > 1000:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.gems = self.player.gems + ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 5
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                if self.player.brawlers_trophies[str(x)] > 500:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.gems = self.player.gems + ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 5
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                if self.player.brawlers_trophies[str(x)] > 50:
                    self.player.brawlers_trophies[str(x)] = ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] + ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 50
                    self.player.gems = self.player.gems + ((self.player.brawlers_trophies[str(x)] // 50) - 1) * 5
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
                else:
                    self.player.trophies = self.player.trophies + self.player.brawlers_trophies[str(x)]
            self.player.season = 1
            self.db.update_player_account(self.player.token, 'Resources', self.player.resources)
            self.db.update_player_account(self.player.token, 'BrawlersTrophies',  self.player.brawlers_trophies)
            self.db.update_player_account(self.player.token, 'Gems',  self.player.gems)
            self.db.update_player_account(self.player.token, 'Season',  self.player.season)
            self.db.update_player_account(self.player.token, 'Trophies',  self.player.trophies)
            self.player.err_code = 1
            LoginFailedMessage(self.client, self.player, "Сброс сезона! Снято " + str(trophies_old - self.player.trophies) + " кубков! Начислено " + str(self.player.trophies) + " старпоинтов, " + str(self.player.trophies // 10) + " кристаллов!").send()
        pass
