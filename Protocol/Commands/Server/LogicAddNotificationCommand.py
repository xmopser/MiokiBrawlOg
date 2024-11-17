from ByteStream.Writer import Writer
from Utils.Helpers import Helpers
import time
class LogicAddNotificationCommand(Writer):

    def encode(self, message):
        #==[Notification array]==#
        for message_data in message:
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
        #==[Notification array]==#

        '''self.writeVint(90) # Notification ID
        self.writeInt(1) # Notification Type
        self.writeBoolean(False) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVint(50000000 + 1) # Brawlers Count
        self.writeVint(29000000 + 10) # Brawlers Count
        self.writeVint(1) # Count
        # Season End Notification End''' 
        print(f"\nNotification Added\n")