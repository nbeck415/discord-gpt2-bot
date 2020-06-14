# Discord GPT-2 Bot

## Dependencies:
Tensorflow v. 1.15, Python 3.7.x or earlier, gpt_2_simple, Pytorch, NLTK, discord.py

## Setup
Using a Python 3.x version prior to 3.8, install Tensorflow 1.15 (later versions will not work with the gpt_2_simple model)
Install pytorch and discord.py. All can be done with pip install

Clone this repository. Ensure you have at least 1.2GB of space on the drive you're using, as the GPT-2 models and training data will be quite large. 

After you've created a bot account on Discord's developer portal, it will give you a token that you will paste into the bot.py file in lieu of "token goes here." Do not share your token with anyone, and especially do not share it on GitHub. 

Now you can run bot.py and the first runthrough will download the model and train on the reddit_comments.txt file. You can use your own file if desired, and I would recommend changing this BEFORE running bot.py if at all. Training will take around 20-40 minutes, but you only have to do it once.

After inviting the bot to your server, you can summon it using the &talk command, giving it a few words following the command to "think" about when formulating a response. The bot will also randomly respond to about 10% of messages.
