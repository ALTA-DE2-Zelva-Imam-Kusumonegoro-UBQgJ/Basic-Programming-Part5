def join_array_remove_duplicate(arrayA, arrayB):
    merged_array = []

    for i in arrayA:
        if i not in merged_array:
            merged_array.append(i)

    for i in arrayB:
        if i not in merged_array:
            merged_array.append(i)

    return merged_array



if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
