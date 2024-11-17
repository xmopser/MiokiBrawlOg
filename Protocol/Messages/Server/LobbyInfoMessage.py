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
        self.writeString("MiokiBrawl\nhttps://t.me/miokibrawl\nServer version: 4.1101.2\nHappy Lunar new year!")

        self.writeVInt(0) # array
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
