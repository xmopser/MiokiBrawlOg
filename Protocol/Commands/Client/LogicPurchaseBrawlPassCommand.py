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

        item = {'Amount': 1900, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 } # Credits
        self.player.delivery_items['Type'] = 100
        self.player.delivery_items['Items'].append(item)
        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 1900
        db.update_player_account(self.player.token, 'Resources', self.player.resources)

        self.player.bp_activated = True
        self.player.gems -= 169
        db.update_player_account(self.player.token, 'Gems', self.player.gems)
        db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated)

        AvailableServerCommandMessage(self.client, self.player, 203, {}).send()