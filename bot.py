import discord
import random
import simple_text_gen

generator = simple_text_gen.SimpleTextGen("reddit_comments.txt", 50)

client = discord.Client()  # starts the discord client.

converse = False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    #10% chance of responding
    chance = random.randrange(10)
    global converse
    #responds by chance or by summon
    if not converse and (chance == 3 or message.content.startswith("&talk")):
        userinput = message.content.replace("&talk ","")
        generator.talk(userinput)
        generator.fileFormat()
        response = open("bot_says.txt","r").read()
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        await message.channel.send(response)
    if message.content.startswith("&convo"):
        converse = True
        return
    if converse and message.author != client.user:
        if message.content.startswith("&stop"):
            converse = False
            return
        generator.talk(message.content)
        generator.fileFormat()
        response = open("bot_says.txt","r").read()
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        await message.channel.send(response)

client.run(token)
