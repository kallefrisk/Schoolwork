from abc import ABC, abstractmethod
import numpy as np

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
    def evaluate(self, X, y):
        """
        Evaluate the model on the given data.

        Parameters:
        X (array-like): Features of the data.
        y (array-like): Target variable of the data.

        Returns:
        score (float): Evaluation score.
        """
        pass

class RegressionModelNormalEquation(MachineLearningModel):
    """
    Class for regression models using the Normal Equation for polynomial regression.
    """

    def __init__(self, degree):
        """
        Initialize the model with the specified polynomial degree.

        Parameters:
        degree (int): Degree of the polynomial features.
        """
        #--- Write your code here ---#
        self.degree = degree

    def fit(self, X, y):
        """
        Train the model using the given training data.

        Parameters:
        X (array-like): Features of the training data.
        y (array-like): Target variable of the training data.

        Returns:
        None
        """
        #--- Write your code here ---#

        Xe = _polynomial_features(X, self.degree)

        # Use linear algebra to find the best betas in a LeastSquares-sense
        self.beta = np.linalg.inv(Xe.T @ Xe) @ Xe.T @ y

        # Compute the cost-function
        self.cost = ((Xe @ self.beta - y).T @ (Xe @ self.beta - y)) / len(y)

    def predict(self, X):
        """
        Make predictions on new data.

        Parameters:
        X (array-like): Features of the new data.

        Returns:
        predictions (array-like): Predicted values.
        """
        #--- Write your code here ---#

        # Multiply the found betas with the testdata
        return _polynomial_features(X, self.degree) @ self.beta

    def evaluate(self, y_true, y_predicted):
        """
        Evaluate the model on the given data.

        Parameters:
        y_true (array-like): true target values.
        y_predicted (array-like): predicted target values.

        Returns:
        score (float): Evaluation score (MSE).
        """
        #--- Write your code here ---#

        return np.mean((y_true - y_predicted)**2, axis=0)


class RegressionModelGradientDescent(MachineLearningModel):
    """
    Class for regression models using gradient descent optimization.
    """

    def __init__(self, degree, learning_rate=0.01, num_iterations=1000):
        """
        Initialize the model with the specified parameters.

        Parameters:
        degree (int): Degree of the polynomial features.
        learning_rate (float): Learning rate for gradient descent.
        num_iterations (int): Number of iterations for gradient descent.
        """
        #--- Write your code here ---#
        self.degree = degree
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.list_of_cost = None
        self.beta = None
        self.count = None

    def fit(self, X, y, beta=None, tol=None):
        """
        Train the model using the given training data.

        Parameters:
        X (array-like): Features of the training data.
        y (array-like): Target variable of the training data.

        Returns:
        None
        """
        #--- Write your code here ---#

        Xe = _polynomial_features(X, self.degree)

        # Start all betas at zero (0, 0, ... 0) unless specific beta given
        if beta is None:
            self.beta = np.zeros((Xe.shape[1], 1))

        self.list_of_cost = np.empty((self.num_iterations, 1))

        if tol is None:

            # Iterate the new betas recursively as well as the cost function
            for k in range(self.num_iterations):
                self.list_of_cost[k] = (((Xe @ self.beta - y).T @ (Xe @ self.beta - y)) / Xe.shape[0])
                self.beta = self.beta - (2 * self.learning_rate / Xe.shape[0]) * (Xe.T @ (Xe @ self.beta - y))
        
        else:

            true_beta = np.linalg.inv(Xe.T @ Xe) @ Xe.T @ y

            true_value = ((Xe @ true_beta - y).T @ (Xe @ true_beta - y)) / len(y)

            self.count = 0

            # Iterate the new betas recursively until the cost function gets under the tolerance given
            while abs(true_value - ((Xe @ self.beta - y).T @ (Xe @ self.beta - y)) / len(y)) / true_value > tol:
                self.beta = self.beta - (2 * self.learning_rate / Xe.shape[0]) * (Xe.T @ (Xe @ self.beta - y))
                self.count += 1

    def predict(self, X):
        """
        Make predictions on new data.

        Parameters:
        X (array-like): Features of the new data.

        Returns:
        predictions (array-like): Predicted values.
        """
        #--- Write your code here ---#

        # Multiply the found betas with the testdata
        return _polynomial_features(X, self.degree) @ self.beta

    def evaluate(self, y_true, y_predicted):
        """
        Evaluate the model on the given data.

        Parameters:
        y_true (array-like): true target values.
        y_predicted (array-like): predicted target values.

        Returns:
        score (float): Evaluation score (MSE).
        """
        #--- Write your code here ---#

        return np.mean(((y_true - y_predicted))**2, axis=0)

