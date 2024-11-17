from ByteStream.Reader import Reader
from Logic.Home.LogicShopData import LogicShopData
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class LogicPurchaseBrawlPassCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()

    def process(self, db):

        self.player.delivery_items = {
            'Count': 1,
            'Type': 0,
            'Items': []
        }

        item = {'Amount': 1, 'DataRef': [0, 0 ], 'SkinRef': [29, 213], 'Value':9 } # Skin 1
        self.player.delivery_items['Type'] = 100
        self.player.delivery_items['Items'].append(item)
        self.player.unlocked_skins.append(213)
        db.update_player_account(self.player.token, 'UnlockedSkins2', self.player.unlocked_skins)

        item = {'Amount': 1, 'DataRef': [16, 39], 'SkinRef': [0, 0 ], 'Value':1 } # Brawler
        self.player.delivery_items['Type'] = 100
        self.player.delivery_items['Items'].append(item)
        self.player.brawlers_unlocked.append(39)
        db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

        item = {'Amount': 1, 'DataRef': [0, 0 ], 'SkinRef': [29, 211], 'Value':9 } # Skin 70
        self.player.delivery_items['Type'] = 100
        self.player.delivery_items['Items'].append(item)
        self.player.unlocked_skins.append(211)
        db.update_player_account(self.player.token, 'UnlockedSkins2', self.player.unlocked_skins)

        item = {'Amount': 500, 'DataRef': [16, 39 ], 'SkinRef': [0, 0 ], 'Value':6 } # Power Points
        self.player.delivery_items['Type'] = 100
        self.player.delivery_items['Items'].append(item)
        self.player.brawlers_powerpoints[str(39)] = self.player.brawlers_powerpoints[str(39)] + 500
        db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

        item = {'Amount': 430, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 } # Credits
        self.player.delivery_items['Type'] = 100
        self.player.delivery_items['Items'].append(item)
        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 430
        db.update_player_account(self.player.token, 'Resources', self.player.resources)

        for x in [312, 313, 314, 315, 316, 317, 318, 319, 487]:
            item = {'Amount': 1, 'DataRef': [0, 0 ], 'SkinRef': [29, 0 ], 'PinRef': [52, x ], 'Value':11 }
            self.player.delivery_items['Type'] = 100
            self.player.delivery_items['Items'].append(item)
            self.player.emotes_id.append(x)
            db.update_player_account(self.player.token, 'UnlockedPins', self.player.emotes_id)

        self.player.bp_activated = True
        self.player.gems -= 169
        db.update_player_account(self.player.token, 'Gems', self.player.gems)
        db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated)

        AvailableServerCommandMessage(self.client, self.player, 203, {}).send()