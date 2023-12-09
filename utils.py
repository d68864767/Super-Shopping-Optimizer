def calculate_travel_cost(distances, travel_cost):
    """
    Function to calculate the total travel cost given the distances and cost per unit distance.
    """
    total_distance = sum(distances)
    return total_distance * travel_cost

def find_min_item_cost(items):
    """
    Function to find the minimum cost item in each department.
    """
    min_costs = [min(department) for department in items]
    return min_costs

def calculate_total_cost(min_costs, travel_cost):
    """
    Function to calculate the total cost given the minimum item costs and travel cost.
    """
    return sum(min_costs) + travel_cost
