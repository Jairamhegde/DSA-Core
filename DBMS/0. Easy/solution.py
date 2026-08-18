            if i not in ary:
                index += 1
                if index == k:
                    return i

        while index < k:
            max_ele += 1
            index += 1
        return max_ele



