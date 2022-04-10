

def quick_sort(collection: list) -> list:
    """
    """

    if len(collection) < 2:
        return collection

    pivot = collection.pop()

    greater: list[int] = []
    lesser: list[int] = []
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == '__main__':

    unsorted = [4,6,7,3,100,2,1,0]

    print(quick_sort(unsorted))
