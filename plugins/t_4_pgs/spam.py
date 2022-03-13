from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter

@bot.on_message(filters.command('spam', COMMAND_HAND_LER) & filters.f_onw_filter)
