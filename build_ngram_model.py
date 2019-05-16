# Project 3 by Ell Buscemi

# fixed 5.16.19


import sys
import re
import collections
import generate_output

input_file_name = sys.argv[1]  # "twitter_output.txt"
output_file_name = sys.argv[2]  # "output.txt"
bigramsTypes = 0
bigramsTokens = 0
bigramsDictionary = {}
trigramsTokens = 0
trigramsTypes = 0
trigramsDictionary = {}
outputString = ""


def sortDictByValues(dictt):
    dictt = [(b, a) for (a, b) in dictt.items()]
    dictt.sort()
    dictt = [(b, a) for (a, b) in dictt]
    dictt = collections.OrderedDict(dictt)
    return dictt


def sortDictByTotals(dictt, uniDict):
    #problem here: it includes "total" which doesn't have a sub dict
    keysList = sorted(dictt, key=lambda x: (uniDict[x]))
    keysDict = {}
    for i in range(len(keysList)):
        keysDict[keysList[i]] = i
    dictt = sorted(dictt.items(), key=lambda x: keysDict.get(x[0]))
    dictt = collections.OrderedDict(dictt)
    return dictt


def makeCountedDict(dictt):
    dictCounted = {}
    types = 0
    tokens = 0
    for wordd in dictt:
        wordd = wordd.lower()
        if wordd in dictCounted:
            dictCounted[wordd] += 1
            tokens += 1
        else:
            dictCounted[wordd] = 1
            types += 1
            tokens += 1
    return (dictCounted, types, tokens)


with open(input_file_name, 'r', encoding='utf-8') as input:

        text = input.read()
        text = re.sub(r'^|\n(?=.+)', '<s>', text, re.MULTILINE)#? only working for the first 10 or so lines???
        text = re.sub(r'(?!^)(?=<s>)|$', '</s>', text, re.MULTILINE)
        words = re.findall(r'(?:\b\w+\b)|(?:</?s>)', text, re.MULTILINE) #?

        # words = [line.split() for line in input.readlines()]


        #make tallied dictionary of unigrams
        u = makeCountedDict(words)
        unigramsTypes = u[1]
        unigramsTokens = u[2]
        unigramsDictionary = u[0]
        unigramsDictionary = sortDictByValues(unigramsDictionary)

        #make tallied dictionary of bigrams
        i = 0
        for word in words:
            word = word.lower()
            if (i + 1) >= (len(words)):
                break
            word1 = word
            word2 = (words[i + 1]).lower()
            if word1 not in bigramsDictionary:
                bigramsDictionary[word] = {}
            if bigramsDictionary[word].get(word2) is None:
                bigramsDictionary[word][word2] = 1
                bigramsTokens += 1
                bigramsTypes += 1
            elif bigramsDictionary[word].get(word2) is not None:
                bigramsDictionary[word][word2] += 1
                bigramsTokens += 1

            i += 1

        bigramsDictionary = sortDictByTotals(bigramsDictionary, unigramsDictionary)
        # make tallied dictionary from trigrams

        for dictt in trigramsDictionary:
            dictt = sortDictByTotals(trigramsDictionary[dictt], bigramsDictionary[dictt])
            for trigram in trigramsDictionary[dictt]:
                trigramsDictionary[dictt][trigram] = sortDictByValues(trigramsDictionary[dictt][trigram])

        i = 0
        for word in words:
            word = word.lower()
            if (i + 2) >= (len(words)):
                #print("reached end")
                break
            word1 = word
            word2 = (words[i + 1]).lower()
            word3 = (words[i + 2]).lower()

            if word1 not in trigramsDictionary:
                trigramsDictionary[word1] = {}
                trigramsDictionary[word1][word2] = {}
                trigramsDictionary[word1][word2][word3] = 1
                trigramsTokens += 1
                trigramsTypes += 1

            elif (word1 in trigramsDictionary) & (word2 not in trigramsDictionary[word1]):
                trigramsDictionary[word1][word2] = {}
                trigramsDictionary[word1][word2][word3] = 1
                trigramsTokens += 1
                trigramsTypes += 1

            elif (word2 in trigramsDictionary[word1]) & (word3 not in trigramsDictionary[word1][word2]):
                trigramsDictionary[word1][word2][word3] = 1
                trigramsTokens += 1
                trigramsTypes += 1

            elif word3 in trigramsDictionary[word1][word2]:
                trigramsDictionary[word1][word2][word3] += 1
                trigramsTokens += 1
            i += 1



        generate_output.writeOutput(output_file_name, unigramsDictionary, bigramsDictionary, trigramsDictionary, (unigramsTokens, unigramsTypes), (bigramsTokens, bigramsTypes),  (trigramsTokens, trigramsTypes))

