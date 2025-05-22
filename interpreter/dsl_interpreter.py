import sys
sys.path.append('./generated')

from antlr4 import *
from DeepLearningDSLLexer import DeepLearningDSLLexer
from DeepLearningDSLParser import DeepLearningDSLParser
from DeepLearningDSLBaseVisitor import DeepLearningDSLBaseVisitor

# Import our engines
from arithmetic_engine import ArithmeticEngine
from matrix_engine import MatrixEngine
from ml_engine import LinearRegressionEngine, MLPClassifierEngine, NeuralNetworkEngine
from file_manager import FileManager
from plotter import Plotter


class DSLInterpreter(DeepLearningDSLBaseVisitor):
    def __init__(self):
        # Symbol tables
        self.variables = {}
        self.functions = {}
        
        # Engines
        self.arithmetic = ArithmeticEngine()
        self.matrix = MatrixEngine()
        self.linear_reg = LinearRegressionEngine()
        self.mlp = MLPClassifierEngine()
        self.neural_net = NeuralNetworkEngine()
        self.file_manager = FileManager()
        self.plotter = Plotter()
        
        # Flag for return values
        self.return_value = None
        self.in_function = False
    
    def visitProgram(self, ctx):
        """Visit the main program"""
        return self.visit(ctx.statement_list())
    
    def visitStatement_list(self, ctx):
        """Visit a list of statements"""
        if ctx.statement():
            # Visit first statement
            result = self.visit(ctx.statement())
            
            # If there's a return in function, stop executing
            if self.return_value is not None and self.in_function:
                return self.return_value
                
            # Visit rest of statements
            if ctx.statement_list():
                rest_result = self.visit(ctx.statement_list())
                return rest_result if rest_result is not None else result
        return None
    
    def visitStatement(self, ctx):
        """Visit a single statement"""
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.conditional():
            return self.visit(ctx.conditional())
        elif ctx.loop():
            return self.visit(ctx.loop())
        elif ctx.function_def():
            return self.visit(ctx.function_def())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None
    
    def visitAssignment(self, ctx):
        """Handle variable assignment"""
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value
    
    def visitExpression(self, ctx):
        """Evaluate expressions with precedence"""
        term_value = self.visit(ctx.term())
        return self.visit_expr_rest(ctx.expr_rest(), term_value)
    
    def visit_expr_rest(self, ctx, left_value):
        """Handle expression rest (+ and - operations)"""
        if not ctx:
            return left_value
            
        if ctx.PLUS():
            right_value = self.visit(ctx.term())
            result = self.arithmetic.add(left_value, right_value)
            return self.visit_expr_rest(ctx.expr_rest(), result)
        elif ctx.MINUS():
            right_value = self.visit(ctx.term())
            result = self.arithmetic.subtract(left_value, right_value)
            return self.visit_expr_rest(ctx.expr_rest(), result)
        else:
            return left_value
    
    def visitTerm(self, ctx):
        """Evaluate terms (*, /, % operations)"""
        factor_value = self.visit(ctx.factor())
        return self.visit_term_rest(ctx.term_rest(), factor_value)
    
    def visit_term_rest(self, ctx, left_value):
        """Handle term rest (*, /, % operations)"""
        if not ctx:
            return left_value
            
        if ctx.MULT():
            right_value = self.visit(ctx.factor())
            result = self.arithmetic.multiply(left_value, right_value)
            return self.visit_term_rest(ctx.term_rest(), result)
        elif ctx.DIV():
            right_value = self.visit(ctx.factor())
            result = self.arithmetic.divide(left_value, right_value)
            return self.visit_term_rest(ctx.term_rest(), result)
        elif ctx.MOD():
            right_value = self.visit(ctx.factor())
            result = self.arithmetic.modulo(left_value, right_value)
            return self.visit_term_rest(ctx.term_rest(), result)
        else:
            return left_value
    
    def visitFactor(self, ctx):
        """Evaluate factors (^ operations)"""
        base_value = self.visit(ctx.base())
        return self.visit_factor_rest(ctx.factor_rest(), base_value)
    
    def visit_factor_rest(self, ctx, left_value):
        """Handle factor rest (^ operation)"""
        if not ctx:
            return left_value
            
        if ctx.POWER():
            right_value = self.visit(ctx.base())
            result = self.arithmetic.power(left_value, right_value)
            return self.visit_factor_rest(ctx.factor_rest(), result)
        else:
            return left_value
    
    def visitBase(self, ctx):
        """Evaluate base expressions"""
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise NameError(f"Variable '{var_name}' not defined")
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            # Remove quotes
            return ctx.STRING().getText()[1:-1]
        elif ctx.expression():
            # Parenthesized expression
            return self.visit(ctx.expression())
        elif ctx.matrix_expr():
            return self.visit(ctx.matrix_expr())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.unary_expr():
            return self.visit(ctx.unary_expr())
        return None
    
    def visitUnary_expr(self, ctx):
        """Handle unary expressions"""
        if ctx.MINUS():
            value = self.visit(ctx.base())
            return self.arithmetic.negate(value)
        elif ctx.trig_func():
            func_name = ctx.trig_func().getText()
            value = self.visit(ctx.expression())
            return self.arithmetic.trigonometric(func_name, value)
        return None
    
    def visitMatrix_expr(self, ctx):
        """Handle matrix expressions"""
        if ctx.matrix_content():
            return self.visit(ctx.matrix_content())
        elif ctx.matrix_operation():
            return self.visit(ctx.matrix_operation())
        return None
    
    def visitMatrix_content(self, ctx):
        """Build matrix from content"""
        rows = []
        # Get first row
        first_row = self.visit(ctx.matrix_row())
        rows.append(first_row)
        
        # Get rest of rows
        rest_rows = self.visit_matrix_content_rest(ctx.matrix_content_rest())
        rows.extend(rest_rows)
        
        return self.matrix.create_matrix(rows)
    
    def visit_matrix_content_rest(self, ctx):
        """Get remaining matrix rows"""
        if not ctx or not ctx.matrix_row():
            return []
        
        rows = []
        row = self.visit(ctx.matrix_row())
        rows.append(row)
        
        if ctx.matrix_content_rest():
            rest_rows = self.visit_matrix_content_rest(ctx.matrix_content_rest())
            rows.extend(rest_rows)
        
        return rows
    
    def visitMatrix_row(self, ctx):
        """Build a matrix row"""
        return self.visit(ctx.expression_list())
    
    def visitExpression_list(self, ctx):
        """Build list of expressions"""
        elements = []
        # Get first expression
        first_expr = self.visit(ctx.expression())
        elements.append(first_expr)
        
        # Get rest of expressions
        rest_elements = self.visit_expression_list_rest(ctx.expression_list_rest())
        elements.extend(rest_elements)
        
        return elements
    
    def visit_expression_list_rest(self, ctx):
        """Get remaining expressions"""
        if not ctx or not ctx.expression():
            return []
        
        elements = []
        expr = self.visit(ctx.expression())
        elements.append(expr)
        
        if ctx.expression_list_rest():
            rest_elements = self.visit_expression_list_rest(ctx.expression_list_rest())
            elements.extend(rest_elements)
        
        return elements
    
    def visitMatrix_operation(self, ctx):
        """Handle matrix operations"""
        if ctx.TRANSPOSE():
            matrix = self.visit(ctx.expression())
            return self.matrix.transpose(matrix)
        elif ctx.INVERSE():
            matrix = self.visit(ctx.expression())
            return self.matrix.inverse(matrix)
        elif ctx.MATMULT():
            matrix1 = self.visit(ctx.expression(0))
            matrix2 = self.visit(ctx.expression(1))
            return self.matrix.multiply(matrix1, matrix2)
        elif ctx.MATADD():
            matrix1 = self.visit(ctx.expression(0))
            matrix2 = self.visit(ctx.expression(1))
            return self.matrix.add(matrix1, matrix2)
        elif ctx.MATSUB():
            matrix1 = self.visit(ctx.expression(0))
            matrix2 = self.visit(ctx.expression(1))
            return self.matrix.subtract(matrix1, matrix2)
        return None
    
    def visitConditional(self, ctx):
        """Handle if-else statements"""
        condition_value = self.visit(ctx.condition())
        
        if self.is_truthy(condition_value):
            return self.visit(ctx.statement_list())
        elif ctx.else_part() and ctx.else_part().statement_list():
            return self.visit(ctx.else_part().statement_list())
        return None
    
    def visitCondition(self, ctx):
        """Evaluate conditions"""
        if ctx.rel_op():
            # Relational operation
            left_value = self.visit(ctx.expression(0))
            right_value = self.visit(ctx.expression(1))
            operator = ctx.rel_op().getText()
            return self.arithmetic.compare(left_value, right_value, operator)
        else:
            # Single expression
            return self.visit(ctx.expression(0))
    
    def visitFor_loop(self, ctx):
        """Handle for loops"""
        # Initialize
        self.visit(ctx.assignment(0))
        
        results = []
        while True:
            # Check condition
            condition_value = self.visit(ctx.condition())
            if not self.is_truthy(condition_value):
                break
            
            # Execute body
            result = self.visit(ctx.statement_list())
            if result is not None:
                results.append(result)
            
            # Update
            self.visit(ctx.assignment(1))
        
        return results[-1] if results else None
    
    def visitWhile_loop(self, ctx):
        """Handle while loops"""
        results = []
        while True:
            # Check condition
            condition_value = self.visit(ctx.condition())
            if not self.is_truthy(condition_value):
                break
            
            # Execute body
            result = self.visit(ctx.statement_list())
            if result is not None:
                results.append(result)
        
        return results[-1] if results else None
    
    def visitFunction_def(self, ctx):
        """Define a function"""
        func_name = ctx.ID().getText()
        params = self.visit(ctx.param_list()) if ctx.param_list() else []
        body = ctx.statement_list()
        return_stmt = ctx.return_stmt()
        
        self.functions[func_name] = {
            'params': params,
            'body': body,
            'return_stmt': return_stmt
        }
        return None
    
    def visitParam_list(self, ctx):
        """Get function parameters"""
        if not ctx.ID():
            return []
        
        params = [ctx.ID().getText()]
        if ctx.param_list_rest():
            rest_params = self.visit_param_list_rest(ctx.param_list_rest())
            params.extend(rest_params)
        
        return params
    
    def visit_param_list_rest(self, ctx):
        """Get remaining parameters"""
        if not ctx or not ctx.ID():
            return []
        
        params = [ctx.ID().getText()]
        if ctx.param_list_rest():
            rest_params = self.visit_param_list_rest(ctx.param_list_rest())
            params.extend(rest_params)
        
        return params
    
    def visitReturn_stmt(self, ctx):
        """Handle return statement"""
        self.return_value = self.visit(ctx.expression())
        return self.return_value
    
    def visitFunction_call(self, ctx):
        """Handle function calls"""
        if ctx.ID():
            # User-defined function
            func_name = ctx.ID().getText()
            args = self.visit(ctx.arg_list()) if ctx.arg_list() else []
            return self.call_user_function(func_name, args)
        elif ctx.ml_function():
            return self.visit(ctx.ml_function())
        elif ctx.io_function():
            return self.visit(ctx.io_function())
        elif ctx.plot_function():
            return self.visit(ctx.plot_function())
        return None
    
    def visitArg_list(self, ctx):
        """Get function arguments"""
        if not ctx.expression():
            return []
        
        args = [self.visit(ctx.expression())]
        if ctx.arg_list_rest():
            rest_args = self.visit_arg_list_rest(ctx.arg_list_rest())
            args.extend(rest_args)
        
        return args
    
    def visit_arg_list_rest(self, ctx):
        """Get remaining arguments"""
        if not ctx or not ctx.expression():
            return []
        
        args = [self.visit(ctx.expression())]
        if ctx.arg_list_rest():
            rest_args = self.visit_arg_list_rest(ctx.arg_list_rest())
            args.extend(rest_args)
        
        return args
    
    def visitMl_function(self, ctx):
        """Handle ML function calls"""
        if ctx.LINEAR_REGRESSION():
            X = self.visit(ctx.expression(0))
            y = self.visit(ctx.expression(1))
            return self.linear_reg.fit(X, y)
        elif ctx.MLP_CLASSIFIER():
            X = self.visit(ctx.expression(0))
            y = self.visit(ctx.expression(1))
            hidden_size = self.visit(ctx.expression(2))
            return self.mlp.fit(X, y, hidden_size)
        elif ctx.NEURAL_NETWORK():
            X = self.visit(ctx.expression(0))
            y = self.visit(ctx.expression(1))
            architecture = self.visit(ctx.expression(2))
            return self.neural_net.create(X, y, architecture)
        elif ctx.PREDICT():
            model = self.visit(ctx.expression(0))
            X = self.visit(ctx.expression(1))
            return model.predict(X)
        elif ctx.TRAIN():
            model = self.visit(ctx.expression(0))
            data = self.visit(ctx.expression(1))
            return model.train(data)
        return None
    
    def visitIo_function(self, ctx):
        """Handle IO function calls"""
        if ctx.READ_FILE():
            filename = self.visit(ctx.expression())
            return self.file_manager.read_file(filename)
        elif ctx.WRITE_FILE():
            filename = self.visit(ctx.expression(0))
            content = self.visit(ctx.expression(1))
            return self.file_manager.write_file(filename, content)
        elif ctx.PRINT():
            value = self.visit(ctx.expression())
            return self.file_manager.print_value(value)
        return None
    
    def visitPlot_function(self, ctx):
        """Handle plot function calls"""
        if ctx.PLOT():
            data = self.visit(ctx.expression())
            return self.plotter.plot(data)
        elif ctx.SCATTER():
            x_data = self.visit(ctx.expression(0))
            y_data = self.visit(ctx.expression(1))
            return self.plotter.scatter(x_data, y_data)
        elif ctx.HISTOGRAM():
            data = self.visit(ctx.expression())
            return self.plotter.histogram(data)
        return None
    
    def call_user_function(self, func_name, args):
        """Call a user-defined function"""
        if func_name not in self.functions:
            raise NameError(f"Function '{func_name}' not defined")
        
        func_def = self.functions[func_name]
        params = func_def['params']
        
        if len(args) != len(params):
            raise ValueError(f"Function '{func_name}' expects {len(params)} arguments, got {len(args)}")
        
        # Save current state
        old_variables = self.variables.copy()
        old_in_function = self.in_function
        old_return_value = self.return_value
        
        # Set up function context
        self.in_function = True
        self.return_value = None
        
        # Bind arguments to parameters
        for param, arg in zip(params, args):
            self.variables[param] = arg
        
        try:
            # Execute function body
            self.visit(func_def['body'])
            
            # Execute return statement
            result = self.visit(func_def['return_stmt'])
            
            return result
        finally:
            # Restore state
            self.variables = old_variables
            self.in_function = old_in_function
            self.return_value = old_return_value
    
    def is_truthy(self, value):
        """Check if value is truthy"""
        if isinstance(value, bool):
            return value
        elif isinstance(value, (int, float)):
            return value != 0
        elif isinstance(value, str):
            return len(value) > 0
        elif isinstance(value, list):
            return len(value) > 0
        else:
            return value is not None


