import json
from Utils.Helpers import Helpers
from Utils.Fingerprint import Fingerprint
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards
from Files.CsvLogic.Emotes import Emotes

class Player:
    try:
        config = open('config.json', 'r')
        content = config.read()
    except FileNotFoundError:
        Helpers().create_config()
        config = open('config.json', 'r')
        content = config.read()

    settings = json.loads(content)

    skins_id = Skins().get_skins_id()
    brawlers_id = Characters().get_brawlers_id()

    ID = 0
    token = None

    trophies = settings['Trophies']
    tickets = settings['Tickets']
    gems = settings['Gems']
    resources = [{'ID': 1, 'Amount': settings['BrawlBoxTokens']}, {'ID': 8, 'Amount': settings['Gold']}, {'ID': 9, 'Amount': settings['BigBoxTokens']}, {'ID': 10, 'Amount': settings['StarPoints']}]
    high_trophies = 0
    tokeni = 0
    spa = 0
    trp = 0
    tkn = 0
    trophy_reward = 300
    exp_points = settings['ExperiencePoints']
    tutorial = settings['tutorial']
    profile_icon = 0
    name_color = 0
    selected_brawler = 0
    region = settings['Region']
    content_creator = "Miokiru Brawl"
    name_set = False
    name = 'Guest'
    map_id = 0
    use_gadget = True
    starpower = 76
    gadget = 255
    home_brawler = 0
    home_skin = 0
    leaderboard_type = 0
    leaderboard_is_global = False
    bp_activated = True
    token_doubler = 0
    welcome_msg_viewed = False
    theme_id = settings['ThemeID']
    content_creator_codes = settings['ContentCreatorCodes']
    maintenance = False
    maintenance_time  = settings['MaintenanceOverTimer']
    patch = settings['Patch']
    patch_url = settings['PatchURL']
    patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")
    update_url = settings['UpdateURL']
    claimshop = []
    season = 0
    wins = 0
    day = 0
    dailyskins = [0, 0, 0, 0]
    version = settings['Version']
    versionname = settings['VersionHame']
    snapshot = settings['Snapshot']
    environment = settings['Environment']
    hosting = settings['Hosting']
    lobbymsg = settings['LobbyMsg']
    quest = [{'BrawlerID': 0, 'Goal': 3, 'Wins': 0, 'Reward': 100}, {'BrawlerID': 0, 'Goal': 3, 'Wins': 0, 'Reward': 100}, {'BrawlerID': 0, 'Goal': 5, 'Wins': 0, 'Reward': 250}, {'BrawlerID': 0, 'Goal': 8, 'Wins': 0, 'Reward': 500}, {'BrawlerID': 0, 'Goal': 5, 'Wins': 0, 'Reward': 250}, {'BrawlerID': 0, 'Goal': 8, 'Wins': 0, 'Reward': 500}]
    brawlers_rare = [2, 6, 8, 10, 13, 22, 24]
    brawlers_superrare = [3, 4, 7, 9, 18, 19, 25, 34]
    brawlers_epic = [1, 15, 16, 20, 26, 27, 49, 43, 36, 45, 29]
    brawlers_megaepic = [11, 14, 17, 21, 31, 37, 30, 32, 42, 47]
    brawlers_legendary = [5, 12, 23, 28, 40]
    brawlers_chromatic = [35, 38, 41, 39, 44, 46, 48, 50]
    ban = False
    ban_reason = False
    account_type = "Player"
    test_state = True
    gems_remove = False
    creatorcodes_activated = []
    pvp_wins = 0
    sd_wins = 0

    delivery_items = {}
    box_rewards = {}

    db = None

    battle_tick = 0

    emotes_id = []

    unlocked_skins = []

    selected_skins = {}
    for id in brawlers_id:
        selected_skins.update({f"{id}": 0})

    brawlers_unlocked = [0]

    brawlers_card_id = []
    for x in brawlers_unlocked:
        brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))

    brawlers_spg = Cards().get_spg_id()

    def_trophies = 0
    def_high_trophies = 0
    
    brawlers_trophies = {}
    for x in brawlers_id:
        brawlers_trophies.update({f'{x}': def_trophies})

    brawlers_high_trophies = {}
    for x in brawlers_id:
        brawlers_high_trophies.update({f'{x}': def_high_trophies})

    def_level = 0

    brawlers_level = {}
    for x in brawlers_id:
        brawlers_level.update({f'{x}': def_level})

    def_pp = 0

    brawlers_powerpoints = {}
    for x in brawlers_id:
        brawlers_powerpoints.update({f'{x}': def_pp})


    club_id = 0
    club_role = 0

    message_tick = 0

    clients = {}


    def __init__(self, device):
        self.device = device


