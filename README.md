<div align="center">
<img src="https://graph.org/file/574a46c1e4372fa86999d.jpg" alt="JPG" width="500" height="500"/>
</p>
<a href="https://github.com/DX-MODS/BIXBY-BOT/stargazers"><img src="https://img.shields.io/github/stars/DX-MODS/BIXBY-BOT?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars" /></a>
<a href="https://github.com/DX-MODS/BIXBY-BOT/network/members"> <img src="https://img.shields.io/github/forks/DX-MODS/BIXBY-BOT?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/DX-MODS/BIXBY-BOT/blob/master/LICENSE"> <img src="https://img.shields.io/badge/License- GPL 2.0 license -blueviolet?style=for-the-badge" alt="License" /> </a>
<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Written%20in-Python-skyblue?style=for-the-badge&logo=python" alt="Python" /> </a>
<a href="https://pypi.org/project/Pyrogram/"> <img src="https://img.shields.io/pypi/v/pyrogram?color=white&label=pyrogram&logo=python&logoColor=blue&style=for-the-badge" /></a>
<a href="https://github.com/DX-MODS/BIXBY-BOT"> <img src="https://img.shields.io/github/repo-size/DX-MODS/BIXBY-BOT?color=skyblue&logo=github&logoColor=blue&style=for-the-badge" /></a>
<a href="https://github.com/DX-MODS/BIXBY-BOT/commits/DX-MODS"> <img src="https://img.shields.io/github/last-commit/DX-MODS/BIXBY-BOT?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>

<div align="left">

## Features

- [x] Auto Filter
- [x] Manual Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB Search
- [x] Inline Search
- [x] Random Pics
- [x] Ids And User Info
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel
- [x] Spelling Check Feature
- [x] Custom File Caption
- [x] Group Broadcast 
- [x] AutoFilter Auto Delete
- [x] Junk Group & Users Clearing On Database
- [x] Global Filter
- [x] Url Shortner In Autofilter
- [x] Custom Button Lock
- [x] Image Editor & Background Remover
- [x] Telegraph, Pin, Json, Password Generator
- [x] Ban, Mute, Unmute, Etc... Group Manager
- [x] Custom Welcome Message
- [x] Advanced Admin Panel
- [x] Photo Changing In All Buttons
- [x] Custom Start Message
- [x] Custom Button Alter Message
- [x] Advanced Status (Disk, Cpu, Ram, Uptime..) In Image Type
- [x] Logo Maker anime and normal logo
### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `Support Chat` : Username of a Support Group / ADMIN. ( Should be username without @ and not ID
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used seperated by space )
* `USE_CAPTION_FILTER` : Whether bot should use captions to improve search results. (True False)
* `CUSTOM_FILE_CAPTION` : A custom file caption for your files. formatable with , file_name, file_caption, file_size, Read Readme.md for better understanding
* `CACHE_TIME` : The maximum amount of time in seconds that the result of the inline query may be cached on the server
* `IMDB` : Imdb, the view of information when making True/False
* `SINGLE_BUTTON` : choose b/w single or double buttons 
* `P_TTI_SHOW_OFF` : Customize Result Buttons to Callback or Url by (True = url / False = callback)

### Deploy
<details><summary>Deploy To Koyeb</summary>
<p>
<br>
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/DX-MODS&env[BOT_TOKEN]&env[API_ID]&env[API_HASH]&env[CHANNELS]&env[ADMINS]&env[PICS]&env[LOG_CHANNEL]&env[AUTH_CHANNEL]&env[MAX_RIST_BTNS]=10&env[CUSTOM_FILE_CAPTION]&env[DATABASE_URI]&env[DATABASE_NAME]=MknBotz&env[COLLECTION_NAME]=Telegram_files&env[SUPPORT_CHAT]&env[IMDB]=True&env[PM_IMDB]=True&env[IMDB_TEMPLATE]&env[IMDB_DELET_TIME]=900&env[SINGLE_BUTTON]=True&env[START_MESSAGE]&env[FORCE_SUB_TEXT]&env[AUTH_GROUPS]&env[WELCOM_PIC]&env[WELCOM_TEXT]&env[BUTTON_LOCK_TEXT]&env[PMFILTER]=True&env[G_FILTER]=True&env[BUTTON_LOCK]=True&env[RemoveBG_API]&env[P_TTI_SHOW_OFF]=True&run_command=python%20bot.py&branch=main&name=bixby-bot)">
  <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To Railway</summary>
<p>
<br>
<a href="https://railway.app/new/template/Qe0zMt">
  <img src="https://railway.app/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://heroku.com/deploy?template=https://github.com/DX-MODS/BIXBY-BOT">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>




## Commands
```
start - check bot alive
ping - pong
settings - get settings 
logs - to get the rescent errors
stats - to get status of files in db.
filter - add manual filters
filters - view filters
connect - connect to PM.
disconnect - disconnect from PM
del - delete a filter
delall - delete all filters
deleteall - delete all index(autofilter)
delete - delete a specific file from index.
info - get user info
id - get tg ids.
imdb - fetch info from imdb.
users - to get list of my users and ids.
chats - to get list of the my chats and ids 
index  - to add files from a channel
leave  - to leave from a chat.
disable  -  do disable a chat.
enable - re-enable chat.
ban_user  - to ban a user.
unban_user  - to unban a user.
channel - to get list of total connected channels
broadcast - to broadcast a message to all Eva Maria users
```

## TELAGRAM SUPPORT 

* [![DX-MODS](https://img.shields.io/static/v1?label=DX&message=MODS&color=critical)](https://t.me/DX_MODS1)

## Disclaimer
[![GNU Affero General Public License 2.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under [GNU AGPL 2.0.](https://github.com/DX-MODS/BIXBY-BOT/blob/master/LICENSE)
Don't copy the codes and re distribute without my license and credits is strictly prohibited as per the MIT license provided here

