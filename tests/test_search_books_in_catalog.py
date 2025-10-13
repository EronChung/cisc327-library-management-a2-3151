import pytest
from library_service import (
    search_books_in_catalog
)


def test_search_books_valid_input():
    """Test searching for books with valid input."""
    success, message = search_books_in_catalog("1984", "title")
    
    assert success == True
    # No return message yet to assert on


def test_search_books_invalid_no_term():
    """Test searching for books with no term."""
    success, message = search_books_in_catalog("", "title")
    
    assert success == False
    # No return message yet to assert on


def test_search_books_invalid_no_type():
    """Test searching for books with no search type."""
    success, message = search_books_in_catalog("1984", "")
    
    assert success == False
    # No return message yet to assert on


def test_search_books_invalid_wrong_type():
    """Test searching for books with invalid search type."""
    success, message = search_books_in_catalog("1984", "abc123")
    
    assert success == False
    # No return message yet to assert on