from ByteStream.Reader import Reader
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Protocol.Messages.Server.AvatarNameChangeFailedMessage import AvatarNameChangeFailedMessage
from Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage

class SetNameMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.username = self.readString()
        self.state = self.readVInt()

    def process(self, db):
        if self.username != '':
            if len(self.username) >= 2 and len(self.username) <= 20:
                if self.player.environment == "prod":
                    self.player.name = self.username
                    db.update_player_account(self.player.token, 'Name', self.username)
                    db.update_player_account(self.player.token, 'NameSet', True)
                    AvailableServerCommandMessage(self.client, self.player, 201, {}).send()
                else:
                    if self.username == "tc-xmopser-3578":
                        self.player.name = "xmopser"
                        db.update_player_account(self.player.token, 'Name', self.player.name)
                        db.update_player_account(self.player.token, 'NameSet', True)
                        AvailableServerCommandMessage(self.client, self.player, 201, {}).send()
                    elif self.username == "tc-insafer-2342":
                        self.player.name = "insafer"
                        db.update_player_account(self.player.token, 'Name', self.player.name)
                        db.update_player_account(self.player.token, 'NameSet', True)
                        AvailableServerCommandMessage(self.client, self.player, 201, {}).send()
                    elif self.username == "tc-sigma-8213":
                        self.player.name = "sigma"
                        db.update_player_account(self.player.token, 'Name', self.player.name)
                        db.update_player_account(self.player.token, 'NameSet', True)
                        AvailableServerCommandMessage(self.client, self.player, 201, {}).send()
                    elif self.username == "tc-love-3479":
                        self.player.name = "love"
                        db.update_player_account(self.player.token, 'Name', self.player.name)
                        db.update_player_account(self.player.token, 'NameSet', True)
                        AvailableServerCommandMessage(self.client, self.player, 201, {}).send()
                    elif self.username == "tc-bon-6892":
                        self.player.name = "bon"
                        db.update_player_account(self.player.token, 'Name', self.player.name)
                        db.update_player_account(self.player.token, 'NameSet', True)
                        AvailableServerCommandMessage(self.client, self.player, 201, {}).send()
                    elif self.username == "tc-mexa-6892":
                        self.player.name = "mexa"
                        db.update_player_account(self.player.token, 'Name', self.player.name)
                        db.update_player_account(self.player.token, 'NameSet', True)
                        AvailableServerCommandMessage(self.client, self.player, 201, {}).send()
                    else:
                        self.player.err_code = 1
                        LoginFailedMessage(self.client, self.player, "Неверный код доступа!").send()
            else:
                AvatarNameChangeFailedMessage(self.client, self.player).send()
        else:
            AvatarNameChangeFailedMessage(self.client, self.player).send()