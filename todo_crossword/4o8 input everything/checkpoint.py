import collections


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
    print(sol.words)
    print(sol.horizontal_search())
    print(sol.words)
    print(sol.vertical_search())
    print(sol.words)
    print(sol.diagonal_search())
    print(sol.words)

if __name__ == "__main__":
    main()
