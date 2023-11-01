def process_text(text):
    # Remove characters that are not numbers, letters, or spaces, and change to lowercase
    processed_text = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text).lower()
    words = processed_text.split()
    return words

def create_word_frequency_dict(words):
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

if __name__ == '__main__':
    # Read the text from the file
    with open('thevelveteenrabbit.txt', 'r') as file:
        text = file.read()

    # Process the text and create a word frequency dictionary
    words = process_text(text)
    word_frequency_dict = create_word_frequency_dict(words)

    while True:
        user_word = input("What word would you like to search? ").lower()
        
        if user_word == 'quit':
            break

        frequency = word_frequency_dict.get(user_word, 0)
        print(word_frequency_dict)
