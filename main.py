#bot.py
import hikari
import discord
import random
import os 


bot = hikari.GatewayBot(token='UR_TOKEN_HERE')


@bot.listen()
async def ben(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return

    random_responses = [
        'yes',
        'no',
        'hahaha',
        'ughhh',
       
    ]

    if event.content.startswith("ben"):
        response = random.choice(random_responses)
        await event.message.respond(response)

bot.run()
