import tkinter as tk
from tkinter import messagebox

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.entries = []

        self.create_grid()

        check_button = tk.Button(root, text="Check Solution", command=self.check_solution, font=("Arial", 16))
        check_button.grid(row=9, column=0, columnspan=9)

    def create_grid(self):
        for i in range(9):
            row_entries = []
            for j in range(9):
                if puzzle[i][j] != 0:
                    entry = tk.Entry(self.root, width=4, font=("Arial", 18), justify='center', state='disabled')
                    entry.insert(0, str(puzzle[i][j]))
                else:
                    entry = tk.Entry(self.root, width=4, font=("Arial", 18), justify='center')
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def check_solution(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit():
                    row.append(int(value))
                else:
                    row.append(0)
            grid.append(row)

        if self.is_valid_solution(grid):
            messagebox.showinfo("Sudoku", "Congratulations! The solution is correct!")
        else:
            messagebox.showerror("Sudoku", "Oops! There are mistakes in your solution.")

    def is_valid_solution(self, grid):
        # Check rows, columns, and 3x3 subgrids
        for i in range(9):
            if not self.is_valid_row(grid, i) or not self.is_valid_column(grid, i) or not self.is_valid_subgrid(grid, i // 3 * 3, i % 3 * 3):
                return False
        return True

    def is_valid_row(self, grid, row):
        return self.is_valid_unit(grid[row])

    def is_valid_column(self, grid, col):
        return self.is_valid_unit([grid[row][col] for row in range(9)])

    def is_valid_subgrid(self, grid, start_row, start_col):
        subgrid = []
        for i in range(3):
            for j in range(3):
                subgrid.append(grid[start_row + i][start_col + j])
        return self.is_valid_unit(subgrid)

    def is_valid_unit(self, unit):
        nums = [num for num in unit if num != 0]
        return len(nums) == len(set(nums))

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
