import sys
import os
import traceback
sys.path.append('./interpreter')
sys.path.append('./generated')

# Import the main interpreter
from dsl_interpreter import interpret_code

class Console:
    """Interactive console for the DSL"""
    
    def __init__(self):
        self.history = []
        self.variables = {}
        self.functions = {}
        self.running = True
        self.show_welcome()
    
    def show_welcome(self):
        """Display welcome message"""
        print("\n" + "="*60)
        print("  Deep Learning DSL Interactive Console")
        print("  Version 1.0")
        print("="*60)
        print("\nAvailable commands:")
        print("  :help     - Show this help message")
        print("  :history  - Show command history")
        print("  :clear    - Clear screen")
        print("  :save     - Save current session")
        print("  :load     - Load session from file")
        print("  :vars     - Show current variables")
        print("  :funcs    - Show defined functions")
        print("  :exit     - Exit the console")
        print("\nExample DSL syntax:")
        print("  x = 5;")
        print("  y = 3.14;")
        print("  result = x + y * 2;")
        print("  matrix = [[1, 2], [3, 4]];")
        print("  print(result);")
        print("\nType your commands and press Enter...")
        print("-"*60 + "\n")
    
    def run(self):
        """Main console loop"""
        while self.running:
            try:
                # Get user input
                prompt = "dsl> "
                user_input = input(prompt).strip()
                
                # Check for special commands
                if user_input.startswith(':'):
                    self.handle_command(user_input)
                    continue
                
                # Skip empty input
                if not user_input:
                    continue
                
                # Add to history
                self.history.append(user_input)
                
                # Execute DSL code
                result, errors = interpret_code(user_input)
                
                if errors:
                    print("Errors:")
                    for error in errors:
                        print(f"  {error}")
                else:
                    if result is not None:
                        print(f"Result: {result}")
                
                print()  # Empty line for readability
                
            except KeyboardInterrupt:
                print("\n\nUse :exit to quit the console.")
                print()
            except EOFError:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Console error: {e}")
                if hasattr(e, '__traceback__'):
                    traceback.print_exc()
                print()
    
    def handle_command(self, command):
        """Handle special console commands"""
        command = command.lower()
        
        if command == ':help':
            self.show_help()
        elif command == ':history':
            self.show_history()
        elif command == ':clear':
            self.clear_screen()
        elif command == ':save':
            self.save_session()
        elif command == ':load':
            self.load_session()
        elif command == ':vars':
            self.show_variables()
        elif command == ':funcs':
            self.show_functions()
        elif command == ':exit' or command == ':quit':
            print("Goodbye!")
            self.running = False
        elif command == ':examples':
            self.show_examples()
        elif command == ':version':
            self.show_version()
        else:
            print(f"Unknown command: {command}")
            print("Type :help for available commands.")
    
    def show_help(self):
        """Show help message"""
        print("\nDSL Console Help")
        print("-" * 40)
        print("Console commands (start with ':'):")
        print("  :help     - Show this help")
        print("  :history  - Show command history")
        print("  :clear    - Clear screen")
        print("  :save     - Save session to file")
        print("  :load     - Load session from file")
        print("  :vars     - Show current variables")
        print("  :funcs    - Show defined functions")
        print("  :examples - Show DSL examples")
        print("  :version  - Show version info")
        print("  :exit     - Exit console")
        print("\nDSL Language Features:")
        print("  • Arithmetic: +, -, *, /, %, ^")
        print("  • Variables: x = 5;")
        print("  • Matrices: [[1,2],[3,4]]")
        print("  • Functions: sin(), cos(), sqrt()")
        print("  • Control flow: if/else, for, while")
        print("  • User functions: def func(x) { return x*2; }")
        print("  • ML/DL: linear_regression(), mlp_classifier()")
        print("  • I/O: print(), read_file(), write_file()")
        print("  • Plotting: plot(), scatter(), histogram()")
        print()
    
    def show_history(self):
        """Show command history"""
        print("\nCommand History:")
        print("-" * 40)
        if not self.history:
            print("  (empty)")
        else:
            for i, cmd in enumerate(self.history, 1):
                print(f"  {i:3d}: {cmd}")
        print()
    
    def clear_screen(self):
        """Clear the console screen"""
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/Mac
            os.system('clear')
    
    def save_session(self):
        """Save current session to file"""
        filename = input("Enter filename to save (default: session.dsl): ").strip()
        if not filename:
            filename = "session.dsl"
        
        try:
            with open(filename, 'w') as f:
                f.write("# DSL Session saved\n")
                f.write("# Generated automatically\n\n")
                for cmd in self.history:
                    f.write(f"{cmd}\n")
            print(f"Session saved to {filename}")
        except Exception as e:
            print(f"Error saving session: {e}")
    
    def load_session(self):
        """Load session from file"""
        filename = input("Enter filename to load: ").strip()
        if not filename:
            print("No filename provided.")
            return
        
        try:
            if not os.path.exists(filename):
                print(f"File {filename} not found.")
                return
            
            with open(filename, 'r') as f:
                lines = f.readlines()
            
            print(f"Loading session from {filename}...")
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    print(f"Executing: {line}")
                    self.history.append(line)
                    result, errors = interpret_code(line)
                    if errors:
                        print(f"  Errors: {errors}")
                    elif result is not None:
                        print(f"  Result: {result}")
            
            print("Session loaded successfully.")
        except Exception as e:
            print(f"Error loading session: {e}")
    
    def show_variables(self):
        """Show current variables (placeholder)"""
        print("\nCurrent Variables:")
        print("-" * 40)
        print("(Variable tracking not implemented in current interpreter)")
        print("Variables are tracked internally by the interpreter.")
        print()
    
    def show_functions(self):
        """Show defined functions (placeholder)"""
        print("\nDefined Functions:")
        print("-" * 40)
        print("(Function tracking not implemented in current interpreter)")
        print("Functions are tracked internally by the interpreter.")
        print()
    
    def show_examples(self):
        """Show DSL examples"""
        print("\nDSL Examples:")
        print("-" * 40)
        
        examples = [
            ("Basic arithmetic", 
             "x = 10;\ny = 5;\nresult = x + y * 2;\nprint(result);"),
            
            ("Matrix operations",
             "m1 = [[1, 2], [3, 4]];\nm2 = [[5, 6], [7, 8]];\nresult = matmult(m1, m2);\nprint(result);"),
            
            ("Trigonometric functions",
             "angle = 3.14159 / 4;\nsine_val = sin(angle);\ncosine_val = cos(angle);\nprint(sine_val);\nprint(cosine_val);"),
            
            ("Conditional statement",
             "x = 15;\nif (x > 10) {\n    print(\"x is greater than 10\");\n} else {\n    print(\"x is not greater than 10\");\n}"),
            
            ("For loop",
             "sum = 0;\nfor (i = 1; i <= 5; i = i + 1) {\n    sum = sum + i;\n}\nprint(sum);"),
            
            ("User-defined function",
             "def square(x) {\n    return x * x;\n}\nresult = square(7);\nprint(result);"),
            
            ("Linear regression",
             "X = [[1], [2], [3], [4], [5]];\ny = [2, 4, 6, 8, 10];\nmodel = linear_regression(X, y);\npredictions = predict(model, [[6], [7]]);\nprint(predictions);"),
            
            ("File operations",
             "data = [1, 2, 3, 4, 5];\nwrite_file(\"data.txt\", data);\nloaded_data = read_file(\"data.txt\");\nprint(loaded_data);"),
            
            ("Plotting",
             "data = [1, 4, 2, 8, 5, 7];\nplot(data);\nhistogram(data);")
        ]
        
        for i, (title, code) in enumerate(examples, 1):
            print(f"{i}. {title}:")
            for line in code.split('\n'):
                print(f"     {line}")
            print()
    
    def show_version(self):
        """Show version information"""
        print("\nDSL Version Information:")
        print("-" * 40)
        print("  Deep Learning DSL v1.0")
        print("  Parser: ANTLR4")
        print("  Implementation: Pure Python")
        print("  Features: Arithmetic, Matrices, ML/DL, I/O, Plotting")
        print("  Grammar Type: LL(1)")
        print()


