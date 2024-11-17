from datetime import datetime
from Utils.Helpers import Helpers
from datetime import datetime
from Logic.Home.LogicShopData import LogicShopData

class LogicDailyData:

    def encode(self):

        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        self.writeVInt(time_stamp)

        self.writeVInt(self.player.trophies)
        self.writeVInt(self.player.high_trophies)
        self.writeVInt(self.player.high_trophies)

        self.writeVInt(self.player.trophy_reward)
        self.writeVInt(self.player.exp_points)

        self.writeDataReference(28, self.player.profile_icon)
        self.writeDataReference(43, self.player.name_color)

        self.writeVInt(50)
        for x in range(50):
            self.writeVInt(x)

        self.writeVInt(len(self.player.selected_skins))
        for x in self.player.selected_skins:
            self.writeDataReference(29, self.player.selected_skins[x])

        self.writeVInt(len(self.player.unlocked_skins))
        for x in self.player.unlocked_skins:
            self.writeDataReference(29, x)

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            self.writeDataReference(0,0)

        self.writeVInt(0)      # Leaderboard Global TID
        self.writeVInt(self.player.high_trophies)  # Trophy Road Reached Icon
        self.writeVInt(0)      # Unknown
        self.writeVInt(0)      # Unknown

        self.writeUInt8(0)     # Is Token Limit Reached

        self.writeVInt(self.player.token_doubler)
        self.writeVInt(Helpers.timerglobal(self, [12, 2, 2], [12, 25, 2]))  # Brawl Pass Timer
        self.writeVInt(0)      # Power Play Timer
        self.writeVInt(Helpers.timerglobal(self, [0, 0, 0], [12, 25, 2]))  # Brawl Pass Timer

        self.writeVInt(0)  # Unknown

        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeUInt8(4) # Shop Token Doubler

        self.writeVInt(2) # Unknown
        self.writeVInt(2) # Unknown
        self.writeVInt(2) # Unknown

        self.writeVInt(0) # Name Change Cost
        self.writeVInt(0) # Name Change Timer


        LogicShopData.encodeShopOffers(self)

        self.writeVInt(0)  # AdStatus
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(200) # Available Battle Tokens
        self.writeVInt(0)   # Time till Bonus Tokens

        self.writeVInt(0)  # Unknown Array
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(1)
        self.writeVInt(1)  # Unknown
        hb = "False"
        for i in range(50):
            if self.player.home_brawler == i:
                hb = "True"
        if hb == "True":
            self.writeDataReference(16, self.player.home_brawler)
        else:
            self.writeDataReference(16, 0)

        self.writeString(self.player.region)
        self.writeString(self.player.content_creator)

        self.writeVInt(2)  # animka Count
        self.writeInt(4) #4-трофеи, 3-токены, 14-монеты, 8 ?-стар поинты, 5-жетоны(врядли робят сейчас), 13-жетоны бравлера
        self.writeInt(self.player.trp)
        self.writeInt(8) #4-трофеи, 3-токены, 14-монеты, 8 ?-стар поинты, 5-жетоны(врядли робят сейчас), 13-жетоны бравлера
        self.writeInt(self.player.spa)

        self.writeVInt(0)  # CooldownEntry
        for x in range(0):
            self.writeVInt(99999)
            self.writeDataReference(16, 36)
            self.writeVInt(99999)

        self.writeVInt(1)  # BrawlPassSeasonData
        for x in range(1):
            self.writeVInt(0)  # сезон бп
            self.writeVInt(-1)  #Tokens
            self.writeBool(self.player.bp_activated)
            self.writeVInt(2)  # Pass Progress

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)

        self.writeVInt(0)  # ProLeagueSeasonData
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeBoolean(True) # LogicQuests
        if True:
            self.writeVInt(len(self.player.quest))
            for x in self.player.quest:
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Unknown
                self.writeVInt(1)     # Mission Type
                self.writeVInt(x['Wins'])     # Achieved Goal
                self.writeVInt(x['Goal'])     # Quest Goal
                self.writeVInt(x['Reward'])    # Tokens Reward
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Current level
                self.writeVInt(0)     # Max level
                if x['Goal'] == 3:
                    self.writeVInt(1)     # Quest Type
                else:
                    self.writeVInt(0)     # Quest Type
                self.writeUInt8(2)    # Quest State
                self.writeDataReference(16, x['BrawlerID'])
                self.writeVInt(0)     # GameMode
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Unknown

        # Emotes Array
        self.writeBoolean(True)
        if True:
            self.writeVInt(len(self.player.emotes_id))
            for x in self.player.emotes_id:
                self.writeDataReference(52, x)
                self.writeVInt(1)     # Unknown
                self.writeVInt(1)     # Unknown
                self.writeVInt(1)     # Unknown

