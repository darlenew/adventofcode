def get_data(path):
    with open(path, 'r') as fd:
        data = [int(line.strip()) for line in fd]

    return data

def is_sum2(lst, num):
    """Return True if there are 2 values in the lst that sum to num, otherwise False"""
    complements = set()

    for x in lst:
        if x in complements:
            return True
        complements.add(num - x)

    return False

def find_error(data, preamble):
    i = preamble

    while True:
        start = i - preamble
        window = data[start:i]
        print(window, data[i])

        if not is_sum2(window, data[i]):
            return data[i]

        i += 1

def find_contiguous_sum(lst, target):
    """Return contiguous sum of at least 2 numbers in the lst that add up to target"""
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            contiguous_sum = sum(lst[i:j])
            if contiguous_sum == target:
                return lst[i:j]
            if contiguous_sum > target:
                break

data = get_data('09-encoding-error.txt')
num = find_error(data, 25)
print(num)
contiguous_sum = find_contiguous_sum(data, num)
print(contiguous_sum)
answer = min(contiguous_sum) + max(contiguous_sum)
print(answer)
