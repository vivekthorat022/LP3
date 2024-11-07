from collections import Counter
from heapq import heapify, heappop, heappush

def huffman_code_tree(frequencies):
    heap = [[freq, [char, " "]] for char, freq in frequencies.items()]
    heapify(heap)
    while len(heap) > 1:
        low, high = heappop(heap), heappop(heap)
        for pair in low[1:]: pair[1] = '0' + pair[1]
        for pair in high[1:]: pair[1] = '1' + pair[1]
        heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

string = 'BCAADDDCCACACAC'
freq = Counter(string)
huffman_code = huffman_code_tree(freq)

print(" Char | Huffman Code ")
print("---------------------")
for char, code in huffman_code:
    print(f" {char}    | {code}")
