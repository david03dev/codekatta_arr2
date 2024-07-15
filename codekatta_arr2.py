def trapped_water(heights):
    if not heights or len(heights) < 3:
        return 0
    
    n = len(heights)
    left = 0
    right = n - 1
    max_left = heights[left]
    max_right = heights[right]
    trapped_water_units = 0
    
    while left <= right:
        if heights[left] <= heights[right]:
            if heights[left] >= max_left:
                max_left = heights[left]
            else:
                trapped_water_units += max_left - heights[left]
            left += 1
        else:
            if heights[right] >= max_right:
                max_right = heights[right]
            else:
                trapped_water_units += max_right - heights[right]
            right -= 1
    
    return trapped_water_units

# Reading input
import sys
input = sys.stdin.read().strip().split('\n')
n = int(input[0].strip())
heights = list(map(int, input[1].strip().split()))

# Calculating trapped water units
result = trapped_water(heights)

# Output the result
print(result)
