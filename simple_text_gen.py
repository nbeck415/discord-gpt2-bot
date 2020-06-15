#Natalie Lunbeck
#This program creates a simple GPT2 Model and uses it to generate text

#modifying this version to work as a Discord bot

import torch
import gpt_2_simple as gpt2
import sys
import os
import tensorflow as tf
import nltk.data

class SimpleTextGen:

    def __init__(self, source, num_words, prompt="DEFAULT", temp=0.7):
        #separating blocks into sentence tokens
        nltk.download('punkt')
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        #where the training data is stored
        self.source = source
        #deviation from original dataset
        self.temperature = temp
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
        tf.reset_default_graph()
        self.session = gpt2.start_tf_sess()
        gpt2.load_gpt2(self.session, run_name='run1')
        print('Done')


    def setupModel(self, size="124M"):
        #create a gpt2 model based on dataset
        #first time runthrough
        gpt2.download_gpt2(model_name=size)

    def trainGenerator(self, num_steps=50):
        #train the generator on a file and use our preset parameters
        session = gpt2.start_tf_sess()
        gpt2.finetune(session, dataset=self.source, model_name='124M', steps=num_steps, restore_from='fresh', run_name='run1', sample_every=200, save_every=500, print_every=10)

    def loadRun(self):
        #load an existing trained run and generate from it
        session = gpt2.start_tf_sess()
        gpt2.load_gpt2(session, run_name='run1')
        gpt2.generate_to_file(session, include_prefix=False, truncate = ".", destination_path='bot_says.txt', length=self.num_words, temperature=self.temperature, prefix=self.prompt)

    def talk(self, prompt, temp=0.7, words=50):
        #respond to given prompt from loaded run with specified parameters
        session = self.session
        gpt2.generate_to_file(session, include_prefix=False, destination_path='bot_says.txt', length=words, temperature=temp, prefix=prompt)

    def fileFormat(self):
        #give full sentence
        text = open('bot_says.txt').read()
        text.replace('"','').replace('"','').replace("“",'').replace("”",'').replace("\"","")
        split = self.tokenizer.tokenize(text)
        edited = open('bot_says.txt', 'w')
        ind = 1
        if len(split) < 2:
            ind = 0
        edited.write(split[ind])
        edited.close()


def main(gen_text):
    story = SimpleTextGen('reddit_comments.txt', 50, gen_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        main("DEFAULT")
    main(sys.argv[1])
