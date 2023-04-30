def merge(l1,l2):
        size1 = len(l1)
        size2 = len(l2)
        merged = []
        i = 0
        j = 0
        while i < size1 and j < size2:
                if l1[i] <= l2[i]:
                        merged.append(l1[i])
                        i = i + 1
                else:
                        merged.append(l2[j])
                        j = j + 1
        if(i<size1):
                merged.extend(l1[i:])
        if(j<size2):
                merged.extend(l2[j:])
        return merged
