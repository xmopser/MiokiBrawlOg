from Core.Networking.Server import Server
from Protocol.Messages.Server.LobbyInfoMessage import LobbyInfoMessage
from Utils.Helpers import Helpers


def main():

    print(f"{Helpers.green}    ____                      __   _____ __                    / __ )_________ __      __/ /  / ___// /_____ ___________  / __  / ___/ __ `/ | /| / / /   \__ \/ __/ __ `/ ___/ ___/ / /_/ / /  / /_/ /| |/ |/ / /   ___/ / /_/ /_/ / /  (__  ) /_____/_/   \__,_/ |__/|__/_/   /____/\__/\__,_/_/  /____/                                                                ")

    Server("0.0.0.0", 8934).start()


if __name__ == '__main__':
    main()
