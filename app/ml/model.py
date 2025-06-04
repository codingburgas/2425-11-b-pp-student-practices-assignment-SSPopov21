import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None
        
    def sigmoid(self, z):
        """Compute sigmoid function"""
        return 1 / (1 + np.exp(-z))
    
    def initialize_parameters(self, n_features):
        """Initialize weights and bias"""
        self.weights = np.zeros((n_features,))
        self.bias = 0
        
    def fit(self, X, y):
        """Train the model using gradient descent"""
        m = X.shape[0]  # number of training examples
        n = X.shape[1]  # number of features
        
        # Initialize parameters
        self.initialize_parameters(n)
        
        # Gradient descent
        for _ in range(self.num_iterations):
            # Forward propagation
            z = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(z)
            
            # Compute gradients
            dz = predictions - y
            dw = (1/m) * np.dot(X.T, dz)
            db = (1/m) * np.sum(dz)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
    
    def predict_proba(self, X):
        """Predict probability of success"""
        z = np.dot(X, self.weights) + self.bias
        return self.sigmoid(z)
    
    def predict(self, X, threshold=0.5):
        """Predict class labels"""
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)

def prepare_data(surveys):
    """Convert survey data to numpy arrays for training"""
    X = np.array([survey.to_feature_vector() for survey in surveys])
    y = np.array([1 if survey.success else 0 for survey in surveys])
    return X, y

def normalize_features(X):
    """Normalize features to have zero mean and unit variance"""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std, mean, std 