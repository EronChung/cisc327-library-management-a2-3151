import pytest
from services.library_service import (
    search_books_in_catalog
)


def test_search_books_valid_input_title():
    """Test searching for books with valid title."""
    books = search_books_in_catalog("1984", "title")
    
    assert len(books) == 1
    assert books[0]["id"] == 3


def test_search_books_valid_input_author():
    """Test searching for books with valid author."""
    books = search_books_in_catalog("Harper", "author")
    
    assert len(books) == 1
    assert books[0]["id"] == 2


def test_search_books_valid_input_isbn():
    """Test searching for books with valid isbn."""
    books = search_books_in_catalog("9780743273565", "isbn")
    
    assert len(books) == 1
    assert books[0]["id"] == 1


def test_search_books_invalid_no_term():
    """Test searching for books with no term."""
    books = search_books_in_catalog("", "title")
    
    assert len(books) == 0


def test_search_books_invalid_no_type():
    """Test searching for books with no search type."""
    books = search_books_in_catalog("1984", "")
    
    assert len(books) == 0


def test_search_books_invalid_wrong_type():
    """Test searching for books with invalid search type."""
    books = search_books_in_catalog("1984", "abc123")
    
    assert len(books) == 0