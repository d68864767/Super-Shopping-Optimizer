import heapq
from utils import calculate_travel_cost, find_min_item_cost, calculate_total_cost

def super_shopping_optimizer(n, distances, items, travel_cost):
    """
    Function to find the minimum total cost of shopping and travel.
    """
    # Create a list to store the minimum cost to reach each department
    min_cost_to_reach = [float('inf')] * n
    min_cost_to_reach[0] = 0

    # Create a priority queue and add the first department to it
    queue = [(0, 0)]  # (cost, department)

    while queue:
        cost, department = heapq.heappop(queue)

        # If we have already found a cheaper way to reach this department, skip it
        if cost > min_cost_to_reach[department]:
            continue

        # Try to move to each other department
        for next_department in range(n):
            if next_department != department:
                # Calculate the cost to move to the next department
                travel_distance = distances[department][next_department]
                travel_cost_to_next = calculate_travel_cost([travel_distance], travel_cost)

                # Calculate the cost to buy the cheapest item in the next department
                item_cost_in_next = find_min_item_cost([items[next_department]])[0]

                # Calculate the total cost to move to the next department and buy an item there
                total_cost_to_next = calculate_total_cost([item_cost_in_next], travel_cost_to_next)

                # If this is a cheaper way to reach the next department, update our cost to reach it
                if cost + total_cost_to_next < min_cost_to_reach[next_department]:
                    min_cost_to_reach[next_department] = cost + total_cost_to_next
                    heapq.heappush(queue, (min_cost_to_reach[next_department], next_department))

    # Return the minimum cost to reach the last department
    return min_cost_to_reach[-1]
