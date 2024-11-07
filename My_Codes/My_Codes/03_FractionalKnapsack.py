class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def fractionalKnapsack(W, arr):
        arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
        finalvalue = 0.0
        for item in arr:
            if item.weight <= W:
                W -= item.weight
                finalvalue += item.value
            else:
                finalvalue += item.value * W / item.weight
                break
        return finalvalue

if __name__ == "__main__":
    W = float(input("Enter the total capacity of the knapsack: "))
    n = int(input("Enter the number of items: "))
    arr = []
    for i in range(n):
        value = float(input(f"\nEnter the value of item {i+1}: "))
        weight = float(input(f"Enter the weight of item {i+1}: "))
        arr.append(Item(value, weight))
    max_val = Item.fractionalKnapsack(W, arr)
    print(f"\nThe maximum value that can be obtained in the knapsack is: {max_val}")