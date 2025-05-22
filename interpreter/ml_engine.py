import sys
import math
import random
sys.path.append('./math_engine')
from matrix_engine import MatrixEngine
from arithmetic_engine import ArithmeticEngine

class LinearRegressionEngine:
    """Linear regression implementation using pure Python"""
    
    def __init__(self):
        self.matrix_engine = MatrixEngine()
        self.arithmetic_engine = ArithmeticEngine()
        self.coefficients = None
        self.intercept = None
        self.fitted = False
    
    def fit(self, X, y):
        """
        Fit linear regression model
        X: feature matrix (list of lists) or list for single feature
        y: target values (list)
        Returns: self (fitted model)
        """
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        # Validate dimensions
        if len(X) != len(y):
            raise ValueError("X and y must have same number of samples")
        
        n_samples = len(X)
        n_features = len(X[0])
        
        # Add bias column (intercept term)
        X_with_bias = []
        for i in range(n_samples):
            row = [1] + X[i]  # Add 1 as first column
            X_with_bias.append(row)
        
        # Calculate coefficients using normal equation: θ = (X^T X)^(-1) X^T y
        try:
            # X^T
            X_T = self.matrix_engine.transpose(X_with_bias)
            
            # X^T X
            XTX = self.matrix_engine.multiply(X_T, X_with_bias)
            
            # (X^T X)^(-1)
            XTX_inv = self.matrix_engine.inverse(XTX)
            
            # X^T y
            # Convert y to column vector for matrix multiplication
            y_matrix = [[val] for val in y]
            XTy = self.matrix_engine.multiply(X_T, y_matrix)
            
            # Final coefficients
            theta = self.matrix_engine.multiply(XTX_inv, XTy)
            
            # Extract intercept and coefficients
            self.intercept = theta[0][0]
            self.coefficients = [theta[i][0] for i in range(1, len(theta))]
            
            self.fitted = True
            return self
            
        except ValueError as e:
            raise ValueError(f"Unable to fit linear regression: {e}")
    
    def predict(self, X):
        """
        Make predictions using fitted model
        X: feature matrix or list for single feature
        Returns: list of predictions
        """
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        predictions = []
        for sample in X:
            # Calculate prediction: y = intercept + sum(coef * feature)
            prediction = self.intercept
            for i, feature_value in enumerate(sample):
                prediction += self.coefficients[i] * feature_value
            predictions.append(prediction)
        
        return predictions
    
    def score(self, X, y):
        """
        Calculate R^2 score (coefficient of determination)
        X: feature matrix
        y: true target values
        Returns: R^2 score
        """
        if not self.fitted:
            raise ValueError("Model must be fitted before scoring")
        
        y_pred = self.predict(X)
        
        # Calculate R^2 = 1 - (SS_res / SS_tot)
        y_mean = self.arithmetic_engine.mean(y)
        
        # Sum of squares of residuals
        ss_res = sum((y_true - y_pred_val) ** 2 for y_true, y_pred_val in zip(y, y_pred))
        
        # Total sum of squares
        ss_tot = sum((y_true - y_mean) ** 2 for y_true in y)
        
        if ss_tot == 0:
            return 1.0 if ss_res == 0 else 0.0
        
        r2_score = 1 - (ss_res / ss_tot)
        return r2_score
    
    def mean_squared_error(self, X, y):
        """Calculate mean squared error"""
        if not self.fitted:
            raise ValueError("Model must be fitted before calculating MSE")
        
        y_pred = self.predict(X)
        mse = sum((y_true - y_pred_val) ** 2 for y_true, y_pred_val in zip(y, y_pred)) / len(y)
        return mse
    
    def mean_absolute_error(self, X, y):
        """Calculate mean absolute error"""
        if not self.fitted:
            raise ValueError("Model must be fitted before calculating MAE")
        
        y_pred = self.predict(X)
        mae = sum(abs(y_true - y_pred_val) for y_true, y_pred_val in zip(y, y_pred)) / len(y)
        return mae
    
    def root_mean_squared_error(self, X, y):
        """Calculate root mean squared error"""
        return self.mean_squared_error(X, y) ** 0.5
    
    def residuals(self, X, y):
        """Calculate residuals (y_true - y_pred)"""
        if not self.fitted:
            raise ValueError("Model must be fitted before calculating residuals")
        
        y_pred = self.predict(X)
        return [y_true - y_pred_val for y_true, y_pred_val in zip(y, y_pred)]
    
    def get_coefficients(self):
        """Get fitted coefficients"""
        if not self.fitted:
            raise ValueError("Model must be fitted first")
        return {
            'intercept': self.intercept,
            'coefficients': self.coefficients.copy()
        }
    
    def feature_importance(self):
        """Get absolute values of coefficients as feature importance"""
        if not self.fitted:
            raise ValueError("Model must be fitted first")
        return [abs(coef) for coef in self.coefficients]


