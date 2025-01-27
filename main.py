from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from collections import defaultdict
import copy

app = FastAPI()

class SudokuRequest(BaseModel):
    board: List[List[int]]

def is_valid(board):
    def has_duplicates(numbers):
        numbers = [n for n in numbers if n != 0]
        return len(numbers) != len(set(numbers))

    for i in range(9):
        if has_duplicates(board[i]) or has_duplicates([board[j][i] for j in range(9)]):
            return False

    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            block = [board[r][c] for r in range(row_start, row_start+3) for c in range(col_start, col_start+3)]
            if has_duplicates(block):
                return False

    return True

def find_empty_cell(board):
    possibilities = defaultdict(list)

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                candidates = [n for n in range(1, 10) if is_safe(board, row, col, n)]
                possibilities[(row, col)] = candidates

    if not possibilities:
        return None

    return min(possibilities, key=lambda k: len(possibilities[k]))

def is_safe(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False

    box_start_row, box_start_col = (row // 3) * 3, (col // 3) * 3
    if num in [board[r][c] for r in range(box_start_row, box_start_row+3) for c in range(box_start_col, box_start_col+3)]:
        return False

    return True

def solve(board, find_all=False):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return [copy.deepcopy(board)]

    row, col = empty_cell
    solutions = []

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            result = solve(board, find_all)
            if result:
                if find_all:
                    solutions.extend(result)
                else:
                    return result

            board[row][col] = 0

    return solutions if find_all else None

@app.post("/solve")
def solve_sudoku(request: SudokuRequest):
    board = request.board

    if len(board) != 9 or any(len(row) != 9 for row in board):
        raise HTTPException(status_code=400, detail="Invalid board size. It must be 9x9.")

    if not is_valid(board):
        raise HTTPException(status_code=400, detail="Invalid Sudoku puzzle.")

    solution = solve(board)

    if solution:
        return {"solved_board": solution[0]}
    else:
        raise HTTPException(status_code=400, detail="No solution found for the given Sudoku.")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)