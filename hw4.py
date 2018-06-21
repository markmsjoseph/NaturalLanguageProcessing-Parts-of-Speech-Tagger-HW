from collections import defaultdict


# create an array with POS tags, Start and end in order to calculate the freq of the
# previous words
def createArray():
    file = open('test.pos', 'r')
    posArray = []
    for line in file:
        # split each line where [0] will be the word and [1] will be the POS
        line1 = line.split( )
        if(len(line1)== 0):
            line1.append("START" )
            line1.append('START')
        elif(line1[1] == "."):
                line1[1] = "END"
        elif(line1[1] == ")"):
                continue
        elif(line1[1] == "("):
                continue
        elif(line1[1] == ","):
                continue
        elif(line1[1] == "``"):
                continue
        elif(line1[1] == "''"):
                continue
        elif(line1[1] == ":"):
                continue
        elif(line1[1] == "$"):
                continue
        elif(line1[1] == "#"):
                continue

        posArray.append(line1[1])
    return posArray

# create a dictionary with the total counts for the POS tags
def dictionaryOfCounts():
    # empty dictionary to hold word and POS
    dict = {}
    # this dictionary will hold counts
    d = defaultdict(int)

    f = open('WSJ_24.pos', 'r')
    count = 0
    for line in f:
        # split each line where [0] will be the word and [1] will be the POS
        line1 = line.split( )
        # skip lines that are blank because they will be out of bounds
         # # skip lines that are blank because they will be out of bounds
        if(len(line)== 1):
            line1 = []
            line1.append("START" )
            line1.append('START')
            count = count +  1
            dict.update({count:line1[1]})
        else:
            if(line1[1] == "."):
                line1[1] = "END"
                count = count +  1
                dict.update({count:line1[1]})
            elif(line1[1] == ")"):
                continue
            elif(line1[1] == "("):
                continue
            elif(line1[1] == ","):
                continue
            elif(line1[1] == "``"):
                continue
            elif(line1[1] == "''"):
                continue
            elif(line1[1] == ":"):
                continue
            elif(line1[1] == "$"):
                continue
            elif(line1[1] == "#"):
                continue
            else:
                # add all words to dictionary with count being the key and the POS as the value
                count = count +  1
                dict.update({count:line1[1]})

    # print("Number of items in the dictionary is " + str(len(dict)))

    # if the POS is in the values increment its counter, the default
    # dictionary will create a new key where d[word] will be a new field
    for word in dict.values():
        d[word] = d[word] + 1

    cnt = 0
    arrOfTuples = []
    for key, value in d.items():
        cnt = cnt + 1
        # print(str(cnt) + " : " + str(key) + " : " + str(value))

        tuple = (value, key)
        arrOfTuples.append(tuple)
    return arrOfTuples


array = createArray()
wordDict = {}

for i in range(len(array)):
    # if(array[i] == "START"):
    #     continue
    # elif(array[i] == "END"):
    #     continue
    # else:
        innerDict = {}
        d = defaultdict(int)
        count = 0
        doneAlready = []
        for j in range(len(array)):

            if(array[j] == array[i]):
                if(array[j-1] == 'START'):
                    continue
                else:
                    count = count + 1
                    innerDict.update({count:array[j-1]})
                    # print(innerDict)

        for word in innerDict.values():
            d[word] = d[word] + 1

        cnt = 0
        # print out the count and value
        # print("KEY IS: " + str(array[i]))
        for key, value in d.items():
            cnt = cnt + 1
            tuple = (value, key)

        wordDict.update({array[i]:d.items()})




print("\n\n\n================Prior probability/Transition probability : PROBABILITY OF A TAG GIVEN THE PREVIOUS TAG=========================\n")
for key, value in wordDict.items():
    print("KEY is " + key )
    count = 0
    for v in value:
        count = count + v[1]
        # print(str(v))
    for v in value:
        print("%-11s"%str(v) + "probability of going from tag of " + key + " to tag of " + str(v[0]) + " is: "+ str(v[1]) + "/" + str(count) + " = " + str(v[1]/float(count)))
    # print("total number of words that came before " + str(key) + ' is ' + str(count))
    print(" ")

