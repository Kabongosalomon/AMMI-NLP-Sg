from collections import Counter

def question38(Text):
    uni_bi_gram = {'unigrams': dict(), 'trigrams':dict()}
    words = Text.split() 
    words = [word.lower() for word in words]
    word_counts = Counter(words)
    sorted_vocab = sorted(word_counts, key=word_counts.get, reverse=True)
    uni_bi_gram['unigrams'] = {word: word_counts[word] for word in sorted_vocab}
    temp_bigram = {}
    for i in range(0,len(words) -1):
        bigram  = " ".join(words[i:i+2] )
        if not bigram  in temp_bigram:
            temp_bigram[bigram] = 1
        else:
            temp_bigram[bigram] += + 1
    uni_bi_gram['trigrams'] = temp_bigram
    return uni_bi_gram

Text = "The workplace has changed: as technology continues to rapidly \
    transform industries and jobs, staying relevant and competitive requires \
    continuously building completely new skill sets. But we are here to help you \
    adapt to the demands of the modern workplace and the lifestyle of the modern worker. \
    Read up on what modular education is and how it can benefit you!"
print(question38(Text))

