import pandas as pd
import numpy as np
import random as rand
import time
from collections  import Counter
class RTLearner(object):
    def __init__(self,leaf_size=1, verbose=False ):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.data = None
        self.tree = None
    
    def add_evidence(self,data_x, data_y):
        '''
        Add training data to learner

        Parameters
            data_x (numpy.ndarray) – A set of feature values used to train the learner
            data_y (numpy.ndarray) – The value we are attempting to predict given the X data

        '''
        data = np.column_stack((data_x,data_y))     
        self.tree = self.build_tree(data)
        #self.tree)
        
      
    def get_corr(self,data_x,data_y):
        corr = np.corrcoef(data_x, data_y, rowvar = False)
        corr = abs(corr)
        corr[np.isnan(corr)] = 0
        index = np.argmax(corr[:-1,-1])
        
        return index
    def build_tree(self,data):
        data_y  = data[:,-1:]
        data_x = data[:,:-1]
        if data_x.shape[0] <= self.leaf_size: 
            return np.asarray([-1, np.mean(data_y), -1, -1])
               
        unique_rows = np.unique(data_y, axis=0)


        if unique_rows.shape[0] == 1:
            return np.asarray([-1, np.mean(data_y), -1, -1])
        #https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint
        #get the random feature and random row to split on
        feature = rand.randint(0,data_x.shape[1]-1)
        splitVal = (data_x[rand.randint(0,data_x.shape[0]-1)][feature] + data_x[rand.randint(0,data_x.shape[0]-1)][feature]) / 2
        stop = data[:,feature]<=splitVal
       
        #https://stackoverflow.com/questions/26163727/how-to-test-if-all-rows-are-equal-in-a-numpy helped me 
        if (stop == stop[0]).all():
            return np.asarray([-1, Counter(data_y.flatten().tolist()).most_common(1)[0][0], -1, -1])
        lefttree = self.build_tree(data[data[:,feature]<=splitVal])
        righttree = self.build_tree(data[data[:,feature]>splitVal])
        if data_x.shape[0] == data[data[:,feature]<=splitVal].shape[0]:
              return np.asarray([-1, Counter(data_y.flatten().tolist()).most_common(1)[0][0], -1, -1])
        if data_x.shape[0] == data[data[:,feature]>splitVal].shape[0]:
             return np.asarray([-1,Counter(data_y.flatten().tolist()).most_common(1)[0][0], -1, -1])
        if len(lefttree.shape)!= 1:
            root = np.array([int(feature), splitVal, 1, int(lefttree.shape[0]+1)])
        else:
            root = np.array([int(feature), splitVal, 1, 2])
        return np.vstack((root,lefttree,righttree))



    def author(self):
        return 'radjei3'
    def study_group():
        '''
        Returns
            A comma separated string of GT_Name of each member of your study group
            # Example: "gburdell3, jdoe77, tbalch7" or "gburdell3" if a single individual working alone
        
        Return type
            str 
        '''
        return None
    
       
    def query(self,points):
        results = np.empty((points.shape[0]))
        for  point in range(points.shape[0]):
            tree_row = 0
            index  = 0
            for _ in range(self.tree.shape[0]):
                if np.isscalar(points):
                    points
                split_value = points[point ,int(self.tree[tree_row][0])]
                feature = self.tree[tree_row][0]
                if  feature  == -1:
                    results[point] = self.tree[tree_row][1]
                    break 
                if split_value > self.tree[tree_row][1]:
                    
                    tree_row += int(self.tree[tree_row][3])
                else:
                    tree_row += int(self.tree[tree_row][2])
                    
            results[point] = self.tree[tree_row][1]
        
        return results

             
            
            
        
        
          
    

