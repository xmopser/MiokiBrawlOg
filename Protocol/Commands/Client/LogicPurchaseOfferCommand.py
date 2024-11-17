from ByteStream.Reader import Reader
from Logic.Home.LogicShopData import LogicShopData
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class LogicPurchaseOfferCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readLogicLong()

        self.offer_index = self.readVInt()

        self.brawler = self.readDataReference()[1]

    def process(self, db):
        offer_claim       = LogicShopData.offers[self.offer_index]['ClaimID']
        if offer_claim in self.player.claimshop:
            offer_claim_b = True
        else:
            offer_claim_b = False
        offer_count       = LogicShopData.offers[self.offer_index]['OffersCount']
        offer_resource = LogicShopData.offers[self.offer_index]['ShopType']
        offer_cost     = LogicShopData.offers[self.offer_index]['Cost']
        if offer_count >= 1:
            offer_id       = LogicShopData.offers[self.offer_index]['OfferID']
            offer_amount   = LogicShopData.offers[self.offer_index]['Multiplier']
            offer_skin   = LogicShopData.offers[self.offer_index]['SkinID']
            offer_char = LogicShopData.offers[self.offer_index]['DataReference'][1]
        if offer_count >= 2:
            offer_id2       = LogicShopData.offers[self.offer_index]['OfferID2']
            offer_amount2   = LogicShopData.offers[self.offer_index]['Multiplier2']
            offer_skin2   = LogicShopData.offers[self.offer_index]['SkinID2']
            offer_char2 = LogicShopData.offers[self.offer_index]['DataReference2'][1]
        if offer_count >= 3:
            offer_id3       = LogicShopData.offers[self.offer_index]['OfferID3']
            offer_amount3   = LogicShopData.offers[self.offer_index]['Multiplier3']
            offer_skin3   = LogicShopData.offers[self.offer_index]['SkinID3']
            offer_char3 = LogicShopData.offers[self.offer_index]['DataReference3'][1]

        if not offer_claim_b and offer_count >= 1:


            self.player.delivery_items = {
                'Count': 1,
                'Type': 0,
                'Items': []
            }

            if offer_id == 1:
                item = {'Amount': offer_amount, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + offer_amount
                db.update_player_account(self.player.token, 'Resources', self.player.resources)


            elif offer_id == 16:
                item = {'Amount': offer_amount, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':8 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.gems = self.player.gems + offer_amount
                db.update_player_account(self.player.token, 'Gems', self.player.gems)

            elif offer_id == 9:
                item = {'Amount': offer_amount, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':2 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.token_doubler = self.player.token_doubler + offer_amount
                db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)

            elif offer_id == 3:
                print("ok")
                item = {'Amount': offer_amount, 'DataRef': [16, offer_char ], 'SkinRef': [0, 0 ], 'Value':1 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                if offer_char not in self.player.brawlers_unlocked:
                    self.player.brawlers_unlocked.append(offer_char)
                    db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

            elif offer_id == 12:
                item = {'Amount': offer_amount, 'DataRef': [16, self.brawler ], 'SkinRef': [0, 0 ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(self.brawler)] = self.player.brawlers_powerpoints[str(self.brawler)] + offer_amount
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            elif offer_id == 4:
                if offer_claim == "skin1":
                    offer_skin = self.player.dailyskins[0]
                elif offer_claim == "skin2":
                    offer_skin = self.player.dailyskins[1]
                elif offer_claim == "skin3":
                    offer_skin = self.player.dailyskins[2]
                elif offer_claim == "skin4":
                    offer_skin = self.player.dailyskins[3]
                item = {'Amount': offer_amount, 'DataRef': [0, 0 ], 'SkinRef': [29, offer_skin ], 'Value':9 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                self.player.unlocked_skins.append(offer_skin)
                db.update_player_account(self.player.token, 'UnlockedSkins2', self.player.unlocked_skins)

            elif offer_id == 8:
                item = {'Amount': offer_amount, 'DataRef': [16, offer_char ], 'SkinRef': [0, 0 ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(offer_char)] = self.player.brawlers_powerpoints[str(offer_char)] + offer_amount
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            elif offer_id in [0, 6]:
                self.player.delivery_items['Type'] = 10
                self.player.delivery_items['Count'] = offer_amount


            elif offer_id == 14:
                self.player.delivery_items['Type'] = 12
                self.player.delivery_items['Count'] = offer_amount


            elif offer_id == 10:
                self.player.delivery_items['Type'] = 11
                self.player.delivery_items['Count'] = offer_amount

            else:
                print(f"Unsupported offer ID: {offer_id}")

        if not offer_claim_b and offer_count >= 2:

            if offer_id2 == 1:
                item = {'Amount': offer_amount2, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + offer_amount2
                db.update_player_account(self.player.token, 'Resources', self.player.resources)


            elif offer_id2 == 16:
                item = {'Amount': offer_amount2, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':8 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.gems = self.player.gems + offer_amount2
                db.update_player_account(self.player.token, 'Gems', self.player.gems)

            elif offer_id2 == 9:
                item = {'Amount': offer_amount2, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':2 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.token_doubler = self.player.token_doubler + offer_amount2
                db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)

            elif offer_id2 == 3:
                item = {'Amount': offer_amount2, 'DataRef': [16, offer_char2 ], 'SkinRef': [0, 0 ], 'Value':1 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                if offer_char not in self.player.brawlers_unlocked:
                    self.player.brawlers_unlocked.append(offer_char2)
                    db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

            elif offer_id2 == 12:
                item = {'Amount': offer_amount2, 'DataRef': [16, self.brawler ], 'SkinRef': [0, 0 ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(self.brawler)] = self.player.brawlers_powerpoints[str(self.brawler)] + offer_amount2
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            elif offer_id2 == 4:
                item = {'Amount': offer_amount2, 'DataRef': [0, 0 ], 'SkinRef': [29, offer_skin2 ], 'Value':9 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                self.player.unlocked_skins.append(offer_skin2)
                db.update_player_account(self.player.token, 'UnlockedSkins', self.player.unlocked_skins)

            elif offer_id2 == 8:
                item = {'Amount': offer_amount2, 'DataRef': [29, offer_char2 ], 'SkinRef': [0, 0 ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(offer_char)] = self.player.brawlers_powerpoints[str(offer_char)] + offer_amount2
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            elif offer_id2 in [0, 6]:
                self.player.delivery_items['Type'] = 10
                self.player.delivery_items['Count'] = offer_amount2


            elif offer_id2 == 14:
                self.player.delivery_items['Type'] = 12
                self.player.delivery_items['Count'] = offer_amount2


            elif offer_id2 == 10:
                self.player.delivery_items['Type'] = 11
                self.player.delivery_items['Count'] = offer_amount2

            else:
                print(f"Unsupported offer ID: {offer_id}")

        if not offer_claim_b and offer_count >= 3:

            if offer_id3 == 1:
                item = {'Amount': offer_amount3, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':7 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + offer_amount3
                db.update_player_account(self.player.token, 'Resources', self.player.resources)


            elif offer_id3 == 16:
                item = {'Amount': offer_amount3, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':8 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.gems = self.player.gems + offer_amount3
                db.update_player_account(self.player.token, 'Gems', self.player.gems)

            elif offer_id3 == 9:
                item = {'Amount': offer_amount3, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':2 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.token_doubler = self.player.token_doubler + offer_amount3
                db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)

            elif offer_id3 == 3:
                item = {'Amount': offer_amount3, 'DataRef': [16, offer_char3 ], 'SkinRef': [0, 0 ], 'Value':1 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                if offer_char not in self.player.brawlers_unlocked:
                    self.player.brawlers_unlocked.append(offer_char3)
                    db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)

            elif offer_id3 == 12:
                item = {'Amount': offer_amount3, 'DataRef': [16, self.brawler ], 'SkinRef': [0, 0 ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(self.brawler)] = self.player.brawlers_powerpoints[str(self.brawler)] + offer_amount3
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            elif offer_id3 == 4:
                item = {'Amount': offer_amount3, 'DataRef': [0, 0 ], 'SkinRef': [29, offer_skin3 ], 'Value':9 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)
                self.player.unlocked_skins.append(offer_skin3)
                db.update_player_account(self.player.token, 'UnlockedSkins', self.player.unlocked_skins)

            elif offer_id3 == 8:
                item = {'Amount': offer_amount3, 'DataRef': [29, offer_char3 ], 'SkinRef': [0, 0 ], 'Value':6 }
                self.player.delivery_items['Type'] = 100
                self.player.delivery_items['Items'].append(item)

                self.player.brawlers_powerpoints[str(offer_char)] = self.player.brawlers_powerpoints[str(offer_char)] + offer_amount3
                db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            elif offer_id3 in [0, 6]:
                self.player.delivery_items['Type'] = 10
                self.player.delivery_items['Count'] = offer_amount3


            elif offer_id3 == 14:
                self.player.delivery_items['Type'] = 12
                self.player.delivery_items['Count'] = offer_amount3


            elif offer_id3 == 10:
                self.player.delivery_items['Type'] = 11
                self.player.delivery_items['Count'] = offer_amount3

            else:
                print(f"Unsupported offer ID: {offer_id}")

        if not offer_claim_b:
            if offer_claim != 898989:
                self.player.claimshop.append(offer_claim)
                db.update_player_account(self.player.token, 'ClaimShop', self.player.claimshop)

            if offer_resource == 0:
                self.player.gems = self.player.gems - offer_cost
                db.update_player_account(self.player.token, 'Gems', self.player.gems)

            elif offer_resource == 1:
                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] - offer_cost
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

            elif offer_resource == 3:
                self.player.resources[3]['Amount'] = self.player.resources[3]['Amount'] - offer_cost
                db.update_player_account(self.player.token, 'Resources', self.player.resources)

            self.player.db = db

            AvailableServerCommandMessage(self.client, self.player, 203, {}).send()



