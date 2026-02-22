"""
Motif entropy
"""
import math
import numpy as np

def count_motif_percent(motifs):
    count = {}
    columns = []
    for i in range(len(motifs[0])):
        columns.append([motif[i] for motif in motifs])
    for i in range(len(columns)):
        n = len(columns[i])
        count[i] = {
            "A": columns[i].count("A") / n,
            "C": columns[i].count("C") / n,
            "G": columns[i].count("G") / n,
            "T": columns[i].count("T") / n,
        }
    return count

def motif_entropy(motifs):
    entropy = 0
    percents = count_motif_percent(motifs)
    for i in range(len(percents)):
        for nucleotide in percents[i]:
            if percents[i][nucleotide] != 0:
                entropy += percents[i][nucleotide] * math.log2(percents[i][nucleotide])
    print(-entropy)
    return -entropy

if __name__=='__main__':
    f = '/Users/gandalf/Code/BioinformaticsExercises/Chapter_3/motifs.txt'
    with open(f) as file:
        data = file.read()
        data = np.transpose(data.split("\n"))
    motif_entropy(data)


