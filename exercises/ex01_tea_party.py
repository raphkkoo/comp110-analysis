"""Tea Party Planning"""

__author__: str = "730748337"


def main_planner(guests: int) -> None:
    """Master planner"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# realized that I had to standardize every return value to a string since I was writing a sentence


def tea_bags(people: int) -> int:
    """Calculate for how many teabags we need"""
    return people * 2


def treats(people: int) -> int:
    """Calculate for how many treats we need"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
