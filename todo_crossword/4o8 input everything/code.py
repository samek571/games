import collections
"""
diagonal printing is fucked up because of the diagonal search being the way it is
"""

class MatrixPrinter:
    def printing(self, matrix, dictionary, character):
        for key, positions in dictionary.items():
            for pos in positions:

                start_row, start_col, end_row, end_col, word = pos
                flip = set()

                #horizontal
                if start_row == end_row:
                    print(f"Word: {word} (Horizontal) - Start: ({start_row}, {start_col}), End: ({end_row}, {end_col})")
                    for col in range(start_col, end_col + 1):
                        flip.add((start_row, col))

                #vertical
                elif start_col == end_col:
                    print(f"Word: {word} (Vertical) - Start: ({start_row}, {start_col}), End: ({end_row}, {end_col})")
                    for row in range(start_row, end_row + 1):
                        flip.add((row,start_col))

                #diagonal
                else:
                    print(f"Word: {word} (Diagonal) - Start: ({start_row}, {start_col}), End: ({end_row}, {end_col})")
                    row, col = start_row, start_col
                    while row <= end_row and col <= end_col:
                        flip.add((row,col))
                        row += 1
                        col += 1


                for i in range(len(matrix)):
                    tmp=''
                    for j in range(len(matrix[0])):
                        if (i,j) in flip:
                            tmp+=matrix[i][j]
                        else:
                            tmp+=character



                    print(tmp)
                print()



class Solution:
    def __init__(self):
        with open('crosspuzzle.txt', 'r') as file:
            self.matrix = [list(line.strip()) for line in file]

        with open('words.txt', 'r') as file2:
            self.words = set(line.strip() for line in file2 if len(line.strip()) > 0)

    def search_direction(self, board, direction):
        coords = collections.defaultdict(list)
        cntr = 0
        found = set()

        for idx, line in enumerate(board):
            for word in self.words:
                #it could be written in other direction
                for regex in [word, word[::-1]]:
                    positions = None

                    if direction == 'horizontal':
                        positions = [(idx, line.find(regex), idx, line.find(regex) + len(regex) - 1)]
                    elif direction == 'vertical':
                        positions = [(line.find(regex), idx, line.find(regex) + len(regex) - 1, idx)]

                    #because it returns -1 if not fount by the .find() function
                    # ^^ tries to find the word in each row/column, only rarely it is successful
                    if positions and all(pos >= 0 for pos in positions[0]):
                        positions[0] += (regex,) #the actual word that has been fount within the board
                        coords[cntr] += positions
                        cntr += 1
                        found.add(regex)

        #to see the progress and time optimization
        for word in found:
            for regex in [word, word[::-1]]:
                if regex in self.words:
                    self.words.remove(regex)

        return coords

    def horizontal_search(self):
        board = [''.join(line) for line in self.matrix]
        return self.search_direction(board, 'horizontal')

    def vertical_search(self):
        board = [''.join(col) for col in zip(*self.matrix)]
        return self.search_direction(board, 'vertical')

    def diagonal_search(self):
        board1 = self.get_diagonal_levels(self.matrix)
        board2 = self.get_diagonal_levels(["".join(row)[::-1] for row in zip(*self.matrix)])

        coords1 = self.search_direction(board1, 'horizontal')
        coords2 = self.search_direction(board2, 'horizontal')

        return coords1, coords2


    def get_diagonal_levels(self, board):
        rows = len(board)
        cols = len(board[0])
        levels = []

        for k in range(rows + cols - 1):
            if k < rows:
                start_row = k
                start_col = 0
            else:
                start_row = rows - 1
                start_col = k - rows + 1

            row, col = start_row, start_col
            diagonal_elements = ''

            while 0 <= row < rows and 0 <= col < cols:
                diagonal_elements+=board[row][col]
                row -= 1
                col += 1

            levels.append(diagonal_elements)

        return levels


def main():
    sol = Solution()
    printer = MatrixPrinter()

    horizontal_dict = sol.horizontal_search()
    printer.printing(sol.matrix, horizontal_dict, "#")

    vertical_dict = sol.vertical_search()
    printer.printing(sol.matrix, vertical_dict, "#")

    #returning 2 values so it is sexier
    diagonal_dicts = sol.diagonal_search()
    for dictionary in diagonal_dicts:
        printer.printing(sol.matrix, dictionary, "#")

if __name__ == "__main__": main()
