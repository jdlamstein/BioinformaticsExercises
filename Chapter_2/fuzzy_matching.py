def fuzzy_matching(f: str):
    with open(f) as file:
        data = file.read()
        lines = data.split("\n")
        target, genome, thresh = lines[0], lines[1], lines[2]
        thresh = int(thresh)
    current = None
    k = len(target)
    N = len(genome) - k + 1
    idxs = []
    for i in range(N):
        snippet = genome[i : k + i]
        current = hamming_distance_list(snippet, target)
        hamming_dist = sum(current)
        if hamming_dist <= thresh:
            idxs.append(i)
    print(*idxs)
    return idxs


def hamming_distance_list(a: str, b: str):
    # Count mismatches
    return [int(x != y) for x, y in zip(a, b)]


if __name__ == "__main__":
    f = "/Users/gandalf/Downloads/ApproximatePatternMatching/inputs/input_2.txt"
    g = "/Users/gandalf/Downloads/dataset_30278_4_3.txt"
    fuzzy_matching(g)
