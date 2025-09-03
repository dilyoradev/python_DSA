def translate(text):
    vowels = ('a', 'e', 'i', 'o', 'u')

    words = text.split()
    translated_words = []
    for word in words:
        if word.startswith(vowels) or word.startswith(("xr", "yt")):
            translated_word = word + "ay"
        else:
            for i, letter in enumerate(word):
                if word[i : i+2] == "qu":
                    translated_word = word[i+2:] + word[:i+2] + "ay"
                    break
                elif letter in vowels or (letter == "y" and i!=0):
                    translated_word = word[i:] + word[:i] + "ay"
                    break
                    
        translated_words.append(translated_word)
    return " ".join(translated_words)
    

            
