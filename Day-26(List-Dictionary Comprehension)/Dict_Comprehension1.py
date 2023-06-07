sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_list = sentence.split(' ');
wordLen_dictionary = {word:len(word) for word in word_list}
print(wordLen_dictionary)