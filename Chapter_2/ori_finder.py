from tqdm import tqdm

def find_clumps(f, k=None, ell=None, t=None):
    with open(f) as file:
        data = file.read()
        if k is None:
            txt, digits = data.strip().split("\n")
            k, ell, t = digits.split(" ")
            k = int(k)
            ell = int(ell)
            t = int(t)
        else:
            txt = data.strip()
        patterns = set()
        n = len(txt)
        window = txt[:ell]
        freq_map = {}

        for i in tqdm(range(n - ell)):
            if i == 0:
                # Calculate the window
                for j in range(ell - k):
                    pttern = window[j : j + k]
                    if pttern not in freq_map:
                        freq_map[pttern] = 1
                    else:
                        freq_map[pttern] += 1
                for s in freq_map.keys():
                    if freq_map[s] >= t:
                        patterns.add(s)
            else:
                new_mer = window[-k + 1 :] + txt[i + ell - 1]
                old_mer = window[:k]
                window = txt[i : ell + i]
                if old_mer in freq_map:
                    freq_map[old_mer] -= 1
                    if freq_map[old_mer] < 0:
                        freq_map[old_mer] = 0
                if new_mer not in freq_map:
                    freq_map[new_mer] = 1
                else:
                    freq_map[new_mer] += 1

                if freq_map[new_mer] >= t:
                    patterns.add(new_mer)
    res = list(patterns)
    print(f"Count: {len(res)}")
    result = " ".join(res)
    print(f"answer: {result}")
    return result

if __name__=='__main__': 
    f = "/Users/gandalf/Downloads/Salmonella_enterica.txt"
    find_clumps(f, k=9, ell=1000, t=1)