class MatrixEngine:
    """Engine for matrix operations - pure Python implementation"""
    
    def __init__(self):
        self.epsilon = 1e-10  # For numerical stability
    
    def create_matrix(self, rows):
        """Create a matrix from list of rows"""
        if not rows:
            raise ValueError("Matrix cannot be empty")
        
        # Validate dimensions
        cols = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != cols:
                raise ValueError(f"Row {i} has different length than first row")
        
        return [row[:] for row in rows]  # Deep copy
    
    def get_dimensions(self, matrix):
        """Get matrix dimensions"""
        if not matrix:
            return (0, 0)
        return (len(matrix), len(matrix[0]))
    
    def add(self, matrix1, matrix2):
        """Matrix addition"""
        rows1, cols1 = self.get_dimensions(matrix1)
        rows2, cols2 = self.get_dimensions(matrix2)
        
        if rows1 != rows2 or cols1 != cols2:
            raise ValueError("Matrices must have same dimensions for addition")
        
        result = []
        for i in range(rows1):
            row = []
            for j in range(cols1):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        
        return result
    
    def subtract(self, matrix1, matrix2):
        """Matrix subtraction"""
        rows1, cols1 = self.get_dimensions(matrix1)
        rows2, cols2 = self.get_dimensions(matrix2)
        
        if rows1 != rows2 or cols1 != cols2:
            raise ValueError("Matrices must have same dimensions for subtraction")
        
        result = []
        for i in range(rows1):
            row = []
            for j in range(cols1):
                row.append(matrix1[i][j] - matrix2[i][j])
            result.append(row)
        
        return result
    
    def multiply(self, matrix1, matrix2):
        """Matrix multiplication"""
        rows1, cols1 = self.get_dimensions(matrix1)
        rows2, cols2 = self.get_dimensions(matrix2)
        
        if cols1 != rows2:
            raise ValueError(f"Cannot multiply {rows1}x{cols1} and {rows2}x{cols2} matrices")
        
        result = []
        for i in range(rows1):
            row = []
            for j in range(cols2):
                sum_val = 0
                for k in range(cols1):
                    sum_val += matrix1[i][k] * matrix2[k][j]
                row.append(sum_val)
            result.append(row)
        
        return result
    
    def scalar_multiply(self, matrix, scalar):
        """Multiply matrix by scalar"""
        result = []
        for row in matrix:
            new_row = [elem * scalar for elem in row]
            result.append(new_row)
        return result
    
    def transpose(self, matrix):
        """Matrix transpose"""
        rows, cols = self.get_dimensions(matrix)
        
        result = []
        for j in range(cols):
            row = []
            for i in range(rows):
                row.append(matrix[i][j])
            result.append(row)
        
        return result
    
    def determinant(self, matrix):
        """Calculate matrix determinant"""
        rows, cols = self.get_dimensions(matrix)
        
        if rows != cols:
            raise ValueError("Determinant requires square matrix")
        
        n = rows
        
        # Base cases
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        # Create copy for manipulation
        mat = [row[:] for row in matrix]
        
        # Forward elimination with partial pivoting
        det = 1
        for i in range(n):
            # Find pivot
            max_row = i
            for k in range(i + 1, n):
                if abs(mat[k][i]) > abs(mat[max_row][i]):
                    max_row = k
            
            # Swap rows if needed
            if max_row != i:
                mat[i], mat[max_row] = mat[max_row], mat[i]
                det *= -1
            
            # Check for zero pivot
            if abs(mat[i][i]) < self.epsilon:
                return 0
            
            det *= mat[i][i]
            
            # Eliminate column
            for k in range(i + 1, n):
                factor = mat[k][i] / mat[i][i]
                for j in range(i, n):
                    mat[k][j] -= factor * mat[i][j]
        
        return det
    
    def inverse(self, matrix):
        """Calculate matrix inverse using Gauss-Jordan elimination"""
        rows, cols = self.get_dimensions(matrix)
        
        if rows != cols:
            raise ValueError("Inverse requires square matrix")
        
        n = rows
        det = self.determinant(matrix)
        
        if abs(det) < self.epsilon:
            raise ValueError("Matrix is singular (non-invertible)")
        
        # Create augmented matrix [A|I]
        augmented = []
        for i in range(n):
            row = matrix[i][:] + [0] * n
            row[n + i] = 1
            augmented.append(row)
        
        # Forward elimination
        for i in range(n):
            # Find pivot
            max_row = i
            for k in range(i + 1, n):
                if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                    max_row = k
            
            # Swap rows
            if max_row != i:
                augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
            
            # Make diagonal elements 1
            if abs(augmented[i][i]) < self.epsilon:
                raise ValueError("Matrix is singular")
            
            pivot = augmented[i][i]
            for j in range(2 * n):
                augmented[i][j] /= pivot
            
            # Eliminate column
            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2 * n):
                        augmented[k][j] -= factor * augmented[i][j]
        
        # Extract inverse matrix
        result = []
        for i in range(n):
            row = augmented[i][n:]
            result.append(row)
        
        return result
    
    def rank(self, matrix):
        """Calculate matrix rank"""
        rows, cols = self.get_dimensions(matrix)
        
        # Create copy
        mat = [row[:] for row in matrix]
        rank = 0
        
        for col in range(min(rows, cols)):
            # Find pivot
            pivot_row = -1
            for row in range(rank, rows):
                if abs(mat[row][col]) > self.epsilon:
                    pivot_row = row
                    break
            
            if pivot_row == -1:
                continue
            
            # Swap rows
            if pivot_row != rank:
                mat[rank], mat[pivot_row] = mat[pivot_row], mat[rank]
            
            # Make pivot 1
            pivot = mat[rank][col]
            for j in range(cols):
                mat[rank][j] /= pivot
            
            # Eliminate column
            for i in range(rows):
                if i != rank and abs(mat[i][col]) > self.epsilon:
                    factor = mat[i][col]
                    for j in range(cols):
                        mat[i][j] -= factor * mat[rank][j]
            
            rank += 1
        
        return rank
    
    def trace(self, matrix):
        """Calculate matrix trace (sum of diagonal elements)"""
        rows, cols = self.get_dimensions(matrix)
        
        if rows != cols:
            raise ValueError("Trace requires square matrix")
        
        trace = 0
        for i in range(rows):
            trace += matrix[i][i]
        
        return trace
    
    def is_symmetric(self, matrix):
        """Check if matrix is symmetric"""
        rows, cols = self.get_dimensions(matrix)
        
        if rows != cols:
            return False
        
        for i in range(rows):
            for j in range(cols):
                if abs(matrix[i][j] - matrix[j][i]) > self.epsilon:
                    return False
        
        return True
    
    def is_identity(self, matrix):
        """Check if matrix is identity matrix"""
        rows, cols = self.get_dimensions(matrix)
        
        if rows != cols:
            return False
        
        for i in range(rows):
            for j in range(cols):
                expected = 1 if i == j else 0
                if abs(matrix[i][j] - expected) > self.epsilon:
                    return False
        
        return True
    
    def create_identity(self, n):
        """Create n×n identity matrix"""
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(1 if i == j else 0)
            matrix.append(row)
        return matrix
    
    def create_zeros(self, rows, cols):
        """Create matrix of zeros"""
        matrix = []
        for i in range(rows):
            row = [0] * cols
            matrix.append(row)
        return matrix
    
    def create_ones(self, rows, cols):
        """Create matrix of ones"""
        matrix = []
        for i in range(rows):
            row = [1] * cols
            matrix.append(row)
        return matrix
    
    def matrix_power(self, matrix, n):
        """Calculate matrix to the power of n"""
        rows, cols = self.get_dimensions(matrix)
        
        if rows != cols:
            raise ValueError("Matrix power requires square matrix")
        
        if n < 0:
            # Negative power means inverse^|n|
            return self.matrix_power(self.inverse(matrix), -n)
        
        if n == 0:
            return self.create_identity(rows)
        
        if n == 1:
            return [row[:] for row in matrix]
        
        # Use exponentiation by squaring
        result = self.create_identity(rows)
        base = [row[:] for row in matrix]
        
        while n > 0:
            if n % 2 == 1:
                result = self.multiply(result, base)
            base = self.multiply(base, base)
            n //= 2
        
        return result
    
    def frobenius_norm(self, matrix):
        """Calculate Frobenius norm of matrix"""
        norm_squared = 0
        for row in matrix:
            for elem in row:
                norm_squared += elem * elem
        return norm_squared ** 0.5
    
    def max_norm(self, matrix):
        """Calculate maximum norm (largest absolute value)"""
        max_val = 0
        for row in matrix:
            for elem in row:
                max_val = max(max_val, abs(elem))
        return max_val
    
    def solve_linear_system(self, A, b):
        """Solve Ax = b using Gaussian elimination"""
        rows_A, cols_A = self.get_dimensions(A)
        
        if len(b) != rows_A:
            raise ValueError("Incompatible dimensions for linear system")
        
        # Create augmented matrix [A|b]
        augmented = []
        for i in range(rows_A):
            row = A[i][:] + [b[i]]
            augmented.append(row)
        
        # Forward elimination
        for i in range(min(rows_A, cols_A)):
            # Find pivot
            max_row = i
            for k in range(i + 1, rows_A):
                if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                    max_row = k
            
            # Swap rows
            if max_row != i:
                augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
            
            # Check for zero pivot
            if abs(augmented[i][i]) < self.epsilon:
                raise ValueError("System has no unique solution")
            
            # Eliminate
            for k in range(i + 1, rows_A):
                factor = augmented[k][i] / augmented[i][i]
                for j in range(cols_A + 1):
                    augmented[k][j] -= factor * augmented[i][j]
        
        # Back substitution
        x = [0] * cols_A
        for i in range(min(rows_A, cols_A) - 1, -1, -1):
            x[i] = augmented[i][cols_A]
            for j in range(i + 1, cols_A):
                x[i] -= augmented[i][j] * x[j]
            x[i] /= augmented[i][i]
        
        return x
    
    def print_matrix(self, matrix, precision=4):
        """Print matrix in readable format"""
        if not matrix:
            print("[]")
            return
        
        # Find maximum width for formatting
        max_width = 0
        for row in matrix:
            for elem in row:
                width = len(f"{elem:.{precision}f}")
                max_width = max(max_width, width)
        
        print("[")
        for i, row in enumerate(matrix):
            print("  [", end="")
            for j, elem in enumerate(row):
                if j > 0:
                    print(", ", end="")
                print(f"{elem:>{max_width}.{precision}f}", end="")
            print("]")
        print("]")