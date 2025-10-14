import pytest
from library_service import (
    get_patron_status_report
)


def test_patron_status_valid_input():
    """Test getting status report for a patron with valid input."""
    report = get_patron_status_report("123456")
    
    assert len(report["borrowed_books"]) > 0
    assert report["borrowed_books"][0]["book_id"] == 3  # Still borrowing 1984
    assert report["borrow_count"] == 1
    assert report["total_late_fees"] == 0


def test_patron_status_invalid_no_patron():
    """Test getting status report for a patron with no ID."""
    report = get_patron_status_report("")
    
    assert len(report["borrowed_books"]) == 0
    assert report["borrow_count"] == 0


def test_patron_status_invalid_patron_too_short():
    """Test getting status report for a patron with ID being too short."""
    report = get_patron_status_report("12345")
    
    assert len(report["borrowed_books"]) == 0
    assert report["borrow_count"] == 0


def test_patron_status_invalid_patron_too_long():
    """Test getting status report for a patron with ID being too long."""
    report = get_patron_status_report("1234567")
    
    assert len(report["borrowed_books"]) == 0
    assert report["borrow_count"] == 0


def test_patron_status_invalid_patron_not_number():
    """Test getting status report for a patron with ID not being a number."""
    report = get_patron_status_report("1a2b3c")
    
    assert len(report["borrowed_books"]) == 0
    assert report["borrow_count"] == 0