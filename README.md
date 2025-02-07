# Rush Hour Solver

## Overview
This project implements a **Rush Hour puzzle solver** using multiple search algorithms. The goal is to move vehicles within a **6x6 grid** to free a path for a designated car to exit. The solver uses **Breadth-First Search (BFS)**, **A* Search**, and **Depth-First Search (DFS)** to find solutions efficiently.

This project was part of **Milestone 1 for 2802ICT Intelligent Systems** and involved implementing **pathfinding algorithms** to find solutions to the game Rush Hour.

---

## About the Game
**Rush Hour** is a sliding block puzzle where the goal is to move a target vehicle (typically a red car) out of a congested 6x6 traffic grid. The player (or algorithm) must rearrange the other vehicles, which can only move forward or backward within their allocated lanes, to clear a path for the target vehicle to exit. The challenge lies in finding the optimal sequence of moves to reach the solution efficiently.

---

## Features
- **Rush Hour Game Representation**
  - The game board is stored as a **6x6 grid** with different vehicles represented by uppercase letters (vertical vehicles) and lowercase letters (horizontal vehicles).
  - Vehicles can be **cars (length 2)** or **trucks (length 3)**.

- **Search Algorithms Implemented**
  - **Breadth-First Search (BFS)** – Guarantees shortest path but may explore many nodes.
  - **A* Search** – Uses heuristics to optimize search efficiency.
  - **Depth-First Search (DFS)** – Explores paths deeply before backtracking.
  - **Iterative Deepening Depth-First Search (IDDFS)** – Combines advantages of BFS and DFS.

- **Precomputed Solutions**
  - BFS and A* solutions are stored in `BFS Solutions.txt` and `A* Solutions.txt`, respectively.
  - Execution time, number of nodes visited (BFS), and solution depth (BFS) are logged.

---

## File Structure

### `rush_hour.py`
- **Core Implementation**
  - Reads game instances from `rh.txt`.
  - Converts board state to **6x6 representation**.
  - Generates **valid moves** for vehicles.
  - Runs **search algorithms** to find solutions.
- **Functions:**
  - `text_load()` – Loads game instances.
  - `display_problem()` – Converts board representation to 6x6.
  - `gen_next_states()` – Generates valid next moves.
  - `bfs_search()` – Implements BFS.
  - `dfs_search()` – Implements DFS.
  - `iterative_deepening()` – Implements IDDFS.
  - `clean_movement_path()` – Formats solution output.

### `rh.txt`
- Contains **Rush Hour puzzle instances**.
- Each puzzle is represented as a **6x6 grid**.
- Below each puzzle, a **precomputed solution** is provided.

### `A* Solutions.txt`
- Stores **A* search solutions**.
- Each solution includes:
  - **Move sequence** (e.g., `['AR1', 'PU1', 'OD1', ...]`).
  - **Execution time** in seconds.

### `BFS Solutions.txt`
- Stores **BFS search solutions**.
- Each solution includes:
  - **Move sequence**.
  - **Execution time**.
  - **Nodes visited**.
  - **Solution depth**.

---

## Search Algorithm Performance
| Problem | A* Time (s) | BFS Time (s) | Nodes Visited (BFS) |
|---------|------------|-------------|-----------------|
| 1       | 0.298     | 0.306       | 1076            |
| 14      | 147.29    | 180.49      | 16495           |
| 25      | 42.79     | 38.83       | 8896            |

- **A* Search is generally faster**, especially for complex puzzles.
- **BFS guarantees shortest paths** but explores significantly more nodes.

---

## How to Run
### Requirements
- Python 3.x
- Required Libraries: `ujson`, `heapq`, `re`, `time`, `queue`, `copy`.

### Running the Solver
```bash
python rush_hour.py
```
- The program will read a puzzle from `rh.txt` and attempt to solve it using the chosen search algorithm.
- Solutions will be displayed and logged in the output files.

---

## Future Improvements
- Implement additional heuristics to improve **A* efficiency**.
- Add a **GUI visualization** for interactive solving.
- Optimize **state generation** to reduce redundant calculations.

---

## Author
Developed as part of a project to explore **search algorithms in AI problem-solving**.
