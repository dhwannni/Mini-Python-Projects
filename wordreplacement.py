def replace_word():
    str = "Python is cool, and hi hi hi "
    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))
replace_word()