class LogisticRegression:
    """
    Logistic Regression model using gradient descent optimization.
    """

    def __init__(self, degree=1, learning_rate=0.01, num_iterations=1000):
        """
        Initialize the logistic regression model.

        Parameters:
        learning_rate (float): The learning rate for gradient descent.
        num_iterations (int): The number of iterations for gradient descent.
        """
        #--- Write your code here ---#
        self.degree = degree
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.list_of_cost = None

    def fit(self, X, y, beta=None, pure_powers=True):
        """
        Train the logistic regression model using gradient descent.

        Parameters:
        X (array-like): Features of the training data.
        y (array-like): Target variable of the training data.
        beta (array-like): Starting values for the betas, default zeros

        Returns:
        None
        """
        #--- Write your code here ---#

        if pure_powers:
            Xe = _polynomial_features(X, self.degree)
        else:
            Xe = self.mapFeature(X[:, 0], X[:, 1], self.degree)

        if beta is None:
            self.beta = np.zeros((Xe.shape[1], 1))
        else:
            self.beta = beta

        self.list_of_cost = np.empty((self.num_iterations, 1))

        if pure_powers:
            for k in range(self.num_iterations):
                z = Xe @ self.beta
                self.list_of_cost[k] = self._cost_function(X, y)
                self.beta -= self.learning_rate * (Xe.T @ (self._sigmoid(z) - y)) / Xe.shape[0]
        else:
            for k in range(self.num_iterations):
                z = Xe @ self.beta
                self.beta -= self.learning_rate * (Xe.T @ (self._sigmoid(z) - y)) / Xe.shape[0]

    def predict(self, X, pure_powers=True):
        """
        Make predictions using the trained logistic regression model.

        Parameters:
        X (array-like): Features of the new data.

        Returns:
        predictions (array-like): Predicted probabilities.
        """
        #--- Write your code here ---#

        if pure_powers:
            Xe = _polynomial_features(X, self.degree)
        else:
            Xe = self.mapFeature(X[:, 0], X[:, 1], self.degree)

        return (self._sigmoid(Xe @ self.beta) >= 0.5).astype(int)

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
        
        # Return the accuracy of the model
        return np.mean(y_true.ravel() == y_predicted.ravel())

    def _sigmoid(self, z):
        """
        Sigmoid function.

        Parameters:
        z (array-like): Input to the sigmoid function.

        Returns:
        result (array-like): Output of the sigmoid function.
        """
        #--- Write your code here ---#
        return 1 / (1 + np.exp(-z))

    def _cost_function(self, X, y):
        """
        Compute the logistic regression cost function.

        Parameters:
        X (array-like): Features of the data.
        y (array-like): Target variable of the data.

        Returns:
        cost (float): The logistic regression cost.
        """
        #--- Write your code here ---#

        Xe = _polynomial_features(X, self.degree)

        predictions = self._sigmoid(Xe @ self.beta)

        return (- (1 / Xe.shape[0]) * np.sum(y * np.log(predictions + 1e-15) + (1 - y) * np.log(1 - predictions + 1e-15)))

    def mapFeature(self, X1, X2, D):
        """
        Map the features to a higher-dimensional space using polynomial features.
        Check the slides to have hints on how to implement this function.
        Parameters:
        X1 (array-like): Feature 1.
        X2 (array-like): Feature 2.
        D (int): Degree of polynomial features.

        Returns:
        X_poly (array-like): Polynomial features.
        """
        #--- Write your code here ---#

        one = np.ones([len(X1), 1])
        Xe = np.c_[one, X1, X2]  # Start with [1,X1,X2]
        for i in range(2, D+1):
            for j in range(0, i+1):
                Xnew = X1**(i-j)*X2**j  # type (N)
                Xnew = Xnew.reshape(-1, 1)  # type (N,1) required by append
                Xe = np.append(Xe, Xnew, 1)  # axis = 1 ==> append column
        return Xe

    
