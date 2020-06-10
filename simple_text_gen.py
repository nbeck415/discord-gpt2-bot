#Natalie Lunbeck
#This program creates a simple GPT2 Model and uses it to generate text

#modifying this version to work as a Discord bot

import torch
import gpt_2_simple as gpt2
import sys
import os

class SimpleTextGen:

    def __init__(self, source, num_words, prompt="DEFAULT"):
        #where the training data is stored
        self.source = source
        #length of output
        self.num_words = num_words
        #user input
        self.prompt = prompt
        if self.prompt == "DEFAULT":
            self.prompt = "The quick brown fox jumped over the lazy dog."
        files = os.listdir(os.getcwd())
        if "models" not in files:
            #first-time runthrough
            self.setupModel()
            print('Setup Complete')
        if "checkpoint" not in files:
            #story generator, give parameters if necessary
            self.trainGenerator()
            print('Training Complete')
        self.loadRun()
        print('Done')


    def setupModel(self, size="124M"):
        #create a gpt2 model based on dataset
        #first time runthrough
        gpt2.download_gpt2(model_name=size)

    def trainGenerator(self, num_words=200, variance=0.9):
        session = gpt2.start_tf_sess()
        gpt2.finetune(session, dataset=self.source, model_name='124M', steps=50, restore_from='fresh',run_name='run1',sample_every=200,save_every=500, print_every=10)

    def loadRun(self):
        session = gpt2.start_tf_sess()
        gpt2.load_gpt2(session, run_name='run1')
        gpt2.generate_to_file(session, include_prefix=False, truncate = ".", destination_path='bot_says.txt', length=self.num_words, temperature=0.9, prefix=self.prompt)


def main(gen_text):
    story = SimpleTextGen('reddit_comments.txt', 50, gen_text)

if __name__ == "__main__":
    if len sys.argv < 2:
        main("DEFAULT")
    main(sys.argv[1])
