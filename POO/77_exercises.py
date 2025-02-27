class FormatadorDeFrase:
    """
    A class for formatting phrases with various text transformations.
    """

    def __init__(self, userText):
        """
        Initializes the FormatadorDeFrase class with a given text.

        Args:
            userText (str): The text to be formatted.
        """
        self.userText = userText

    def uppercaseLetters(self):
        """
        Converts all letters in the text to uppercase and prints the result.
        """
        sentence = self.userText
        uppercase = sentence.upper()
        print(uppercase)

    def lowcaseLetters(self):
        """
        Converts all letters in the text to lowercase and prints the result.
        """
        sentence = self.userText
        lowcase = sentence.lower()
        print(lowcase)

    def capitalizeText(self):
        """
        Capitalizes the first letter of the text and prints the result.
        """
        sentence = self.userText
        capitalizetxt = sentence.capitalize()
        print(capitalizetxt)

    def formatTitle(self):
        """
        Converts the first letter of each word in the text to uppercase and prints the result.
        """
        sentence = self.userText
        splitSentence = sentence.split(" ")
        temp = []

        for i in splitSentence:
            capitalizeEachWord = i.capitalize()
            temp.append(capitalizeEachWord)
        joinllWords = " ".join(temp)
        print(joinllWords)

    def countVowels(self):
        sentence = self.userText
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        temp = []
        for v in sentence.lower():
            if v in vowels:
                temp.append(v)
                count += 1
        print(count)
        print(f"All vowels: {temp}")

    def countConsonant(self):
        sentence = self.userText
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        temp = []
        for v in sentence.lower():
            if v not in vowels:
                temp.append(v)
                count += 1
        print(count)
        print(f"All Consonants: {temp}")

    def countLetterA(self):
        sentence = self.userText
        count = 0
        for letter in sentence.lower():
            if letter == "a":
                count += 1
        print(count)


# Example usage
mySentence = "My name is Arthur"
myPrototype = FormatadorDeFrase(mySentence)
myPrototype.uppercaseLetters()
myPrototype.lowcaseLetters()
myPrototype.capitalizeText()
myPrototype.formatTitle()
myPrototype.countVowels()
myPrototype.countConsonant()
