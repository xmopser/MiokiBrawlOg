import random

class LogicBoxData:

    def randomize(self, type):
        self.box_rewards = { 'Rewards': [] }

        if (type == 10):
            self.player.resources[0]['Amount'] = self.player.resources[0]['Amount'] - 100
            self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

            gold_reward = {'Amount': 25, 'DataRef': [0, 0], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 7}
            self.box_rewards['Rewards'].append(gold_reward)
            self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + 25
            self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)

            brawlers_pp = []
            for brawler in self.player.brawlers_unlocked:
                if (self.player.brawlers_level[str(brawler)] < 8):
                    brawlers_pp.append(brawler)
            brawler_pp = []
            brawler_pp = random.choice(sorted(set(brawlers_pp)))
            pp_reward = {'Amount': 100, 'DataRef': [16, brawler_pp], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 6}
            self.box_rewards['Rewards'].append(pp_reward)
            self.player.brawlers_powerpoints[str(brawler_pp)] = self.player.brawlers_powerpoints[ str(brawler_pp)] + 100
            self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)

            item = {'Amount': 5, 'DataRef': [0, 0], 'SkinRef': [0, 0 ], 'Value':8 }
            self.box_rewards['Type'] = 100
            self.box_rewards['Rewards'].append(item)
            self.player.gems = self.player.gems + 5
            self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)


            if (random.randint(0,100) < 30):
                bonus = random.choice([2, 8])
                if (bonus == 8):
                    bonus_value = random.randint(5, 10)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                else:
                    bonus_value = random.randint(20, 50)
                    self.player.token_doubler = self.player.token_doubler + bonus_value
                    self.player.db.update_player_account(self.player.token, 'TokenDoubler', self.player.token_doubler)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': bonus}
                self.box_rewards['Rewards'].append(bonus_reward)



        elif (type == 12):
            brawlers_id = []
            for i in range(24):
                brawlers_id.append(i)
            brawlers_id.append(31)
            brawlers_id.append(26)
            brawlers_id.append(27)
            brawlers_id.append(47)
            brawlers_id.append(45)
            print(brawlers_id)
            locked_brawlers = sorted(set(brawlers_id) - set(self.player.brawlers_unlocked))
            print(locked_brawlers)
            brawlers_pp = []
            for brawler in self.player.brawlers_unlocked:
                if (self.player.brawlers_level[str(brawler)] < 8):
                    brawlers_pp.append(brawler)
            if (random.randint(0,100) < 100):
                gold_value = random.randint(50, 100)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                pp_value = random.randint(25, 55)
                for i in range(3):
                    pp_value = pp_value + random.randint(5, 15)
                    rewarded = []
                    if sorted(set(brawlers_pp) - set(rewarded)) != []:
                        brawler_pp = random.choice(sorted(set(brawlers_pp) - set(rewarded)))
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler_pp], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 6}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler_pp)] = self.player.brawlers_powerpoints[ str(brawler_pp)] + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler_pp)

            if (random.randint(0,100) < 6):
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 1}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if brawler not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(brawler)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
            if (random.randint(0,100) < 101):
                if (True):
                    bonus_value = random.randint(5, 12)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 8}
                self.box_rewards['Rewards'].append(bonus_reward)


        elif (type == 11):
            brawlers_id = []
            for i in range(24):
                brawlers_id.append(i)
            brawlers_id.append(31)
            brawlers_id.append(26)
            brawlers_id.append(27)
            brawlers_id.append(47)
            brawlers_id.append(45)
            print(brawlers_id)
            brawlers_pp = []
            locked_brawlers = sorted(set(brawlers_id) - set(self.player.brawlers_unlocked))
            print(locked_brawlers)
            for brawler in self.player.brawlers_unlocked:
                if (self.player.brawlers_level[str(brawler)] < 8):
                    brawlers_pp.append(brawler)
            if (random.randint(0,100) < 100):
                gold_value = random.randint(50, 300)
                gold_reward = {'Amount': gold_value, 'DataRef': [0, 0], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 7}
                self.box_rewards['Rewards'].append(gold_reward)

                self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + gold_value
                self.player.db.update_player_account(self.player.token, 'Resources', self.player.resources)
                rewarded = []
                pp_value = random.randint(50, 100)
                for i in range(5):
                    pp_value = pp_value + random.randint(5, 10)
                    if sorted(set(brawlers_pp) - set(rewarded)) != []:
                        brawler_pp = random.choice(sorted(set(brawlers_pp) - set(rewarded)))
                        pp_reward = {'Amount': pp_value, 'DataRef': [16, brawler_pp], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 6}
                        self.box_rewards['Rewards'].append(pp_reward)
                        self.player.brawlers_powerpoints[str(brawler_pp)] = self.player.brawlers_powerpoints[ str(brawler_pp)] + pp_value
                        self.player.db.update_player_account(self.player.token, 'BrawlersPowerPoints', self.player.brawlers_powerpoints)
                        rewarded.append(brawler_pp)

            if (random.randint(0,100) < 6):
                if (locked_brawlers):
                    brawler = random.choice(locked_brawlers)
                    brawler_reward = {'Amount': 1, 'DataRef': [16, brawler], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 1}
                    self.box_rewards['Rewards'].append(brawler_reward)
                    if brawler not in self.player.brawlers_unlocked:
                        self.player.brawlers_unlocked.append(brawler)
                        self.player.db.update_player_account(self.player.token, 'UnlockedBrawlers', self.player.brawlers_unlocked)
            if (random.randint(0,100) < 101):
                if (True):
                    bonus_value = random.randint(5, 12)
                    self.player.gems = self.player.gems + bonus_value
                    self.player.db.update_player_account(self.player.token, 'Gems', self.player.gems)
                bonus_reward = {'Amount': bonus_value, 'DataRef': [0, 0], 'Skin': [0, 0], 'Pin': [0, 0], 'Star': [0, 0], 'Value': 8}
                self.box_rewards['Rewards'].append(bonus_reward)



        return self.box_rewards


