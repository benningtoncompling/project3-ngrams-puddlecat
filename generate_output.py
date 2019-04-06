import generate_from_ngram
import random
import math

def writeOutput(output_file_name, unigramsDictionary, bigramsDictionary, trigramsDictionary, unigramsd, bigramsd, trigramsd):
    with open(output_file_name, 'w', encoding='utf-8') as output:
        output.write("data: \n\nngram 1: types= " + str(unigramsd[1]) + " tokens= " + str(unigramsd[0])) #tokens= 0 types = 1
        output.write("\nngram 2: types= " + str(bigramsd[1]) + " tokens= " + str(bigramsd[0]))
        output.write("\nngram 3: types= " + str(trigramsd[1]) + " tokens= " + str(trigramsd[0]))

        output.write("\n\n1-grams:\n")

        for unigram in unigramsDictionary:
            output.write("\n1-gram: " + unigram + ", Count: " + str(unigramsDictionary[unigram]) + ", Probability: " + str(unigramsDictionary[unigram]/unigramsd[0]) + ", Log-Probability: "+ str(math.log10(unigramsDictionary[unigram]/unigramsd[0])))

        output.write("\n\n2-grams:\n")

        for bigram in bigramsDictionary:
            for bigramm in bigramsDictionary[bigram]:
                if bigramm != "TOTAL":
                    output.write("\n2-gram: " + str(bigram) + " " + str(bigramm) + ", Count: " + str(bigramsDictionary[bigram][bigramm]) + ", Probability: " + str(bigramsDictionary[bigram][bigramm]/len(bigramsDictionary[bigram]))+ ", Log-Probability: "+ str(math.log10(bigramsDictionary[bigram][bigramm]/len(bigramsDictionary[bigram]))))

        output.write("\n\n3-grams:\n")

        for trigram in trigramsDictionary:
            for trigramm in trigramsDictionary[trigram]:
                if trigramm != "TOTAL":
                    for trigrammm in trigramsDictionary[trigram][trigramm]:
                        if trigrammm != "TOTAL":
                            output.write("\n3-gram: " + str(trigram) + " " + str(trigramm) + " " + str(trigrammm)+ ", Count: " + str(trigramsDictionary[trigram][trigramm][trigrammm]) + ", Probability: " + str(trigramsDictionary[trigram][trigramm][trigrammm] / trigramsd[0])+ ", Log-Probability: "+str(math.log10(trigramsDictionary[trigram][trigramm][trigrammm] / trigramsd[0])))

        output.write("\n\ntop 10 words: \n\n")
        unigramsList = [(k, v) for k, v in unigramsDictionary.items()]
        unigramsList.reverse()
        output.write(str(unigramsList[0:10]))

        output.write("\nunigram sentences: \n")
        for i in range(0, 5):
            output.write(generate_from_ngram.generateUnigramSentence(unigramsDictionary, (random.randint(3, 10)), unigramsd[0]))
            output.write("\n")
        output.write("\nbigram sentences: \n")
        for i in range(0, 5):
            output.write(generate_from_ngram.generateBigramSentence(bigramsDictionary, (random.randint(3, 10))))
            print(generate_from_ngram.generateBigramSentence(bigramsDictionary, (random.randint(3, 10))))
            output.write("\n")
        output.write("\ntrigram sentences: \n")
        for i in range(0, 5):
            output.write(generate_from_ngram.generateTrigramSentence(trigramsDictionary, bigramsDictionary, (random.randint(3, 10))))
            print(generate_from_ngram.generateTrigramSentence(trigramsDictionary, bigramsDictionary, (random.randint(3, 10))))
            output.write("\n")