class PolynomialRegressionEngine:
    """Polynomial regression using linear regression with polynomial features"""
    
    def __init__(self, degree=2):
        self.degree = degree
        self.linear_reg = LinearRegressionEngine()
        self.fitted = False
    
    def _create_polynomial_features(self, X):
        """Create polynomial features up to given degree"""
        # For single feature polynomial regression
        if isinstance(X[0], (int, float)):
            X_poly = []
            for x in X:
                features = []
                for d in range(1, self.degree + 1):
                    features.append(x ** d)
                X_poly.append(features)
            return X_poly
        else:
            # For multiple features (interaction terms)
            raise NotImplementedError("Multiple feature polynomial regression not implemented")
    
    def fit(self, X, y):
        """Fit polynomial regression model"""
        X_poly = self._create_polynomial_features(X)
        self.linear_reg.fit(X_poly, y)
        self.fitted = True
        return self
    
    def predict(self, X):
        """Make predictions using polynomial features"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        X_poly = self._create_polynomial_features(X)
        return self.linear_reg.predict(X_poly)
    
    def score(self, X, y):
        """Calculate R^2 score"""
        if not self.fitted:
            raise ValueError("Model must be fitted before scoring")
        X_poly = self._create_polynomial_features(X)
        return self.linear_reg.score(X_poly, y)


class RidgeRegressionEngine:
    """Ridge regression with L2 regularization"""
    
    def __init__(self, alpha=1.0):
        self.alpha = alpha  # Regularization strength
        self.matrix_engine = MatrixEngine()
        self.coefficients = None
        self.intercept = None
        self.fitted = False
    
    def fit(self, X, y):
        """Fit ridge regression model"""
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        n_samples = len(X)
        n_features = len(X[0])
        
        # Center the data
        X_mean = [sum(col) / n_samples for col in zip(*X)]
        y_mean = sum(y) / n_samples
        
        # Center X and y
        X_centered = []
        for row in X:
            centered_row = [row[i] - X_mean[i] for i in range(n_features)]
            X_centered.append(centered_row)
        
        y_centered = [val - y_mean for val in y]
        
        # Ridge regression: θ = (X^T X + α I)^(-1) X^T y
        try:
            # X^T
            X_T = self.matrix_engine.transpose(X_centered)
            
            # X^T X
            XTX = self.matrix_engine.multiply(X_T, X_centered)
            
            # Add regularization: X^T X + α I
            regularization = self.matrix_engine.scalar_multiply(
                self.matrix_engine.create_identity(n_features), self.alpha)
            XTX_reg = self.matrix_engine.add(XTX, regularization)
            
            # (X^T X + α I)^(-1)
            XTX_reg_inv = self.matrix_engine.inverse(XTX_reg)
            
            # X^T y
            y_matrix = [[val] for val in y_centered]
            XTy = self.matrix_engine.multiply(X_T, y_matrix)
            
            # Final coefficients
            theta = self.matrix_engine.multiply(XTX_reg_inv, XTy)
            
            # Extract coefficients
            self.coefficients = [theta[i][0] for i in range(len(theta))]
            
            # Calculate intercept
            self.intercept = y_mean - sum(coef * x_mean for coef, x_mean in zip(self.coefficients, X_mean))
            
            self.fitted = True
            return self
            
        except ValueError as e:
            raise ValueError(f"Unable to fit ridge regression: {e}")
    
    def predict(self, X):
        """Make predictions using fitted model"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        predictions = []
        for sample in X:
            # Calculate prediction: y = intercept + sum(coef * feature)
            prediction = self.intercept
            for i, feature_value in enumerate(sample):
                prediction += self.coefficients[i] * feature_value
            predictions.append(prediction)
        
        return predictions


class LogisticRegressionEngine:
    """Logistic regression for binary classification"""
    
    def __init__(self, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.weights = None
        self.intercept = None
        self.fitted = False
    
    def _sigmoid(self, z):
        """Sigmoid activation function"""
        # Clip z to prevent overflow
        z = max(-250, min(250, z))
        return 1 / (1 + (2.718281828459045 ** (-z)))  # Using e ≈ 2.718281828459045
    
    def _log_likelihood(self, X, y):
        """Calculate log-likelihood"""
        total = 0
        for i in range(len(X)):
            z = self.intercept + sum(self.weights[j] * X[i][j] for j in range(len(X[i])))
            p = self._sigmoid(z)
            # Avoid log(0)
            p = max(1e-15, min(1 - 1e-15, p))
            total += y[i] * (z - (-1) * (2.718281828459045 ** z)) + (1 - y[i]) * (-1) * (2.718281828459045 ** z)
        return total
    
    def fit(self, X, y):
        """Fit logistic regression using gradient descent"""
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        n_samples = len(X)
        n_features = len(X[0])
        
        # Initialize weights
        self.weights = [0.0] * n_features
        self.intercept = 0.0
        
        prev_likelihood = float('-inf')
        
        for iteration in range(self.max_iterations):
            # Calculate predictions
            predictions = []
            for i in range(n_samples):
                z = self.intercept + sum(self.weights[j] * X[i][j] for j in range(n_features))
                p = self._sigmoid(z)
                predictions.append(p)
            
            # Calculate gradients
            intercept_gradient = 0
            weight_gradients = [0.0] * n_features
            
            for i in range(n_samples):
                error = predictions[i] - y[i]
                intercept_gradient += error
                for j in range(n_features):
                    weight_gradients[j] += error * X[i][j]
            
            # Update parameters
            self.intercept -= self.learning_rate * intercept_gradient / n_samples
            for j in range(n_features):
                self.weights[j] -= self.learning_rate * weight_gradients[j] / n_samples
            
            # Check convergence
            if iteration % 100 == 0:
                current_likelihood = self._log_likelihood(X, y)
                if abs(current_likelihood - prev_likelihood) < self.tolerance:
                    break
                prev_likelihood = current_likelihood
        
        self.fitted = True
        return self
    
    def predict_proba(self, X):
        """Predict class probabilities"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        probabilities = []
        for sample in X:
            z = self.intercept + sum(self.weights[i] * sample[i] for i in range(len(sample)))
            p = self._sigmoid(z)
            probabilities.append(p)
        
        return probabilities
    
    def predict(self, X, threshold=0.5):
        """Make binary predictions"""
        probabilities = self.predict_proba(X)
        return [1 if p >= threshold else 0 for p in probabilities]
    
    def accuracy(self, X, y):
        """Calculate accuracy"""
        predictions = self.predict(X)
        correct = sum(1 for pred, true in zip(predictions, y) if pred == true)
        return correct / len(y)
