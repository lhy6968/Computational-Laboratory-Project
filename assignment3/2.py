import random
from collections import defaultdict, Counter
from datetime import datetime

g_dataset = {}
g_test_good = {}
g_test_bad = {}
NUM_ROWS = 32
NUM_COLS = 32
DATA_TRAINING = 'digit-training.txt'
DATA_TESTING = 'digit-testing.txt'
DATA_PREDICT = 'digit-predict.txt'
g_spaces_title = 14
g_spaces_digit = 15
g_spaces_result = 3
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
        return -1, bits
    # convert bit string as digit vector
    vec = [int(b) for b in bits if b != '\n']
    val = int(p_fp.readline())
    return val, vec

# Parse all digits from training file
# and store all digits (as vectors)
# in dictionary g_dataset
def load_data(p_filename=DATA_TRAINING):
    global g_dataset
    # Initial each key as empty list
    g_dataset = defaultdict(list)
    with open(p_filename) as f:
        while True:
            val, vec = read_digit(f)
            if val == -1:
                break
            g_dataset[val].append(vec)

##########################
##### kNN Models #########
##########################


# Given a digit vector, returns
# the k nearest neighbor by vector distance
def knn(p_v, size=KNN_NEIGHBOR):
    nn = []
    for d, vectors in g_dataset.items():
        for v in vectors:
            dist = round(distance(p_v, v), 2)
            nn.append((dist, d))
    nn.sort()
    kNearestNeighbors = []
    for i in range(size):
        kNearestNeighbors.append(nn[i][1])
    return kNearestNeighbors


# Based on the knn Model (nearest neighbor),
# return the target value
def knn_by_most_common(p_v):
    nn = knn(p_v)
    print(nn)
    target_value = Counter(nn).most_common()[0][0]
    '''
    According to the property of method most_common, when there is a tie, 
    the neighbor who takes the first position will be considered as the 
    so called nearest.
    '''
    return target_value
##########################
##### Prediction  ########
##########################

# Make prediction based on kNN model
# Parse each digit from the predict file
# and print the predicted value
def predict(p_filename=DATA_PREDICT):
    predicts = []
    with open(p_filename) as f:
        while True:
            val, vec = read_digit(f)
            if val == -1:
                break
            predict = knn_by_most_common(vec)
            predicts.append(predict)
    linesDividing(g_spaces_title*' '+'Prediction')
    print('The prediction of the digits in target file shown as below:')
    for predict in predicts:
        print(predict)

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

    start = datetime.now()

    with open(p_filename) as f:
        while True:
            val, vec = read_digit(f)
            if val == -1:
                break
            predict = knn_by_most_common(vec)
            if predict == val:
                g_test_good[val] += 1
            else:
                g_test_bad[val] += 1

    stop = datetime.now()
    show_test(start, stop)

##########################
##### Data Models ########
##########################

# Randomly select X samples for each digit
def data_by_random(size=25):  # size=25 initially
    for digit in g_dataset.keys():
        g_dataset[digit] = random.sample(g_dataset[digit], size)

##########################
##### Vector     #########
##########################

# Return distance between vectors v & w
def distance(v, w):
    # numOfDifference=[0]
    # numOfDifference=[1 for v_i,w_i in zip(v,w) if v_i!=w_i]
    # return reduce(lambda x,y: x+y,numOfDifference)
    '''
    The method above is slower than the method below by testing. Afterall,
    I decided not to use the function reduce.
    '''
    d = 0
    for v_i, w_i in zip(v, w):
        if v_i != w_i:
            d += 1
    return d

##########################
##### Report     #########
##########################

# Show info for training data set
def linesDividing(ts):  # ts= target string
    divided_lines = '_ '*20
    print(divided_lines)
    print('')
    print(ts)
    print(divided_lines)


def show_info():
    global g_spaces_title, g_spaces_digit, g_spaces_result
    linesDividing(g_spaces_title*' '+'Training Info')
    total_samples = 0
    for d in range(10):
        print(g_spaces_digit*' ', d, '=', len(g_dataset[d]))
        total_samples += len(g_dataset[d])
    linesDividing(g_spaces_result*' '+'Total Samples ='+str(total_samples))


def percentageGet(numerator, denominator):
    rate = numerator/denominator
    return str(round(rate*100))+'%'

# Show test results
def show_test(start="????", stop="????"):
    global g_spaces_digit, g_spaces_result, g_spaces_title
    linesDividing('Beginning of Validation @ '+str(start))
    linesDividing(g_spaces_title*' '+'Testing Info')
    correct = 0
    wrong = 0
    for d in range(10):
        good = g_test_good[d]
        bad = g_test_bad[d]
        correct += good
        wrong += bad
        print(g_spaces_digit*' ', d, '=', good,
              bad, percentageGet(good, good+bad))
    result = g_spaces_result*' '+'Accuracy = ' + \
        percentageGet(correct, correct+wrong)+'\n'+g_spaces_result * \
        ' '+'Correct/Total = '+str(correct)+'/'+str(correct+wrong)
    linesDividing(result)
    print('End of Validation @ ', stop)
    divided_lines = 20
    print('_ '*divided_lines)


if __name__ == '__main__':
    load_data()
    show_info()
    validate()
    predict()
