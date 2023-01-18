import random
from collections import defaultdict, Counter
from datetime import datetime
from functools import reduce

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
def load_data(p_filename = DATA_TRAINING):
    global g_dataset
    # Initial each key as empty list 
    g_dataset = defaultdict(list) 
    with open(p_filename) as f: 
        while True: 
            val,vec = read_digit(f)
            if val == -1: 
                break
            g_dataset[val].append(vec) 

##########################
##### kNN Models #########
##########################

# Given a digit vector, returns
# the k nearest neighbor by vector distance
def knn(p_v, size = KNN_NEIGHBOR):
    nn = []
    for d,vectors in g_dataset.items():
        for v in vectors:
            dist = distance(p_v,v)
            nn.append((dist,d))
    nn.sort()
    return nn[:size]

# Based on the knn Model (nearest neighhor),
# return the target value
def knn_by_most_common(p_v):
    nn = knn(p_v)
    nn = [nn[i][1] for i in range(KNN_NEIGHBOR)]
    return Counter(nn).most_common()[0][0]

##########################
##### Prediction  ########
##########################

# Make prediction based on kNN model
# Parse each digit from the predict file
# and print the predicted balue
def predict(p_filename=DATA_PREDICT):
    print('TO DO: show results of prediction')
    results = []
    with open(p_filename) as f: 
        while True: 
            val,vec = read_digit(f)
            if val == -1: 
                break
            results.append(knn_by_most_common(vec))

    for result in results:
        print(result)


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

    with open(p_filename) as f: 
        while True: 
            val,vec = read_digit(f)
            if val == -1: 
                break
            knn_result = knn_by_most_common(vec)
            if knn_result == val:
                g_test_good[val] += 1
            else:
                g_test_bad[val] += 1
            
    accuracy = ['%.2f' % (g_test_good[val] / (g_test_good[val] + g_test_bad[val]) * 100) for val in range(10)]
    print()
    
    Accuracy = 0
    for val in range(10):
        print(val, "=", accuracy[val], "%")
        Accuracy += accuracy[val]
    print("Accuracy = ", Accuracy, "%")
    print("Correct/Total = ", g_test_good[val], "/", g_test_good[val] + g_test_bad[val])


##########################
##### Data Models ########
##########################

# Randomly select X samples for each digit
def data_by_random(size = 5):
    for digit in g_dataset.keys():
        g_dataset[digit] = random.sample(g_dataset[digit],size)

##########################
##### Vector     #########
##########################

# Return distance between vectors v & w
def distance(v, w):
    dist = 0
    for i in range(len(v)):
        dist += v[i] ^ w[i]
    return dist

##########################
##### Report     #########
##########################

# Show info for training data set
def show_info():
    print("-" * 40)
    print('Training Info'.center(50, " "))
    print("-" * 40)
    total = 0
    for d in range(10):
        pr = str(d)+ ' = '+ str(len(g_dataset[d]))
        total += len(g_dataset[d])
        print(pr.center(50, " "))
    print("-" * 40)
    print("Total Samples = ", total)

# Show test results
def show_test():
    print(g_test_good)
    print("-" * 40)
    print('Testing Info'.center(50, " "))
    print("-" * 40)
    for d in range(10):
        good = g_test_good[d]
        bad = g_test_bad[d]
        pr = str(d)+ ' = '+ str(good)+' '+ str(bad)
        print(pr.center(50, " "))

if __name__ == '__main__':
    load_data()
    start = datetime.now()
    print("Beginning of Training @ ", start)
    show_info()
#    show_test()
    print(g_test_good,'**************')
    data_by_random()
    validate()
    predict()
    stop = datetime.now()
    print("End of Training @ ", stop)