class FileRunner:
    """Run DSL files non-interactively"""
    
    def __init__(self):
        pass
    
    def run_file(self, filename, verbose=False):
        """Execute a DSL file"""
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return False
        
        try:
            with open(filename, 'r') as f:
                content = f.read()
            
            if verbose:
                print(f"Executing file: {filename}")
                print("-" * 40)
            
            # Execute the entire file content
            result, errors = interpret_code(content)
            
            if errors:
                print("Execution errors:")
                for error in errors:
                    print(f"  {error}")
                return False
            else:
                if verbose and result is not None:
                    print(f"Final result: {result}")
                return True
                
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
            return False
    
    def run_files(self, filenames, verbose=False):
        """Execute multiple DSL files"""
        results = {}
        
        for filename in filenames:
            if verbose:
                print(f"\n{'='*50}")
                print(f"Processing: {filename}")
                print(f"{'='*50}")
            
            results[filename] = self.run_file(filename, verbose)
        
        return results


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # File execution mode
        runner = FileRunner()
        
        if '--verbose' in sys.argv or '-v' in sys.argv:
            verbose = True
            files = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
        else:
            verbose = False
            files = sys.argv[1:]
        
        if files:
            results = runner.run_files(files, verbose)
            
            # Show summary
            if len(files) > 1:
                print(f"\n{'='*50}")
                print("Execution Summary:")
                print(f"{'='*50}")
                for filename, success in results.items():
                    status = "SUCCESS" if success else "FAILED"
                    print(f"  {filename}: {status}")
        else:
            print("No files specified for execution.")
    else:
        # Interactive console mode
        console = Console()
        console.run()


if __name__ == "__main__":
    main()