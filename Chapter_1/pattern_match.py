"""
Count k-mers in DNA.
"""


def patternMatch(f, pattern=None):
    with open(f) as file:
        data = file.read()
        print(data)
        if pattern is None:
            pattern, txt = data.strip().split("\n")
        else:
            txt = data.strip()

        res = []
        for i in range(len(txt) - len(pattern)):
            if txt[i : len(pattern) + i] == pattern:
                res.append(str(i))
        index_str = " ".join(res)
        print(f"answer: {index_str}")
        return index_str


# f = "/Users/gandalf/Downloads/dataset_30273_5.txt"
f = "/Users/gandalf/Downloads/Vibrio_cholerae.txt"
# g = "/Users/gandalf/Downloads/PatternCount/inputs/input_1.txt"
patternMatch(f, pattern="CTTGATCAT")
