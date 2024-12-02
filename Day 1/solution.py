import numpy as np

def task_p1(data: np.array) -> int:
    
    data.sort(axis=1)
    return np.sum(np.abs(data[0:,] - data[-1:,]))

def part_1() -> None:
    with open("data/data.txt", "r") as f:
        data = np.array([tuple(map(int, line.split())) for line in f]).T

    print(task_p1(data))

def task_p2(data: np.array) -> int:
    
    freq = dict(zip(*np.unique(data[1], return_counts=True)))
    return np.sum([i*freq[i] if i in freq else 0 for i in data[0]])

def part_2() -> None:
    with open("data/data.txt", "r") as f:
        data = np.array([tuple(map(int, line.split())) for line in f]).T

    print(task_p2(data))

if __name__ == "__main__":
    part_1()
    part_2()