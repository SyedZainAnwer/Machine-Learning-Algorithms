import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, leftNode=None, rightNode=None,*, value=None):
        self.feature = feature
        self.threshold = threshold
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.value = None
    
    def is_leaf_node(self):
        return self.value is not None


class DecisionTree:
    def __init__(self, min_sample_split=2, max_depth=100, n_features=None):
        self.min_sample_split = min_sample_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None
    
    def fit(self, X, y):
        self.n_features = X.shape[1] if self.n_features else min(X.shape[1], self.n_features)
        self.root = self._grow_tree(X, y)
        
    
    def _grow_tree(self, X, y):
        n_samples, n_feats = X.shape
        n_labels = len(np.unique(y))
        
        # check stopping criteria
        
        
        # find best split
        
        
        # create child nodes
    
    # def predict():
        