def task(array):
    for i in range(len(array)):
        if i == len(array) - 1:
            return f"No 0 in array"
        elif array[i] != array[i+1]:
            return i + 1