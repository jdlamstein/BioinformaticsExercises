import numpy as np


def count_nucleotide_g_c(f: str):

    vals = [0]
    with open(f) as file:
        data = file.read()
        for s in data:
            if s.lower() == "g":
                vals.append(vals[-1] + 1)
            elif s.lower() == "c":
                vals.append(vals[-1] - 1)
            else:
                vals.append(vals[-1])
    minval = min(vals)
    idxs = []
    for i, x in enumerate(vals):
        if x == minval:
            idxs.append(i)
    print(idxs)
    return idxs


if __name__ == "__main__":
    f = "/Users/gandalf/Code/BioinformaticsExercises/Data/dataset_30277_10_4.txt"
    g = "/Users/gandalf/Code/BioinformaticsExercises/Data/skew.txt"
    count_nucleotide_g_c(f)
    count_nucleotide_g_c(g)
