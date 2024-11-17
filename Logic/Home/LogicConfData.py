from datetime import datetime
from Logic.Home.LogicEventData import LogicEventData
from Logic.Home.LogicShopData import LogicShopData
from Logic.Home.LogicGlobal import LogicGlobal
from Utils.Helpers import Helpers

class LogicConfData:

    def encode(self):

        LogicShopData.encodeShopResources(self)

        self.writeVInt(500)    # Unknown
        self.writeVInt(50)     # Unknown
        self.writeVInt(999900) # Unknown

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        LogicEventData.encode(self)

        LogicShopData.encodeShopPacks(self)

        self.writeVInt(0)   # Unknown
        self.writeVInt(200) # Max Tokens
        self.writeVInt(20)  # Plus Tokens
        self.writeVInt(0)   # Unknown
        self.writeVInt(10)  # Unknown
        self.writeVInt(0)   # Unknown
        self.writeVInt(0)   # Unknown
        self.writeVInt(0)   # Unknown
        self.writeVInt(0)   # Unknown
        self.writeUInt8(1)  # Shop Box State

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            # ReleaseEntry::encode
            self.writeDataReference(16, 35)
            self.writeInt(99999)
            self.writeInt(99999)

        self.writeVInt(1)  # Menu Theme Array
        for x in range(1):
            # IntValueEntry::encode
            self.writeInt(1)         # Unknown
            if Helpers.timerglobal(self, [12, 4, 2], [12, 18, 2]) < 0:
                self.writeInt(41000000 + 6)  # Theme ID
            else:
                self.writeInt(41000000 + 6)  # Theme ID

        self.writeVInt(0)
        for x in range(0):
            # CustomEvent::encode
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)


        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            for x in range(3):
                self.writeInt(0)
                self.writeStringReference('Test')
