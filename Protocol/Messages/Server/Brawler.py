from ByteStream.Writer import Writer
from DataBase.MongoDB import MongoDB

class Brawler(Writer):

    def __init__(self, client, player, db):
        super().__init__(client)
        self.player = player
        self.id = 24403
        self.db = db
        #self.type = type

    def encode(self):
        #data = db.sortPlayers('trophies')
        data = db.load_all_players_sorted({}, 'Trophies')
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(16,self.player.brawlerL)
        self.writeString()
        x=1
        y = 0
        self.writeVInt(1)
        for i in data:
            	
            	self.writeVInt(0) # High ID
            	self.writeVInt(self.player.ID) # Low ID
            	self.writeVInt(1)
            	self.writeVInt(self.player.brawlers_trophies[str(self.player.brawlerL)]) # Player Trophies
            	self.writeVInt(1)
            	self.writeString("pon")
            	
            	self.writeString(self.player.name)# Player Name
            	self.writeVInt(9999) # Player Level
            	self.writeVInt(28000000 + 0)
            	self.writeVInt(43000000 + 0)
            	self.writeVInt(0)
            	self.writeVInt(0) # Unknown


        self.writeVInt(0)
        self.writeVInt(x)
        self.writeVInt(0)
        self.writeVInt(0) # Leaderboard global TID
        self.writeString("RU") #22