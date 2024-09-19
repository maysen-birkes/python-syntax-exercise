def print_upper_words(words):
    """Print out each word on a separate line all uppercased.

        >>> print_upper_words(["Hello", "world", "lets", "write", "python"])
        HELLO
        WORLD
        LETS
        WRITE
        PYTHON
    """

    for word in words:
        print(word.upper())


def print_upper_words_2(words):
    """Print each word on a separate line all uppercased, only if word start with E or e.

        >>> print_upper_words_2(["cat", "Elephant", "dog", "elk"])
        ELEPHANT
        ELK
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words_3(words, must_start_with):
    """Print each word on a separate line all uppercase, if it starts with the selected letter(s)

        >>> print_upper_words_3(["cat", "Elephant", "dog", "elk"],
        ...                 must_start_with=["c", "d"])
        CAT
        DOG
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print(print_upper_words(["Hello", "world", "lets", "write", "python"]))
print(print_upper_words_2(["cat", "Elephant", "dog", "elk"]))
print(print_upper_words_3(["Cat", "Elephant", "Dog", "elk"], must_start_with=["C", "D"]))