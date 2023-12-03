import regex as re


# Part one

def get_numbers(path: str):
    data = []

    with open(path, "r") as f:
        for raw in f.readlines():
            line = raw.strip()
            res = re.findall(r"\d", line, overlapped=True)

            first, last = res[0], res[-1]
            data.append(int(first + last))
    return data


# Part two

def get_numbers_string(path: str):
    data = []
    num_string = {"zero": 0, "one": "1", "two": "2", "three": "3", "four": "4",
                  "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    to_append = "|".join(num_string.keys())
    pattern = f"\d|{to_append}"
    # pattern = f"(?=(\d|{to_append}))"

    with open(path, "r") as f:
        for raw in f.readlines():
            line = raw.strip().lower()

            res = re.findall(pattern, line, overlapped=True)
            if len(res) == 0:
                continue

            first, last = res[0], res[-1]

            if first in num_string.keys():
                first = num_string[first]

            if last in num_string.keys():
                last = num_string[last]

            num = int(first + last)
            data.append(num)
    return data


if __name__ == "__main__":
    justNumbers = get_numbers("input.txt")
    print(f"Sum of just numbers: {sum(justNumbers)}")

    numbers = get_numbers_string("input.txt")
    print(f"Sum of all numbers: {sum(numbers)}")

# correct
# 1. 53974
# 2. 52840
