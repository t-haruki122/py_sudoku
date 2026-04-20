from sudoku import Table

def main():
    init = [
        [5, 2, 6, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 7, 9, 6, 0, 2],
        [0, 1, 0, 0, 0, 0, 0, 0, 8],
        [0, 7, 0, 3, 6, 5, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 4, 9, 2, 0, 5, 0],
        [4, 0, 0, 0, 0, 0, 0, 6, 0],
        [3, 0, 1, 7, 8, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 3, 7, 4],
    ]
    t = Table(init = init)
    t.show()
    t = easy_solve(t)

def easy_solve(t: Table):
    tasks_count = 9999
    while True:
        if t.count_rest() == 0:
            print("OK")
            break
        if tasks_count == 0:
            print("FAIL")
            break
        tasks = t.search(dof = 1)
        tasks_count = len(tasks)
        for task in tasks:
            (val, ) = task[2] # unpack
            t._set(task[0], task[1], val)
        t.show()
    return t

if __name__ == "__main__":
    init = [
        [5, 2, 6, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 7, 9, 6, 0, 2],
        [0, 1, 0, 0, 0, 0, 0, 0, 8],
        [0, 7, 0, 3, 6, 5, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 4, 9, 2, 0, 5, 0],
        [4, 0, 0, 0, 0, 0, 0, 6, 0],
        [3, 0, 1, 7, 8, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 3, 7, 4],
    ]
    t = Table(init = init)
    t.show()
    s = t.out()
    t.parse(s)