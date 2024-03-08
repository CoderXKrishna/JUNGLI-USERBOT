import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from jungliBot import LOGS, bot, tbot
from jungliBot.config import Config
from jungliBot.utils import load_module
from jungliBot.version import jungli as jungliver
hl = Config.HANDLER
jungli_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/e594b8dfaea400858d01a.mp4"

# let's get the bot ready
async def jungli_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"jungli_DANAV_SESSION - {str(e)}")
        sys.exit()


# jungliBot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Jungli Arank Bot KO START KR RHE HAI DADA 🔰")
            bot.loop.run_until_complete(jungli_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 Jυɳɠʅι Aɾαɳƙ Bσƚ STARTUP COMPLETE 🔥 AB BASS PLUGINS DAALNA HE WAIT KRO 😂😂🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "jungliBot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# Extra Modules...
# extra_repo = Config.EXTRA_REPO or "https://github.com/CoderXKrishna/Extra"
# if Config.EXTRA == "True":
#     try:
#         os.system(f"git clone {extra_repo}")
#     except BaseException:
#         pass
#     LOGS.info("Installing Extra Plugins")
#     path = "jungliBot/plugins/*.py"
#     files = glob.glob(path)
#     for name in files:
#         with open(name) as ex:
#             path2 = Path(ex.name)
#             shortname = path2.stem
#             load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ YOUR BOT IS NOW READY BABE ⚡")
LOGS.info(
    "CONGRATULATIONS 🥳🥳🎊🎊 YOUR Jυɳɠʅι Aɾαɳƙ Bσƚ IS DEPLOYED 🎊 ... NOW TYPE .ping OR .alive TO CHECK OUR AMAZING BOT 🥳🔥 IF U HAVE ANY PROBLEM THEN JOIN @Carding_Chronicle"
)

# that's life...
async def jungli_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                jungli_PIC,
                caption=f"#START \n\nDeployed Jυɳɠʅι Aɾαɳƙ Bσƚ Successfully\n\n**Jυɳɠʅι Aɾαɳƙ Bσƚ - {jungliver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [Jυɳɠʅι Aɾαɳƙ Bσƚ Channel](t.me/Carding_Chronicle) for Updates & [Jυɳɠʅι Aɾαɳƙ Bσƚ Chat](t.me/walky_talky) for any query regarding Jυɳɠʅι Aɾαɳƙ Bσƚ",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join jungliBot Channel after deploying 🤐😅
    try:
         await bot(JoinChannelRequest("@Carding_Chronicle"))
         await bot(JoinChannelRequest("@walky_talky"))
         await bot(JoinChannelRequest("@jungli_FIGHTERS"))
    except BaseException:
        pass

# Why not come here and chat??
#    try:
#        await bot(JoinChannelRequest("@jungli_userbot"))
#    except BaseException:
#        pass


bot.loop.create_task(jungli_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# jungliBot
