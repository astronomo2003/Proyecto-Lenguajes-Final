import math
import sys

class Plotter:
    """Plotting engine using pure Python (ASCII art plots)"""
    
    def __init__(self, width=80, height=25):
        self.width = width
        self.height = height
        self.symbols = {
            'point': '*',
            'line': '-',
            'vertical': '|',
            'cross': '+',
            'filled': '#',
            'empty': ' '
        }
    
    def plot(self, data, title="Plot", x_label="X", y_label="Y", symbol='*'):
        """
        Create a line plot from data
        data: list of y-values or list of (x, y) tuples
        """
        if not data:
            print("No data to plot")
            return
        
        # Convert data format
        if isinstance(data[0], (list, tuple)):
            # Data is (x, y) pairs
            x_values = [point[0] for point in data]
            y_values = [point[1] for point in data]
        else:
            # Data is just y-values
            y_values = data
            x_values = list(range(len(y_values)))
        
        if not x_values or not y_values:
            print("No valid data to plot")
            return
        
        # Calculate ranges
        x_min, x_max = min(x_values), max(x_values)
        y_min, y_max = min(y_values), max(y_values)
        
        # Handle edge cases
        if x_min == x_max:
            x_min -= 1
            x_max += 1
        if y_min == y_max:
            y_min -= 1
            y_max += 1
        
        # Create plot area
        plot_area = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Plot points
        for x, y in zip(x_values, y_values):
            # Convert to plot coordinates
            plot_x = int((x - x_min) / (x_max - x_min) * (self.width - 1))
            plot_y = self.height - 1 - int((y - y_min) / (y_max - y_min) * (self.height - 1))
            
            if 0 <= plot_x < self.width and 0 <= plot_y < self.height:
                plot_area[plot_y][plot_x] = symbol
        
        # Connect points with lines
        for i in range(len(x_values) - 1):
            x1, y1 = x_values[i], y_values[i]
            x2, y2 = x_values[i + 1], y_values[i + 1]
            
            plot_x1 = int((x1 - x_min) / (x_max - x_min) * (self.width - 1))
            plot_y1 = self.height - 1 - int((y1 - y_min) / (y_max - y_min) * (self.height - 1))
            plot_x2 = int((x2 - x_min) / (x_max - x_min) * (self.width - 1))
            plot_y2 = self.height - 1 - int((y2 - y_min) / (y_max - y_min) * (self.height - 1))
            
            # Draw line between points
            self._draw_line(plot_area, plot_x1, plot_y1, plot_x2, plot_y2, '-')
        
        # Create output
        print(f"\n{title}")
        print("=" * len(title))
        
        # Y-axis labels
        for i in range(self.height):
            y_val = y_max - (y_max - y_min) * i / (self.height - 1)
            if i == 0 or i == self.height - 1 or i == self.height // 2:
                label = f"{y_val:8.2f}"
            else:
                label = " " * 8
            print(f"{label} |{''.join(plot_area[i])}|")
        
        # X-axis
        print(f"{' ' * 9}+{'-' * self.width}+")
        
        # X-axis labels
        x_labels = [
            f"{x_min:.2f}",
            f"{(x_min + x_max) / 2:.2f}",
            f"{x_max:.2f}"
        ]
        label_positions = [0, self.width // 2, self.width - 1]
        x_axis_line = [' '] * self.width
        
        for label, pos in zip(x_labels, label_positions):
            for i, char in enumerate(label):
                if pos + i < self.width:
                    x_axis_line[pos + i] = char
        
        print(f"{' ' * 10}{''.join(x_axis_line)}")
        print(f"{' ' * 10}{x_label}")
        print()
        
        return plot_area
    
    def scatter(self, x_data, y_data, title="Scatter Plot", x_label="X", y_label="Y", symbol='o'):
        """Create a scatter plot"""
        if len(x_data) != len(y_data):
            raise ValueError("X and Y data must have same length")
        
        data_pairs = list(zip(x_data, y_data))
        return self._create_scatter_plot(data_pairs, title, x_label, y_label, symbol)
    
    def _create_scatter_plot(self, data, title, x_label, y_label, symbol):
        """Create scatter plot from (x, y) pairs"""
        if not data:
            print("No data to plot")
            return
        
        x_values = [point[0] for point in data]
        y_values = [point[1] for point in data]
        
        # Calculate ranges
        x_min, x_max = min(x_values), max(x_values)
        y_min, y_max = min(y_values), max(y_values)
        
        # Handle edge cases
        if x_min == x_max:
            x_min -= 1
            x_max += 1
        if y_min == y_max:
            y_min -= 1
            y_max += 1
        
        # Create plot area
        plot_area = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Plot points
        for x, y in data:
            plot_x = int((x - x_min) / (x_max - x_min) * (self.width - 1))
            plot_y = self.height - 1 - int((y - y_min) / (y_max - y_min) * (self.height - 1))
            
            if 0 <= plot_x < self.width and 0 <= plot_y < self.height:
                plot_area[plot_y][plot_x] = symbol
        
        # Print plot
        print(f"\n{title}")
        print("=" * len(title))
        
        # Y-axis labels
        for i in range(self.height):
            y_val = y_max - (y_max - y_min) * i / (self.height - 1)
            if i == 0 or i == self.height - 1 or i == self.height // 2:
                label = f"{y_val:8.2f}"
            else:
                label = " " * 8
            print(f"{label} |{''.join(plot_area[i])}|")
        
        # X-axis
        print(f"{' ' * 9}+{'-' * self.width}+")
        
        # X-axis labels
        x_labels = [
            f"{x_min:.2f}",
            f"{(x_min + x_max) / 2:.2f}",
            f"{x_max:.2f}"
        ]
        label_positions = [0, self.width // 2, self.width - 1]
        x_axis_line = [' '] * self.width
        
        for label, pos in zip(x_labels, label_positions):
            for i, char in enumerate(label):
                if pos + i < self.width:
                    x_axis_line[pos + i] = char
        
        print(f"{' ' * 10}{''.join(x_axis_line)}")
        print(f"{' ' * 10}{x_label}")
        print()
        
        return plot_area
    
    def histogram(self, data, bins=10, title="Histogram", x_label="Value", y_label="Frequency"):
        """Create a histogram"""
        if not data:
            print("No data to plot")
            return
        
        # Calculate histogram
        data_min, data_max = min(data), max(data)
        
        if data_min == data_max:
            print("All values are the same")
            return
        
        bin_width = (data_max - data_min) / bins
        bin_edges = [data_min + i * bin_width for i in range(bins + 1)]
        bin_counts = [0] * bins
        
        # Count values in each bin
        for value in data:
            bin_index = min(int((value - data_min) / bin_width), bins - 1)
            bin_counts[bin_index] += 1
        
        # Create histogram plot
        max_count = max(bin_counts) if bin_counts else 1
        
        print(f"\n{title}")
        print("=" * len(title))
        
        # Plot bars
        for i in range(self.height):
            y_val = max_count - (max_count * i / (self.height - 1))
            if i == 0 or i == self.height - 1 or i == self.height // 2:
                label = f"{y_val:8.1f}"
            else:
                label = " " * 8
            
            line = []
            for count in bin_counts:
                bar_height = int((count / max_count) * (self.height - 1))
                if self.height - 1 - i <= bar_height:
                    line.append('#')
                else:
                    line.append(' ')
            
            print(f"{label} |{''.join(line)}|")
        
        # X-axis
        print(f"{' ' * 9}+{'-' * bins}+")
        
        # X-axis labels
        step = max(1, bins // 5)
        x_axis_line = [' '] * bins
        for i in range(0, bins, step):
            label = f"{bin_edges[i]:.1f}"
            for j, char in enumerate(label):
                if i + j < bins:
                    x_axis_line[i + j] = char
        
        print(f"{' ' * 10}{''.join(x_axis_line)}")
        print(f"{' ' * 10}{x_label}")
        print(f"Total samples: {len(data)}")
        print()
        
        return bin_counts, bin_edges
    
    def box_plot(self, data, title="Box Plot", label="Data"):
        """Create a box plot"""
        if not data:
            print("No data to plot")
            return
        
        # Calculate statistics
        sorted_data = sorted(data)
        n = len(sorted_data)
        
        q1_index = n // 4
        q2_index = n // 2
        q3_index = 3 * n // 4
        
        q1 = sorted_data[q1_index]
        q2 = sorted_data[q2_index]  # median
        q3 = sorted_data[q3_index]
        
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        
        min_val = min(data)
        max_val = max(data)
        
        # Find outliers
        outliers = [x for x in data if x < lower_fence or x > upper_fence]
        
        # Create box plot
        data_range = max_val - min_val
        if data_range == 0:
            data_range = 1
        
        box_width = self.width - 20
        
        def to_plot_coord(value):
            return int((value - min_val) / data_range * box_width)
        
        print(f"\n{title}")
        print("=" * len(title))
        print()
        
        # Create the box plot
        plot_line = [' '] * box_width
        
        # Mark quartiles and median
        q1_pos = to_plot_coord(q1)
        q2_pos = to_plot_coord(q2)
        q3_pos = to_plot_coord(q3)
        min_pos = to_plot_coord(min_val)
        max_pos = to_plot_coord(max_val)
        
        # Draw whiskers
        for i in range(min_pos, max_pos + 1):
            if i < box_width:
                plot_line[i] = '-'
        
        # Draw box
        for i in range(q1_pos, q3_pos + 1):
            if i < box_width:
                if i == q2_pos:
                    plot_line[i] = '|'  # Median line
                else:
                    plot_line[i] = '#'  # Box
        
        # Mark outliers
        for outlier in outliers:
            outlier_pos = to_plot_coord(outlier)
            if 0 <= outlier_pos < box_width:
                plot_line[outlier_pos] = 'o'
        
        print(f"{label:15} |{''.join(plot_line)}|")
        
        # Labels
        labels = [f"{min_val:.2f}", f"{q1:.2f}", f"{q2:.2f}", f"{q3:.2f}", f"{max_val:.2f}"]
        positions = [min_pos, q1_pos, q2_pos, q3_pos, max_pos]
        
        label_line = [' '] * box_width
        for label, pos in zip(labels, positions):
            for i, char in enumerate(label):
                if pos + i < box_width:
                    label_line[pos + i] = char
        
        print(f"{' ' * 16}{''.join(label_line)}")
        print(f"{' ' * 16}Min   Q1   Med   Q3   Max")
        
        if outliers:
            print(f"Outliers: {outliers}")
        
        print()
        
        return {
            'min': min_val,
            'q1': q1,
            'median': q2,
            'q3': q3,
            'max': max_val,
            'outliers': outliers
        }
    
    def _draw_line(self, plot_area, x1, y1, x2, y2, symbol):
        """Draw a line between two points using Bresenham's algorithm"""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        
        error = dx - dy
        
        x, y = x1, y1
        
        while True:
            if 0 <= x < self.width and 0 <= y < self.height:
                if plot_area[y][x] == ' ':
                    plot_area[y][x] = symbol
            
            if x == x2 and y == y2:
                break
            
            error2 = 2 * error
            
            if error2 > -dy:
                error -= dy
                x += x_step
            
            if error2 < dx:
                error += dx
                y += y_step
    
    def correlation_plot(self, x_data, y_data, title="Correlation Plot"):
        """Create a correlation plot with trend line"""
        if len(x_data) != len(y_data):
            raise ValueError("X and Y data must have same length")
        
        # Calculate correlation coefficient
        n = len(x_data)
        sum_x = sum(x_data)
        sum_y = sum(y_data)
        sum_xy = sum(x * y for x, y in zip(x_data, y_data))
        sum_x2 = sum(x * x for x in x_data)
        sum_y2 = sum(y * y for y in y_data)
        
        correlation = (n * sum_xy - sum_x * sum_y) / math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
        
        # Create scatter plot
        self.scatter(x_data, y_data, f"{title} (r = {correlation:.3f})")
        
        return correlation
    
    def multiple_plots(self, datasets, labels=None, title="Multiple Plots", colors=None):
        """Plot multiple datasets on the same axes"""
        if not datasets:
            print("No data to plot")
            return
        
        symbols = ['*', 'o', '+', 'x', '#', '@', '%', '&'] if not colors else colors
        labels = labels or [f"Series {i+1}" for i in range(len(datasets))]
        
        # Find global ranges
        all_x = []
        all_y = []
        
        for data in datasets:
            if isinstance(data[0], (list, tuple)):
                x_vals = [point[0] for point in data]
                y_vals = [point[1] for point in data]
            else:
                y_vals = data
                x_vals = list(range(len(y_vals)))
            all_x.extend(x_vals)
            all_y.extend(y_vals)
        
        x_min, x_max = min(all_x), max(all_x)
        y_min, y_max = min(all_y), max(all_y)
        
        # Handle edge cases
        if x_min == x_max:
            x_min -= 1
            x_max += 1
        if y_min == y_max:
            y_min -= 1
            y_max += 1
        
        # Create plot area
        plot_area = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Plot each dataset
        for i, data in enumerate(datasets):
            symbol = symbols[i % len(symbols)]
            
            if isinstance(data[0], (list, tuple)):
                x_vals = [point[0] for point in data]
                y_vals = [point[1] for point in data]
            else:
                y_vals = data
                x_vals = list(range(len(y_vals)))
            
            # Plot points
            for x, y in zip(x_vals, y_vals):
                plot_x = int((x - x_min) / (x_max - x_min) * (self.width - 1))
                plot_y = self.height - 1 - int((y - y_min) / (y_max - y_min) * (self.height - 1))
                
                if 0 <= plot_x < self.width and 0 <= plot_y < self.height:
                    plot_area[plot_y][plot_x] = symbol
        
        # Print plot
        print(f"\n{title}")
        print("=" * len(title))
        
        # Legend
        print("Legend:")
        for i, label in enumerate(labels):
            symbol = symbols[i % len(symbols)]
            print(f"  {symbol} : {label}")
        print()
        
        # Y-axis labels and plot
        for i in range(self.height):
            y_val = y_max - (y_max - y_min) * i / (self.height - 1)
            if i == 0 or i == self.height - 1 or i == self.height // 2:
                label = f"{y_val:8.2f}"
            else:
                label = " " * 8
            print(f"{label} |{''.join(plot_area[i])}|")
        
        # X-axis
        print(f"{' ' * 9}+{'-' * self.width}+")
        
        # X-axis labels
        x_labels = [f"{x_min:.2f}", f"{(x_min + x_max) / 2:.2f}", f"{x_max:.2f}"]
        label_positions = [0, self.width // 2, self.width - 1]
        x_axis_line = [' '] * self.width
        
        for label, pos in zip(x_labels, label_positions):
            for i, char in enumerate(label):
                if pos + i < self.width:
                    x_axis_line[pos + i] = char
        
        print(f"{' ' * 10}{''.join(x_axis_line)}")
        print()
        
        return plot_area
    
    def set_dimensions(self, width, height):
        """Set plot dimensions"""
        self.width = max(20, width)
        self.height = max(10, height)
    
    def get_dimensions(self):
        """Get current plot dimensions"""
        return self.width, self.height