# Error listener for custom error handling
class DSLErrorListener(ErrorListener):
    def __init__(self):
        super(DSLErrorListener, self).__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Syntax error at line {line}, column {column}: {msg}"
        self.errors.append(error_msg)
        print(error_msg)
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print(f"Ambiguity detected at positions {startIndex}-{stopIndex}")
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print(f"Attempting full context at positions {startIndex}-{stopIndex}")
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print(f"Context sensitivity at positions {startIndex}-{stopIndex}")


def interpret_code(code):
    """Main function to interpret DSL code"""
    try:
        # Create input stream
        input_stream = InputStream(code)
        
        # Create lexer
        lexer = DeepLearningDSLLexer(input_stream)
        
        # Create token stream
        token_stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = DeepLearningDSLParser(token_stream)
        
        # Add error listener
        error_listener = DSLErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        # Parse the program
        tree = parser.program()
        
        # Check for syntax errors
        if error_listener.errors:
            return None, error_listener.errors
        
        # Create interpreter and visit the tree
        interpreter = DSLInterpreter()
        result = interpreter.visit(tree)
        
        return result, []
        
    except Exception as e:
        return None, [str(e)]


if __name__ == "__main__":
    # Example usage
    code = """
    x = 5;
    y = 3;
    z = x + y * 2;
    print(z);
    
    matrix1 = [[1, 2], [3, 4]];
    matrix2 = [[5, 6], [7, 8]];
    result = matmult(matrix1, matrix2);
    print(result);
    """
    
    result, errors = interpret_code(code)
    
    if errors:
        print("Errors found:")
        for error in errors:
            print(f"  {error}")
    else:
        print(f"Program executed successfully. Result: {result}")

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
    
    def _tanh(self, x):
        """Hyperbolic tangent activation function"""
        x = max(-250, min(250, x))
        return math.tanh(x)
    
    def _tanh_derivative(self, tanh_output):
        """Derivative of tanh function"""
        return 1.0 - tanh_output * tanh_output
    
    def _relu(self, x):
        """ReLU activation function"""
        return max(0, x)
    
    def _relu_derivative(self, x):
        """Derivative of ReLU function"""
        return 1.0 if x > 0 else 0.0
    
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
        if activation == 'sigmoid':
            hidden_output = [self._sigmoid(x) for x in hidden_input]
        elif activation == 'tanh':
            hidden_output = [self._tanh(x) for x in hidden_input]
        elif activation == 'relu':
            hidden_output = [self._relu(x) for x in hidden_input]
        else:
            raise ValueError(f"Unknown activation function: {activation}")
        
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
            if activation == 'sigmoid':
                error *= self._sigmoid_derivative(hidden_output[i])
            elif activation == 'tanh':
                error *= self._tanh_derivative(hidden_output[i])
            elif activation == 'relu':
                error *= self._relu_derivative(hidden_input[i])
            
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
    
    def confusion_matrix(self, X, y, activation='sigmoid'):
        """Calculate confusion matrix"""
        predictions = self.predict(X, activation)
        
        # Get unique classes
        classes = sorted(list(set(y + predictions)))
        n_classes = len(classes)
        
        # Initialize confusion matrix
        matrix = [[0 for _ in range(n_classes)] for _ in range(n_classes)]
        
        # Fill confusion matrix
        class_to_index = {cls: i for i, cls in enumerate(classes)}
        for true_label, pred_label in zip(y, predictions):
            true_idx = class_to_index[true_label]
            pred_idx = class_to_index[pred_label]
            matrix[true_idx][pred_idx] += 1
        
        return matrix, classes
    
    def classification_report(self, X, y, activation='sigmoid'):
        """Generate classification report with precision, recall, F1-score"""
        confusion_matrix, classes = self.confusion_matrix(X, y, activation)
        n_classes = len(classes)
        
        report = {}
        
        for i, cls in enumerate(classes):
            # True positives, false positives, false negatives
            tp = confusion_matrix[i][i]
            fp = sum(confusion_matrix[j][i] for j in range(n_classes)) - tp
            fn = sum(confusion_matrix[i][j] for j in range(n_classes)) - tp
            
            # Calculate metrics
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
            f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
            
            report[cls] = {
                'precision': precision,
                'recall': recall,
                'f1_score': f1_score,
                'support': sum(confusion_matrix[i])
            }
        
        # Overall accuracy
        total_correct = sum(confusion_matrix[i][i] for i in range(n_classes))
        total_samples = sum(sum(row) for row in confusion_matrix)
        overall_accuracy = total_correct / total_samples if total_samples > 0 else 0.0
        
        report['accuracy'] = overall_accuracy
        return report
    
    def get_weights(self):
        """Get network weights and biases"""
        if not self.fitted:
            raise ValueError("Model must be fitted first")
        
        return {
            'weights_input_hidden': [row[:] for row in self.weights_input_hidden],
            'weights_hidden_output': [row[:] for row in self.weights_hidden_output],
            'bias_hidden': self.bias_hidden[:],
            'bias_output': self.bias_output[:]
        }
    
    def set_weights(self, weights_dict):
        """Set network weights and biases"""
        self.weights_input_hidden = [row[:] for row in weights_dict['weights_input_hidden']]
        self.weights_hidden_output = [row[:] for row in weights_dict['weights_hidden_output']]
        self.bias_hidden = weights_dict['bias_hidden'][:]
        self.bias_output = weights_dict['bias_output'][:]
        self.fitted = True


