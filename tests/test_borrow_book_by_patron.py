import pytest
from services.library_service import (
    borrow_book_by_patron
)


def test_borrow_book_valid_input():
    """Test borrowing a book with valid input."""
    success, message = borrow_book_by_patron("123456", 1)
    
    assert success == True
    assert "successfully" in message.lower()


def test_borrow_book_invalid_no_patron():
    """Test borrowing a book with no patron."""
    success, message = borrow_book_by_patron("", 1)
    
    assert success == False
    assert "Invalid patron" in message


def test_borrow_book_invalid_patron_too_short():
    """Test borrowing a book with patron ID too short."""
    success, message = borrow_book_by_patron("12345", 1)
    
    assert success == False
    assert "Invalid patron" in message


def test_borrow_book_invalid_patron_too_long():
    """Test borrowing a book with patron ID too long."""
    success, message = borrow_book_by_patron("1234567", 1)
    
    assert success == False
    assert "Invalid patron" in message


def test_borrow_book_invalid_patron_not_number():
    """Test borrowing a book with patron ID being a non-number."""
    success, message = borrow_book_by_patron("123abc", 1)
    
    assert success == False
    assert "Invalid patron" in message


def test_borrow_book_invalid_book_not_found():
    """Test borrowing a book with book not existing."""
    success, message = borrow_book_by_patron("123456", 100000)
    
    assert success == False
    assert "Book not" in message


# ===== Tests added in Assignment 3 =====

def test_borrow_book_invalid_no_copies(mocker):
    """Test borrowing a book with no more copies left."""
    mocker.patch("services.library_service.get_book_by_id",
                 return_value={
                    "available_copies": 0
                 })
    
    success, message = borrow_book_by_patron("123456", 1)
    
    assert success == False
    assert "currently not available" in message


def test_borrow_book_invalid_borrow_limit(mocker):
    """Test borrowing a book when borrow limit is already reached."""
    mocker.patch("services.library_service.get_patron_borrow_count", return_value=6)
    
    success, message = borrow_book_by_patron("123456", 1)
    
    assert success == False
    assert "maximum borrowing limit" in message