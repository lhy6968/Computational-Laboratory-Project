import random
from collections import defaultdict, Counter
from datetime import datetime

#create a dict to store training data
g_dataset = {}
#create a dict to store number of correct data identified
g_test_good = {}
#create a dict to store number of incorrect data identified
g_test_bad = {}
#number of rows of each identified data
NUM_ROWS = 32
#number of columns of each identified data
NUM_COLS = 32
#training file that need to be used
DATA_TRAINING = 'digit-training.txt'
#testing file that need to be used
DATA_TESTING = 'digit-testing.txt'
#prediction file that need to be used
DATA_PREDICT = 'digit-predict.txt'
# kNN parameter
KNN_NEIGHBOR = 7

##########################
##### Load Data  #########
##########################

# Convert next digit from input file as a list
# This list contains all the index for "1" in each digit
# Return (digit, indexList) or (-1, '') on end of file
def read_digit(p_fp):
    # read entire digit (inlude linefeeds)
    bits = p_fp.read(NUM_ROWS * (NUM_COLS + 1))
    if bits == '':
        return -1,bits
    # convert bit string as a list
    # This list contains all the index for "1" in each digit
    vec = [int(bit) for bit in range(0,len(bits)) if bits[bit] == '1']
    val = int(p_fp.readline())
    return val,vec

# Parse all digits from training file
# and store all digits (as lists)
# each list contains all the index for "1" in each digit 
# in dictionary g_dataset
def load_data(p_filename = DATA_TRAINING):
    global g_dataset
    #record the time when starting training
    start = datetime.now()
    # Initial each key as empty list 
    g_dataset = defaultdict(list)
    #convert each data into a list
    with open(p_filename) as f:
        while True:
            val,vec = read_digit(f)
            if val == -1:
                break
            g_dataset[val].append(vec)
    #record the end of training time
    stop = datetime.now()
    #display start and end times in the terminal
    show_train(start,stop)

##########################
##### kNN Models #########
##########################

# Given a digit list, returns
# the k nearest neighbor by vector distance
def knn(p_v, size = KNN_NEIGHBOR):
    #create a list to store all the numbers with each distance
    nn = []
    for d,vectors in g_dataset.items():
        for v in vectors:
            dist = round(distance(p_v,v),2)
            nn.append((dist,d))
    #sort the list from smallest to largest
    nn.sort()
    #create a list to store k nearest neigbhors
    k_neighbors = []
    #append the k nearest neigbhors to the list
    for i in range(size):
        k_neighbors.append(nn[i][1])
    return k_neighbors

# Based on the knn Model (nearest neighhor),
# return the target value
def knn_by_most_common(p_v):
    nn = knn(p_v)
    #find the most common number
    target_value = Counter(nn).most_common()[0][0]
    return target_value

##########################
##### Prediction  ########
##########################

# Make prediction based on kNN model
# Parse each digit from the predict file
# and print the predicted balue
def predict(p_filename = DATA_PREDICT):
    #create the title "Prediction"
    title = ' '*12 + 'Prediction'
    #show the title "Prediction" in the terminal
    lineBoundary(title)
    #create a list to store all the results of prediction
    predicts = []
    #append each result of prediction to the list
    with open(p_filename) as f:
        while True:
            val,vec = read_digit(f)
            if val == -1:
                break
            predictNum = knn_by_most_common(vec)
            predicts.append(predictNum)
    #show the results of prediction in the terminal
    print('The prediction of the digits in target file is shown as below:')
    for predictNum in predicts:
        print(predictNum)

##########################
##### Accuracy   #########
##########################

# Compile an accuracy report by
# comparing the data set with every
# digit from the testing file 
def validate(p_filename = DATA_TESTING):
    global g_test_bad, g_test_good
    g_test_bad = defaultdict(int)
    g_test_good = defaultdict(int)
    #record the starting time of testing
    start = datetime.now()
    #test each digit in the testing file
    with open(p_filename) as f:
        while True:
            val,vec = read_digit(f)
            if val == -1:
                break
            test_value = knn_by_most_common(vec)
            if test_value == val:
                g_test_good[val] += 1
            else:
                g_test_bad[val] += 1
    #record the end time of testing
    stop = datetime.now()
    #display start and end times in the terminal
    show_test(start,stop)

##########################
##### Data Models ########
##########################

# Randomly select X samples for each digit
#X is the new size of each digit data in g_dataset
def data_by_random(size = 25):
    global g_dataset
    for digit in g_dataset.keys():
        g_dataset[digit] = random.sample(g_dataset[digit],size)

##########################
##### Vector     #########
##########################

# Return distance between vectors v & w
#Compare two lists which contain the index of all the "1" in each digit
def distance(v,w):
    #find the distance
    #for every index in these two vectors,if they are both 1 or 0,
    #the subdistance will be 0,
    #only when they are different(one is 1 and the other is 0),
    #the sub distance will be 1,
    #so using the differences between two vectors we can find the distance
    distance = (2 * len(set(v+w)) - len(v + w)) ** 0.5
    return distance
##########################
##### Report     #########
##########################

# Show info for training data set
def show_train(start='????',stop='????'):
    #show the beginning time of training in the terminal
    print('Beginning of Training @ ', start)
    #create a title for training
    title = ' ' * 12 + 'Training Info'
    #show the title in the terminal
    lineBoundary(title)
    #create a "sum" to record the number of all digits
    sum = 0
    for d in range(10):
        print(' ' * 14,d,'=',len(g_dataset[d]))
        sum += len(g_dataset[d])
    #create a title for the "total"
    total = ' ' * 5 + 'Total Samples = ' + str(sum)
    #show the title "total" in the terminal
    lineBoundary(total)
    #show the end time of training in the terminal
    print('End of Training @ ',stop) 
    

# Show test results
def show_test(start="????", stop="????"):
    #show the beginning time of testing in the terminal
    print('Beginning of Validation @ ',start)
    #create a title for testing
    title = ' ' * 12 + 'Testing Info'
    #show the title in the terminal
    lineBoundary(title)
    #record the total number of good digits 
    goodSum = 0
    #record the total number of bad digits 
    badSum = 0
    #find all the good and bad digits
    for d in range(10):
        good = g_test_good[d]
        bad = g_test_bad[d]
        average = int((good / (good + bad)) * 100)
        content = "%12d = %3d,%4d,%4d%%"%(d,good,bad,average) 
        print(content)
        goodSum += good
        badSum += bad
    #find the accuracy of testing
    accuracy = (goodSum / (goodSum + badSum)) * 100
    #create a title for "total" information
    total = ' ' * 7 + 'Accuracy = %.2f%%'%(accuracy) + '\n' + ' ' * 7 +  'Correct/Total = %3d/%3d'%(goodSum,goodSum + badSum)
    #show the title in terminal
    lineBoundary(total)
    #show the end time of testing in the terminal
    print('End of Validation @ ',stop)

#show each title with boundary in the terminal  
def lineBoundary(content):
    print('-' * 40)
    print(content)
    print('-' * 40)
    
#execute the entire program
if __name__ == '__main__':
    load_data()
    validate()
    predict()

