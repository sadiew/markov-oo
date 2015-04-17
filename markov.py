import sys
from random import choice


class SimpleMarkovGenerator(object):

    def __init__(self, filenames):
       self.corpus = self.read_files(filenames)
       self.chains = self.make_chains(self.corpus)

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        
        corpus = ''
        for filename in filenames:
            file_content = open(filename).read()
            corpus += file_content
        return corpus 


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""
        chains = {}

        words = self.corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"

        return chains
        # your code here

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        output_text = " ".join(words)
        return output_text[0].upper + output_text[1:]

class TwitterableMarkovGenerator(SimpleMarkovGenerator):

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        punctuation ='!?%.]^_|}'
        key = choice(chains.keys())
        twitter_string = key[0][0].upper() + key[0][1:] + " " + key[1]
        
        while key in chains:
            word = choice(chains[key])
            twitter_string = twitter_string + " " + word 
            key = (key[1], word)

            if word[-1] in punctuation and 100 < len(twitter_string) <= 140:
                return twitter_string   
            
        return twitter_string 


    def ask_user(self): 
        print self.make_text(self.chains)
        reply = raw_input("Would you like to create another tweet? Y/N \n").upper()

        while reply == 'Y': 
            print self.make_text(self.chains)
            reply = raw_input("Would you like to create another tweet? Y/N \n").upper()

if __name__ == "__main__":

    filenames = sys.argv[1:]
    # simple_markov = SimpleMarkovGenerator(filenames)
    twitter_markov = TwitterableMarkovGenerator(filenames)
    
    # print twitter_markov.make_text(twitter_markov.chains)
    # reply = raw_input("Would you like to create another tweet? Y/N \n").upper()

    # while reply == 'Y': 
    #     print twitter_markov.make_text(twitter_markov.chains)
    #     reply = raw_input("Would you like to create another tweet? Y/N \n").upper()

    twitter_markov.ask_user()