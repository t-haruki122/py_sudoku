import math

class Table:
    def __init__(self, length: int = 9, init = None) -> None:
        len_sqrt = math.sqrt(length)
        if len_sqrt % 1 != 0:
            raise ValueError("length must be square number")
        self.len_sqrt = int(len_sqrt)
        self.length = length
        if init != None:
            self.table = init
        else:
            self.table = [[0 for _ in range(length)] for _ in range(length)]
    def _set(self, x, y, val) -> None:
        if x >= self.length: raise IndexError(f"index x = {x} is too big")
        if y >= self.length: raise IndexError(f"index y = {y} is too big")
        self.table[y][x] = val
    def _get(self, x, y) -> int:
        if x >= self.length: raise IndexError(f"index x = {x} is too big")
        if y >= self.length: raise IndexError(f"index y = {y} is too big")
        return self.table[y][x]
    
    def out(self) -> str:
        string = ""
        for y in range(self.length):
            for x in range(self.length):
                string += f"{self._get(x, y)},"
        return f"({self.length}){string[:-1]}"
    
    def parse(self, string: str) -> None:
        idx_parL = string.index("(")
        idx_parR = string.index(")")
        length = int(string[idx_parL+1:idx_parR])
        string = string[idx_parR+1:]
        slist = string.split(",")
        # validation
        if length ** 2 != len(slist):
            raise ValueError(f"Invalid input string length (now: {len(slist)} / need: {length ** 2}")
        table = []
        for i in range(length):
            line = []
            for k in range(length):
                line.append(int(slist[i*length+k]))
            table.append(line)
        self.table = table
    
    def count_rest(self) -> int:
        count = 0
        for y in range(self.length):
            for x in range(self.length):
                count += 1 if self._get(x, y) == 0 else 0
        return count
    def show(self) -> None:
        for line in self.table:
            print(" ".join([str(i) if i != 0 else "." for i in line]))
        print()
    
    def get_line(self, y) -> set[int]:
        return set([i for i in self.table[y] if i != 0])
    def get_row(self, x) -> set[int]:
        out = set()
        for i in range(self.length):
            val = self._get(x, i)
            if val != 0:
                out.add(val)
        return out
    def get_box(self, x, y) -> set[int]:
        out = set()
        for delta_y in range(self.len_sqrt):
            for delta_x in range(self.len_sqrt):
                val = self._get(
                    x * self.len_sqrt + delta_x,
                    y * self.len_sqrt + delta_y
                )
                if val != 0:
                    out.add(val)
        return out
    
    def get_available(self, x, y) -> set[int]:
        alphabet = set(range(1, self.length + 1))
        av_line = self.get_line(y) ^ alphabet
        av_row = self.get_row(x) ^ alphabet
        av_box = self.get_box(x // self.len_sqrt, y // self.len_sqrt) ^ alphabet
        return av_line & av_row & av_box
    
    def search(self, dof: int = 1) -> list[list[int, int, set[int]]]:
        availables = []
        for y in range(self.length):
            for x in range(self.length):
                val = self._get(x, y)
                if val != 0:
                    continue
                av = self.get_available(x, y)
                if len(av) <= dof:
                    # print(f"Available: {av} can be placed in {x}, {y}")
                    availables.append([x, y, av])
        return availables