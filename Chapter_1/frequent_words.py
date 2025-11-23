"""
Count the maximum occurence of k-mers in the nucleotides.
"""

from tqdm import tqdm


def frequent_words(f: str):
    frequency_patterns = []

    with open(f) as file:
        data = file.read()
        print(data)
        txt, k_str = data.strip().split("\n")
        k = int(k_str)
        freq_map = frequency_table(txt, k)
        print(freq_map)
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


"""
FindClumps(Text, k, L, t)
    Patterns ← an array of strings of length 0
    n ← |Text|
    for every integer i between 0 and n − L
        Window ← Text(i, L)
        freqMap ← FrequencyTable(Window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t
                append s to Patterns
    remove duplicates from Patterns
    return Patterns
    """


def find_clumps(f, k=None, ell=None, t=None):
    with open(f) as file:
        data = file.read()
        print(data)
        if k is None:
            txt, digits = data.strip().split("\n")
            k, ell, t = digits.split(" ")
            k = int(k)
            ell = int(ell)
            t = int(t)
        else:
            txt = data.strip()
        patterns = set()
        n = len(txt)
        window = txt[:ell]
        freq_map = {}

        for i in tqdm(range(n - ell)):
            if i == 0:
                # Calculate the window
                for j in range(ell - k):
                    pttern = window[j : j + k]
                    if pttern not in freq_map:
                        freq_map[pttern] = 1
                    else:
                        freq_map[pttern] += 1
                for s in freq_map.keys():
                    if freq_map[s] >= t:
                        patterns.add(s)
            else:
                new_mer = window[-k + 1 :] + txt[i + ell - 1]
                old_mer = window[:k]
                window = txt[i : ell + i]
                if old_mer in freq_map:
                    freq_map[old_mer] -= 1
                    if freq_map[old_mer] < 0:
                        freq_map[old_mer] = 0
                if new_mer not in freq_map:
                    freq_map[new_mer] = 1
                else:
                    freq_map[new_mer] += 1

                if freq_map[new_mer] >= t:
                    patterns.add(new_mer)
    res = list(patterns)
    print(f"Count: {len(res)}")
    result = " ".join(res)
    # print(f"answer: {result}")
    return result


if __name__ == "__main__":
    # f = "/Users/gandalf/Code/BioinformaticsExercises/Data/frequent_words.txt"
    g = "/Users/gandalf/Downloads/dataset_30272_13.txt"
    f = "/Users/gandalf/Downloads/dataset_30274_5.txt"
    f = "/Users/gandalf/Downloads/E_coli.txt"
    h = "Data/genome.txt"
    frequent_words(h)
    # find_clumps(f, k=9, ell=500, t=3)
