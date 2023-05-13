bases = ['x', 'y', 'z', 'yz', 'zx', 'xy', 'xyz']
length = len(bases)

def evaluate(product):
    characters = list(product)
    count = len(characters)
    notSorted = True
    sign = 1
    while notSorted:
        notSorted = False
        for i in range(count-1):
            if characters[i] > characters[i+1]:
                swap = characters[i]
                characters[i] = characters[i+1]
                characters[i+1] = swap
                sign = -sign
                notSorted = True
    processed = []
    i = 0
    while i < count-1:
        if characters[i] < characters[i+1]:
            processed += characters[i]
            i += 1
        else:
            sign = -sign
            i += 2
    if i < count:
        processed += characters[i]
    if len(processed) == 0:
        processed += '1'
    pseudo = list(bases[length-1])
    first = pseudo[0]
    last = pseudo[len(pseudo)-1]
    if processed == [first, last]:
        processed = [last, first]
        sign = -sign
    if sign < 0:
        processed.insert(0, '-')
    result = ''.join(processed)
    return result

def printHeader():
    header = '\t1\t'
    for h in range(length):
        header += bases[h] + '\t'
    print(header)
    print('-------------------------------------------------------------------')

def printRows():
    first = '1\t1\t'
    for i in range(length):
        first += bases[i] + '\t'
    print(first)
    for i in range(length):
        row = bases[i] + '\t' + bases[i] + '\t'
        for j in range(length):
            product = bases[i] + bases[j]
            row += evaluate(product) + '\t'
        print(row)

def printTable():
    printHeader()
    printRows()

printTable()
