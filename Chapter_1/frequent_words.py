"""
Count the maximum occurence of k-mers in the nucleotides.
"""


def frequent_words(f: str):
    frequency_patterns = []

    with open(f) as file:
        data = file.read()
        print(data)
        txt, k_str = data.strip().split("\n")
        k = int(k_str)
        freq_map = frequency_table(txt, k)
        max_val = max_map(freq_map)
        for pattern, cnt in freq_map.items():
            if cnt == max_val:
                frequency_patterns.append(pattern)
    print(frequency_patterns)
    return frequency_patterns


def frequency_table(txt: str, k: int):
    freq_map = {}
    n = len(txt)

    for i in range(n - k):
        pattern = txt[i : i + k]
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1
    return freq_map


def max_map(freq_map: dict[str, int]):
    max_val = 0
    for pattern, cnt in freq_map.items():
        max_val = max(cnt, max_val)
    return max_val


if __name__ == "__main__":
    # f = "/Users/gandalf/Code/BioinformaticsExercises/Data/frequent_words.txt"
    g = "/Users/gandalf/Downloads/dataset_30272_13.txt"
    frequent_words(g)
