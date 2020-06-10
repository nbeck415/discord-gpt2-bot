import discord
import random
import simple_text_gen

generator = simple_text_gen.SimpleTextGen("reddit_comments.txt", 50)
token = myTokenHere
client = discord.Client()  # starts the discord client.


@client.event 
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    #10% chance of responding
    chance = random.randrange(10)
    #responds by chance or by summon
    if chance == 3 or message.content.startswith("&talk"):
        userinput = message.content.replace("&talk","")
        generator.talk(userinput)
        response = open("bot_says.txt","r").read()
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        await client.send_message(message.channel, response)

client.run(token)  # recall my token was saved!
