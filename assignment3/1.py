import random
from collections import defaultdict, Counter
from datetime import datetime
from functools import reduce
#import time

g_dataset = {}
g_test_good = {}
g_test_bad = {}
NUM_ROWS = 32
NUM_COLS = 32
DATA_TRAINING = 'digit-training.txt'
DATA_TESTING = 'digit-testing.txt'
DATA_PREDICT = 'digit-predict.txt'

# kNN parameter
KNN_NEIGHBOR = 7

##########################
##### Load Data  #########
##########################

# Convert next digit from input file as a vector 
# Return (digit, vector) or (-1, '') on end of file
def read_digit(p_fp):
    # read entire digit (inlude linefeeds)
    bits = p_fp.read(NUM_ROWS * (NUM_COLS + 1))
    if bits == '':
        return -1,bits
    # convert bit string as digit vector
    vec = [int(b) for b in bits if b != '\n']
    val = int(p_fp.readline())
    return val,vec

# Parse all digits from training file
# and store all digits (as vectors) 
# in dictionary g_dataset
def load_data(p_filename=DATA_TRAINING):
    global g_dataset
    # Initial each key as empty list 
    g_dataset = defaultdict(list)
    with open(p_filename) as f:
        while True:
            val,vec = read_digit(f)
            if val == -1:
                break
            g_dataset[val].append(vec)
        #print(g_dataset)
        #time.sleep(1000) 

##########################
##### kNN Models #########
##########################

# Given a digit vector, returns
# the k nearest neighbor by vector distance
def knn(p_v, size=KNN_NEIGHBOR):
    nn = []
    for d,vectors in g_dataset.items():
        for v in vectors:
            dist = round(distance(p_v,v),2)
            nn.append((dist,d))
    #print(nn,'*****************************')
    # TODO: find the nearest neigbhors

    return []

# Based on the knn Model (nearest neighhor),
# return the target value
def knn_by_most_common(p_v):
    nn = knn(p_v)

    # TODO: target value
    return -1

########################## 
##### Prediction  ########
##########################

# Make prediction based on kNN model
# Parse each digit from the predict file
# and print the predicted balue
def predict(p_filename=DATA_PREDICT):
    # TODO
    print('TO DO: show results of prediction')

##########################
##### Accuracy   #########
##########################

# Compile an accuracy report by
# comparing the data set with every
# digit from the testing file 
def validate(p_filename=DATA_TESTING):
    global g_test_bad, g_test_good
    g_test_bad = defaultdict(int)
    g_test_good = defaultdict(int)
        
    start=datetime.now()

    # TODO: Validate your kNN model with 
    # digits from test file.
    
    stop=datetime.now()
    show_test(start, stop)

##########################
##### Data Models ########
##########################

# Randomly select X samples for each digit
def data_by_random(size=25):
    for digit in g_dataset.keys():
        g_dataset[digit] = random.sample(g_dataset[digit],size)

##########################
##### Vector     #########
##########################

# Return distance between vectors v & w
def distance(v, w):
    return 0

##########################
##### Report     #########
##########################

# Show info for training data set
def show_info():
    print('TODO: Training Info')
    for d in range(10):
        
        print(d, '=', len(g_dataset[d]))
    #print(g_dataset[d])
# Show test results
def show_test(start="????", stop="????"):
    print('Beginning of Validation @ ', start)    
    print('TODO: Testing Info')
    for d in range(10):
        good = g_test_good[d]
        bad = g_test_bad[d]
        print(d, '=', good, bad)
    print('End of Validation @ ', stop)  

if __name__ == '__main__':
    load_data()
    show_info()
    validate()
    predict()
    print(type(g_dataset[0]))
    print(type(g_dataset[0][0]))
    for i in range(len(g_dataset[0][0])):
        print(g_dataset[0][0][i],end='')
        if i % 32 == 0:
            print('\n')
    print(g_test_good)
    print(g_test_bad)

