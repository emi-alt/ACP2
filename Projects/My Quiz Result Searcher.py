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

Best_case = 45
Avg_case = 85
Worst_case = 88

pair_steps = 0
for i in quiz_scores:
    for j in quiz_scores:
        pair_steps += 1

print("SUMMARY")

print("O(1): Direct access is fastest.")
print("O(n): Linear search grows with the number of scores.")
print("O(n^2): Nested loops grow much faster.")
print("Omega(1): Best case for search when the target is found first.")
print("Theta(1): Direct access always takes constant time.")
print("Big-O shows the upper/worst-case growth.")