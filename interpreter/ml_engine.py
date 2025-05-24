#!/usr/bin/env python3

"""
Machine Learning Engine for DSL Deep Learning
==============================================

Este módulo contiene todas las implementaciones de algoritmos de machine learning
para el DSL, incluyendo regresión lineal, MLP y redes neuronales profundas.
"""

import sys
import math
import random

# Importar motores locales
from arithmetic_engine import ArithmeticEngine
from matrix_engine import MatrixEngine


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


class MLPClassifierEngine:
    """Multi-Layer Perceptron Classifier using pure Python"""
    
    def __init__(self, hidden_size=10, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        
        # Network weights
        self.weights_input_hidden = None
        self.weights_hidden_output = None
        self.bias_hidden = None
        self.bias_output = None
        
        # Utilities
        self.matrix_engine = MatrixEngine()
        self.arithmetic_engine = ArithmeticEngine()
        self.fitted = False
        
        # Set random seed for reproducibility
        random.seed(42)
    
    def _xavier_initialization(self, n_inputs, n_outputs):
        """Xavier/Glorot weight initialization"""
        limit = math.sqrt(6.0 / (n_inputs + n_outputs))
        weights = []
        for i in range(n_outputs):
            row = []
            for j in range(n_inputs):
                weight = random.uniform(-limit, limit)
                row.append(weight)
            weights.append(row)
        return weights
    
    def _sigmoid(self, x):
        """Sigmoid activation function"""
        # Clip to prevent overflow
        x = max(-250, min(250, x))
        return 1.0 / (1.0 + math.exp(-x))
    
    def _sigmoid_derivative(self, sigmoid_output):
        """Derivative of sigmoid function"""
        return sigmoid_output * (1.0 - sigmoid_output)
    
    def _softmax(self, outputs):
        """Softmax activation function for multi-class classification"""
        # Numerical stability: subtract max value
        max_output = max(outputs)
        exp_outputs = [math.exp(output - max_output) for output in outputs]
        sum_exp = sum(exp_outputs)
        return [exp_output / sum_exp for exp_output in exp_outputs]
    
    def _forward_pass(self, X, activation='sigmoid'):
        """Forward pass through the network"""
        # Input to hidden layer
        hidden_input = []
        for i in range(self.hidden_size):
            weighted_sum = self.bias_hidden[i]
            for j in range(len(X)):
                weighted_sum += X[j] * self.weights_input_hidden[i][j]
            hidden_input.append(weighted_sum)
        
        # Apply activation function to hidden layer
        hidden_output = [self._sigmoid(x) for x in hidden_input]
        
        # Hidden to output layer
        output_input = []
        for i in range(len(self.weights_hidden_output)):
            weighted_sum = self.bias_output[i]
            for j in range(self.hidden_size):
                weighted_sum += hidden_output[j] * self.weights_hidden_output[i][j]
            output_input.append(weighted_sum)
        
        # Apply activation to output layer
        if len(output_input) == 1:
            # Binary classification
            final_output = [self._sigmoid(output_input[0])]
        else:
            # Multi-class classification
            final_output = self._softmax(output_input)
        
        return hidden_input, hidden_output, output_input, final_output
    
    def _backward_pass(self, X, y, hidden_input, hidden_output, output_input, final_output, activation='sigmoid'):
        """Backward pass (backpropagation)"""
        n_classes = len(self.weights_hidden_output)
        
        # Calculate output layer error
        output_errors = []
        if n_classes == 1:
            # Binary classification
            error = final_output[0] - y
            output_errors.append(error)
        else:
            # Multi-class classification
            for i in range(n_classes):
                target = 1.0 if i == y else 0.0
                error = final_output[i] - target
                output_errors.append(error)
        
        # Calculate hidden layer errors
        hidden_errors = []
        for i in range(self.hidden_size):
            error = 0.0
            for j in range(len(output_errors)):
                error += output_errors[j] * self.weights_hidden_output[j][i]
            
            # Apply derivative of activation function
            error *= self._sigmoid_derivative(hidden_output[i])
            hidden_errors.append(error)
        
        # Update weights and biases
        # Output layer weights
        for i in range(len(self.weights_hidden_output)):
            for j in range(self.hidden_size):
                self.weights_hidden_output[i][j] -= self.learning_rate * output_errors[i] * hidden_output[j]
            self.bias_output[i] -= self.learning_rate * output_errors[i]
        
        # Hidden layer weights
        for i in range(self.hidden_size):
            for j in range(len(X)):
                self.weights_input_hidden[i][j] -= self.learning_rate * hidden_errors[i] * X[j]
            self.bias_hidden[i] -= self.learning_rate * hidden_errors[i]
    
    def _prepare_targets(self, y):
        """Prepare target values for training"""
        unique_classes = list(set(y))
        n_classes = len(unique_classes)
        
        # Create class mapping
        class_to_index = {cls: i for i, cls in enumerate(unique_classes)}
        
        if n_classes == 2:
            # Binary classification - use 0/1 targets
            return [1 if label == unique_classes[1] else 0 for label in y], 1
        else:
            # Multi-class classification - use class indices
            return [class_to_index[label] for label in y], n_classes
    
    def fit(self, X, y, activation='sigmoid', verbose=False):
        """
        Fit the MLP classifier
        X: feature matrix (list of lists) or list for single feature
        y: target labels (list)
        activation: activation function ('sigmoid', 'tanh', 'relu')
        """
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        n_samples = len(X)
        n_features = len(X[0])
        
        # Prepare targets
        targets, n_classes = self._prepare_targets(y)
        
        # Initialize weights using Xavier initialization
        self.weights_input_hidden = self._xavier_initialization(n_features, self.hidden_size)
        self.weights_hidden_output = self._xavier_initialization(self.hidden_size, n_classes)
        
        # Initialize biases to zero
        self.bias_hidden = [0.0] * self.hidden_size
        self.bias_output = [0.0] * n_classes
        
        # Training loop
        prev_loss = float('inf')
        
        for epoch in range(self.max_iterations):
            total_loss = 0.0
            
            # Shuffle training data
            indices = list(range(n_samples))
            random.shuffle(indices)
            
            for idx in indices:
                sample = X[idx]
                target = targets[idx]
                
                # Forward pass
                hidden_input, hidden_output, output_input, final_output = self._forward_pass(sample, activation)
                
                # Calculate loss
                if n_classes == 1:
                    # Binary cross-entropy
                    pred = max(1e-15, min(1 - 1e-15, final_output[0]))  # Prevent log(0)
                    loss = -(target * math.log(pred) + (1 - target) * math.log(1 - pred))
                else:
                    # Multi-class cross-entropy
                    pred = max(1e-15, min(1 - 1e-15, final_output[target]))
                    loss = -math.log(pred)
                
                total_loss += loss
                
                # Backward pass
                self._backward_pass(sample, target, hidden_input, hidden_output, 
                                  output_input, final_output, activation)
            
            # Check convergence
            avg_loss = total_loss / n_samples
            if verbose and epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {avg_loss:.6f}")
            
            if abs(prev_loss - avg_loss) < self.tolerance:
                if verbose:
                    print(f"Converged at epoch {epoch}")
                break
            
            prev_loss = avg_loss
        
        self.fitted = True
        self.n_classes = n_classes
        self.classes = list(set(y))
        return self
    
    def predict_proba(self, X, activation='sigmoid'):
        """Predict class probabilities"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        predictions = []
        for sample in X:
            _, _, _, final_output = self._forward_pass(sample, activation)
            
            if self.n_classes == 1:
                # Binary classification - return probability for both classes
                prob_class1 = final_output[0]
                prob_class0 = 1.0 - prob_class1
                predictions.append([prob_class0, prob_class1])
            else:
                # Multi-class classification
                predictions.append(final_output)
        
        return predictions
    
    def predict(self, X, activation='sigmoid'):
        """Make class predictions"""
        probabilities = self.predict_proba(X, activation)
        
        predictions = []
        for prob in probabilities:
            if self.n_classes == 1:
                # Binary classification
                pred_class = self.classes[1] if prob[1] > 0.5 else self.classes[0]
            else:
                # Multi-class classification
                pred_index = prob.index(max(prob))
                pred_class = self.classes[pred_index]
            predictions.append(pred_class)
        
        return predictions
    
    def accuracy(self, X, y, activation='sigmoid'):
        """Calculate accuracy"""
        predictions = self.predict(X, activation)
        correct = sum(1 for pred, true in zip(predictions, y) if pred == true)
        return correct / len(y)


class NeuralNetworkEngine:
    """Deep Neural Network implementation using pure Python"""
    
    def __init__(self, architecture=None, learning_rate=0.001, max_epochs=1000, 
                 batch_size=32, tolerance=1e-6):
        """
        Initialize Neural Network
        architecture: list of layer sizes [input_size, hidden1, hidden2, ..., output_size]
        learning_rate: learning rate for gradient descent
        max_epochs: maximum training epochs
        batch_size: size of mini-batches
        tolerance: convergence tolerance
        """
        self.architecture = architecture or [1, 10, 1]
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.batch_size = batch_size
        self.tolerance = tolerance
        
        # Network parameters
        self.weights = []
        self.biases = []
        
        # Training history
        self.loss_history = []
        self.fitted = False
        
        # Utilities
        self.matrix_engine = MatrixEngine()
        self.arithmetic_engine = ArithmeticEngine()
        
        # Set random seed
        random.seed(42)
    
    def _he_initialization(self, fan_in, fan_out):
        """He initialization for ReLU networks"""
        stddev = math.sqrt(2.0 / fan_in)
        weights = []
        for i in range(fan_out):
            row = []
            for j in range(fan_in):
                weight = random.gauss(0, stddev)
                row.append(weight)
            weights.append(row)
        return weights
    
    def _initialize_parameters(self, initialization='he'):
        """Initialize network weights and biases"""
        self.weights = []
        self.biases = []
        
        for i in range(len(self.architecture) - 1):
            fan_in = self.architecture[i]
            fan_out = self.architecture[i + 1]
            
            if initialization == 'he':
                layer_weights = self._he_initialization(fan_in, fan_out)
            else:
                # Xavier initialization
                limit = math.sqrt(6.0 / (fan_in + fan_out))
                layer_weights = []
                for j in range(fan_out):
                    row = []
                    for k in range(fan_in):
                        weight = random.uniform(-limit, limit)
                        row.append(weight)
                    layer_weights.append(row)
            
            layer_biases = [0.0] * fan_out
            
            self.weights.append(layer_weights)
            self.biases.append(layer_biases)
    
    def _relu(self, x):
        """ReLU activation function"""
        return max(0, x)
    
    def _relu_derivative(self, x):
        """ReLU derivative"""
        return 1.0 if x > 0 else 0.0
    
    def _sigmoid(self, x):
        """Sigmoid activation function"""
        x = max(-250, min(250, x))
        return 1.0 / (1.0 + math.exp(-x))
    
    def _sigmoid_derivative(self, sigmoid_output):
        """Sigmoid derivative"""
        return sigmoid_output * (1.0 - sigmoid_output)
    
    def forward_pass(self, X, hidden_activation='relu', output_activation='linear'):
        """Forward pass through the network"""
        activations = [X[:]]  # Store all layer activations
        z_values = []  # Store pre-activation values
        
        current_activation = X[:]
        
        for i in range(len(self.weights)):
            # Linear transformation
            z = []
            for j in range(len(self.weights[i])):
                weighted_sum = self.biases[i][j]
                for k in range(len(current_activation)):
                    weighted_sum += self.weights[i][j][k] * current_activation[k]
                z.append(weighted_sum)
            
            z_values.append(z[:])
            
            # Apply activation function
            if i == len(self.weights) - 1:
                # Output layer
                if output_activation == 'linear':
                    current_activation = z[:]
                else:
                    current_activation = [self._sigmoid(zi) for zi in z]
            else:
                # Hidden layer
                if hidden_activation == 'relu':
                    current_activation = [self._relu(zi) for zi in z]
                else:
                    current_activation = [self._sigmoid(zi) for zi in z]
            
            activations.append(current_activation[:])
        
        return activations, z_values
    
    def fit(self, X, y, task_type='regression', hidden_activation='relu', 
            output_activation='linear', verbose=False):
        """
        Train the neural network
        X: input features (list of lists)
        y: target values (list or list of lists for multi-output)
        task_type: 'regression', 'binary_classification', 'multiclass_classification'
        """
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        # Set architecture if not provided
        if not self.architecture or len(self.architecture) < 2:
            n_features = len(X[0])
            n_outputs = len(y[0]) if isinstance(y[0], list) else 1
            self.architecture = [n_features, 10, n_outputs]
        
        # Initialize parameters
        self._initialize_parameters()
        
        # Convert targets for different task types
        if task_type == 'multiclass_classification' and not isinstance(y[0], list):
            # Convert class labels to indices
            unique_classes = sorted(list(set(y)))
            class_to_idx = {cls: i for i, cls in enumerate(unique_classes)}
            y = [[class_to_idx[label]] for label in y]
            self.architecture[-1] = len(unique_classes)
            self._initialize_parameters()  # Re-initialize with correct output size
        elif task_type == 'regression' and not isinstance(y[0], list):
            # Convert to list format
            y = [[target] for target in y]
        
        n_samples = len(X)
        
        # Training loop
        self.loss_history = []
        prev_loss = float('inf')
        
        for epoch in range(self.max_epochs):
            epoch_loss = 0.0
            
            # Shuffle training data
            indices = list(range(n_samples))
            random.shuffle(indices)
            
            for idx in indices:
                sample = X[idx]
                target = y[idx]
                
                # Forward pass
                activations, z_values = self.forward_pass(sample, hidden_activation, output_activation)
                
                # Calculate loss
                if task_type == 'regression':
                    loss = sum((pred - true) ** 2 for pred, true in zip(activations[-1], target)) / len(target)
                else:
                    # Classification loss (simplified)
                    pred = activations[-1][0]
                    pred = max(1e-15, min(1 - 1e-15, pred))
                    loss = -(target[0] * math.log(pred) + (1 - target[0]) * math.log(1 - pred))
                
                epoch_loss += loss
                
                # Simplified backward pass (gradient descent)
                self._simple_backward_pass(sample, target, activations, z_values, 
                                         hidden_activation, output_activation, task_type)
            
            avg_loss = epoch_loss / n_samples
            self.loss_history.append(avg_loss)
            
            if verbose and epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {avg_loss:.6f}")
            
            # Check convergence
            if abs(prev_loss - avg_loss) < self.tolerance:
                if verbose:
                    print(f"Converged at epoch {epoch}")
                break
            
            prev_loss = avg_loss
        
        self.fitted = True
        self.task_type = task_type
        self.hidden_activation = hidden_activation
        self.output_activation = output_activation
        
        return self
    
    def _simple_backward_pass(self, X, y, activations, z_values, 
                            hidden_activation, output_activation, task_type):
        """Simplified backward pass implementation"""
        n_layers = len(self.weights)
        
        # Calculate output layer error
        if task_type == 'regression':
            output_errors = [pred - true for pred, true in zip(activations[-1], y)]
        else:
            # Binary classification
            output_errors = [activations[-1][0] - y[0]]
        
        # Update output layer
        for i in range(len(self.weights[-1])):
            for j in range(len(self.weights[-1][i])):
                gradient = output_errors[i] * activations[-2][j]
                self.weights[-1][i][j] -= self.learning_rate * gradient
            self.biases[-1][i] -= self.learning_rate * output_errors[i]
        
        # Update hidden layers (simplified)
        for layer in range(n_layers - 2, -1, -1):
            for i in range(len(self.weights[layer])):
                for j in range(len(self.weights[layer][i])):
                    # Simplified gradient calculation
                    gradient = 0.01 * activations[layer][j]  # Simplified
                    self.weights[layer][i][j] -= self.learning_rate * gradient
    
    def predict(self, X):
        """Make predictions"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        predictions = []
        for sample in X:
            activations, _ = self.forward_pass(sample, self.hidden_activation, self.output_activation)
            predictions.append(activations[-1][:])
        
        return predictions
    
    def score(self, X, y):
        """Calculate score based on task type"""
        if not self.fitted:
            raise ValueError("Model must be fitted before scoring")
        
        predictions = self.predict(X)
        
        if self.task_type == 'regression':
            # R^2 score
            if not isinstance(y[0], list):
                y = [[target] for target in y]
            
            y_flat = [target[0] for target in y]
            pred_flat = [pred[0] for pred in predictions]
            
            y_mean = self.arithmetic_engine.mean(y_flat)
            ss_res = sum((true - pred) ** 2 for true, pred in zip(y_flat, pred_flat))
            ss_tot = sum((true - y_mean) ** 2 for true in y_flat)
            
            return 1 - (ss_res / ss_tot) if ss_tot != 0 else 1.0
        
        else:
            # Accuracy for classification
            correct = 0
            for i in range(len(y)):
                pred_class = 1 if predictions[i][0] > 0.5 else 0
                true_class = y[i] if not isinstance(y[i], list) else y[i][0]
                
                if pred_class == true_class:
                    correct += 1
            
            return correct / len(y)