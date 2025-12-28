from Chapter_1.frequent_words import max_map
from Chapter_2.fuzzy_matching import hamming_distance_list
from Chapter_1.complement import complement

NUCLEOTIDES = ["A", "T", "G", "C"]


def run_frequent_words_with_mismatch(f: str):
    with open(f) as file:
        data = file.read()
        data = data.split("\n")
        text = data[0]
        line = data[1].strip().split(" ")
        k = int(line[0])
        d = int(line[1])
    patterns, _ = frequent_words_with_mismatch(text=text, k=k, d=d)
    return patterns


def frequent_words_with_mismatch(text: str, k: int, d: int):
    patterns = []
    freqmap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        neighborhood = neighborhoods(pattern, d)
        for neighbor in neighborhood:
            if neighbor not in freqmap:
                freqmap[neighbor] = 1
            else:
                freqmap[neighbor] += 1
    m = max_map(freqmap)
    for pattern, val in freqmap.items():
        if freqmap[pattern] == m:
            patterns.append(pattern)
    return " ".join(map(str, patterns)), freqmap


def frequent_words_with_mismatch_with_reverse_complement(text: str, k: int, d: int):
    patterns = []
    freqmap = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        reverse_pattern = complement(pattern)
        neighborhood = neighborhoods(pattern, d)
        reverse_neighborhood = neighborhoods(reverse_pattern, d)
        for neighbor in neighborhood:
            if neighbor not in freqmap:
                freqmap[neighbor] = 1
            else:
                freqmap[neighbor] += 1
        for neighbor in reverse_neighborhood:
            if neighbor not in freqmap:
                freqmap[neighbor] = 1
            else:
                freqmap[neighbor] += 1
    print(freqmap)
    m = max_map(freqmap)
    for pattern, val in freqmap.items():
        if freqmap[pattern] == m:
            patterns.append(pattern)
    return " ".join(map(str, patterns)), freqmap


def run_frequent_words_with_mismatch_and_reverse_complement(f: str):
    with open(f) as file:
        data = file.read()
        data = data.split("\n")
        text = data[0]
        line = data[1].strip().split(" ")
        k = int(line[0])
        d = int(line[1])
    patterns, _ = frequent_words_with_mismatch_with_reverse_complement(
        text=text, k=k, d=d
    )
    return patterns


def neighborhoods(pattern: str, d: int):
    src_pattern = list(pattern)
    neighborhood = [pattern]
    use_sources = [src_pattern]
    for q in range(d):
        new_sources = []
        for i in range(0, len(src_pattern)):
            symbol = src_pattern[i]
            for nucleotide in NUCLEOTIDES:
                if nucleotide != symbol:
                    for src in use_sources:
                        neighbor = list(src).copy()
                        # Replace one nucleotide
                        neighbor[i] = nucleotide
                        new_sources.append(neighbor)
                        neighbor_str = "".join(neighbor)
                        neighborhood.append(neighbor_str)
        use_sources = new_sources
    neighborhood = list(set(neighborhood))
    return neighborhood


def replace_nucleotide(src_pattern: list, neighborhood: list, d: int):
    use_sources = src_pattern
    for q in range(d):
        new_sources = []
        for i in range(0, len(src_pattern)):
            symbol = src_pattern[i]
            for nucleotide in NUCLEOTIDES:
                if nucleotide != symbol:
                    for src in use_sources:
                        neighbor = src.copy()
                        # Replace one nucleotide
                        neighbor[i] = nucleotide
                        new_sources.append(neighbor)
                        neighbor_str = "".join(neighbor)
                        neighborhood.append(neighbor_str)
        use_sources = new_sources
    return neighborhood


if __name__ == "__main__":
    f = "/Users/gandalf/Downloads/dataset_30278_10.txt"
    res = run_frequent_words_with_mismatch_and_reverse_complement(f)
    print(res)
