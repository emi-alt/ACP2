seats = ["100", "110", "120", "130", "140", "150", "160", "170", "180", "190"]
target_seat = "130"
if target_seat in seats:
    print(f"Seat {target_seat} is available.")

    low = 0
    high = len(seats) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high)//2
        if seats[mid] == target_seat:
            print(f"Seat {target_seat} found at index {mid}.")
            print(f"Steps taken: {steps}")
            break
        elif seats[mid] < target_seat:
            low = mid + 1
            print(f"Searching in the upper half: low={low}, high={high}")
            if seats[low] == target_seat:
                print(f"Seat {target_seat} found at index {low}.")
                print(f"Steps taken: {steps}")
                break
        else:
            high = mid - 1
            print(f"Searching in the lower half: low={low}, high={high}")
            if seats[high] == target_seat:
                print(f"Seat {target_seat} found at index {high}.")
                print(f"Steps taken: {steps}")
                break
print("Steps Taken:", steps)
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")

def recursive_search(seats, target, low, high):
    if low > high:
        print(f"Seat {target} not found.")
        return -1 
    mid = (low + high)//2
    if seats[mid] == target:
        return mid
    elif seats[mid] > target:
        return recursive_search(seats, target, low, mid - 1)
    else:
        return recursive_search(seats, target, mid + 1, high)

print("Recursive Search Steps Taken:", steps)
print("Recursive Time Complexity: O(log n)")
print("Space Complexity: O(log n) because of the call stack")

print("Complexity Ladder: ")
print("1. Linear Search - O(n) \nChecking every number one by one.")
print("2. Binary Search - O(log n) \nDividing the search space in half each time.")
print("3. Double Loop   - O(n^2) \nChecking every number in a nested loop.")