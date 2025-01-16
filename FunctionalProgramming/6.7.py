# List of ratings from 5 judges for each competitor
ratings = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16)
]

# Function to calculate the total score by removing the highest and lowest scores
def calculate_final_score(scores):
    return sum(scores) - min(scores) - max(scores)

# Use map() to calculate the final scores for each competitor
final_scores = list(map(calculate_final_score, ratings))

# Display the result
print(final_scores)
