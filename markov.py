from sys import argv
from secrets import choice
from string import punctuation
from locale import getencoding


class SimpleMarkovGenerator():

    def __init__(self, filenames):
        self.corpus = self.read_files(filenames)
        self.chains = self.make_chains()

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        corpus = ''
        for filename in filenames:
            # Replace 'strict' with 'ignore' if there are too many errors
            corpus += open(file=filename, encoding=getencoding, errors='strict').read()
        return corpus

    def make_chains(self):
        """Takes input text as string; stores chains."""

        chains = {}
        words = self.corpus.split()

        for i in range(len(words) - 2):
            chains.setdefault((words[i], words[i + 1]), []).append(words[i + 2])

        return chains

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
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
        while True:
            print(self.make_text(self.chains))

            if input("Would you like to create another tweet? Y/N \n").upper() == 'Y':
                break


if __name__ == "__main__":
    TwitterableMarkovGenerator(argv[1:]).ask_user()