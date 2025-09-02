def is_pangram(sentence):
    lower_sentence = sentence.lower()
    pangram = set()
    for letter in lower_sentence:
        if "a" <= letter <= "z":
            pangram.add(letter)
        if len(pangram) == 26:
                return True
    return False
    
