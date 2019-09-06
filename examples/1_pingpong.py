#!/usr/bin/env python3

###################################
# WHAT IS IN THIS EXAMPLE?
#
# This bot listens to two channels for a special text message. When
# it sees this message, it replies in the same channel with a response.
# This also shows sending and receiving unicode characters.
###################################

import asyncio
import logging
import os

import pykeybasebot.types.chat1 as chat1
from pykeybasebot import Bot

logging.basicConfig(level=logging.DEBUG)


class Handler:
    async def __call__(self, bot, event):
        if event.msg.content.type_name != chat1.MessageTypeStrings.TEXT.value:
            return
        if event.msg.content.text.body == "🌴ping🌴":
            channel = event.msg.channel
            await bot.chat.send(channel, "🍹PONG!🍹")


listen_options = {
    "filter-channels": [
        {"name": "nsmith9,nathunsmitty"},
        # {
        #     "name": "yourcompany.marketing",
        #     "topic_name": "lunchtalk",
        #     "members_type": "team",
        # },
    ]
}

bot = Bot(
    username="nsmith9", paperkey=os.environ["KEYBASE_PAPERKEY"], handler=Handler()
)
asyncio.run(bot.start(listen_options))
