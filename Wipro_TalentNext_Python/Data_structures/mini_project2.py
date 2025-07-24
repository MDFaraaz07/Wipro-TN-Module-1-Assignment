# mini_project2.py

def find_runner_up(scores):
    # Remove duplicates by converting to set
    unique_scores = list(set(scores))

    # Sort in descending order
    unique_scores.sort(reverse=True)

    # Check if we have at least 2 unique scores
    if len(unique_scores) < 2:
        return "Runner-up score not found. Not enough unique scores."
    
    # Return the second highest score
    return unique_scores[1]

def main():
    # You can take input from user or hardcode like this
    scores = [2, 3, 6, 6, 5]

    runner_up = find_runner_up(scores)
    print("Runner-up score:", runner_up)

if __name__ == "__main__":
    main()
