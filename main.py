from sudoku import Table
from collections import deque


def main():
    initn = 9
    init = [
        [0, 2, 1, 9, 0, 0, 0, 7, 0],
        [4, 0, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 7, 0, 0, 0, 8, 0, 6],
        [0, 0, 0, 0, 8, 0, 0, 0, 2],
        [7, 0, 0, 5, 0, 4, 0, 0, 3],
        [9, 0, 0, 0, 3, 0, 0, 0, 0],
        [6, 0, 5, 0, 0, 0, 1, 0, 4],
        [0, 0, 0, 1, 0, 0, 0, 0, 8],
        [0, 8, 0, 0, 0, 2, 6, 9, 0],
    ]
    t = Table(init = init)
    t.show()

    q = deque([]) # append, popleft
    q.append(t.out())
    t.parse(bfs(q))
    t.show()


def bfs(q: deque):
    t = Table()
    task_count = 1
    while True:
        if len(q) == 0:
            raise RuntimeError("Couldn't solve input table !!")
        task = q.pop()
        print(f"TASK #{task_count} started")
        t.parse(task)
        try:
            t.partly_solve()
        except RuntimeError as e:
            print(f"TASK #{task_count} failed: {e}")
            task_count += 1
            continue
        if t.is_solved():
            print(f"TASK #{task_count} succeeded")
            break
        [ q.append(a) for a in t.get_min_assumption() ]
        print(f"TASK #{task_count} ended")
        task_count += 1
    return t.out()


if __name__ == "__main__":
    main()


# init = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
