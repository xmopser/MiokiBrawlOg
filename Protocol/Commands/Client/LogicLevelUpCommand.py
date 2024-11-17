from ByteStream.Reader import Reader

class LogicLevelUpCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.brawler = self.readDataReference()[1]

    def process(self, db):
        print(self.player.brawlers_level[str(self.brawler)])
        if (self.player.brawlers_level[str(self.brawler)] == 0):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 20
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif (self.player.brawlers_level[str(self.brawler)] == 1):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 35
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif (self.player.brawlers_level[str(self.brawler)] == 2):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 75
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif (self.player.brawlers_level[str(self.brawler)] == 3):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 140
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif (self.player.brawlers_level[str(self.brawler)] == 4):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 290
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif (self.player.brawlers_level[str(self.brawler)] == 5):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 480
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif (self.player.brawlers_level[str(self.brawler)] == 6):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 800
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        elif (self.player.brawlers_level[str(self.brawler)] == 7):
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - 1250
            db.update_player_account(self.player.token, 'Resources', self.player.resources)
        self.player.brawlers_level[str(self.brawler)] = self.player.brawlers_level[str(self.brawler)] + 1
        db.update_player_account(self.player.token, 'BrawlersLevel', self.player.brawlers_level)
