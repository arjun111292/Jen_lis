from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter

@Client.on_message(filters.command('spam', COMMAND_HAND_LER) & filters.f_onw_filter)
async def spam (cli, m):
  time = 0
  count = 100
  cunt = 0
  while True:
    cunt += 1
    await m.reply_text(f"spam {cunt}")
    time += 1
    if time >= count:
      break
