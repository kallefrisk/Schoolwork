from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt


class MachineLearningModel(ABC):
    """
    Abstract base class for machine learning models.
    """

    @abstractmethod
    def fit(self, X, y):
        """
        Train the model using the given training data.

        Parameters:
        X (array-like): Features of the training data.
        y (array-like): Target variable of the training data.

        Returns:
        None
        """
        pass

    @abstractmethod
    def predict(self, X):
        """
        Make predictions on new data.

        Parameters:
        X (array-like): Features of the new data.

        Returns:
        predictions (array-like): Predicted values.
        """
        pass

    @abstractmethod
    def evaluate(self, y_true, y_predicted):
        """
        Evaluate the model on the given data.

        Parameters:
        y_true (array-like): True target variable of the data.
        y_predicted (array-like): Predicted target variable of the data.

        Returns:
        score (float): Evaluation score.
        """
        pass


class KNNRegressionModel(MachineLearningModel):
    """
    Class for KNN regression model.
    """

    def __init__(self, k):
        """
        Initialize the model with the specified instructions.

        Parameters:
        k (int): Number of neighbors.
        """
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """
        Train the model using the given training data.
        In this case, the training data is stored for later use in the prediction step.
        The model does not need to learn anything from the training data, as KNN is a lazy learner.
        The training data is stored in the class instance for later use in the prediction step.

        Parameters:
        X (array-like): Features of the training data.
        y (array-like): Target variable of the training data.

        Returns:
        None
        """
        #--- Write your code here ---#

        # Assigning the values to the class for later use
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """
        Make predictions on new data.
        The predictions are made by averaging the target variable of the k nearest neighbors.

        Parameters:
        X (array-like): Features of the new data.

        Returns:
        predictions (array-like): Predicted values.
        """
        #--- Write your code here ---#
        
        predictions = []

        # Iterating through all the points in X
        for x in X:

            # Compute all the distances
            distances = np.linalg.norm(self.X_train - x.reshape(-1, 1), axis=1)
        
            # Sort the indexes to get the k nearest points
            sorted_index = np.argsort(distances)[:self.k]

            # Compute the mean of the k nearest values
            k_nearest_mean = np.mean(self.y_train[sorted_index])
        
            # Build the list of predictions
            predictions += [k_nearest_mean]

        # Return the predicted values
        return np.array(predictions)

    def evaluate(self, y_true, y_predicted):
        """
        Evaluate the model on the given data.
        You must implement this method to calculate the Mean Squared Error (MSE) between the true and predicted values.
        The MSE is calculated as the average of the squared differences between the true and predicted values.        

        Parameters:
        y_true (array-like): True target variable of the data.
        y_predicted (array-like): Predicted target variable of the data.

        Returns:
        score (float): Evaluation score.
        """
        #--- Write your code here ---#

        # Return the MSE
        return np.mean((y_true - y_predicted)**2)


class KNNClassificationModel(MachineLearningModel):
    """
    Class for KNN classification model.
    """

    def __init__(self, k):
        """
        Initialize the model with the specified instructions.

        Parameters:
        k (int): Number of neighbors.
        """
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """
        Train the model using the given training data.
        In this case, the training data is stored for later use in the prediction step.
        The model does not need to learn anything from the training data, as KNN is a lazy learner.
        The training data is stored in the class instance for later use in the prediction step.

        Parameters:
        X (array-like): Features of the training data.
        y (array-like): Target variable of the training data.

        Returns:
        None
        """
        #--- Write your code here ---#

        # Assigning the values to the class for later use
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """
        Make predictions on new data.
        The predictions are made by taking the mode (majority) of the target variable of the k nearest neighbors.
        
        Parameters:
        X (array-like): Features of the new data.

        Returns:
        predictions (array-like): Predicted values.
        """
        #--- Write your code here ---#

        predictions = []
        # Iterate over all data-points
        for x in X:

            # Calculate all distances
            distances = np.linalg.norm(self.X_train - x, axis=1)
            
            # Find the incices for the k nearest data-points
            k_nearest_indices = np.argsort(distances)[:self.k]

            # Get the labels of the nearest points
            k_nearest_labels = self.y_train[k_nearest_indices]

            # Find the most common label in the k nearest points
            counter = {}
            for c in k_nearest_labels:

                if c in counter:
                    counter[c] += 1
                else:
                    counter[c] = 1

            predictions += [max(counter, key=counter.get)]
        
        # Return the predicted labels
        return np.array(predictions)

    def evaluate(self, y_true, y_predicted):
        """
        Evaluate the model on the given data.
        You must implement this method to calculate the total number of correct predictions only.
        Do not use any other evaluation metric.

        Parameters:
        y_true (array-like): True target variable of the data.
        y_predicted (array-like): Predicted target variable of the data.

        Returns:
        score (float): Evaluation score.
        """
        #--- Write your code here ---#
        
        correct = 0

        # Compare the predicted labels to the true labels
        for c in range(len(y_predicted)):
            if y_predicted[c] == y_true[c]:
                correct += 1
        
        # Return the accurace of the model
        return correct/len(y_true)
    
    def decision_boundary(self, X, resolution=200):
        """
        Generate a decision boundary heatmap for visualization.
        
        Parameters:
        X (array-like): Input data.
        resolution (int): Grid resolution (defaults to 200).

        Returns:
        XX, YY, heatmap: Meshgrid and predicted class heatmap.
        """

        # Compute the limits of the grid
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

        # Create a meshgrid with the limits
        XX, YY = np.meshgrid(np.linspace(x_min, x_max, resolution),
                             np.linspace(y_min, y_max, resolution))
        
        heatmap = np.zeros(XX.shape)

        # Iterate over each point in the grid
        for i in range(XX.shape[0]):
            for j in range(XX.shape[1]):
                point = np.array([XX[i, j], YY[i, j]])

                # Compute the most common label of the k nearest points
                heatmap[i, j] = self.predict(point.reshape(1, -1))[0]
        
        # Return the meshgrid and the heatmap
        return XX, YY, heatmap


# Function for turning the csv-files into workable data
def csv_to_array(csv):
    rows = []
    transformer = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    with open(csv, 'r') as file:
        for row in file:
            rows += [row]
    rows.pop(0)
    rows = [row for row in rows if any(value.strip() for value in row)]
    for k, entry in enumerate(rows):
        clean = entry.removesuffix('\n').split(',')
        for i, value in enumerate(clean):
            if clean[i] in transformer:
                clean[i] = int(transformer[value])
            else:
                clean[i] = float(value)
        rows[k] = clean
    return np.array(rows)