class MLPRegressorEngine:
    """Multi-Layer Perceptron Regressor using pure Python"""
    
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
    
    def _relu(self, x):
        """ReLU activation function"""
        return max(0, x)
    
    def _relu_derivative(self, x):
        """Derivative of ReLU function"""
        return 1.0 if x > 0 else 0.0
    
    def _forward_pass(self, X):
        """Forward pass through the network"""
        # Input to hidden layer
        hidden_input = []
        for i in range(self.hidden_size):
            weighted_sum = self.bias_hidden[i]
            for j in range(len(X)):
                weighted_sum += X[j] * self.weights_input_hidden[i][j]
            hidden_input.append(weighted_sum)
        
        # Apply ReLU activation to hidden layer
        hidden_output = [self._relu(x) for x in hidden_input]
        
        # Hidden to output layer (linear activation for regression)
        output_value = self.bias_output[0]
        for j in range(self.hidden_size):
            output_value += hidden_output[j] * self.weights_hidden_output[0][j]
        
        return hidden_input, hidden_output, output_value
    
    def _backward_pass(self, X, y, hidden_input, hidden_output, output_value):
        """Backward pass (backpropagation)"""
        # Calculate output error (MSE derivative)
        output_error = output_value - y
        
        # Calculate hidden layer errors
        hidden_errors = []
        for i in range(self.hidden_size):
            error = output_error * self.weights_hidden_output[0][i]
            # Apply ReLU derivative
            error *= self._relu_derivative(hidden_input[i])
            hidden_errors.append(error)
        
        # Update output layer weights and bias
        for j in range(self.hidden_size):
            self.weights_hidden_output[0][j] -= self.learning_rate * output_error * hidden_output[j]
        self.bias_output[0] -= self.learning_rate * output_error
        
        # Update hidden layer weights and biases
        for i in range(self.hidden_size):
            for j in range(len(X)):
                self.weights_input_hidden[i][j] -= self.learning_rate * hidden_errors[i] * X[j]
            self.bias_hidden[i] -= self.learning_rate * hidden_errors[i]
    
    def fit(self, X, y, verbose=False):
        """
        Fit the MLP regressor
        X: feature matrix (list of lists) or list for single feature
        y: target values (list)
        """
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        n_samples = len(X)
        n_features = len(X[0])
        
        # Initialize weights using Xavier initialization
        self.weights_input_hidden = self._xavier_initialization(n_features, self.hidden_size)
        self.weights_hidden_output = self._xavier_initialization(self.hidden_size, 1)
        
        # Initialize biases to zero
        self.bias_hidden = [0.0] * self.hidden_size
        self.bias_output = [0.0]
        
        # Training loop
        prev_mse = float('inf')
        
        for epoch in range(self.max_iterations):
            total_mse = 0.0
            
            # Shuffle training data
            indices = list(range(n_samples))
            random.shuffle(indices)
            
            for idx in indices:
                sample = X[idx]
                target = y[idx]
                
                # Forward pass
                hidden_input, hidden_output, output_value = self._forward_pass(sample)
                
                # Calculate MSE
                error = (output_value - target) ** 2
                total_mse += error
                
                # Backward pass
                self._backward_pass(sample, target, hidden_input, hidden_output, output_value)
            
            # Check convergence
            avg_mse = total_mse / n_samples
            if verbose and epoch % 100 == 0:
                print(f"Epoch {epoch}, MSE: {avg_mse:.6f}")
            
            if abs(prev_mse - avg_mse) < self.tolerance:
                if verbose:
                    print(f"Converged at epoch {epoch}")
                break
            
            prev_mse = avg_mse
        
        self.fitted = True
        return self
    
    def predict(self, X):
        """Make predictions"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        predictions = []
        for sample in X:
            _, _, output_value = self._forward_pass(sample)
            predictions.append(output_value)
        
        return predictions
    
    def score(self, X, y):
        """Calculate R^2 score"""
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
    
class NeuralNetworkEngine:
    """Deep Neural Network implementation using pure Python"""
    
    def __init__(self, architecture=None, learning_rate=0.001, max_epochs=1000, 
                 batch_size=32, tolerance=1e-6, dropout_rate=0.0):
        """
        Initialize Neural Network
        architecture: list of layer sizes [input_size, hidden1, hidden2, ..., output_size]
        learning_rate: learning rate for gradient descent
        max_epochs: maximum training epochs
        batch_size: size of mini-batches
        tolerance: convergence tolerance
        dropout_rate: dropout rate for regularization
        """
        self.architecture = architecture or [1, 10, 1]
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        self.batch_size = batch_size
        self.tolerance = tolerance
        self.dropout_rate = dropout_rate
        
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
    
    def _xavier_initialization(self, fan_in, fan_out):
        """Xavier initialization for sigmoid/tanh networks"""
        limit = math.sqrt(6.0 / (fan_in + fan_out))
        weights = []
        for i in range(fan_out):
            row = []
            for j in range(fan_in):
                weight = random.uniform(-limit, limit)
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
            elif initialization == 'xavier':
                layer_weights = self._xavier_initialization(fan_in, fan_out)
            else:
                raise ValueError(f"Unknown initialization: {initialization}")
            
            layer_biases = [0.0] * fan_out
            
            self.weights.append(layer_weights)
            self.biases.append(layer_biases)
    
    def _relu(self, x):
        """ReLU activation function"""
        return max(0, x)
    
    def _relu_derivative(self, x):
        """ReLU derivative"""
        return 1.0 if x > 0 else 0.0
    
    def _leaky_relu(self, x, alpha=0.01):
        """Leaky ReLU activation function"""
        return x if x > 0 else alpha * x
    
    def _leaky_relu_derivative(self, x, alpha=0.01):
        """Leaky ReLU derivative"""
        return 1.0 if x > 0 else alpha
    
    def _sigmoid(self, x):
        """Sigmoid activation function"""
        x = max(-250, min(250, x))
        return 1.0 / (1.0 + math.exp(-x))
    
    def _sigmoid_derivative(self, sigmoid_output):
        """Sigmoid derivative"""
        return sigmoid_output * (1.0 - sigmoid_output)
    
    def _tanh(self, x):
        """Hyperbolic tangent activation function"""
        x = max(-250, min(250, x))
        return math.tanh(x)
    
    def _tanh_derivative(self, tanh_output):
        """Tanh derivative"""
        return 1.0 - tanh_output * tanh_output
    
    def _softmax(self, x):
        """Softmax activation function"""
        max_x = max(x)
        exp_x = [math.exp(xi - max_x) for xi in x]
        sum_exp = sum(exp_x)
        return [exp_xi / sum_exp for exp_xi in exp_x]
    
    def _apply_activation(self, z, activation):
        """Apply activation function"""
        if activation == 'relu':
            return [self._relu(zi) for zi in z]
        elif activation == 'leaky_relu':
            return [self._leaky_relu(zi) for zi in z]
        elif activation == 'sigmoid':
            return [self._sigmoid(zi) for zi in z]
        elif activation == 'tanh':
            return [self._tanh(zi) for zi in z]
        elif activation == 'softmax':
            return self._softmax(z)
        elif activation == 'linear':
            return z[:]
        else:
            raise ValueError(f"Unknown activation function: {activation}")
    
    def _apply_activation_derivative(self, a, z, activation):
        """Apply activation function derivative"""
        if activation == 'relu':
            return [self._relu_derivative(zi) for zi in z]
        elif activation == 'leaky_relu':
            return [self._leaky_relu_derivative(zi) for zi in z]
        elif activation == 'sigmoid':
            return [self._sigmoid_derivative(ai) for ai in a]
        elif activation == 'tanh':
            return [self._tanh_derivative(ai) for ai in a]
        elif activation == 'linear':
            return [1.0] * len(z)
        else:
            raise ValueError(f"Unknown activation function: {activation}")
    
    def _apply_dropout(self, activations, dropout_rate, training=True):
        """Apply dropout regularization"""
        if not training or dropout_rate == 0.0:
            return activations, [1.0] * len(activations)
        
        keep_prob = 1.0 - dropout_rate
        mask = [1.0 if random.random() < keep_prob else 0.0 for _ in activations]
        
        # Scale up remaining activations
        dropped_activations = [a * m / keep_prob for a, m in zip(activations, mask)]
        
        return dropped_activations, mask
    
    def forward_pass(self, X, hidden_activation='relu', output_activation='linear', training=False):
        """Forward pass through the network"""
        activations = [X[:]]  # Store all layer activations
        z_values = []  # Store pre-activation values
        dropout_masks = []  # Store dropout masks
        
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
                current_activation = self._apply_activation(z, output_activation)
                dropout_masks.append([1.0] * len(current_activation))  # No dropout on output
            else:
                # Hidden layer
                current_activation = self._apply_activation(z, hidden_activation)
                # Apply dropout
                current_activation, mask = self._apply_dropout(current_activation, 
                                                             self.dropout_rate, training)
                dropout_masks.append(mask)
            
            activations.append(current_activation[:])
        
        return activations, z_values, dropout_masks
    
    def backward_pass(self, X, y, activations, z_values, dropout_masks, 
                     hidden_activation='relu', output_activation='linear', task_type='regression'):
        """Backward pass (backpropagation)"""
        n_layers = len(self.weights)
        
        # Calculate output layer error
        if task_type == 'regression':
            # Mean squared error derivative
            output_errors = [pred - true for pred, true in zip(activations[-1], y)]
        elif task_type == 'binary_classification':
            # Binary cross-entropy derivative
            output_errors = [pred - y[0] for pred in activations[-1]]
        elif task_type == 'multiclass_classification':
            # Categorical cross-entropy derivative
            output_errors = []
            for i, pred in enumerate(activations[-1]):
                target = 1.0 if i == y[0] else 0.0
                output_errors.append(pred - target)
        else:
            raise ValueError(f"Unknown task type: {task_type}")
        
        # Backpropagate errors
        layer_errors = [output_errors]
        
        for i in range(n_layers - 1, 0, -1):
            # Calculate errors for previous layer
            prev_errors = []
            for j in range(len(activations[i])):
                error = 0.0
                for k in range(len(layer_errors[0])):
                    error += layer_errors[0][k] * self.weights[i][k][j]
                
                # Apply activation derivative
                if i == 1:
                    # First hidden layer
                    if hidden_activation in ['sigmoid', 'tanh']:
                        error *= self._apply_activation_derivative([activations[i][j]], 
                                                                 [z_values[i-1][j]], 
                                                                 hidden_activation)[0]
                    else:
                        error *= self._apply_activation_derivative([], 
                                                                 [z_values[i-1][j]], 
                                                                 hidden_activation)[0]
                else:
                    # Other hidden layers
                    if hidden_activation in ['sigmoid', 'tanh']:
                        error *= self._apply_activation_derivative([activations[i][j]], 
                                                                 [z_values[i-1][j]], 
                                                                 hidden_activation)[0]
                    else:
                        error *= self._apply_activation_derivative([], 
                                                                 [z_values[i-1][j]], 
                                                                 hidden_activation)[0]
                
                # Apply dropout mask
                error *= dropout_masks[i-1][j]
                
                prev_errors.append(error)
            
            layer_errors.insert(0, prev_errors)
        
        # Update weights and biases
        for i in range(n_layers):
            # Update weights
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    gradient = layer_errors[i+1][j] * activations[i][k]
                    self.weights[i][j][k] -= self.learning_rate * gradient
                
                # Update bias
                self.biases[i][j] -= self.learning_rate * layer_errors[i+1][j]
    
    def _calculate_loss(self, predictions, targets, task_type):
        """Calculate loss based on task type"""
        if task_type == 'regression':
            # Mean squared error
            return sum((pred - target) ** 2 for pred, target in zip(predictions, targets)) / len(predictions)
        elif task_type == 'binary_classification':
            # Binary cross-entropy
            loss = 0.0
            for pred, target in zip(predictions, targets):
                pred = max(1e-15, min(1 - 1e-15, pred))  # Clip to prevent log(0)
                loss += -(target * math.log(pred) + (1 - target) * math.log(1 - pred))
            return loss / len(predictions)
        elif task_type == 'multiclass_classification':
            # Categorical cross-entropy
            loss = 0.0
            for preds, target_idx in zip(predictions, targets):
                pred = max(1e-15, min(1 - 1e-15, preds[target_idx]))
                loss += -math.log(pred)
            return loss / len(predictions)
        else:
            raise ValueError(f"Unknown task type: {task_type}")
    
    def fit(self, X, y, task_type='regression', hidden_activation='relu', 
            output_activation='linear', validation_split=0.2, verbose=False):
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
        
        # Split data for validation
        n_samples = len(X)
        n_val = int(n_samples * validation_split)
        n_train = n_samples - n_val
        
        indices = list(range(n_samples))
        random.shuffle(indices)
        
        train_indices = indices[:n_train]
        val_indices = indices[n_train:]
        
        X_train = [X[i] for i in train_indices]
        y_train = [y[i] for i in train_indices]
        X_val = [X[i] for i in val_indices] if n_val > 0 else []
        y_val = [y[i] for i in val_indices] if n_val > 0 else []
        
        # Training loop
        self.loss_history = []
        prev_loss = float('inf')
        
        for epoch in range(self.max_epochs):
            # Mini-batch training
            batch_indices = list(range(n_train))
            random.shuffle(batch_indices)
            
            epoch_loss = 0.0
            n_batches = 0
            
            for i in range(0, n_train, self.batch_size):
                batch_end = min(i + self.batch_size, n_train)
                batch_indices_slice = batch_indices[i:batch_end]
                
                batch_loss = 0.0
                
                for idx in batch_indices_slice:
                    sample = X_train[idx]
                    target = y_train[idx]
                    
                    # Forward pass
                    activations, z_values, dropout_masks = self.forward_pass(
                        sample, hidden_activation, output_activation, training=True)
                    
                    # Calculate loss
                    loss = self._calculate_loss(activations[-1], target, task_type)
                    batch_loss += loss
                    
                    # Backward pass
                    self.backward_pass(sample, target, activations, z_values, dropout_masks,
                                     hidden_activation, output_activation, task_type)
                
                epoch_loss += batch_loss
                n_batches += 1
            
            avg_loss = epoch_loss / n_train if n_train > 0 else 0.0
            self.loss_history.append(avg_loss)
            
            # Validation loss
            if X_val and verbose and epoch % 100 == 0:
                val_loss = self._calculate_validation_loss(X_val, y_val, hidden_activation, 
                                                         output_activation, task_type)
                print(f"Epoch {epoch}, Train Loss: {avg_loss:.6f}, Val Loss: {val_loss:.6f}")
            elif verbose and epoch % 100 == 0:
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
    
    def _calculate_validation_loss(self, X_val, y_val, hidden_activation, output_activation, task_type):
        """Calculate validation loss"""
        total_loss = 0.0
        
        for i in range(len(X_val)):
            activations, _, _ = self.forward_pass(X_val[i], hidden_activation, 
                                                output_activation, training=False)
            loss = self._calculate_loss(activations[-1], y_val[i], task_type)
            total_loss += loss
        
        return total_loss / len(X_val) if X_val else 0.0
    
    def predict(self, X):
        """Make predictions"""
        if not self.fitted:
            raise ValueError("Model must be fitted before making predictions")
        
        # Convert single feature to matrix format
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        predictions = []
        for sample in X:
            activations, _, _ = self.forward_pass(sample, self.hidden_activation, 
                                                self.output_activation, training=False)
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
        
        elif self.task_type in ['binary_classification', 'multiclass_classification']:
            # Accuracy
            correct = 0
            for i in range(len(y)):
                if self.task_type == 'binary_classification':
                    pred_class = 1 if predictions[i][0] > 0.5 else 0
                    true_class = y[i] if not isinstance(y[i], list) else y[i][0]
                else:
                    pred_class = predictions[i].index(max(predictions[i]))
                    true_class = y[i] if not isinstance(y[i], list) else y[i][0]
                
                if pred_class == true_class:
                    correct += 1
            
            return correct / len(y)
    
    def get_parameters(self):
        """Get network parameters"""
        if not self.fitted:
            raise ValueError("Model must be fitted first")
        
        return {
            'weights': [[row[:] for row in layer] for layer in self.weights],
            'biases': [bias[:] for bias in self.biases],
            'architecture': self.architecture[:],
            'loss_history': self.loss_history[:]
        }
    
    def set_parameters(self, params):
        """Set network parameters"""
        self.weights = [[row[:] for row in layer] for layer in params['weights']]
        self.biases = [bias[:] for bias in params['biases']]
        self.architecture = params['architecture'][:]
        self.loss_history = params.get('loss_history', [])
        self.fitted = True
