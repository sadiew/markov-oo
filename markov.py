import sys
from random import choice


class SimpleMarkovGenerator(object):

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

        words = corpus.split()

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

        return " ".join(words)


if __name__ == "__main__":

    filenames = sys.argv[1:]
    simple_markov = SimpleMarkovGenerator()
    corpus = simple_markov.read_files(filenames) 
    chains = simple_markov.make_chains(corpus)
    
    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x
    for i in range(5):
        print simple_markov.make_text(chains) 
    

# simple_markov = SimpleMarkovGenerator()
# corpus = simple_markov.read_files(['green-eggs.txt', 'sadie-pam.txt'])
# chains = simple_markov.make_chains(corpus)
# simple_markov.make_text(chains)