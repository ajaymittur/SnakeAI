import math

def h(curr, dest):
    """
    Parameters:
        curr: tuple -> (currx, curry)
        dest: tuple -> (destx, desty)

    Return:
        cost: float

    """

    # Euclidean distance between destination and current cell
    cost = math.sqrt((dest[0] - curr[0])**2 + (dest[1] - curr[1])**2)
    return cost


def getAdjacentCells(head):
    """
    Parameters:
        head: tuple -> (headx, heady)

    each cell size in this game = 20x20

    Return:
        adj_cells: list -> [top, right, bottom, left]
        top, right, bottom, left: tuples -> (x, y)
    """

    adj_cells = []
    multipliers = ((0, -1), (1, 0), (0, 1), (-1, 0))

    for dirX, dirY in multipliers:
        cell = head[0] + 20*dirX, head[1] + 20*dirY  
        adj_cells.append(cell)

    return adj_cells


def getValidCells(cells, snake_body_coords):
    """
    Parameters:
        cells: list -> [top, right, bottom, left]
            top, right, bottom, left: tuples -> (x, y)
        snake_body_coords: list -> [coord1, coord2, .....]
            coords: tuples -> (bodyx, bodyy)

    screen size of the game = 820x820

    Return:
        valid_cells: list
    """

    valid_cells = []

    for cell in cells:
        if cell[0] >= 0 and cell[0] < 820 and cell[1] >= 0 and cell[1] < 820:
            if cell not in snake_body_coords:
                valid_cells.append(cell)

    return valid_cells


def getCosts(valid_cells, dest):
    """
    Parameters:
        valid_cells: list -> [cell1, cell2, .....]
            cells: tuples -> (x, y)
        dest: tuple -> (destx, desty)

    Return:
        costs: list -> [cost_of_cell1, cost_of_cell2, .....]
            cost_of_cell: float
    """

    costs = []

    for cell in valid_cells:
        costs.append(h(cell, dest))

    return costs


def cellWithLeastCost(valid_cells, costs):
    """
        Parameters:
            valid_cells: list -> [cell1, cell2, .....]
                cells: tuples -> (x, y)
            costs: list -> [cost_of_cell1, cost_of_cell2, .....]
                cost_of_cell: float

        Return:
            cell_with_least_cost: tuple -> (x, y)
    """
    if costs:
        lowest_cost = min(costs)
        least_cost_cell_index = costs.index(lowest_cost)  
        cell_with_least_cost = valid_cells[least_cost_cell_index]  
        return cell_with_least_cost
    else:
        return None

def getDirection(cell_with_least_cost, head):
    """
    Parameters:
        cell_with_least_cost: tuple -> (x, y)
        head: tuple -> (headx, heady)

    Return:
        direction: tuple -> (dirX, dirY)
    """

    dirX = int((cell_with_least_cost[0] - head[0]) / 20)
    dirY = int((cell_with_least_cost[1] - head[1]) / 20)

    return (dirX, dirY)

