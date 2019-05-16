import random
import math

'''''
def getTrigramWords(triDict, biDict, w1):
    prob = random.uniform(0, 1)
    probTotal = 0
    stringg = ""
    for w2 in triDict[w1]:
        if (w2 != "<s>") & (w2 != "</s>") & (w2 != "TOTAL"):
            for w3 in triDict[w1][w2]:
                if w3 != "TOTAL":
                    #print(((triDict[w1][w2][w3])/(triDict[w1][w2]["TOTAL"])))
                    probTotal += (((biDict[w1][w2])/(triDict[w1]["TOTAL"])) * ((triDict[w1][w2][w3])/(triDict[w1][w2]["TOTAL"])))
                    if (probTotal > prob) & (w3 != "<s>") & (w3 != "</s>"):
                        stringg += w2
                        stringg += " "
                        stringg += w3
                        stringg += " "
                        return(stringg, w3)
    return("NULL ", w1)#something went wrong
'''''

# probability of bigram: bigram[w1][w2]/unigram[w1]
# trigram takes w1 and w2

def getTrigramFromBigram(triDict, biDict, w1, w2):
    prob = random.uniform(0, 1)
    probTotal = 0
    stringg = ""
    for w3 in triDict[w1][w2]:
        probTotal += (triDict[w1][w2][w3] / biDict[w1][w2])
        if (probTotal > prob) & (w3 != "<s>") & (w3 != "</s>"):
            stringg += w3
            stringg += " "
            return(stringg, w3)
    return("NULL ", w1)#something went wrong


def generateUnigramSentence(dictionary, sentenceLength, tokensCount):
    generatedSentence = "<s>"
    for i in range(sentenceLength):
        prob = random.uniform(0, 1)
        probTotal = 0
        for word in dictionary:
            probTotal += (dictionary[word]/tokensCount)
            if (probTotal > prob) & (word != "<s>") & (word != "</s>"):
                generatedSentence += word
                generatedSentence += " "
                break

    generatedSentence += "</s>"
    return generatedSentence

def generateBigramSentence(biDictionary, uniDictionary, sentenceLength):
    generatedSentence = "<s>"
    wordd = "<s>"
    for i in range(sentenceLength):
        prob = random.uniform(0, 1)
        probTotal = 0
        for word in biDictionary[wordd]:
            if (word != "<s>") & (word != "</s>"):
                probTotal += (biDictionary[wordd][word] / uniDictionary[wordd])
                if probTotal > prob:
                    generatedSentence += word
                    generatedSentence += " "
                    wordd = word
                    break
    generatedSentence += "</s>"
    return generatedSentence


def generateTrigramSentence(triDictionary, biDictionary, uniDictionary, sentenceLength):
    generatedSentence = "<s>"
    word1 = "<s>"
    word2 = ""
    prob = random.uniform(0, 1)
    probTotal = 0
    for word in biDictionary[word1]:
        probTotal += (biDictionary[word1][word] / uniDictionary[word1])#?
        if (probTotal > prob) & (word != "<s>") & (word != "</s>"):
            generatedSentence += word
            generatedSentence += " "
            word2 = word
            break

    for i in range(sentenceLength): #fix sentence length
        w = getTrigramFromBigram(triDictionary, biDictionary, word1, word2)
        generatedSentence += w[0]
        word1 = word2
        word2 = w[1]

    generatedSentence += "</s>"
    return generatedSentence
