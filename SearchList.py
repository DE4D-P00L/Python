a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def b_search(lst, elem):
    lb = 0
    ub = len(lst)
    while lb <= ub:
        mid = int((lb+ub)/2)

        if lst[mid] == elem:
            return 1

        elif lst[mid] < elem:
            lb = mid + 1

        elif lst[mid] > elem:
            ub = mid - 1

    return 0


x = b_search(a, 12)
print(x)
