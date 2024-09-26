def rain(walls):
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
