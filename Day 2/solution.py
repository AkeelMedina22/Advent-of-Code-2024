import numpy as np

def is_safe(levels):
    if len(levels) < 2:
        return False  
    differences = np.diff(levels)

    return (np.all(differences > 0) or np.all(differences < 0)) and np.all((1 <= abs(differences)) & (abs(differences) <= 3))

def task_p1(data: np.array) -> int:
    return sum(is_safe(d) for d in data)

def part_1() -> None:
    with open("data/data.txt", "r") as f:
        data = [np.array(list(map(int, line.split()))) for line in f]

    print(task_p1(data))

def task_p2(data: np.array) -> int:
    
    def is_fixable(levels):
        for i in range(len(levels)):
            modified_levels = np.delete(levels, i)
            if is_safe(modified_levels):
                return True
        return False

    safe_reports = sum(is_safe(d) for d in data)

    for report in data:
        if not is_safe(report) and is_fixable(report):
            safe_reports += 1 

    return safe_reports
        

def part_2() -> None:
    with open("data/data.txt", "r") as f:
        data = [np.array(list(map(int, line.split()))) for line in f]

    print(task_p2(data))

if __name__ == "__main__":
    part_1()
    part_2()