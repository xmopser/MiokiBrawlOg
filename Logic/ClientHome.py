from Logic.Home.LogicDailyData import LogicDailyData
from Logic.Home.LogicConfData import LogicConfData
import random, json, time
from DataBase.MongoDB import MongoDB
from Protocol.Commands.Server.LogicAddNotificationCommand import LogicAddNotificationCommand

class LogicClientHome:

    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)

        self.writeLong(self.player.ID) # ID Игрока
        
        # Массив с Фабрикой Уведомлений
        if self.player.club_id != 0:
            self.config = json.loads(open('config.json', 'r').read())
            self.db = MongoDB(self.config['MongoConnectionURL'])
            self.club_data = self.db.load_club(self.player.club_id)
            self.writeVInt(len(self.club_data['Inbox'])) # Notifications Count
            if (len(self.club_data['Inbox'])) != 0:
                for inbox_data in self.club_data['Inbox']:
                    self.writeVInt(82) # Notification ID

                    self.writeByte(0)
                    self.writeInt(0) # IsNotificationSeen
                    self.writeInt(int(time.time() - inbox_data['Timer'])) # Timer
                    self.writeString(inbox_data['Message']) # Notification Message Entry

                    self.writeString(inbox_data['Name']) # Sender name
                    self.writeVInt(0)
                    self.writeVInt(28000000 + inbox_data['ProfileIcon'])
                    self.writeVInt(43000000 + inbox_data['NameColor'])
                    self.writeVInt(43000000 + inbox_data['NameColor'])
        else:
            self.writeVInt(0)            
            '''self.writeVInt(85) # Notification ID
            self.writeInt(2) # Notification Type
            self.writeBoolean(False) # (Notification Read
            self.writeInt(0) # Notification Time Ago
            self.writeString() # Notification Message Entry
            self.writeVInt(0) # Revoke Type
            self.writeVInt(6974) # Gems revoked
            self.writeInt(0)
            self.writeInt(0)
            self.writeVInt(0)
            self.writeString("BreadDEV") # Revoke Requested 
            self.writeVInt(83) # Notification ID
            self.writeInt(1) # Notification Type
            self.writeBoolean(False) # Notification Read
            self.writeInt(0) # Notification Time Ago
            self.writeString() # Notification Message Entry
            for x in range(1):
                self.writeStringShort('OfferTitle')
                self.writeStringShort('OfferTitle')
                self.writeStringShort('OfferTitle')
                self.writeStringReference('OfferTitle')
                self.writeString("OfferTitle")
                self.writeLong(0)
                self.writeVInt(0)'''
        # Массив с Фабрикой Уведомлений

        self.writeVInt(0) # Неизвестно
        self.writeUInt8(0) # Неизвестно