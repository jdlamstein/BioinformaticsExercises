"""
Run function and compare with output file
"""

from Chapter_2.count_fuzzy import approximate_pattern_count
from Chapter_2.freq_words_with_mismatch import (
    run_frequent_words_with_mismatch,
    run_frequent_words_with_mismatch_and_reverse_complement,
)
import os
from glob import glob


def runner(test_function, directory: str):
    inputs = sorted(glob(os.path.join(directory, "inputs", "*.txt")))
    outputs = sorted(glob(os.path.join(directory, "outputs", "*.txt")))
    for i, o in zip(inputs, outputs):
        assert (
            os.path.basename(i).split("_")[-1] == os.path.basename(o).split("_")[-1]
        ), f"{i} {o}"
        res = test_function(i)
        with open(o) as file:
            answer = file.read()
        answer_lst = answer.strip().replace("\n", " ").split(" ")
        res_lst = res.strip().split(" ")
        for ans in answer_lst:
            assert ans in res_lst, f"{ans} not in {res_lst}"
        for r in res_lst:
            assert r in answer_lst, f"{r} not in {answer_lst}"
        print(f"Answer: {answer}")
        print(f"Res: {res}")
        print("Pass")


if __name__ == "__main__":
    test_function = run_frequent_words_with_mismatch_and_reverse_complement
    directory = "/Users/gandalf/Downloads/FrequentWordsMismatchesReverseComplements/"

    runner(test_function, directory=directory)
