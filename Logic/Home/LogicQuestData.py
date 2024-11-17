from datetime import datetime

class LogicQuestData:
    def encodeQuests(self):
            self.writeVInt(len(self.player.quest))
            for x in range(len(self.player.quest)):
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Unknown
                self.writeVInt(1)     # Mission Type
                self.writeVInt(self.player.quest[x]['Wins'])     # Achieved Goal
                if self.player.quest[x]['QuestType'] = 0:
                    self.writeVInt(3)     # Quest Goal
                    self.writeVInt(100)    # Tokens Reward
                elif self.player.quest[x]['QuestType'] = 1:
                    self.writeVInt(5)     # Quest Goal
                    self.writeVInt(250)    # Tokens Reward
                elif self.player.quest[x]['QuestType'] = 2:
                    self.writeVInt(8)     # Quest Goal
                    self.writeVInt(500)    # Tokens Reward
                elif self.player.quest[x]['QuestType'] = 3:
                    self.writeVInt(15)     # Quest Goal
                    self.writeVInt(1000)    # Tokens Reward
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Current level
                self.writeVInt(0)     # Max level
                if self.player.quest[x]['QuestType'] = 0:
                    self.writeVInt(1)     # Quest Type
                else:
                    self.writeVInt(0)     # Quest Type
                self.writeUInt8(2)    # Quest State
                self.writeDataReference(16, self.player.quest[x]['BrawlerID'])
                self.writeVInt(0)     # GameMode
                self.writeVInt(0)     # Unknown
                self.writeVInt(0)     # Unknown