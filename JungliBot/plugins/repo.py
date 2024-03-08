import random
import re
import time

import requests
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from . import *


@bot.on(admin_cmd(pattern=f"repo", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo", allow_sudo=True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "[𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴](https://github.com/CoderXKrishna/JUNGLI-ARANK-BOT) 𝚃𝙾 𝙾𝙿𝙴𝙽 𝚃𝙷𝙸𝚂 \n🔥**𝙻𝙸𝚃 𝙰𝙵!!**🔥 Jυɳɠʅι Aɾαɳƙ Bσƚ.\n\n[👑 𝐉𝐮𝐧𝐠𝐥𝐢 𝐔𝐬𝐞𝐫𝐁𝐨𝐭 👑](t.ME/jungli_FIGHTERS)")

