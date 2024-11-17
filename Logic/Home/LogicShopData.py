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
            elif x['ClaimID'] == "event_byebyeboxes_1" and LogicGlobal.battles < 100:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_2" and LogicGlobal.battles < 200:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_3" and LogicGlobal.battles < 300:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_4" and LogicGlobal.battles < 400:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_5" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_6" and LogicGlobal.battles < 600:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_7" and LogicGlobal.battles < 700:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_8" and LogicGlobal.battles < 800:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_9" and LogicGlobal.battles < 900:
                self.writeUInt8(True)
            elif x['ClaimID'] == "event_byebyeboxes_10" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_piper_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_leon_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_bull_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_rico_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_barley_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_frank_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_mortis_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_mortis_hat_silver" and LogicGlobal.battles < 500:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_piper_gold" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_leon_gold" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_bull_gold" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_rico_gold" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_barley_gold" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_frank_gold" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_mortis_gold" and LogicGlobal.battles < 1000:
                self.writeUInt8(True)
            elif x['ClaimID'] == "skin_mortis_hat_gold" and LogicGlobal.battles < 1000:
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
        self.writeVInt(100) # Tokens for 1 Brawl Box
        self.writeVInt(10)  # Tokens for 1 Big Box

        self.writeVInt(LogicShopData.boxes[0]['Cost'])
        self.writeVInt(LogicShopData.boxes[0]['Multiplier'])

        self.writeVInt(LogicShopData.boxes[1]['Cost'])
        self.writeVInt(LogicShopData.boxes[1]['Multiplier'])


    def encodeTokenDoubler(self):
        self.writeVInt(LogicShopData.token_doubler[0]['Cost'])
        self.writeVInt(LogicShopData.token_doubler[0]['Amount'])
