import json
import requests
import colorama
import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import asyncio
import time
import os
from colorama import Fore, init, Style
init(convert=True)

ERROR = "[\x1b[31m-\x1b[39m]"
SUCCESS = "[\x1b[32m+\x1b[39m]"
INPUT = "[\x1b[33m?\x1b[39m]"
INFO = "[\x1b[35m>\x1b[39m]"
RED = "\033[1;31;40m"
GREEN = "\033[1;32;40m"
BLUE = "\033[1;36;40m"
WHITE = "\033[1;37;40m"
LIGHTMAGENTA = "\033[1;35;40m"
YELLOW = Fore.LIGHTYELLOW_EX

webhook_url_1 = 'WEBHOOK LINK FOR 1ST'
webhook_url_2 = 'WEBHOOK LINK FOR 2ND'

async def send_webhook():

    global webhook_url_1
    global webhook_url_2
    
    async with aiohttp.ClientSession() as session:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        os.system('cls')
        
        
        for x in open("usernames.txt", "r").readlines():
            print("")
            webhook = Webhook.from_url(webhook_url_1, adapter=AsyncWebhookAdapter(session))
            webhook1 = Webhook.from_url(webhook_url_2, adapter=AsyncWebhookAdapter(session))
            embed=discord.Embed(url="https://twitter.com/{}".format(x), title="@{}".format(x.strip("\r\n")), description="𝙇𝙤𝙤𝙠𝙞𝙣𝙜 𝙛𝙤𝙧 𝙤𝙛𝙛𝙚𝙧𝙨!", color=1127128)
            embed.set_author(name="BOT NAME - Example: Twitter Claims")
            embed.set_footer(text="Obstacles#1555 - too#1001 * {}".format(current_time))
            embed.set_thumbnail(url='https://media.giphy.com/media/MNa0HKdhc3SGQ/giphy.gif')
            await webhook.send(embed=embed, username='Pure')
            time.sleep(2)
            print("@{} has been claimed!".format(x))
            time.sleep(5)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_webhook())