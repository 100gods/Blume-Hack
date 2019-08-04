import pandas as pd
import numpy as np

global model
global top_query


def read_top_query():
    print('loading frequent queries . . . . . . . . . . . . . . .')
    return pd.read_csv('frequent_query.csv')


def loadGloveModel(gloveFile):
    print("Loading Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
    f = open(gloveFile, 'r')
    global model
    model = {}
    counter = 0
    for line in f:
        counter += 1
        try:
            splitLine = line.split()
            word = splitLine[0]
            embedding = np.array([float(val) for val in splitLine[1:]])
            model[word] = embedding
        except Exception as e:
            # continue
            print('error = {0}, input = {1}'.format(e, line))
        if counter % 100000 == 0:
            print("Done.", len(model), " words loaded . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
    print("Done.", len(model), " words loaded!")
    return model


model = loadGloveModel('glove.6B.300d.txt')
top_query = read_top_query()
