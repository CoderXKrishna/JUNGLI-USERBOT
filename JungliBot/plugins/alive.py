# credit goes to @itsz_radha_3030 and @itsz_krish_babess

from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *


#-------------------------------------------------------------------------------
DEFAULTER = Config.YOUR_NAME

@bot.on(jungli_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(jungli):
    if jungli.fwd_from:
        return
    await jungli.get_chat()
    await jungli.delete()
    await bot.send_file(jungli.chat_id, jungli_PIC, caption=jungli_CAPTION)
    await jungli.delete()

jungli_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/0b9d7bd278272147f1f3c.jpg"
jungli_CAPTION = "🔥 Jυɳɠʅι Aɾαɳƙ Bσƚ 🔥\n\n"
jungli_CAPTION += (
    f"                __↼𝙼𝙰𝚂𝚃𝙴𝚁⇀__\n  **『 {jungli_mention} 』**\n\n"
)
jungli_CAPTION += f"╔═══════════════╗\n"
jungli_CAPTION += f"╠•➳➠ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽:` `{tel_ver}` \n"
jungli_CAPTION += f"╠•➳➠ `𝚅𝙴𝚁𝚂𝙸𝙾𝙽:` `{jungli_ver}`\n"
jungli_CAPTION += f"╠•➳➠ `𝙶𝚁𝙾𝚄𝙿:`  [𝙹𝙾𝙸𝙽](t.me/Carding_Chronicle)\n"
jungli_CAPTION += f"╠•➳➠ `𝙲𝙷𝙰𝙽𝙽𝙴𝙻:` [𝙹𝙾𝙸𝙽](t.me/Carding_Chronicle)\n"
jungli_CAPTION += f"╠•➳➠ `𝙲𝚁𝙴𝙰𝚃𝙾𝚁:` [⚡𝙿𝚁𝙾⚡](t.me/itsz_krish_babess)\n"
jungli_CAPTION += f"╚═══════════════╝\n\n"
jungli_CAPTION += " [✨𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙱𝙾𝚃✨](https://github.com/CoderXKrishna/JUNGLI-ARANK-BOT)"
                                            
#_______



@bot.on(jungli_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def up(jungli):
    if jungli.fwd_from:
        return
    await jungli.get_chat()
    await jungli.delete()
    await bot.send_file(jungli.chat_id, jungli_PIC, caption=jungli_caption)
    await jungli.delete()

jungli_caption = f"🔥 Jυɳɠʅι Aɾαɳƙ Bσƚ 🔥\n\n"
jungli_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"
jungli_caption += f"**{Config.ALIVE_MSG}**\n\n"
jungli_caption += f"≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n\n"                
jungli_caption += f"𖣘 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈 𝚂𝚈𝚂𝚃𝙴𝙼 𖣘\n\n"
jungli_caption += f"➾ `𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽` ➣ `{tel_ver}` \n"
jungli_caption += f"➾ `𝚂𝚄𝙳𝙾 𝙼𝙾𝙳𝙴:` ➣ `{is_sudo}`\n"
jungli_caption += f"➾ 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_CHANNEL)\n"
jungli_caption += f"➾ 𝙼𝚈 𝙶𝚁𝙾𝚄𝙿: ➣ [𝙹𝙾𝙸𝙽](t.me/Config.YOUR_GROUP)\n\n"
jungli_caption += f"[✨ 𝙳𝙴𝙿𝙻𝙾𝚈 𝚈𝙾𝚄𝚁 Jungli Bot ✨](https://github.com/CoderXKrishna/JUNGLI-ARANK-BOT)\n" 
                                     
                                 
                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Awake", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
