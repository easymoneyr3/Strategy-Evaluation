import numpy as np
import random as rand
class BagLearner(object):
    def __init__(self, learner, kwargs={}, bags=20, boost=False, verbose=False):
        self.bags = bags
        self.kwargs = kwargs
        self.boost = boost
        self.verbose = verbose
        self.learners = []
        #addig the learner to the bag
        for _ in range(0,bags):
            self.learners.append(learner(**kwargs))

    def author(self):
        return 'radjei3'
    
    def add_evidence(self, data_x, data_y):
        for i in self.learners:
            num = rand.sample(range(data_x.shape[0]), data_x.shape[0])
            i.add_evidence(data_x[num], data_y[num])
    
    def query(self, points):
        num = []
        for i in self.learners:
            num.append(i.query(points))
        return sum(num)/ self.bags
    