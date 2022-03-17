import time
import os
import string
# ZAFER YALÇIN

unigram = dict()
bigram = dict()
trigram = dict()


# with this function handling punctuation, multiple white spaces etc for given .txt files.
def corpus_creator(folder_name):
    data = ""
    f_list = os.listdir(folder_name)
    translation_table = str.maketrans("", "", string.punctuation)
    print("CORPUS CREATING BEGAN...")
    for files in f_list:
        with open(folder_name + "//" + files, 'r') as f:
            data = data + f.read().lower().translate(translation_table)
        print("\t{filename:<40} {c}".format(filename=folder_name + "/" + files, c="completed."))
    print("CORPUS CREATING FINISHED...\n")
    data = data.split()
    return data


def frequency_calculator(corpus):
    for i in range(len(corpus)):
        if i < len(corpus):
            uni = corpus[i]
            if uni in unigram:
                unigram[uni] = unigram.get(uni) + 1
            else:
                unigram[uni] = 1
        if i < len(corpus) - 1:
            bi = corpus[i] + ", " + corpus[i + 1]
            if bi in bigram:
                bigram[bi] = bigram.get(bi) + 1
            else:
                bigram[bi] = 1
        if i < len(corpus) - 2:
            tri = corpus[i] + ", " + corpus[i + 1] + ", " + corpus[i + 2]
            if tri in trigram:
                trigram[tri] = trigram.get(tri) + 1
            else:
                trigram[tri] = 1


def ngram_printer(ngram, n):
    ngram = dict(sorted(ngram.items(), key=lambda item: item[1], reverse=True))
    counter = 1
    print("{n:<10}{i:<33}{f:<12}{p}".format(n="NO", i="ITEM", f="FREQUENCY", p=" PROBABILITY"))
    print("\n-------------------------------------------------------------------")

    total_words = 0
    probability = 0
    for k in unigram:
        total_words = total_words + unigram.get(k)

    for k, v in ngram.items():
        if n == 1:
            probability = ngram.get(k) / total_words
        elif n == 2:
            probability_strings = k.split(", ")
            probability = ngram.get(k) / unigram.get(probability_strings[0])
        elif n == 3:
            probability_strings = k.split(", ")
            probability = ngram.get(k) / bigram.get(probability_strings[0] + ", " + probability_strings[1])
        print("{c:<10}{key:<36}{value:<12}{probability:.6f}".format(c=counter, key="{" + k + "}", value=v,
                                                                    probability=probability))
        counter = counter + 1
        if counter > 50: break

    print("-------------------------------------------------------------------")


def main():
    corpus = corpus_creator("Novel-Samples")
    frequency_calculator(corpus)
    print("UNIGRAM\n-------------------------------------------------------------------")
    ngram_printer(unigram, 1)
    print("BIGRAM\n-------------------------------------------------------------------")
    ngram_printer(bigram, 2)
    print("TRIGRAM\n-------------------------------------------------------------------")
    ngram_printer(trigram, 3)


start_time = 0
if __name__ == '__main__':
    start_time = time.time()
main()
print("Total running time:\t {00:.5f} sec".format((time.time() - start_time)))
input("Press enter key to exit... ")
