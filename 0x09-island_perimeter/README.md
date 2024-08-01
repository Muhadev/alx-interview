# Island Perimeter Calculator

## Description

This project includes a Python function to calculate the perimeter of an island described in a grid. Each cell in the grid can either be land (`1`) or water (`0`). The function calculates the perimeter by examining the boundaries of the land cells.

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS

## Files

- `0-island_perimeter.py`: Contains the `island_perimeter` function to calculate the perimeter of the island.
- `0-main.py`: Contains a test script to demonstrate the usage of the `island_perimeter` function.

## Usage

1. Ensure that both `0-island_perimeter.py` and `0-main.py` are in the same directory.
2. Make the scripts executable:

    ```bash
    chmod +x 0-island_perimeter.py
    chmod +x 0-main.py
    ```

3. Run the test script:

    ```bash
    ./0-main.py
    ```

    The script will print the perimeter of the island based on the provided grid.

## Example

For the grid:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
