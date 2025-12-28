def hamming_distance(f: str):
    dist = 0
    with open(f) as file:
        data = file.read()
        data_list = data.split("\n")
        for x, y in zip(data_list[0], data_list[1]):
            if x != y:
                dist += 1
    print(dist)
    return dist




if __name__ == "__main__":
    f = "/Users/gandalf/Downloads/dataset_30278_3.txt"
    hamming_distance(f)
