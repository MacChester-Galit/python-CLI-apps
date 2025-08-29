while True:
    sentence = input("Enter a sentence:\n")
    word_count = 0
    is_word = False
    if len(sentence) == 0 or sentence == " ":
        print("Please provide a valid sentence. Blank message is not allowed")
        continue
    for letter in sentence:
        if letter != " " and is_word == False:
            word_count += 1 
            is_word = True
        elif letter == " ":
            is_word = False
    print("Word count: " + str(word_count))
    break