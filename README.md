# SnakeAI

# Algorithm (Domain Specific)
- setup heuristic function to calculate cost of travel from given node to destination 
    - euclidean distance
- get adjacent cells
- validate cells
    - outside boundary
    - belongs to snake body
    - reject invalid cells
- for each valid adj cell 
    - apply heuristic function and find cost
- chose cell with lowest cost
    - if cost of cells is equal
        - chose any one
- find direction of the cell
    - subtract coords to find which coord becomes 0
        -  valid adj cell coords - head coords
    - x > 0 and y = 0
        - move right
    - x < 0 and y = 0
        - move left
    - x = 0 and y > 0
        - move down
    - x = 0 and y < 0
        - move up
- move head in that direction 
- repeat
