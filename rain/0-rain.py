#!/usr/bin/python3
"""
Module to calculate the amount of rainwater retained between walls.

This module contains the `rain` function, which computes the total units
of water that can be trapped after it rains, based on the heights of walls
represented as a list of non-negative integers.

Functions:
- rain(walls): Returns the total amount of rainwater retained.

Example:
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6
"""


def rain(walls):
    """
    Calculate the total amount of rainwater retained.

    Args:
        walls (list): A list of non-negative integers representing the heights 
                       of walls.

    Returns:
        int: The total amount of rainwater retained after raining.
    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    water_retained = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water_retained += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water_retained += right_max - walls[right]
            right -= 1

    return water_retained


if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))  # Output: 6
