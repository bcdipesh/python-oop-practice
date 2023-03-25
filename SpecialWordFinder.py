from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """
    Inherits WordFinder and overrides read_file() method from WordFinder to filter invalid words
    """

    def __init__(self, path):
        """Initialize the class with a path to words file"""
        super().__init__(path)

    def read_file(self):
        """Read the contents of the file and stores the result in a words list. Ignores empty white space strings and strings that starts with #"""
        file = open(self.path, 'r')

        for word in file:
            word = word.strip()
            if not word.startswith("#") and len(word) > 0:
                self.words.append(word)

        print(f'{len(self.words)} words read')
