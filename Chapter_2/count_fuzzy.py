from Chapter_1.frequent_words import frequent_words, frequency_table


def count_fuzzy_matches(text: str, target_pattern: str, d: int):
    freq_map = frequency_table(txt=text, k=len(target_pattern))
    print(freq_map)
    frequent_fuzzy_words = {}

    # check fuzzy matching
    for pattern, cnt in freq_map.items():
        check_cnt = 0
        keep = True
        for ch_txt, ch_target in zip(pattern, target_pattern):
            if ch_txt != ch_target:
                check_cnt += 1
                if check_cnt > d:
                    keep = False
                    break

        if keep:
            if pattern not in frequent_fuzzy_words:
                frequent_fuzzy_words[pattern] = 1
            else:
                frequent_fuzzy_words[pattern] += 1
    print(frequent_fuzzy_words)
    fuzzy_count = sum([cnt for _, cnt in frequent_fuzzy_words.items()])
    print(fuzzy_count)
    return fuzzy_count


def get_indices_fuzzy_matches(text: str, target_pattern: str, d: int):
    fuzzy_words_idx = []

    k = len(target_pattern)
    for i in range(len(text) - k + 1):
        subtext = text[i : i + k]
        check_cnt = 0
        keep = True
        for ch_txt, ch_target in zip(subtext, target_pattern):
            if ch_txt != ch_target:
                check_cnt += 1
                if check_cnt > d:
                    keep = False
                    break

        if keep:
            fuzzy_words_idx.append(i)
    res = " ".join(map(str, fuzzy_words_idx))
    print("length", len(fuzzy_words_idx))
    print(res)
    return res


def approximate_pattern_count(f: str):
    with open(f) as file:
        data = file.read()
        dat = data.split("\n")
        pattern = dat[0]
        text = dat[1]
        d = int(dat[2])
    count = count_fuzzy_matches(text=text, target_pattern=pattern, d=d)
    return count


def test():
    for x in range(10):
        if 1:
            if 1:
                print(x)
                break
        print("yo")


if __name__ == "__main__":
    text = "AACAAGCTGATAAACATTTAAAGAG"
    pattern = "AAAAA"
    d = 2
    # test()
    # count_fuzzy_matches(text=text, target_pattern=pattern, d=d)
    # f = "/Users/gandalf/Downloads/ApproximatePatternCount/inputs/input_1.txt"
    f = "/Users/gandalf/Downloads/dataset_30278_6_8.txt"
    approximate_pattern_count(f)
