"""
Count k-mers in DNA.
"""

def patternCount(f):
    with open(f) as file:
        data = file.read()
        print(data)
        txt, pattern = data.strip().split('\n')
        
        cnt = 0
        for i in range(len(txt)- len(pattern)):
            if txt[i:len(pattern) + i] == pattern:
                cnt += 1
        print(f'answer: {cnt}')
        return cnt
f = '/Users/gandalf/Downloads/dataset_30272_6_2.txt'

# g = "/Users/gandalf/Downloads/PatternCount/inputs/input_1.txt"
patternCount(f)
