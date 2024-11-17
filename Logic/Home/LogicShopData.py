import json
from Utils.Helpers import Helpers
from datetime import datetime
import random
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
        self.writeArrayVint([1, 3, 4, 5, 10, 15, 20, 25])
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
                if x['ClaimID'] == "skin1":
                    self.writeVInt(self.player.dailyskins[0])
                elif x['ClaimID'] == "skin2":
                    self.writeVInt(self.player.dailyskins[1])
                elif x['ClaimID'] == "skin3":
                    self.writeVInt(self.player.dailyskins[2])
                elif x['ClaimID'] == "skin4":
                    self.writeVInt(self.player.dailyskins[3])
                else:
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
            self.writeVInt(Helpers.timerglobal(self, x['TimerStart'], x['TimerEnd']))

            self.writeVInt(1)
            self.writeVInt(100)
            if x['ClaimID'] in self.player.claimshop or Helpers.timerglobal(self, x['TimerStart'], x['TimerEnd']) < 0:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_5" and self.player.trophies < 5:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_10" and self.player.trophies < 10:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_15" and self.player.trophies < 15:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_20" and self.player.trophies < 20:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_30" and self.player.trophies < 30:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_40" and self.player.trophies < 40:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_60" and self.player.trophies < 60:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_100" and self.player.trophies < 100:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_150" and self.player.trophies < 150:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_200" and self.player.trophies < 200:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_250" and self.player.trophies < 250:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_300" and self.player.trophies < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_350" and self.player.trophies < 350:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_400" and self.player.trophies < 400:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_450" and self.player.trophies < 450:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_500" and self.player.trophies < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_550" and self.player.trophies < 550:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_600" and self.player.trophies < 600:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_650" and self.player.trophies < 650:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_700" and self.player.trophies < 700:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_750" and self.player.trophies < 750:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_800" and self.player.trophies < 800:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_850" and self.player.trophies < 850:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_900" and self.player.trophies < 900:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_950" and self.player.trophies < 950:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1000" and self.player.trophies < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1100" and self.player.trophies < 1100:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1200" and self.player.trophies < 1200:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1300" and self.player.trophies < 1300:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1400" and self.player.trophies < 1400:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1500" and self.player.trophies < 1500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1600" and self.player.trophies < 1600:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1700" and self.player.trophies < 1700:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1800" and self.player.trophies < 1800:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_1900" and self.player.trophies < 1900:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2000" and self.player.trophies < 2000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2100" and self.player.trophies < 2100:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2200" and self.player.trophies < 2200:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2300" and self.player.trophies < 2300:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2400" and self.player.trophies < 2400:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2500" and self.player.trophies < 2500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2600" and self.player.trophies < 2600:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2700" and self.player.trophies < 2700:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2800" and self.player.trophies < 2800:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_2900" and self.player.trophies < 2900:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3000" and self.player.trophies < 3000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3100" and self.player.trophies < 3100:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3200" and self.player.trophies < 3200:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3300" and self.player.trophies < 3300:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3400" and self.player.trophies < 3400:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3500" and self.player.trophies < 3500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3600" and self.player.trophies < 3600:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3700" and self.player.trophies < 3700:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3800" and self.player.trophies < 3800:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_3900" and self.player.trophies < 3900:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_4000" and self.player.trophies < 4000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_4150" and self.player.trophies < 4150:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_4300" and self.player.trophies < 4300:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_4500" and self.player.trophies < 4500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_4750" and self.player.trophies < 4750:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_5000" and self.player.trophies < 5000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "tr_5000" and self.player.trophies < 5000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "starrroad_end" and sorted(set([2, 6, 8, 10, 13, 22, 24, 3, 4, 7, 9, 18, 19, 25, 34, 1, 15, 16, 20, 26, 27, 49, 43, 36, 45, 29, 5, 12, 23, 28, 40, 35, 38, 41, 39, 44, 46, 48, 50]) - set(self.player.brawlers_unlocked)) != []:
                self.writeUInt8(True)
            else:
                self.writeUInt8(False)

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
        self.writeVInt(500) # Tokens for 1 Brawl Box
        self.writeVInt(10)  # Tokens for 1 Big Box

        self.writeVInt(LogicShopData.boxes[0]['Cost'])
        self.writeVInt(LogicShopData.boxes[0]['Multiplier'])

        self.writeVInt(LogicShopData.boxes[1]['Cost'])
        self.writeVInt(LogicShopData.boxes[1]['Multiplier'])


    def encodeTokenDoubler(self):
        self.writeVInt(LogicShopData.token_doubler[0]['Cost'])
        self.writeVInt(LogicShopData.token_doubler[0]['Amount'])
