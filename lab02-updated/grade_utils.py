"""TODO: Utility module is for computing the letter grade based on a 5.0 GPA scale."""


def letter_grade(gpa):
    """TODO: Convert a numerical GPA out of -5.0 to- a letter grade."""
    # TODO: your if/elif chain here
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"

