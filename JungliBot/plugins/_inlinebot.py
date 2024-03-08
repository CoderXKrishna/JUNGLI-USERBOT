from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from JungliBot import *
from JungliBot.utils.cmds import *
from JungliBot_config import Config

Jungli_help_pic = Config.ALIVE_PIC
Jungli_row = Config.BUTTONS_IN_HELP
Jungli_emoji = Config.EMOJI_IN_HELP
# thats how a lazy guy imports
# JungliBot

def button(page, modules):
    Row = REBEL_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{REBEL_emoji} " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"◀️ ᏰᎯᏣᏦ {Jungli_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"•{Jungli_emoji} ❌ {Jungli_emoji}•", data="close"
            ),
            custom.Button.inline(
               f"{Jungli_emoji} ᏁᏋﾒᎿ ▶️", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in JungliBot channel to get this module work...

    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@Carding_Chronicle":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**Running JungliBot**[⚡🔥]({Jungli_help_pic})\n\n__Number of plugins installed__ :`{len(CMD_HELP)}`\n**page:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=True,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text=='':
            result = builder.article(
                "@Carding_Chronicle",
                text=f"""**Hey![🤗]({Jungli_help_pic}) This is [JungliBot.](https://t.me/Carding_Chronicle)\nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/Carding_Chronicle"),
                        custom.Button.url(
                            "⚡ GROUP ⚡", "https://t.me/Carding_Chronicle"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "🔰 REPO 🔰", "https://github.com/CoderXKrishna/JUNGLI-USERBOT"),
                        custom.Button.url
                    (
                            "🔰 TUTORIAL 🔰", "https://t.me/Carding_Chronicle"
                    )
                    ],
                ],
                link_preview=True,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN JungliBot AND USE. © JungliBot ™",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**JungliBot[⚡🔥]({Jungli_help_pic})[.](https://t.me/Carding_Chronicle) __Working...__\n\n**Number of modules installed :** `{len(CMD_HELP)}`\n**page:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=True,
        )
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_REBEL(event,
              f"⚜️JungliBot Menu Provider Is now Closed[⚜️]({JungliBot_help_pic})\n\n         **[© JungliBot ™](t.me/Carding_Chronicle)**[⚡🔥]({Jungli_help_pic})", 5, link_preview=True
            )
        else:
            JungliBot_alert = "HELLO THERE. PLEASE MAKE YOUR OWN JungliBot AND USE. © JungliBot ™"
            await event.answer(Jungli_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN KANISHKA USERBOT AND USE. © JungliBot ™",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "🔷" + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"page({page})")])
        await event.edit(
            f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN KANISHKA USERBOT AND USE. © JungliBot ™",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**📗 File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:** `{command['usage']}`\n"
            result += f"**⌨️ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )
