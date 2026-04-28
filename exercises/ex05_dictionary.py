"""Dictionary Utils"""

__author__: str = "730748337"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in result:
            raise KeyError(f"Duplicate key found when inverting: {value}")
        result[value] = key
    return result


def favorite_color(colors_dict: dict[str, str]) -> str:
    color_counts: dict[str, int] = {}
    for color in colors_dict.values():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    max_count: int = 0
    favorite: str = ""

    # Second pass: iterate through the original dictionary's values
    for color in colors_dict.values():
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            favorite = color
    return favorite


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for word in words:
        if len(word) > 0:
            first_letter: str = word[0].lower()
            # Check if the first character is an alphabetic letter
            if first_letter.isalpha():
                if first_letter in result:
                    result[first_letter].append(word)
                else:
                    result[first_letter] = [word]
    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_log:
        # Avoid adding duplicate attendance entries for the same student on the same day
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
