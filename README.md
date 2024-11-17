# MiokiBrawl Original

MiokiBrawl server from 2022.

## What's working ?
- Battles
  - Trophies in offline battles
- Home
  - Resource sets (instead of boxes)
  - Season resets
  - Gadgets and Star Powers
- Shop
  - Daily store update
  - Resource sets (instead of boxes)
  - Credits and other resources
  - Starr Road 
- Club
  - Join
  - Leave
  - Chat
  - Update settings

...and much more!

### Requirements:
- Python 3.7 or higher
- pymongo
- dnspython
- colorama

### MongoDB configuration
First you'll need to put your MongoDB connection string in `config.json`. If you don't know how to get it here's a quick tutorial: https://imgur.com/a/oXI34dA

### Running the server
In a terminal, type __`pip install -r requirements.txt`__ then __`python main.py`__

### Configuring the client app
To connect to your server, a **patched client** is required. 
Download the version of MiokiBrawl you need from the [telegram channel](https://t.me/miokibrawl) and change the IP in `libobjectmod.config.so`, if you want to use Mioki Brawl locally on your device, you can use "127.0.0.1" as the IP. If not, then you can use your device's IPv4 address. 

#### The APK was recently updated to support Android 13+ and Emulators.

### Credits
- [XMopsER](https://github.com/xmopser) - MiokiBrawl developer.
- [athemm](https://github.com/athemm) - for making the patcher.
- [PhoenixFire](https://github.com/PhoenixFire6934) - the creator of Classic Brawl
- [CrazorTheCat](https://github.com/CrazorTheCat) - Contributor and other versions creator
- [8-bitHacc](https://github.com/8-bitHacc) - Contributor
