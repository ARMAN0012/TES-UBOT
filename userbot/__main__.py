# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module
from pytgcalls import idle
from telethon.tl.functions.channels import InviteToChannelRequest
from userbot import BOTLOG_CHATID, BOTLOG_MSG, BOT_USERNAME, BOT_VER, LOGS, bot, karblacklist, call_py
from userbot.modules import ALL_MODULES
from userbot.utils.utils import autobot, autopilot 
from userbot.utils.tools import hadeh_ajg


try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    call_py.start()
    user = bot.get_me()
    if user.id in karblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BANYAK TINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK KAU.\nCredits: @PakkPoll"
        )
        sys.exit(1)
        except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)
    
for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/obrolansuar")
LOGS.info(
    f"karman-userbot ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


async def ram_ubot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"{BOTLOG_MSG}",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(ram_ubot_on())
bot.loop.run_until_complete(autobot())
idle()
bot.loop.run_until_complete(hadeh_ajg())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
