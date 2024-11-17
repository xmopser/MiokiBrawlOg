from ByteStream.Writer import Writer
from Logic.Home.LogicGlobal import LogicGlobal
import time

class LobbyInfoMessage(Writer):

    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.player = player
        self.count = count

    def encode(self):
        self.writeVInt(self.count)
        self.writeString("MiokiBrawl\nhttps://t.me/miokibrawl\nVersion: "+ self.player.versionname + "(" + self.player.version + ")" +"\nServer info: (" + self.player.version + "." + self.player.snapshot + "." + self.player.environment + "." + self.player.hosting +")\nBattles: " + str(LogicGlobal.battles) + "\n" + "PlayerID: " + str(self.player.ID) + "\n" + self.player.lobbymsg)

        self.writeVInt(0) # array
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
