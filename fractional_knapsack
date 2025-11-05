# Fractional Knapsack Problem using Greedy Method

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio


def fractional_knapsack(capacity, items):
    # Step 1: Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Maximum profit that can be achieved
    remaining_capacity = capacity

    # Step 2: Iterate through items
    for item in items:
        if remaining_capacity == 0:
            break

        # If the whole item can be added
        if item.weight <= remaining_capacity:
            total_value += item.value
            remaining_capacity -= item.weight
            print(f"Added full item (value={item.value}, weight={item.weight})")
        else:
            # Take fractional part of the item
            fraction = remaining_capacity / item.weight
            total_value += item.value * fraction
            print(f"Added {fraction*100:.2f}% of item (value={item.value}, weight={item.weight})")
            remaining_capacity = 0  # Knapsack full

    return total_value


# Driver code
if __name__ == "__main__":
    # Input: list of items (value, weight)
    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]

    capacity = 50
    max_value = fractional_knapsack(capacity, items)
    print(f"\nMaximum value in knapsack = {max_value:.2f}")
