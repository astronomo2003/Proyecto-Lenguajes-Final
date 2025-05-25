import sys
import os
import traceback
sys.path.append('./interpreter')
sys.path.append('./generated')

# Import the main interpreter components
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from DeepLearningDSLLexer import DeepLearningDSLLexer
from DeepLearningDSLParser import DeepLearningDSLParser
from dsl_interpreter import DSLInterpreter, DSLErrorListener

class PersistentDSLInterpreter:
    """Wrapper for DSL interpreter that maintains state across executions"""
    
    def __init__(self):
        self.interpreter = DSLInterpreter()
        self.error_listener = DSLErrorListener()
    
    def execute(self, code):
        """Execute code while maintaining interpreter state"""
        try:
            # Create input stream
            input_stream = InputStream(code)
            
            # Create lexer
            lexer = DeepLearningDSLLexer(input_stream)
            
            # Create token stream
            token_stream = CommonTokenStream(lexer)
            
            # Create parser
            parser = DeepLearningDSLParser(token_stream)
            
            # Reset error listener but keep its errors
            self.error_listener.errors = []
            parser.removeErrorListeners()
            parser.addErrorListener(self.error_listener)
            
            # Parse the program
            tree = parser.program()
            
            # Check for syntax errors
            if self.error_listener.errors:
                return None, self.error_listener.errors
            
            # Visit the tree with the SAME interpreter instance (maintains state)
            result = self.interpreter.visit(tree)
            
            return result, []
            
        except Exception as e:
            return None, [str(e)]
    
    def get_variables(self):
        """Get current variables from interpreter"""
        return self.interpreter.variables.copy()
    
    def get_functions(self):
        """Get current functions from interpreter"""
        return self.interpreter.functions.copy()
    
    def clear_state(self):
        """Clear interpreter state"""
        self.interpreter.variables.clear()
        self.interpreter.functions.clear()
        self.interpreter.return_value = None

