from ByteStream.Reader import Reader

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
        self.player.bp_activated = True
        self.player.gems -= 169
        self.db.update_player_account(self.player.token, 'Gems', self.player.gems)
        self.db.update_player_account(self.player.token, 'BrawlPassActivated', self.player.bp_activated, True)