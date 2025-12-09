import numpy as np
from ROCAnalysis import ROCAnalysis

class ForwardSelection:
    """
    A class for performing forward feature selection based on maximizing the F-score of a given model.

    Attributes:
        X (array-like): Feature matrix.
        y (array-like): Target labels.
        model (object): Machine learning model with `fit` and `predict` methods.
        selected_features (list): List of selected feature indices.
        best_cost (float): Best F-score achieved during feature selection.
    """

    def __init__(self, X, y, model):
        """
        Initializes the ForwardSelection object.

        Parameters:
            X (array-like): Feature matrix.
            y (array-like): Target labels.
            model (object): Machine learning model with `fit` and `predict` methods.
        """
        #--- Write your code here ---#
        
        self.X = X
        self.y = y
        self.model = model
        self.selected_features = []
        self.best_cost = 0

    def create_split(self, X, y, test_size=0.2, seed=42):
        """
        Creates a train-test split of the data.

        Parameters:
            X (array-like): Feature matrix.
            y (array-like): Target labels.

        Returns:
            X_train (array-like): Features for training.
            X_test (array-like): Features for testing.
            y_train (array-like): Target labels for training.
            y_test (array-like): Target labels for testing.
        """
        #--- Write your code here ---#
        
        np.random.seed(seed)
        indices = np.arange(X.shape[0])
        np.random.shuffle(indices)
        split = int((1 - test_size) * len(indices))
        train_idx, test_idx = indices[:split], indices[split:]
        return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

    def train_model_with_features(self, features):
        """
        Trains the model using selected features and evaluates it using ROCAnalysis.

        Parameters:
            features (list): List of feature indices.

        Returns:
            float: F-score obtained by evaluating the model.
        """
        #--- Write your code here ---#
        
        X_train, X_test, y_train, y_test = self.create_split(self.X[:, features], self.y)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        roc = ROCAnalysis(y_pred.flatten(), y_test.flatten())
        return roc.f_score()

    def forward_selection(self):
        """
        Performs forward feature selection based on maximizing the F-score.
        """
        #--- Write your code here ---#
        
        n_features = self.X.shape[1]
        remaining_features = list(range(n_features))
        self.selected_features = []
        self.best_cost = 0

        while remaining_features:
            best_feature = None
            best_score = self.best_cost

            for feature in remaining_features:
                trial_features = self.selected_features + [feature]
                score = self.train_model_with_features(trial_features)

                if score >= best_score:
                    best_score = score
                    best_feature = feature

            if best_feature is not None:
                self.selected_features.append(best_feature)
                remaining_features.remove(best_feature)
                self.best_cost = best_score
            else:
                break
                
    def fit(self):
        """
        Fits the model using the selected features.
        """
        #--- Write your code here ---#
        
        if not self.selected_features:
            self.forward_selection()
        X_train, bruh1, y_train, bruh2 = self.create_split(self.X[:, self.selected_features], self.y)
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        """
        Predicts the target labels for the given test features.

        Parameters:
            X_test (array-like): Test features.

        Returns:
            array-like: Predicted target labels.
        """
        #--- Write your code here ---#
        
        return self.model.predict(X_test[:, self.selected_features])
