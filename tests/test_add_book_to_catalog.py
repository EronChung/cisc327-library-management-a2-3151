import pytest
from services.library_service import (
    add_book_to_catalog
)


def test_add_book_valid_input():
    """Test adding a book with valid input."""
    success, message = add_book_to_catalog("Test Book", "Test Author", "1234567890123", 5)
    
    assert success == True
    assert "successfully added" in message.lower()


def test_add_book_invalid_no_title():
    """Test adding a book with no title."""
    success, message = add_book_to_catalog("", "Test Author", "1234567890123", 5)
    
    assert success == False
    assert "Title is required" in message


def test_add_book_invalid_title_too_long():
    """Test adding a book with title too long."""
    success, message = add_book_to_catalog("aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAbcde", "Test Author", "1234567890123", 5)
    
    assert success == False
    assert "200 characters" in message


def test_add_book_invalid_no_author():
    """Test adding a book with no author."""
    success, message = add_book_to_catalog("Test Book", "", "1234567890123", 5)
    
    assert success == False
    assert "Author is required" in message


def test_add_book_invalid_author_too_long():
    """Test adding a book with author too long."""
    success, message = add_book_to_catalog("Test Book", "aaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAaaaaaaaaaaAAAAAAAAAAbcde", "1234567890123", 5)
    
    assert success == False
    assert "100 characters" in message


def test_add_book_invalid_isbn_too_short():
    """Test adding a book with ISBN too short."""
    success, message = add_book_to_catalog("Test Book", "Test Author", "123456789", 5)
    
    assert success == False
    assert "13 digits" in message


def test_add_book_invalid_isbn_too_long():
    """Test adding a book with ISBN too long."""
    success, message = add_book_to_catalog("Test Book", "Test Author", "123456789012345", 5)
    
    assert success == False
    assert "13 digits" in message


def test_add_book_invalid_copies_negative():
    """Test adding a book with total copies being negative."""
    success, message = add_book_to_catalog("Test Book", "Test Author", "1234567890123", -10)
    
    assert success == False
    assert "positive integer" in message


def test_add_book_invalid_copies_zero():
    """Test adding a book with total copies being zero."""
    success, message = add_book_to_catalog("Test Book", "Test Author", "1234567890123", 0)
    
    assert success == False
    assert "positive integer" in message


# ===== Tests added in Assignment 3 =====

def test_add_book_invalid_duplicate_isbn():
    """Test adding a book with an ISBN already in use (input same as first valid test)."""
    success, message = add_book_to_catalog("Test Book", "Test Author", "1234567890123", 5)
    
    assert success == False
    assert "ISBN already exists" in message


def test_add_book_database_error(mocker):
    """Test database error when adding a book."""
    mocker.patch("services.library_service.insert_book", return_value=False)
    
    success, message = add_book_to_catalog("Test Book", "Test Author", "1111111111111", 5)
    
    assert success == False
    assert "Database error" in message