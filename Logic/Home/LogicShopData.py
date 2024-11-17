import json
from datetime import datetime
from Logic.Home.LogicGlobal import LogicGlobal

class LogicShopData:

    shop_resources = json.loads(open('shop.json', 'r').read())

    gold_packs = shop_resources['GoldPacks']
    gold_cost, gold_amount = [], []

    for x in gold_packs:
        gold_cost.append(x['Cost'])
        gold_amount.append(x['Amount'])

    boxes = shop_resources['Boxes']
    token_doubler = shop_resources['TokenDoubler']

    offers = shop_resources['Offers']

    def encodeShopPacks(self):
        # Unknown
        self.writeArrayVint([20, 35, 75, 140, 290, 480, 800, 1250])
        self.writeArrayVint([1, 2, 3, 4, 5, 10, 15, 20])
        # Tickets
        self.writeArrayVint([10, 30, 80])
        self.writeArrayVint([6, 20, 60])
        # Gold
        self.writeArrayVint(LogicShopData.gold_cost)
        self.writeArrayVint(LogicShopData.gold_amount)

    def encodeShopResources(self):
        time_stamp = int(datetime.timestamp(datetime.now()))

        self.writeVInt(time_stamp)
        LogicShopData.encodeBoxes(self)
        LogicShopData.encodeTokenDoubler(self)


    def encodeShopOffers(self):
        self.writeVInt(len(LogicShopData.offers))
        for x in LogicShopData.offers:
            self.writeVInt(x['OffersCount']) # array
            if x['OffersCount'] >= 1:
                self.writeVInt(x['OfferID'])
                self.writeVInt(x['Multiplier'])
                self.writeDataReference(x['DataReference'][0], x['DataReference'][1])
                self.writeVInt(x['SkinID'])
            if x['OffersCount'] >= 2:
                self.writeVInt(x['OfferID2'])
                self.writeVInt(x['Multiplier2'])
                self.writeDataReference(x['DataReference2'][0], x['DataReference2'][1])
                self.writeVInt(x['SkinID2'])
            if x['OffersCount'] >= 3:
                self.writeVInt(x['OfferID3'])
                self.writeVInt(x['Multiplier3'])
                self.writeDataReference(x['DataReference3'][0], x['DataReference3'][1])
                self.writeVInt(x['SkinID3'])

            self.writeVInt(x['ShopType'])

            self.writeVInt(x['Cost'])
            self.writeVInt(x['Timer'])

            self.writeVInt(1)
            self.writeVInt(100)
            if x['ClaimID'] == 898989:
                self.writeUInt8(False)
            elif x['ClaimID'] == 70 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 71 and LogicGlobal.battles < 50:
                self.writeUInt8(True)
            elif x['ClaimID'] == 72 and LogicGlobal.battles < 75:
                self.writeUInt8(True)
            elif x['ClaimID'] == 73 and LogicGlobal.battles < 100:
                self.writeUInt8(True)
            elif x['ClaimID'] == 74 and LogicGlobal.battles < 125:
                self.writeUInt8(True)
            elif x['ClaimID'] == 75 and LogicGlobal.battles < 150:
                self.writeUInt8(True)
            elif x['ClaimID'] == 76 and LogicGlobal.battles < 200:
                self.writeUInt8(True)
            elif x['ClaimID'] == 77 and LogicGlobal.battles < 250:
                self.writeUInt8(True)
            elif x['ClaimID'] == 78 and LogicGlobal.battles < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == 79 and LogicGlobal.battles < 350:
                self.writeUInt8(True)
            elif x['ClaimID'] == 80 and LogicGlobal.battles < 400:
                self.writeUInt8(True)
            elif x['ClaimID'] == 81 and LogicGlobal.battles < 450:
                self.writeUInt8(True)
            elif x['ClaimID'] == 82 and LogicGlobal.battles < 525:
                self.writeUInt8(True)
            elif x['ClaimID'] == 83 and LogicGlobal.battles < 1600:
                self.writeUInt8(True)
            elif x['ClaimID'] == 84 and LogicGlobal.battles < 675:
                self.writeUInt8(True)
            elif x['ClaimID'] == 85 and LogicGlobal.battles < 800:
                self.writeUInt8(True)
            elif x['ClaimID'] == 86 and LogicGlobal.battles < 905:
                self.writeUInt8(True)
            elif x['ClaimID'] == 87 and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == 88 and LogicGlobal.battles < 1150:
                self.writeUInt8(True)
            elif x['ClaimID'] == 89 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 90 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 91 and LogicGlobal.battles < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == 92 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 93 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 94 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 95 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 96 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 97 and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == 98 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 99 and LogicGlobal.battles < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 160 and LogicGlobal.battles < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == 161 and LogicGlobal.battles < 1600:
                self.writeUInt8(True)
            elif x['ClaimID'] == 162 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 163 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 164 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 165 and LogicGlobal.battles < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == 166 and LogicGlobal.battles < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == 167 and LogicGlobal.battles < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == 168 and LogicGlobal.battles < 1600:
                self.writeUInt8(True)
            elif x['ClaimID'] == 169 and LogicGlobal.battles < 1600:
                self.writeUInt8(True)
            elif x['ClaimID'] == 170 and LogicGlobal.battles < 1600:
                self.writeUInt8(True)
            elif x['ClaimID'] == 171 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 172 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 173 and LogicGlobal.battles < 25:
                self.writeUInt8(True)
            elif x['ClaimID'] == 180 and LogicGlobal.battles < 1300:
                self.writeUInt8(True)
            elif x['ClaimID'] == 181 and LogicGlobal.battles < 1400:
                self.writeUInt8(True)
            elif x['ClaimID'] == 182 and LogicGlobal.battles < 1500:
                self.writeUInt8(True)
            elif x['ClaimID'] == 183 and LogicGlobal.battles < 1650:
                self.writeUInt8(True)
            elif x['ClaimID'] == 184 and LogicGlobal.battles < 1800:
                self.writeUInt8(True)
            elif x['ClaimID'] == 185 and LogicGlobal.battles < 1950:
                self.writeUInt8(True)
            elif x['ClaimID'] == 186 and LogicGlobal.battles < 2100:
                self.writeUInt8(True)
            elif x['ClaimID'] == 187 and LogicGlobal.battles < 2250:
                self.writeUInt8(True)
            elif x['ClaimID'] == 188 and LogicGlobal.battles < 2400:
                self.writeUInt8(True)
            else:
                self.writeUInt8(self.player.claim[x['ClaimID']])

            self.writeUInt8(0)
            self.writeVInt(x['ShopDisplay'])
            self.writeVInt(x['OldPrice'])
            self.writeVInt(0)

            self.writeInt(0)
            self.writeStringReference(x['OfferText'])

            self.writeUInt8(0)
            self.writeString(x['BGR'])
            self.writeVInt(0)
            self.writeUInt8(0)
            self.writeVInt(x['ETType'])
            self.writeVInt(x['ETMultiplier'])




    def encodeBoxes(self):
        self.writeVInt(160) # Tokens for 1 Brawl Box
        self.writeVInt(10)  # Tokens for 1 Big Box

        self.writeVInt(LogicShopData.boxes[0]['Cost'])
        self.writeVInt(LogicShopData.boxes[0]['Multiplier'])

        self.writeVInt(LogicShopData.boxes[1]['Cost'])
        self.writeVInt(LogicShopData.boxes[1]['Multiplier'])


    def encodeTokenDoubler(self):
        self.writeVInt(LogicShopData.token_doubler[0]['Cost'])
        self.writeVInt(LogicShopData.token_doubler[0]['Amount'])
