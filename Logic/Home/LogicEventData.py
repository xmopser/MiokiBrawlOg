import json
from Utils.Helpers import Helpers

class LogicEventData:
    events = json.loads(open("events.json", 'r').read())

    def encode(self):
        events = json.loads(open("events.json", 'r').read())

        self.writeVInt(len(events))
        for i in range(len(events)):
            self.writeVInt(i)

        self.writeVInt(len(events))

        for event in events:
            self.writeVInt(events.index(event) + 1)
            self.writeVInt(events.index(event) + 1)
            self.writeVInt(event['Ended'])
            self.writeVInt(Helpers.timerglobal(self, [0, 0, 1], [0, 0, 999]))  # Timer

            self.writeVInt(0)
            self.writeDataReference(15, event['ID'])

            self.writeVInt(event['Status'])

            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)

            self.writeVInt(0)
            self.writeVInt(0)


        self.writeVInt(0)
        for x in range(0):
            pass
