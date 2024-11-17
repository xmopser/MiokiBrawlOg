from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Logic.Home.LogicShopData import LogicShopData
import random
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class LogicGatchaCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()
        self.box_id = self.readVInt()


    def process(self, db):

        self.player.delivery_items = {
            'Count': 1,
            'Type': 0,
            'Items': []
        }

        if self.box_id == 1:
            self.player.gems = self.player.gems - LogicShopData.boxes[0]['Cost']
            db.update_player_account(self.player.token, 'Gems', self.player.gems)
            if True:
                pins = []
                for x in range(318): pins.append(x)
                if len(sorted(set(pins) - set(self.player.emotes_id))) > 3:
                    for r in range(3):
                        pins_locked = sorted(set(pins) - set(self.player.emotes_id))
                        x = random.choice(pins_locked)
                        item = {'Amount': 1, 'DataRef': [0, 0 ], 'SkinRef': [29, 0 ], 'PinRef': [52, x ], 'Value':11 }
                        self.player.delivery_items['Type'] = 100
                        self.player.delivery_items['Items'].append(item)
                        self.player.emotes_id.append(x)
                        db.update_player_account(self.player.token, 'UnlockedPins', self.player.emotes_id)
                else:
                    item = {'Amount': 49, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':8 }
                    self.player.delivery_items['Type'] = 100
                    self.player.delivery_items['Items'].append(item)

                    self.player.gems = self.player.gems + 49
                    db.update_player_account(self.player.token, 'Gems', self.player.gems)

        elif self.box_id == 3:
            self.player.gems = self.player.gems - LogicShopData.boxes[1]['Cost']
            db.update_player_account(self.player.token, 'Gems', self.player.gems)

            brawlers_pp = []
            for brawler in self.player.brawlers_unlocked:
                if (self.player.brawlers_level[str(brawler)] < 8):
                    brawlers_pp.append(brawler)
            if brawlers_pp:
                for x in range(5):
                    brawler_pp = random.choice(sorted(set(brawlers_pp)))
                    item = {'Amount': 100, 'DataRef': [16, brawler_pp ], 'SkinRef': [0, 0 ], 'Value':6 }
                    self.player.delivery_items['Type'] = 100
                    self.player.delivery_items['Items'].append(item)
                    self.player.brawlers_powerpoints[str(brawler_pp)] = self.player.brawlers_powerpoints[str(brawler_pp)] + 75
                    db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
            else:
                item = {'Amount': 430, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 430
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

        elif self.box_id == 5:
            self.player.resources[0]['Amount'] = self.player.resources[0]['Amount'] - 500
            db.update_player_account(self.player.token, 'Resources', self.player.resources)

            item = {'Amount': 50, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 }
            self.player.delivery_items['Type'] = 100
            self.player.delivery_items['Items'].append(item)
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 50
            db.update_player_account(self.player.token, 'Resources', self.player.resources)

            brawlers_pp = []
            for brawler in self.player.brawlers_unlocked:
                if (self.player.brawlers_level[str(brawler)] < 8):
                    brawlers_pp.append(brawler)

            if brawlers_pp:
                for i in range(3):
                    brawler_pp = random.choice(sorted(set(brawlers_pp)))
                    item = {'Amount': 75, 'DataRef': [16, brawler_pp ], 'SkinRef': [0, 0 ], 'Value':6 }
                    self.player.delivery_items['Type'] = 100
                    self.player.delivery_items['Items'].append(item)
                    self.player.brawlers_powerpoints[str(brawler_pp)] = self.player.brawlers_powerpoints[str(brawler_pp)] + 75
                    db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
            else:
                item = {'Amount': 25, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 25
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

        self.player.db = db
        AvailableServerCommandMessage(self.client, self.player, 203, {}).send()



