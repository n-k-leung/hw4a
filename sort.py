def sort_dictionary(dict):
    reverse = {}
    result = []
    for i in dict:
        name = i
        phoneNum = dict[i][0]
        age = dict[i][1]
        if age not in reverse:
            reverse[age] = [(name, phoneNum)]
        else:
            reverse[age].append((name, phoneNum))

    for j in sorted(reverse.keys()):
        result += reverse[j]
    return result
