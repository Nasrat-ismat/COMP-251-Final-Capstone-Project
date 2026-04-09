# Smart Network Logistics Engine (SNLE)

**Name:** Nasratullah Ismat  
**Student ID:** 300151453

## About This Project
For this project, I made a command-line program called Smart Network Logistics Engine, or SNLE. The goal was to model a city delivery network by using a weighted directed graph. In my program, the nodes are depots, warehouses, or zones, and the edges are the routes between them with a cost like travel time or distance.

The program reads the network from a text file and then lets the user choose different options from a menu. It can show a summary of the network, find the shortest path between two places, check if there are cycles in the graph, dispatch packages based on priority, search for depot information, and autocomplete depot names.

## How to Run It
Open the project folder in the terminal and run:

```bash
python src/main.py
```

## Project Structure
```text
snle/
├── src/
│   ├── main.py
│   ├── graph.py
│   ├── heap.py
│   ├── hashmap.py
│   ├── trie.py
│   └── utils.py
├── data/
│   └── network.txt
├── tests/
│   └── test_snle.py
├── README.md
└── requirements.txt
```

## What Each File Is For
### `main.py`
This is the file that runs the menu and lets the user interact with the program.

### `graph.py`
This file stores the graph using an adjacency list. It also has the graph algorithms I used, like counting connected components, Dijkstra's algorithm, cycle detection with DFS coloring, and Bellman-Ford as a bonus feature.

### `heap.py`
This file has my heap classes. I made a `MinHeap` for Dijkstra's algorithm and a `MaxHeap` for the package dispatch queue. I did not use Python's built-in heap for the actual implementation.

### `hashmap.py`
This file has my custom hash map. I used chaining, and it supports insert, search, delete, and resizing when the load factor gets too high.

### `trie.py`
This file has the trie that I used for prefix search and autocomplete for depot and zone names.

### `utils.py`
This file helps load the network data from the file. It also contains the `Package` and `DispatchQueue` classes.

## Features I Implemented
### Mandatory Parts
- graph loading from `data/network.txt`
- directed weighted graph
- adjacency list representation
- network summary with nodes, edges, and connected components
- shortest path using Dijkstra's algorithm with a custom min heap
- cycle detection using DFS coloring
- priority dispatch queue using a custom max heap
- custom hash map for depot lookup
- trie for autocomplete
- interactive menu in `main.py`

### Bonus Parts
- Bellman-Ford algorithm
- unit tests

## Complexity Analysis
### Graph Construction
- Time: `O(V + E)`
- Space: `O(V + E)`

### Dijkstra's Algorithm
- Time: `O((V + E) log V)`
- Space: `O(V)`

### Cycle Detection
- Time: `O(V + E)`
- Space: `O(V)`

### Connected Components
- Time: `O(V + E)`
- Space: `O(V + E)`

### Hash Map
- Average insert/search/delete: `O(1)`
- Worst case: `O(n)`
- Space: `O(n)`

### Trie
- Insert: `O(L)`
- Autocomplete: `O(P + M)`
- Space: depends on how many total characters are stored

### Priority Dispatch Queue
- Enqueue: `O(log n)`
- Dequeue: `O(log n)`
- Peek: `O(1)`
- Space: `O(n)`

## Sample Output
```text
===== Smart Network Logistics Engine =====
1. Display Network Summary
2. Find Shortest Path
3. Detect Cycles
4. Dispatch Highest-Priority Package
5. Search Depot by Name
6. Autocomplete Depot Name
7. Exit
==========================================
Choose an option: 1

--- Network Summary ---
Number of nodes: 6
Number of edges: 6
Connected components (weak): 1
```

Another example:

```text
Choose an option: 2
Enter source node: DepotA
Enter destination node: ZoneNorth
Shortest path: DepotA -> WarehouseX -> ZoneSouth -> DepotC -> ZoneNorth
Total cost: 8.0
```

## Notes
A few things about my program:
- it follows the file format given in the assignment
- depot information is generated automatically when the file is loaded
- if no path exists, the program shows that clearly
- the dispatch queue always removes the highest-priority package first

## Testing
To run the tests, use:

```bash
python -m unittest discover -s tests
```

## Final Thoughts
Overall, this project helped me put a lot of the course topics together in one program instead of seeing them as separate things. The graph part was used for routes, the heaps were useful for priority dispatching, the hash map helped with fast depot lookup, and the trie made the autocomplete part work. I think it was a good way to practice the data structures in a more practical kind of problem.
