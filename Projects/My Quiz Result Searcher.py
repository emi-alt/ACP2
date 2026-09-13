quiz_scores = [45, 62, 78, 85, 91, 56, 73, 88]
print("Quiz Scores:", quiz_scores)
first_score = quiz_scores[0]
print("Time Complexity: O(i)")
print("First Quiz Score:", first_score)
target_score = 88
steps = 0

for score in quiz_scores:
    steps += 1
    if score == target_score:
        print(f"Score {target_score} found after {steps} steps.")
        break
