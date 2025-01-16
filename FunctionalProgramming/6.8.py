# List of student scores
scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

# Higher-order function that returns a lambda to check if a score meets the minimum limit
def min_pts(limit):
    return lambda pts: pts >= limit

# Use filter() to get scores greater than or equal to the specified limits
min_70_pts = list(filter(min_pts(70), scores))
min_40_pts = list(filter(min_pts(40), scores))
min_30_pts = list(filter(min_pts(30), scores))

# Display the results
print(f"Min 70 pts: {min_70_pts}")
print(f"Min 40 pts: {min_40_pts}")
print(f"Min 30 pts: {min_30_pts}")