class NonLinearLogisticRegression:
    """
    Nonlinear Logistic Regression model using gradient descent optimization.
    It works for 2 features (when creating the variable interactions)
    """

    def __init__(self, degree=2, learning_rate=0.01, num_iterations=1000):
        """
        Initialize the nonlinear logistic regression model.

        Parameters:
        degree (int): Degree of polynomial features.
        learning_rate (float): The learning rate for gradient descent.
        num_iterations (int): The number of iterations for gradient descent.
        """
        #--- Write your code here ---#
        self.degree = degree
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.list_of_cost = None

    def fit(self, X, y, beta=None, pure_powers=True):
        """
        Train the nonlinear logistic regression model using gradient descent.

        Parameters:
        X (array-like): Features of the training data.
        y (array-like): Target variable of the training data.

        Returns:
        None
        """
        #--- Write your code here ---#

        if pure_powers:
            Xe = _polynomial_features(X, self.degree)
        else:
            Xe = self.mapFeature(X[:, 0], X[:, 1], self.degree)

        if beta is None:
            self.beta = np.zeros((Xe.shape[1], 1))
        else:
            self.beta = beta
        
        self.list_of_cost = np.empty((self.num_iterations, 1))

        if pure_powers:
            for k in range(self.num_iterations):
                z = Xe @ self.beta
                self.list_of_cost[k] = self._cost_function(X, y)
                self.beta -= self.learning_rate * (Xe.T @ (self._sigmoid(z) - y)) / Xe.shape[0]
        else:
            for k in range(self.num_iterations):
                z = Xe @ self.beta
                self.beta -= self.learning_rate * (Xe.T @ (self._sigmoid(z) - y)) / Xe.shape[0]
        

    def predict(self, X, pure_powers=True):
        """
        Make predictions using the trained nonlinear logistic regression model.

        Parameters:
        X (array-like): Features of the new data.

        Returns:
        predictions (array-like): Predicted probabilities.
        """
        #--- Write your code here ---#

        if pure_powers:
            Xe = _polynomial_features(X, self.degree)
        else:
            Xe = self.mapFeature(X[:, 0], X[:, 1], self.degree)

        return (self._sigmoid(Xe @ self.beta) >= 0.5).astype(int)

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
        
        # Return the accuracy of the model
        return np.mean(y_true.ravel() == y_predicted.ravel())

    def _sigmoid(self, z):
        """
        Sigmoid function.

        Parameters:
        z (array-like): Input to the sigmoid function.

        Returns:
        result (array-like): Output of the sigmoid function.
        """
        #--- Write your code here ---#

        return 1 / (1 + np.exp(-z))

    def mapFeature(self, X1, X2, D):
        """
        Map the features to a higher-dimensional space using polynomial features.
        Check the slides to have hints on how to implement this function.
        Parameters:
        X1 (array-like): Feature 1.
        X2 (array-like): Feature 2.
        D (int): Degree of polynomial features.

        Returns:
        X_poly (array-like): Polynomial features.
        """
        #--- Write your code here ---#

        one = np.ones([len(X1), 1])
        Xe = np.c_[one, X1, X2]  # Start with [1,X1,X2]
        for i in range(2, D+1):
            for j in range(0, i+1):
                Xnew = X1**(i-j)*X2**j  # type (N)
                Xnew = Xnew.reshape(-1, 1)  # type (N,1) required by append
                Xe = np.append(Xe, Xnew, 1)  # axis = 1 ==> append column
        return Xe


    def _cost_function(self, X, y):
        """
        Compute the logistic regression cost function.

        Parameters:
        X (array-like): Features of the data.
        y (array-like): Target variable of the data.

        Returns:
        cost (float): The logistic regression cost.
        """
        #--- Write your code here ---#

        Xe = _polynomial_features(X, self.degree)

        predictions = self._sigmoid(Xe @ self.beta)

        return (- (1 / Xe.shape[0]) * np.sum(y * np.log(predictions + 1e-15) + (1 - y) * np.log(1 - predictions + 1e-15)))


def _polynomial_features(X, degree):
    """
        Generate polynomial features from the input features.
        Check the slides for hints on how to implement this one. 
        This method is used by the regression models and must work
        for any degree polynomial
        Parameters:
        X (array-like): Features of the data.

        Returns:
        X_poly (array-like): Polynomial features.
    """
    #--- Write your code here ---#
    return np.c_[np.ones([X.shape[0], 1]), *[X**i for i in range(1, degree + 1)]]