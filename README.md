# SnakeAI

# Algorithm (Domain Specific)
- **Setup heuristic function to calculate cost of travel from given cell to destination**
    - Euclidean distance
- **Get adjacent cells**
- **Validate cells**
    - Outside boundary
    - Belongs to snake body
    - Reject invalid cells
- **For each valid adjacent cell** 
    - Apply heuristic function and find cost
    - Chose cell with lowest cost
    - If cost of cells is equal
    - Chose any one
- **Find direction of the cell**
    - Subtract coords to find which coord becomes 0
        - (valid adj cell coords - head coords) / 20
        - x = 1 and y = 0 -> move right
        - x = -1 and y = 0 -> move left
        - x = 0 and y = 1 -> move down
        - x = 0 and y = -1 -> move up
- **Move head in that direction**

# Performance
- Does well upto an average score of **50**
- Struggles at **large** body sizes when fruit is present **close** to the body
