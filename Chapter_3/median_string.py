from Chapter_2.fuzzy_matching import hamming_distance


def run_median_motifs(f: str):
    with open(f) as file:
        data = file.read()
        data = data.split("\n")
        pattern = data[0].strip()
        dna = data[1].strip().split(" ")
    motifs = distance_between_pattern_and_str(pattern=pattern, dna=dna)
    return motifs


def distance_between_pattern_and_str(pattern: str, dna: str):
    k = len(pattern)
    distance = 0

    for segment in dna:
        seg_hamming_distance = float("inf")
        for i in range(len(segment) - k + 1):
            kmer = segment[i : i + k]
            kmer_distance = hamming_distance(pattern, kmer)
            seg_hamming_distance = min(seg_hamming_distance, kmer_distance)
        distance += seg_hamming_distance
    print(f"Distance: {distance}")
    return distance
