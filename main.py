from optimizer import super_shopping_optimizer

def main():
    # Example input
    n = 3
    distances = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
    items = [[5, 10], [20, 30], [15, 25]]
    travel_cost = 2

    # Call the super shopping optimizer function
    min_total_cost = super_shopping_optimizer(n, distances, items, travel_cost)

    # Print the minimum total cost
    print(f"The minimum total cost of shopping and travel is: {min_total_cost}")

if __name__ == "__main__":
    main()
