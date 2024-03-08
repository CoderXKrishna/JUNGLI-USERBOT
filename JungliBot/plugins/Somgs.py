# credits - shinchan

from . import *


@bot.on(jungli_cmd(pattern="song ?(.*)"))
@bot.on(sudo_cmd(pattern="song ?(.*)", allow_sudo=True))
async def _(event):
    jungli_ = event.text[4:]
    if jungli_ == "":
        return await eor(event, "Give a song name to search")
    jungli = await eor(event, f"Searching song `{jungli_}`")
    somg = await event.client.inline_query("Lybot", f"{(deEmojify(jungli_))}")
    if somg:
        fak = await somg[0].click(Config.LOGGER_ID)
        if fak:
            await bot.send_file(
                event.chat_id,
                file=fak,
                caption=f"**Song by :** {jungli_mention}",
            )
        await jungli.delete()
        await fak.delete()
    else:
        await jungli.edit("**ERROR 404 :** __NOT FOUND__")


CmdHelp("somgs").add_command(
    "so", "<song name>", "Search the given song and uploads to current chat.", "so into your arms"
).add_info(
    "Fastest Song Module."
).add_warning(
    "✅ Harmless Module."
).add()