#=======================================================================================================================
#returns an array of tuples where the first is the count followed by the word and its pos
def dictionaryOfWords():
    # empty dictionary to hold word and POS
    dict = {}
    # this dictionary will hold counts
    d = defaultdict(int)

    f = open('WSJ_24.pos', 'r')
    count = 0
    for line in f:
        # split each line where [0] will be the word and [1] will be the POS
        line1 = line.split( )
        # skip lines that are blank because they will be out of bounds
         # # skip lines that are blank because they will be out of bounds
        if(len(line1)== 0):
            line1 = []
            line1.append("START" )
            line1.append('START')
            count = count +  1
            dict.update({count:line1[1]})
        else:
            if(line1[1] == "."):
                line1[1] = "END"
                count = count +  1
                dict.update({count:line1[1]})
            elif(line1[1] == ")"):
                continue
            elif(line1[1] == "("):
                continue
            elif(line1[1] == ","):
                continue
            elif(line1[1] == "``"):
                continue
            elif(line1[1] == "''"):
                continue
            elif(line1[1] == ":"):
                continue
            elif(line1[1] == "$"):
                continue
            elif(line1[1] == "#"):
                continue
            else:
                # add all words to dictionary with count being the key and the POS as the value
                count = count +  1
                dict.update({count:line1[0].lower()+ ':' + line1[1]})

    # print("Number of items in the dictionary is " + str(len(dict)))

    # if the POS is in the values increment its counter, the default
    # dictionary will create a new key where d[word] will be a new field
    for word in dict.values():
        d[word] = d[word] + 1

    cnt = 0
    arrOfTuples = []
    for key, value in d.items():
        cnt = cnt + 1
        # print( str(value) + " : " + str(key))
        tuple = (value, key)
        arrOfTuples.append(tuple)
        # print(tuple)
    return arrOfTuples

array = createArray()


tupleArray = dictionaryOfWords()
tupleArrayOfCounts = dictionaryOfCounts()

# print(tupleArrayOfCounts)
# print(tupleArray)

print("\n\n\n==================Word Liklihood Probabilities: Count the number of tags eg.VBZ and divide by the specific word===============\n\n\n")
for y in range(len(tupleArray)):
    # splits by word and POS
    if(tupleArray[y][1] == 'START'):
        continue
    elif(tupleArray[y][1] == 'END'):
        continue
    else:
        splittedTuple = tupleArray[y][1].split(":")
    # print(splittedTuple)

    for i in range(len(tupleArrayOfCounts)):
        if(tupleArrayOfCounts[i][1] == splittedTuple[1]):
            totalCount = tupleArrayOfCounts[i][0]
            # print(totalCount)
            break
        else:
            continue
    word = tupleArray[y][1].split(":")
    print("Likleyhood of "+ str(word[1]) + " being the word  \""  + str(word[0]) + "\" is  " + str(tupleArray[y][0]/float(totalCount)) )








print("\n\n\n================================== VERTIBI ALGORITHM ====================================\n\n\n")

#
# #will contain all POS tags
# all_tags = []
# for key, value in wordDict.items():
#     all_tags.append(key)
#
# # get all sentences
# sentence = []
# f = open('test.pos', 'r')
# for line in f:
#     line1 = line.split(" ")
#     sentence.append(line1[0])
#
# sentlen = len(sentence)
#
#
# # store dictionary that maps each tag to the probability of best tag sequence
# viterbi = []
#
# # store dictionary that maps each tag to the previous tag in the best tag sequence
# backpointer = []
#
# first_viterbi = {}
# first_backpointer = {}
#
# for tag in all_tags:
#     # skip start tag
#     if tag == "START":
#         continue
#     #store keys for both of the 2 following dictionaries
#     first_viterbi [tag] =wordDict.get("START") #store probability times transition
#     first_backpointer [tag] = "START"
#
# print(first_viterbi)
# print(first_backpointer)
#
# # store to arrays
# viterbi.append(first_viterbi)
# backpointer.append(first_backpointer)
#
# #get the maximum value
# best = max(first_viterbi.keys(), key = lambda tag: first_viterbi[ tag ])
#
#
# for wordindex in range(1, len(sentence)):
#     this_viterbi = { }
#     this_backpointer = { }
#     prev_viterbi = viterbi[-1]
#
#     for tag in all_tags:
#         # don't record anything for the START tag
#         if tag == "START": continue
#
