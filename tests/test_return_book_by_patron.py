import pytest
from library_service import (
    return_book_by_patron
)


def test_return_book_valid_input():
    """Test returning a book with valid input."""
    success, message = return_book_by_patron("123456", 1)
    
    assert success == True
    # No return message yet to assert on


def test_return_book_invalid_no_patron():
    """Test returning a book with no patron."""
    success, message = return_book_by_patron("", 1)
    
    assert success == False
    # No return message yet to assert on


def test_return_book_invalid_patron_too_short():
    """Test returning a book with patron ID too short."""
    success, message = return_book_by_patron("12345", 1)
    
    assert success == False
    # No return message yet to assert on


def test_return_book_invalid_patron_too_long():
    """Test returning a book with patron ID too long."""
    success, message = return_book_by_patron("1234567", 1)
    
    assert success == False
    # No return message yet to assert on


def test_return_book_invalid_patron_not_number():
    """Test returning a book with patron ID being a non-number."""
    success, message = return_book_by_patron("123abc", 1)
    
    assert success == False
    # No return message yet to assert on


def test_return_book_invalid_book_not_found():
    """Test returning a book with book not existing."""
    success, message = return_book_by_patron("123456", 100000)
    
    assert success == False
    # No return message yet to assert on