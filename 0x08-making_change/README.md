# 0x08-making_change

## Description

This project involves determining the fewest number of coins needed to meet a given amount total. The solution uses a dynamic programming approach to find the optimal number of coins.

## Usage

To use the `makeChange` function, you need to provide a list of coin values and the total amount. The function returns the fewest number of coins needed to meet the total, or -1 if the total cannot be met with the given coins.

## Example

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
