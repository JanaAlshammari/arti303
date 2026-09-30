"""TODO: describe this module."""
"""Utility functions for cleaning and processing text data."""


def clean_name(raw):
    """TODO: describe this function."""
    """Clean a messy name string by removing extra whitespace and converting to title case."""
    # TODO: collapse whitespace, then title-case
    cleaned = " ".join(raw.split()) 
    return cleaned.title()
    pass

