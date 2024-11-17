import time
from ByteStream.Reader import Reader
from Protocol.Messages.Server.AllianceResponseMessage import AllianceResponseMessage
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class SendAllianceMailMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readInt()
        self.msg = self.readString()

    def process(self, db):
        #result = (time.time() - self.player.club_mail_time)
        #if result >= 43200:
        AllianceResponseMessage(self.client, self.player, 114).send()
        '''if result < 43200:
            AllianceResponseMessage(self.client, self.player, 112).send()'''
        if self.msg != b'' and self.player.club_role in [2, 4]:
            AllianceResponseMessage(self.client, self.player, 113).send()
            #if result >= 43200:
            club_data = db.load_club(self.player.club_id)
            club_data['Inbox'].append(
                {
                    f'IsSeen': 0,
                    'Timer': time.time(),
                    'Message': self.msg,
                    'Trophies': self.player.trophies,
                    'Name': self.player.name,
                    'ProfileIcon': self.player.profile_icon,
                    'NameColor': self.player.name_color
                }
            )
            db.update_club(self.player.club_id, 'Inbox', club_data['Inbox'])

            db.update_player_account(self.player.token, 'ClubMailTime', time.time())
            club_data = db.load_club(self.player.club_id)
            for members in club_data['Members']:
                message = {f'IsSeen': 0, 'Timer': time.time(), 'Message': self.msg, 'Trophies': self.player.trophies, 'Name': self.player.name, 'ProfileIcon': self.player.profile_icon, 'NameColor': self.player.name_color}
                AvailableServerCommandMessage(self.client, self.player, 206, message).sendByID(members[str('ID')])
        elif self.player.club_role not in [2, 4]:
            AllianceResponseMessage(self.client, self.player, 95).send()

