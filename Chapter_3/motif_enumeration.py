"""
MotifEnumeration(Dna, k, d)
    Patterns ← an empty set
    for each k-mer Pattern in Dna
        for each k-mer Pattern’ differing from Pattern by at most d mismatches
            if Pattern' appears in each string from Dna with at most d mismatches
                add Pattern' to Patterns
    remove duplicates from Patterns
    return Patterns
"""

from Chapter_2.fuzzy_matching import hamming_distance


def run_motifEnumeration(f: str):
    with open(f) as file:
        data = file.read()
        data = data.split("\n")
        text = data[1].strip().split(" ")
        line = data[0].strip().split(" ")
        k = int(line[0])
        d = int(line[1])
    motifs = motifEnumeration(dna=text, k=k, d=d)
    return motifs


def brute_force_kmers(dna, k, d):
    patterns = set()


def immediateNeighbors(pattern):
    neighborhood = [pattern]
    for i in range(len(pattern)):
        for j in ["A", "C", "G", "T"]:
            if pattern[i] != j:
                neighborhood.append(pattern[:i] + j + pattern[i + 1 :])
    return neighborhood


def neighbors(pattern, d):
    neighborhood = [pattern]
    for j in range(d):
        for neighbor in neighborhood:
            neighborhood = neighborhood + immediateNeighbors(neighbor)
        neighborhood = list(set(neighborhood))
    neighborhood = list(set(neighborhood))
    return neighborhood


def multiNeighbors(k, d, dna):
    neighborhood = {}
    for s in dna:
        neighborhood[s] = []
        for i in range(len(s) - k + 1):
            pattern = s[i : i + k]
            neighborhood[s] = neighborhood[s] + neighbors(pattern, d)
        neighborhood[s] = list(set(neighborhood[s]))
    return neighborhood


def motifEnumeration(dna, k, d):
    motifs = []
    neighborhood = multiNeighbors(k, d, dna)

    for s in dna:
        for pattern in neighborhood[s]:
            if pattern not in motifs:
                cnt = 0
                for s2 in dna:
                    for i in range(len(s2) - k + 1):
                        if hamming_distance(pattern, s2[i : i + k]) <= d:
                            cnt += 1
                            break
                if cnt == len(dna):
                    motifs.append(pattern)
    motifs = list(set(motifs))

    return motifs


if __name__=='__main__':
    f = "/Users/gandalf/Downloads/dataset_30302_8.txt"

    res = run_motifEnumeration(f=f)
    print(res)