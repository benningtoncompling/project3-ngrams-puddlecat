import random
import math

def getTrigramWords(dictt, w1):
    prob = random.uniform(0, 1)
    probTotal = 0
    stringg = ""
    for w2 in dictt[w1]:
        if (w2 != "<s>") & (w2 != "</s>") & (w2 != "TOTAL"):
            for w3 in dictt[w1][w2]:
                if w3 != "TOTAL":
                    #print(((dictt[w1][w2][w3])/(dictt[w1][w2]["TOTAL"])))
                    probTotal += (((dictt[w1][w2]["TOTAL"])/(dictt[w1]["TOTAL"])) * ((dictt[w1][w2][w3])/(dictt[w1][w2]["TOTAL"])))#((dictt[w1]["TOTAL"])/((len(dictt))))
                    if (probTotal > prob) & (w3 != "<s>") & (w3 != "</s>"):
                        stringg += w2
                        stringg += " "
                        stringg += w3
                        stringg += " "
                        return(stringg, w3)
    return("NULL ", w1)#something went wrong


def getTrigramFromBigram(dictt, w1, w2):
    prob = random.uniform(0, 1)
    probTotal = 0
    stringg = ""
    for w3 in dictt[w1][w2]:
        if w2 != "TOTAL":
            if w3 != "TOTAL":
                #probTotal += (((dictt[w1]["TOTAL"])/((len(dictt)))) * ((dictt[w1][w2]["TOTAL"])/(dictt[w1]["TOTAL"])) * ((dictt[w1][w2][w3])/(dictt[w1][w2]["TOTAL"]))) #
                probTotal += (((dictt[w1][w2]["TOTAL"])/(dictt[w1]["TOTAL"])) * ((dictt[w1][w2][w3])/(dictt[w1][w2]["TOTAL"])))
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

def generateBigramSentence(dictionary, sentenceLength):
    generatedSentence = "<s>"
    wordd = "<s>"
    for i in range(sentenceLength):
        prob = random.uniform(0, 1)
        probTotal = 0
        for word in dictionary[wordd]:
            if (word != "TOTAL") & (word != "<s>") & (word != "</s>"):
                probTotal += (dictionary[wordd][word] / dictionary[wordd]["TOTAL"])
                if probTotal > prob:
                    generatedSentence += word
                    generatedSentence += " "
                    wordd = word
                    break
    generatedSentence += "</s>"
    return generatedSentence


def generateTrigramSentence(triDictionary, biDictionary, sentenceLength):
    generatedSentence = "<s>"
    wordd = "<s>"
    prob = random.uniform(0, 1)
    probTotal = 0
    for word in biDictionary[wordd]:
        if word != "TOTAL":
            probTotal += (biDictionary[wordd][word] / biDictionary[wordd]["TOTAL"])#?
            if (probTotal > prob) & (word != "<s>") & (word != "</s>"):
                generatedSentence += word
                generatedSentence += " "
                wordd = word
                break

    w = getTrigramFromBigram(triDictionary, "<s>", wordd)
    generatedSentence += w[0]
    wordd = w[1]

    for i in range(sentenceLength): #fix sentence length
        w = getTrigramWords(triDictionary, wordd)
        generatedSentence += w[0]
        wordd = w[1]
    generatedSentence += "</s>"
    return generatedSentence
