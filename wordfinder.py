from random import choice


class WordFinder:
    """
    Word Finder: finds random words from a list of words read from a file.

    >>> wf = WordFinder('words.txt')
    235886 words read

    """

    def __init__(self, path):
        """Setup a path to a words file, initialize an empty words list and read the file"""
        self.path = path
        self.words = []
        self.read_file()

    def read_file(self):
        """Read the contents of the file and stores the result in a words list"""
        file = open(self.path, 'r')

        for word in file:
            self.words.append(word.strip())

        print(f'{len(self.words)} words read')

    def random(self):
        """Returns a random word from the list of words"""
        return choice(self.words)
