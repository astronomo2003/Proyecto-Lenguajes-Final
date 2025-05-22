import math

class ArithmeticEngine:
    """Engine for arithmetic operations - no external libraries"""
    
    def add(self, a, b):
        """Addition operation"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction operation"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication operation"""
        return a * b
    
    def divide(self, a, b):
        """Division operation"""
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    
    def modulo(self, a, b):
        """Modulo operation"""
        if b == 0:
            raise ZeroDivisionError("Modulo by zero")
        return a % b
    
    def power(self, base, exponent):
        """Power operation"""
        return base ** exponent
    
    def negate(self, value):
        """Negate a value"""
        return -value
    
    def trigonometric(self, func_name, value):
        """Trigonometric functions"""
        if func_name == 'sin':
            return math.sin(value)
        elif func_name == 'cos':
            return math.cos(value)
        elif func_name == 'tan':
            return math.tan(value)
        elif func_name == 'sqrt':
            if value < 0:
                raise ValueError("Square root of negative number")
            return math.sqrt(value)
        else:
            raise ValueError(f"Unknown trigonometric function: {func_name}")
    
    def compare(self, left, right, operator):
        """Comparison operations"""
        if operator == '==':
            return left == right
        elif operator == '!=':
            return left != right
        elif operator == '<':
            return left < right
        elif operator == '<=':
            return left <= right
        elif operator == '>':
            return left > right
        elif operator == '>=':
            return left >= right
        else:
            raise ValueError(f"Unknown comparison operator: {operator}")
    
    def absolute(self, value):
        """Absolute value"""
        return abs(value)
    
    def floor(self, value):
        """Floor operation"""
        return math.floor(value)
    
    def ceil(self, value):
        """Ceiling operation"""
        return math.ceil(value)
    
    def round_value(self, value, decimals=0):
        """Round operation"""
        return round(value, decimals)
    
    def log(self, value, base=math.e):
        """Logarithm operation"""
        if value <= 0:
            raise ValueError("Logarithm of non-positive number")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base")
        return math.log(value, base)
    
    def exp(self, value):
        """Exponential function"""
        return math.exp(value)
    
    def factorial(self, n):
        """Factorial operation"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial requires non-negative integer")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def gcd(self, a, b):
        """Greatest common divisor"""
        while b:
            a, b = b, a % b
        return abs(a)
    
    def lcm(self, a, b):
        """Least common multiple"""
        return abs(a * b) // self.gcd(a, b)
    
    def is_prime(self, n):
        """Check if number is prime"""
        if not isinstance(n, int) or n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def fibonacci(self, n):
        """Generate fibonacci number"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Fibonacci requires non-negative integer")
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def mean(self, values):
        """Calculate arithmetic mean"""
        if not values:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(values) / len(values)
    
    def median(self, values):
        """Calculate median"""
        if not values:
            raise ValueError("Cannot calculate median of empty list")
        sorted_values = sorted(values)
        n = len(sorted_values)
        if n % 2 == 1:
            return sorted_values[n // 2]
        else:
            return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
    
    def mode(self, values):
        """Calculate mode"""
        if not values:
            raise ValueError("Cannot calculate mode of empty list")
        frequency = {}
        for value in values:
            frequency[value] = frequency.get(value, 0) + 1
        max_freq = max(frequency.values())
        modes = [value for value, freq in frequency.items() if freq == max_freq]
        return modes[0] if len(modes) == 1 else modes
    
    def variance(self, values):
        """Calculate variance"""
        if len(values) < 2:
            raise ValueError("Variance requires at least 2 values")
        mean_val = self.mean(values)
        return sum((x - mean_val) ** 2 for x in values) / (len(values) - 1)
    
    def standard_deviation(self, values):
        """Calculate standard deviation"""
        return math.sqrt(self.variance(values))
    
    def correlation(self, x_values, y_values):
        """Calculate Pearson correlation coefficient"""
        if len(x_values) != len(y_values):
            raise ValueError("Arrays must have same length")
        if len(x_values) < 2:
            raise ValueError("Need at least 2 data points")
        
        n = len(x_values)
        sum_x = sum(x_values)
        sum_y = sum(y_values)
        sum_xy = sum(x * y for x, y in zip(x_values, y_values))
        sum_x2 = sum(x * x for x in x_values)
        sum_y2 = sum(y * y for y in y_values)
        
        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x2 - sum_x * sum_x) * (n * sum_y2 - sum_y * sum_y))
        
        if denominator == 0:
            return 0
        
        return numerator / denominator