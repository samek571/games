class MatrixScanner:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_diagonal_levels(self, scan_direction):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        levels = []

        for k in range(rows + cols - 1):
            if k < rows:
                if scan_direction == "top_right":
                    start_row = k
                    start_col = 0
                elif scan_direction == "top_left":
                    start_row = k
                    start_col = cols - 1
            else:
                if scan_direction == "top_right":
                    start_row = rows - 1
                    start_col = k - rows + 1
                elif scan_direction == "top_left":
                    start_row = rows - 1 - (k - rows + 1)
                    start_col = cols - 1

            row, col = start_row, start_col
            diagonal_elements = ''

            while 0 <= row < rows and 0 <= col < cols:
                diagonal_elements += self.matrix[row][col]
                row -= 1
                col -= 1

            levels.append(diagonal_elements)

        return levels


# Test the function
matrix = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]

scanner = MatrixScanner(matrix)

scan_direction = "top_right"
diagonal_levels = scanner.get_diagonal_levels(scan_direction)
print(f"Scan Direction: {scan_direction}")
for level in diagonal_levels:
    print(level)

print()

scan_direction = "top_left"
diagonal_levels = scanner.get_diagonal_levels(scan_direction)
print(f"Scan Direction: {scan_direction}")
for level in diagonal_levels:
    print(level)