class Console:
    """Interactive console for the DSL with persistent interpreter state"""
    
    def __init__(self):
        self.history = []
        self.running = True
        # Use persistent interpreter that maintains state
        self.dsl_interpreter = PersistentDSLInterpreter()
        self.show_welcome()
    
    def show_welcome(self):
        """Display welcome message"""
        print("\n" + "="*60)
        print("  Deep Learning DSL Interactive Console")
        print("  Version 1.0 - Persistent State")
        print("="*60)
        print("\nFeatures:")
        print("  ✅ Variables persist between commands")
        print("  ✅ Functions persist between commands") 
        print("  ✅ Multiline support for control structures")
        print("  ✅ Full error handling and debugging")
        print("\nAvailable commands:")
        print("  :help     - Show this help message")
        print("  :history  - Show command history")
        print("  :clear    - Clear screen")
        print("  :reset    - Reset interpreter state (clear all variables)")
        print("  :vars     - Show current variables")
        print("  :funcs    - Show defined functions")
        print("  :exit     - Exit the console")
        print("\nExample session:")
        print("  dsl> x = 10;")
        print("  dsl> if (x > 5) {")
        print("  ...>     print(\"x is greater than 5\");")
        print("  ...> }")
        print("\nType your commands and press Enter...")
        print("-"*60 + "\n")
    
    def is_incomplete_block(self, code):
        """Check if code block is incomplete (unmatched braces)"""
        open_braces = 0
        in_string = False
        escape_next = False
        
        for char in code:
            if escape_next:
                escape_next = False
                continue
                
            if char == '\\':
                escape_next = True
                continue
                
            if char == '"' and not escape_next:
                in_string = not in_string
                continue
                
            if not in_string:
                if char == '{':
                    open_braces += 1
                elif char == '}':
                    open_braces -= 1
        
        return open_braces > 0
    
    def is_control_structure_start(self, line):
        """Check if line starts a control structure"""
        stripped = line.strip()
        control_keywords = ['if', 'for', 'while', 'def', 'else']
        
        for keyword in control_keywords:
            if stripped.startswith(keyword + ' ') or stripped.startswith(keyword + '('):
                return True
        return False
    
    def read_multiline_input(self, initial_line=""):
        """Read multiple lines until block is complete"""
        lines = []
        if initial_line:
            lines.append(initial_line)
        
        current_code = initial_line
        continuation_prompt = "...> "
        
        while True:
            try:
                if self.is_incomplete_block(current_code):
                    # Need more input
                    line = input(continuation_prompt).strip()
                    
                    # Check for special commands to exit multiline mode
                    if line.upper() == 'END' or line == '':
                        break
                    
                    lines.append(line)
                    current_code = '\n'.join(lines)
                else:
                    # Block seems complete
                    break
                    
            except KeyboardInterrupt:
                print("\n[Multiline input cancelled]")
                return ""
            except EOFError:
                break
        
        return '\n'.join(lines)
    
    def run(self):
        """Main console loop with persistent state"""
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
                
                # Check if this might be a multiline structure
                if (self.is_control_structure_start(user_input) or 
                    self.is_incomplete_block(user_input)):
                    
                    print("[Multiline mode - type END or empty line to execute]")
                    complete_code = self.read_multiline_input(user_input)
                    
                    if not complete_code.strip():
                        continue
                        
                    user_input = complete_code
                
                # Add to history
                self.history.append(user_input)
                
                # Execute DSL code using persistent interpreter
                result, errors = self.dsl_interpreter.execute(user_input)
                
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
        elif command == ':reset':
            self.reset_interpreter()
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
        elif command == ':save':
            self.save_session()
        elif command == ':load':
            self.load_session()
        else:
            print(f"Unknown command: {command}")
            print("Type :help for available commands.")
    
    def reset_interpreter(self):
        """Reset the interpreter state"""
        self.dsl_interpreter.clear_state()
        print("✅ Interpreter state reset. All variables and functions cleared.")
    
    def show_variables(self):
        """Show current variables"""
        variables = self.dsl_interpreter.get_variables()
        print("\nCurrent Variables:")
        print("-" * 40)
        if not variables:
            print("  (no variables defined)")
        else:
            for name, value in variables.items():
                # Format value for display
                if isinstance(value, list):
                    if value and isinstance(value[0], list):
                        # Matrix
                        print(f"  {name}: Matrix {len(value)}x{len(value[0])}")
                    else:
                        # List
                        value_str = str(value)
                        if len(value_str) > 50:
                            value_str = value_str[:47] + "..."
                        print(f"  {name}: {value_str}")
                else:
                    print(f"  {name}: {value} ({type(value).__name__})")
        print()
    
    def show_functions(self):
        """Show defined functions"""
        functions = self.dsl_interpreter.get_functions()
        print("\nDefined Functions:")
        print("-" * 40)
        if not functions:
            print("  (no functions defined)")
        else:
            for name, func_def in functions.items():
                params = func_def.get('params', [])
                param_str = ', '.join(params) if params else ''
                print(f"  {name}({param_str})")
        print()
    
    def show_help(self):
        """Show help message"""
        print("\nDSL Console Help")
        print("-" * 40)
        print("Console commands (start with ':'):")
        print("  :help      - Show this help")
        print("  :history   - Show command history")
        print("  :clear     - Clear screen")
        print("  :reset     - Reset interpreter (clear variables/functions)")
        print("  :vars      - Show current variables")
        print("  :funcs     - Show defined functions")
        print("  :examples  - Show DSL examples")
        print("  :save      - Save session to file")
        print("  :load      - Load session from file")
        print("  :version   - Show version info")
        print("  :exit      - Exit console")
        print("\nDSL Language Features:")
        print("  • Variables persist between commands")
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
                # Show multiline commands in a compact way
                display_cmd = cmd.replace('\n', ' \\n ')
                if len(display_cmd) > 60:
                    display_cmd = display_cmd[:57] + "..."
                print(f"  {i:3d}: {display_cmd}")
        print()
    
    def show_examples(self):
        """Show DSL examples with persistent state"""
        print("\nDSL Examples (variables persist between commands):")
        print("-" * 50)
        
        examples = [
            ("1. Basic variables", [
                "x = 10;",
                "y = 5;", 
                "z = x + y;",
                "print(z);"
            ]),
            
            ("2. Conditional with persistent variable", [
                "age = 25;",
                "if (age >= 18) {",
                "    print(\"Adult\");",
                "} else {",
                "    print(\"Minor\");",
                "}"
            ]),
            
            ("3. Function definition and use", [
                "def square(x) {",
                "    return x * x;",
                "}",
                "result = square(7);",
                "print(result);"
            ]),
            
            ("4. Matrix operations", [
                "m1 = [[1, 2], [3, 4]];",
                "m2 = [[5, 6], [7, 8]];",
                "result = matmult(m1, m2);",
                "print(result);"
            ]),
            
            ("5. Loop with accumulator", [
                "sum = 0;",
                "for (i = 1; i <= 5; i = i + 1) {",
                "    sum = sum + i;",
                "}",
                "print(sum);"
            ])
        ]
        
        for title, commands in examples:
            print(f"{title}:")
            for cmd in commands:
                print(f"  dsl> {cmd}")
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
                f.write("# Variables and functions will be recreated\n\n")
                for cmd in self.history:
                    f.write(f"{cmd}\n\n")
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
                content = f.read()
            
            print(f"Loading session from {filename}...")
            
            # Execute the entire file content
            result, errors = self.dsl_interpreter.execute(content)
            if errors:
                print(f"Errors: {errors}")
            elif result is not None:
                print(f"Result: {result}")
            
            print("Session loaded successfully.")
        except Exception as e:
            print(f"Error loading session: {e}")
    
    def show_version(self):
        """Show version information"""
        print("\nDSL Version Information:")
        print("-" * 40)
        print("  Deep Learning DSL v1.0")
        print("  Parser: ANTLR4")
        print("  Implementation: Pure Python")
        print("  Features: Arithmetic, Matrices, ML/DL, I/O, Plotting")
        print("  Grammar Type: LL(1)")
        print("  State Management: Persistent")
        print("  Multiline Support: Enabled")
        print()


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        # File execution mode
        from interface.file_runner import FileRunner
        runner = FileRunner()
        
        if '--verbose' in sys.argv or '-v' in sys.argv:
            verbose = True
            files = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
        else:
            verbose = False
            files = sys.argv[1:]
        
        if files:
            results = runner.run_files(files, verbose)
    else:
        # Interactive console mode with persistent state
        console = Console()
        console.run()


if __name__ == "__main__":
    main()