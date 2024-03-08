from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from . import *

@bot.on(jungli_cmd(pattern="history ?(.*)"))
@bot.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(junglievent):
    if junglievent.fwd_from:
        return 
    if not junglievent.reply_to_msg_id:
       await eod(junglievent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await junglievent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eod(junglievent, "Need actual users. Not Bots")
       return
    await eor(junglievent, "Checking...")
    async with junglievent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await eod(junglievent, "Please unblock @Sangmatainfo_bot")
              return
          if response1.text.startswith("No records found"):
             await eor(junglievent, "User never changed his Username...")
          else: 
             await junglievent.delete()
             await junglievent.client.send_message(junglievent.chat_id, response2.message)


@bot.on(jungli_cmd(pattern="unh ?(.*)"))
@bot.on(sudo_cmd(pattern="unh ?(.*)", allow_sudo=True))
async def _(junglievent):
    if junglievent.fwd_from:
        return 
    if not junglievent.reply_to_msg_id:
       await eod(junglievent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await junglievent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eod(junglievent, "Need actual users. Not Bots")
       return
    await eor(junglievent, "Checking...")
    async with junglievent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await eod(junglievent, "Please unblock @Sangmatainfo_bot")
              return
          if response1.text.startswith("No records found"):
             await eor(junglievent, "User never changed his Username...")
          else: 
             await junglievent.delete()
             await junglievent.client.send_message(junglievent.chat_id, response3.message)


CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
  "unh", "<reply to user>", "Fetches the Username History of replied users."
).add_info(
  "Telegram Name History"
).add_warning(
  "✅ Harmless Module."
).add()
