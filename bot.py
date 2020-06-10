import discord
import random
import simple_text_gen
#print(discord.__version__)  # check to make sure at least once you're on the right version!

#token = open("token.txt", "r").read()  # I've opted to just save my token to a text file.
generator = simple_text_gen.SimpleTextGen("reddit_comments.txt", 50)
token = myTokenHere
client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


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
