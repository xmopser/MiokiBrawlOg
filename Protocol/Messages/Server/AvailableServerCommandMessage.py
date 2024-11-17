from ByteStream.Writer import Writer
from Utils.Helpers import Helpers
from Protocol.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from Protocol.Commands.Server.LogicSetSupportedCreatorCommand import LogicSetSupportedCreatorCommand
from Protocol.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand
from Protocol.Commands.Server.LogicAddNotificationCommand import LogicAddNotificationCommand


class AvailableServerCommandMessage(Writer):

    def __init__(self, client, player, commandID, message):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.commandID = commandID
        self.message = message

    def encode(self):

        commands = {
            201: LogicChangeAvatarNameCommand,
            203: LogicGiveDeliveryItemsCommand,
            215: LogicSetSupportedCreatorCommand,
            206: LogicAddNotificationCommand
        }

        if self.commandID in commands:

            self.writeVInt(self.commandID)
            if self.commandID == 206:
                commands[self.commandID].encode(self, self.message)
            else:
                commands[self.commandID].encode(self)
        else:
            print(f"{Helpers.yellow}[SERVER] Cannot create command! ID: {self.commandID}")