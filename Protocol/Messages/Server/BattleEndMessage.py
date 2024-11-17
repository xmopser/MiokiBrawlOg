from ByteStream.Writer import Writer
from DataBase.MongoDB import MongoDB
import random
from Logic.Home.LogicGlobal import LogicGlobal

class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players, db: MongoDB):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players
        self.db = db

    def encode(self):
        self.writeVInt(self.type)
        self.writeVInt(self.result)
        print(self.type)
        print(self.result)
        if self.type == 0:
            if self.result == 0:
                trophies = 8
                trpp = 8
                tokens = 20
            elif self.result == 1:
                trophies = -9
                trpp = -9
                tokens = 10
            else:
                trophies = 0
                trpp = 0
                tokens = 15
        if self.type == 2:
            if True:
                trophies = int(11 - (self.result + 2 * (self.result // 1.5)))
                trpp = int(11 - (self.result + 2 * (self.result // 1.5)))
                tokens = 32
        LogicGlobal.battles += 1
        self.writeVInt(tokens)#токены
        self.writeVInt(trpp)#трофеи

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

        self.writeVInt(0)#аутсайдер
        self.writeVInt(48)
        self.writeVInt(-64)
        self.writeVInt(1)

        self.writeVInt(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']

            if self.type == 5:
                self.writeVInt(player) if self.team == 0 else self.writeVInt(2)
            else:
                self.writeVInt(2 if self.team != 0 else 1) if self.type == 2 else self.writeVInt(self.team if self.team != 1 else 2)

            # 5 - player,
            self.writeDataReference(16, self.brawler)if self.brawler != -1 else self.writeVInt(0)
            self.writeDataReference(29, self.skin)   if self.skin != -1 else self.writeVInt(0)

            self.writeVInt(99999)
            self.writeVInt(99999)
            self.writeVInt(10)

            self.writeBool(False)

            # sub_64DF74
            self.writeString(self.username)
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
            self.writeNullVInt()

                # Experience Array
        self.writeVInt(2) # Count
        self.writeVInt(0) # Normal Experience ID
        self.writeVInt(10) # Normal Experience Gained
        self.writeVInt(0) # Star Player Experience ID
        self.writeVInt(0) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVInt(0) # Count
        
        # Trophies and Experience Bars Array
        self.writeVInt(2) # Count
        self.writeVInt(1) # Trophies Bar Milestone ID
        self.writeVInt(self.player.brawlers_high_trophies[str(self.player.home_brawler)]) # Brawler Trophies Bar
        self.writeVInt(self.player.brawlers_high_trophies[str(self.player.home_brawler)]) # Brawler Trophies for Rank
        self.writeVInt(5) # Experience Bar Milestone ID
        self.writeVInt(self.player.exp_points) # Player Experience
        self.writeVInt(self.player.exp_points) # Player Experience for Level

        self.writeDataReference(28, 0)

        self.writeBool(False)

        for i in range(len(self.player.quest)):
            if 44 == self.player.quest[i]['BrawlerID']:
                self.player.quest[i]['BrawlerID'] = random.choice(sorted(set(self.player.brawlers_unlocked) - set({44})))
            if self.player.home_brawler == self.player.quest[i]['BrawlerID']:
                self.player.quest[i]['Wins'] = self.player.quest[i]['Wins'] + 1
            if self.player.quest[i]['Wins'] >= self.player.quest[i]['Goal']:
                tokens = tokens + self.player.quest[i]['Reward']
                self.player.quest[i]['Wins'] = 0
                self.player.quest[i]['BrawlerID'] = random.choice(sorted(set(self.player.brawlers_unlocked) - set({44})))
        
        self.player.trp = trophies 
        self.player.tkn = tokens
        self.player.spa = tokens // 5
        self.player.tokeni += tokens
        
        self.player.trophies += trophies 
        self.player.high_trophies += trophies
        self.player.brawlers_trophies[str(self.player.home_brawler)] += trophies
        self.player.brawlers_high_trophies[str(self.player.home_brawler)] += trophies
        self.db.update_player_account(self.player.token, 'Trophies',  self.player.trophies)
        self.player.resources[0]['Amount'] += tokens
        self.player.resources[3]['Amount'] += tokens // 5
        self.db.update_player_account(self.player.token, 'Quest', self.player.quest)
        self.db.update_player_account(self.player.token, 'Resources', self.player.resources)
        self.db.update_player_account(self.player.token, 'Wins', self.player.wins)
        self.db.update_player_account(self.player.token, 'Tokens', self.player.tokeni)
        self.db.update_player_account(self.player.token, 'HighestTrophies',  self.player.high_trophies)
        self.db.update_player_account(self.player.token, 'BrawlersTrophies',  self.player.brawlers_trophies)
        self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies',  self.player.brawlers_high_trophies)