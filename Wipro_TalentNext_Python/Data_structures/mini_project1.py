# mini_project.py

def display_facts(facts):
    for person, fact in facts.items():
        print(f"{person}: {fact}")

def main():
    # Initial dictionary of people and their interesting facts
    people_facts = {
        "Jeff": "Is afraid of Dogs.",
        "David": "Plays the piano.",
        "Jason": "Can fly an airplane."
    }

    print("Original facts:")
    display_facts(people_facts)

    print("\nUpdated facts:")
    # Change Jeff's fact
    people_facts["Jeff"] = "Is afraid of heights."
    # Add a new person
    people_facts["Jill"] = "Can hula dance."

    display_facts(people_facts)

if __name__ == "__main__":
    main()
