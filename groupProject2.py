
"""
File name: nlphw3.py
Authors: Taylor Fraker, Mariya Garbuz, Adrian Correa
Data Created: 10/23/2018
Last Modified: 10/23/2018
Python ver: 3.6.6

"""

#import nltk
#from nltk.corpus import gutenberg


def author_name(file_id):
    return file_id[:file_id.index('-')]


def average_word_length(words):
    wordLengths = []
    for w in words:
        wordLengths.append(len(w))
    awl = sum(wordLengths)/len(wordLengths)
    return awl


def TTR(words):
    alphaList = []
    digitList = []
    puncList = []
    
    for token in words:
        if token.isalpha() == True:
            alphaList.append(token)
        elif token.isdigit() == True:
            digitList.append(token)
        else:
            puncList.append(token)
    ttr = [len(alphaList)/len(words), len(digitList)/len(words), len(puncList)/len(words)]

    return ttr


def Hapax_Legomana_Ratio(words):
    
    wordlist = sorted(words)
    singles = []
    '''
    From Brandon :)
    The for loop below, on a list with n elements,
    will go from index 0 to index n-2 (instead of n-1).
    It makes sense since you compare each element of the list with the element before and after,
    and if you were to compare the last element (index n-1) to the one after it you would get an
    IndexError. But you still need to account for the last element somehow. There are two
    ways I chose to address this issue, one is within the loop and one is outside of it.
    I put the outside way within this docstring.

    for i in range(len(wordlist) - 1):
        if wordlist[i] != wordlist[i + 1] and wordlist[i] != wordlist[i - 1]:
            singles.append(wordlist[i])
    if wordlist[len(wordlist) - 1] != wordlist[len(wordlist) - 2]:
        singles.append(wordlist[len(wordlist) - 1])
    '''
    
    for i in range(len(wordlist)):
        if i < (len(wordlist) - 1):
            if wordlist[i] != wordlist[i + 1] and wordlist[i] != wordlist[i - 1]:
                singles.append(wordlist[i])
        else:
            if wordlist[len(wordlist) - 1] != wordlist[len(wordlist) - 2]:
                singles.append(wordlist[len(wordlist) - 1])
     
    
    return len(singles)/len(wordlist)


def average_sent_length(words, sents):
    asl = len(words)/len(sents)
    return asl


def sent_complexity(sents):
    countList = []
    compChars = [',', ':', ';']

    for sent in sents:
        count = 0
        for word in sent:
            if word == ',' or word == ':' or word == ';':
                count += 1
        countList.append(count)
    return sum(countList)/len(countList)



def lexical_div(words):
    '''
    compute the lexical diversity for a files in 
    the gutenberg corpus.  
    '''
    n_words = len(words)
    n_vocab = len(set(words))
    l_div = n_vocab / n_words  
    return l_div


def features(file_id):
    sents = gutenberg.sents(file_id)
    words = gutenberg.words(file_id)
    features = []
    features.append(author_name(file_id))
    features.append(float(format(average_word_length(words), '.2g')))
    ttr = TTR(words)
    features.append(float(format(ttr[0], '.2g')))
    features.append(float(format(ttr[1], '.2g')))
    features.append(float(format(ttr[2], '.2g')))
    features.append(float(format(Hapax_Legomana_Ratio(words), '.2g')))
    features.append(float(format(average_sent_length(words, sents), '.2g')))
    features.append(float(format(sent_complexity(sents), '.2g')))
    features.append(float(format(lexical_div(words), '.2g')))
    return features

def Author_Sig():
    bookLists = [features(file_id) for file_id in gutenberg.fileids()]
    authorsDict = {}

    for book in bookLists:
        if book[0] in authorsDict:
            authorsDict[book[0]].append(book[1:])
        else:
            authorsDict[book[0]] = []
            authorsDict[book[0]].append(book[1:])
    
    for author in authorsDict:
        if len(authorsDict[author]) > 1:
            authorsAvg = []
            for i in range(len(authorsDict[author][0])):
                x = []
                for book in authorsDict[author]:
                    x.append(book[i])
                authorsAvg.append(float(format(sum(x)/len(x), '.2g')))
            authorsDict[author] = authorsAvg
        else:
            authorsDict[author] = authorsDict[author][0]
    return authorsDict

def compare_signatures(sig1, sig2, weight):
    '''Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float) --- done
    2  : TTR (list of floats) --- done
    3  : Hapax Legomana Ratio (float) --- done
    4  : average sentence length (float) --- done
    5  : average sentence complexity (float) --- done
    6  : lexcial diversity (float) --- done
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''
    n_fields = len(sig1)
    score = 0.0
    for i in range(1,n_fields):
        score += abs(sig1[i] - sig2[i])*weight[i]
        
    return  score

'''          
print(Hapax_Legomana_Ratio('austen-emma.txt'))
print(words_per_sent('austen-emma.txt'))
print(average_word_length('austen-emma.txt'))
print(sent_complexity('austen-emma.txt'))
print(average_sent_length('austen-emma.txt'))
print(TTR('austen-emma.txt'))
print(author_name('austen-emma.txt'))
'''


if __name__ == '__main__':

    #print(Author_Sig())
    lst = ['a', 'a', 'b', 'a', 'b', 'b', 'c', 'c', 'd'] #test list for HLR, can delete -BE
    print(Hapax_Legomana_Ratio(lst))

"""
    print('running main')
    for fid in gutenberg.fileids(): 
        print(features(fid))

"""









