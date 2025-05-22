import os
import sys

class FileManager:
    """File I/O operations - pure Python implementation"""
    
    def __init__(self):
        self.encoding = 'utf-8'
    
    def read_file(self, filename):
        """
        Read content from a text file
        Returns: string content or list of lines based on file type
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        try:
            with open(filename, 'r', encoding=self.encoding) as file:
                content = file.read()
            
            # Determine file type and parse accordingly
            if filename.endswith('.csv'):
                return self._parse_csv(content)
            elif filename.endswith('.json'):
                return self._parse_json(content)
            elif filename.endswith(('.txt', '.data')):
                return content
            else:
                # Default to text
                return content
                
        except UnicodeDecodeError:
            raise ValueError(f"Unable to decode file '{filename}' with encoding '{self.encoding}'")
        except Exception as e:
            raise IOError(f"Error reading file '{filename}': {str(e)}")
    
    def write_file(self, filename, content):
        """
        Write content to a text file
        content: string or list/matrix to be written
        """
        try:
            # Create directory if it doesn't exist
            directory = os.path.dirname(filename)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(filename, 'w', encoding=self.encoding) as file:
                if isinstance(content, str):
                    file.write(content)
                elif isinstance(content, list):
                    if filename.endswith('.csv'):
                        self._write_csv(file, content)
                    elif filename.endswith('.json'):
                        self._write_json(file, content)
                    else:
                        # Write as lines
                        for line in content:
                            file.write(str(line) + '\n')
                else:
                    file.write(str(content))
            
            return True
            
        except Exception as e:
            raise IOError(f"Error writing to file '{filename}': {str(e)}")
    
    def append_file(self, filename, content):
        """Append content to a file"""
        try:
            with open(filename, 'a', encoding=self.encoding) as file:
                if isinstance(content, str):
                    file.write(content)
                elif isinstance(content, list):
                    for line in content:
                        file.write(str(line) + '\n')
                else:
                    file.write(str(content))
            
            return True
            
        except Exception as e:
            raise IOError(f"Error appending to file '{filename}': {str(e)}")
    
    def _parse_csv(self, content):
        """Parse CSV content manually"""
        lines = content.strip().split('\n')
        if not lines:
            return []
        
        # Simple CSV parser (handles basic cases)
        rows = []
        for line in lines:
            if line.strip():
                # Handle quoted fields
                fields = self._parse_csv_line(line)
                # Try to convert to numbers
                parsed_fields = []
                for field in fields:
                    try:
                        # Try integer first
                        if '.' not in field:
                            parsed_fields.append(int(field))
                        else:
                            parsed_fields.append(float(field))
                    except ValueError:
                        parsed_fields.append(field)
                rows.append(parsed_fields)
        
        return rows
    
    def _parse_csv_line(self, line):
        """Parse a single CSV line handling quotes"""
        fields = []
        current_field = ''
        in_quotes = False
        
        i = 0
        while i < len(line):
            char = line[i]
            
            if char == '"':
                if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                    # Escaped quote
                    current_field += '"'
                    i += 1
                else:
                    # Toggle quote state
                    in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                # Field separator
                fields.append(current_field.strip())
                current_field = ''
            else:
                current_field += char
            
            i += 1
        
        # Add the last field
        fields.append(current_field.strip())
        
        return fields
    
    def _write_csv(self, file, data):
        """Write data as CSV"""
        for row in data:
            if isinstance(row, list):
                csv_row = []
                for field in row:
                    field_str = str(field)
                    # Quote fields that contain commas or quotes
                    if ',' in field_str or '"' in field_str or '\n' in field_str:
                        field_str = '"' + field_str.replace('"', '""') + '"'
                    csv_row.append(field_str)
                file.write(','.join(csv_row) + '\n')
            else:
                file.write(str(row) + '\n')
    
    def _parse_json(self, content):
        """Parse JSON content manually (basic implementation)"""
        content = content.strip()
        if not content:
            return None
        
        return self._parse_json_value(content, 0)[0]
    
    def _parse_json_value(self, content, index):
        """Parse JSON value starting at index"""
        # Skip whitespace
        while index < len(content) and content[index].isspace():
            index += 1
        
        if index >= len(content):
            raise ValueError("Unexpected end of JSON")
        
        char = content[index]
        
        if char == '"':
            # String
            return self._parse_json_string(content, index)
        elif char == '{':
            # Object
            return self._parse_json_object(content, index)
        elif char == '[':
            # Array
            return self._parse_json_array(content, index)
        elif char in '0123456789-':
            # Number
            return self._parse_json_number(content, index)
        elif content[index:index+4] == 'true':
            return True, index + 4
        elif content[index:index+5] == 'false':
            return False, index + 5
        elif content[index:index+4] == 'null':
            return None, index + 4
        else:
            raise ValueError(f"Unexpected character '{char}' at position {index}")
    
    def _parse_json_string(self, content, index):
        """Parse JSON string"""
        if content[index] != '"':
            raise ValueError("Expected '\"' at start of string")
        
        index += 1
        start = index
        result = ''
        
        while index < len(content):
            char = content[index]
            if char == '"':
                return result, index + 1
            elif char == '\\':
                index += 1
                if index >= len(content):
                    raise ValueError("Unexpected end of string")
                escape_char = content[index]
                if escape_char == 'n':
                    result += '\n'
                elif escape_char == 't':
                    result += '\t'
                elif escape_char == 'r':
                    result += '\r'
                elif escape_char == '\\':
                    result += '\\'
                elif escape_char == '"':
                    result += '"'
                elif escape_char == '/':
                    result += '/'
                else:
                    result += escape_char
            else:
                result += char
            index += 1
        
        raise ValueError("Unterminated string")
    
    def _parse_json_number(self, content, index):
        """Parse JSON number"""
        start = index
        
        # Handle negative sign
        if content[index] == '-':
            index += 1
        
        # Parse integer part
        if index >= len(content) or not content[index].isdigit():
            raise ValueError("Invalid number")
        
        while index < len(content) and content[index].isdigit():
            index += 1
        
        # Parse decimal part
        if index < len(content) and content[index] == '.':
            index += 1
            if index >= len(content) or not content[index].isdigit():
                raise ValueError("Invalid number")
            while index < len(content) and content[index].isdigit():
                index += 1
        
        # Parse exponent
        if index < len(content) and content[index] in 'eE':
            index += 1
            if index < len(content) and content[index] in '+-':
                index += 1
            if index >= len(content) or not content[index].isdigit():
                raise ValueError("Invalid number")
            while index < len(content) and content[index].isdigit():
                index += 1
        
        number_str = content[start:index]
        try:
            if '.' in number_str or 'e' in number_str or 'E' in number_str:
                return float(number_str), index
            else:
                return int(number_str), index
        except ValueError:
            raise ValueError(f"Invalid number: {number_str}")
    
    def _parse_json_object(self, content, index):
        """Parse JSON object"""
        if content[index] != '{':
            raise ValueError("Expected '{' at start of object")
        
        index += 1
        obj = {}
        
        # Skip whitespace
        while index < len(content) and content[index].isspace():
            index += 1
        
        # Handle empty object
        if index < len(content) and content[index] == '}':
            return obj, index + 1
        
        while index < len(content):
            # Parse key
            key, index = self._parse_json_value(content, index)
            if not isinstance(key, str):
                raise ValueError("Object key must be string")
            
            # Skip whitespace
            while index < len(content) and content[index].isspace():
                index += 1
            
            # Expect colon
            if index >= len(content) or content[index] != ':':
                raise ValueError("Expected ':' after object key")
            index += 1
            
            # Parse value
            value, index = self._parse_json_value(content, index)
            obj[key] = value
            
            # Skip whitespace
            while index < len(content) and content[index].isspace():
                index += 1
            
            # Check for end or continuation
            if index >= len(content):
                raise ValueError("Unexpected end of object")
            
            if content[index] == '}':
                return obj, index + 1
            elif content[index] == ',':
                index += 1
            else:
                raise ValueError(f"Expected ',' or '}}' in object, got '{content[index]}'")
        
        raise ValueError("Unterminated object")
    
    def _parse_json_array(self, content, index):
        """Parse JSON array"""
        if content[index] != '[':
            raise ValueError("Expected '[' at start of array")
        
        index += 1
        arr = []
        
        # Skip whitespace
        while index < len(content) and content[index].isspace():
            index += 1
        
        # Handle empty array
        if index < len(content) and content[index] == ']':
            return arr, index + 1
        
        while index < len(content):
            # Parse value
            value, index = self._parse_json_value(content, index)
            arr.append(value)
            
            # Skip whitespace
            while index < len(content) and content[index].isspace():
                index += 1
            
            # Check for end or continuation
            if index >= len(content):
                raise ValueError("Unexpected end of array")
            
            if content[index] == ']':
                return arr, index + 1
            elif content[index] == ',':
                index += 1
            else:
                raise ValueError(f"Expected ',' or ']' in array, got '{content[index]}'")
        
        raise ValueError("Unterminated array")
    
    def _write_json(self, file, data):
        """Write data as JSON"""
        json_str = self._to_json_string(data)
        file.write(json_str)
    
    def _to_json_string(self, obj, indent=0):
        """Convert object to JSON string"""
        indent_str = '  ' * indent
        
        if obj is None:
            return 'null'
        elif isinstance(obj, bool):
            return 'true' if obj else 'false'
        elif isinstance(obj, (int, float)):
            return str(obj)
        elif isinstance(obj, str):
            # Escape special characters
            escaped = obj.replace('\\', '\\\\').replace('"', '\\"')
            escaped = escaped.replace('\n', '\\n').replace('\t', '\\t').replace('\r', '\\r')
            return f'"{escaped}"'
        elif isinstance(obj, list):
            if not obj:
                return '[]'
            items = []
            for item in obj:
                items.append(self._to_json_string(item, indent + 1))
            return '[\n' + indent_str + '  ' + f',\n{indent_str}  '.join(items) + '\n' + indent_str + ']'
        elif isinstance(obj, dict):
            if not obj:
                return '{}'
            items = []
            for key, value in obj.items():
                key_str = self._to_json_string(str(key))
                value_str = self._to_json_string(value, indent + 1)
                items.append(f'{key_str}: {value_str}')
            return '{\n' + indent_str + '  ' + f',\n{indent_str}  '.join(items) + '\n' + indent_str + '}'
        else:
            return self._to_json_string(str(obj))
    
    def file_exists(self, filename):
        """Check if file exists"""
        return os.path.exists(filename)
    
    def delete_file(self, filename):
        """Delete a file"""
        try:
            if os.path.exists(filename):
                os.remove(filename)
                return True
            else:
                return False
        except Exception as e:
            raise IOError(f"Error deleting file '{filename}': {str(e)}")
    
    def list_files(self, directory='.', extension=None):
        """List files in directory"""
        try:
            files = os.listdir(directory)
            if extension:
                files = [f for f in files if f.endswith(extension)]
            return sorted(files)
        except Exception as e:
            raise IOError(f"Error listing files in '{directory}': {str(e)}")
    
    def get_file_size(self, filename):
        """Get file size in bytes"""
        try:
            return os.path.getsize(filename)
        except Exception as e:
            raise IOError(f"Error getting size of file '{filename}': {str(e)}")
    
    def print_value(self, value):
        """Print value to console"""
        if isinstance(value, list):
            # Handle matrices/lists
            if value and isinstance(value[0], list):
                # Matrix
                print("Matrix:")
                for row in value:
                    print(f"  {row}")
            else:
                # List
                print(f"List: {value}")
        elif isinstance(value, dict):
            # Dictionary
            print("Dictionary:")
            for key, val in value.items():
                print(f"  {key}: {val}")
        elif isinstance(value, str):
            print(value)
        else:
            print(f"Value: {value} (type: {type(value).__name__})")
        
        return value
    
    def read_lines(self, filename, start_line=0, num_lines=None):
        """Read specific lines from a file"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        try:
            with open(filename, 'r', encoding=self.encoding) as file:
                lines = file.readlines()
            
            # Remove newline characters
            lines = [line.rstrip('\n\r') for line in lines]
            
            # Slice lines
            if num_lines is None:
                return lines[start_line:]
            else:
                return lines[start_line:start_line + num_lines]
                
        except Exception as e:
            raise IOError(f"Error reading lines from file '{filename}': {str(e)}")
    
    def count_lines(self, filename):
        """Count number of lines in a file"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        try:
            with open(filename, 'r', encoding=self.encoding) as file:
                count = sum(1 for _ in file)
            return count
        except Exception as e:
            raise IOError(f"Error counting lines in file '{filename}': {str(e)}")
    
    def search_in_file(self, filename, search_term, case_sensitive=False):
        """Search for a term in a file and return line numbers and content"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        results = []
        
        try:
            with open(filename, 'r', encoding=self.encoding) as file:
                for line_num, line in enumerate(file, 1):
                    line_content = line.rstrip('\n\r')
                    search_line = line_content if case_sensitive else line_content.lower()
                    search_target = search_term if case_sensitive else search_term.lower()
                    
                    if search_target in search_line:
                        results.append((line_num, line_content))
            
            return results
        except Exception as e:
            raise IOError(f"Error searching in file '{filename}': {str(e)}")
    
    def copy_file(self, source, destination):
        """Copy file from source to destination"""
        try:
            with open(source, 'r', encoding=self.encoding) as src:
                content = src.read()
            
            # Create destination directory if needed
            dest_dir = os.path.dirname(destination)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            with open(destination, 'w', encoding=self.encoding) as dst:
                dst.write(content)
            
            return True
        except Exception as e:
            raise IOError(f"Error copying file from '{source}' to '{destination}': {str(e)}")
    
    def create_directory(self, directory):
        """Create directory if it doesn't exist"""
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                return True
            return False
        except Exception as e:
            raise IOError(f"Error creating directory '{directory}': {str(e)}")
    
    def set_encoding(self, encoding):
        """Set file encoding"""
        self.encoding = encoding
    
    def get_encoding(self):
        """Get current file encoding"""
        return self.encoding