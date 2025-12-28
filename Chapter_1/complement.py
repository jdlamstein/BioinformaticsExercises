def get_complement(f: str):
    with open(f) as file:
        data = file.read()
        print(data)
        template = data.strip()
        complement = []
        dct = {"A": "T", "T": "A", "C": "G", "G": "C"}
        for c in reversed(template):
            complement.append(dct[c])
    res = "".join(complement)
    print(f"answer: {res}")
    return res


def complement(template: str):
    complement = []
    dct = {"A": "T", "T": "A", "C": "G", "G": "C"}
    for c in reversed(template):
        complement.append(dct[c])
    res = "".join(complement)
    return res


f = "/Users/gandalf/Downloads/dataset_30273_2.txt"
h = "Data/complement.txt"
get_complement(h)
