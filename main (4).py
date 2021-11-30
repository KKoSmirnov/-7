def sort_sentence(sentence):
    word_list = sentence.split()
    final_sentence = ""
    for i in sorted(word_list, key=lambda a: len(a)):
        final_sentence = final_sentence + " " + i
    return final_sentence

