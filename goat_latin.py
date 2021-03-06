"""
Problem:

    Goat latin, much like pig latin, is a simple way of encoding words to
    disguise their meaning.  It works like so:

    * For small words (3 characters or less), repeat it twice.
      eg: "and" -> "andand"

    * For longer words beginning with a vowel, remove the first letter and
    append it to the end.  eg: "abacus" -> "bacusa"

    * For longer words beginning with a consonant, reverse them.
    eg: "world" -> "dlrow"

    The function encode should take a word, and convert it to its goat latin
    form. All inputs will be lower case.

    Hint: print("a" + "b") will print a concatenated (joined up) string.


Tests:

    >>> encode("it")
    itit
    >>> encode("dob")
    dobdob
    >>> encode("apple")
    pplea
    >>> encode("rhubarb")
    brabuhr
    >>> encode("orange")
    rangeo
    >>> encode("pineapple")
    elppaenip

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def encode(word):

    length = len(word)
    newword = ""

    if length < 4:
        print(word * 2)

    elif word[0].lower() in "aeoiu":
        print(word[1:length] + word[0])

    else:
        print(word[::-1])
        
