import pytest
from services.library_service import (
    calculate_late_fee_for_book
)


def test_calculate_late_fee_valid_input():
    """Test calculating late fee with valid input."""
    fee_dict = calculate_late_fee_for_book("123456", 1)
    
    assert fee_dict["fee_amount"] == 0
    assert fee_dict["days_overdue"] == 0
    assert fee_dict["status"] == "Not late"


def test_calculate_late_fee_invalid_no_patron():
    """Test calculating late fee with no patron."""
    fee_dict = calculate_late_fee_for_book("", 1)
    
    assert fee_dict["fee_amount"] == -1
    assert fee_dict["days_overdue"] == -1
    assert fee_dict["status"] == "Unknown"


def test_calculate_late_fee_invalid_patron_too_short():
    """Test calculating late fee with patron ID too short."""
    fee_dict = calculate_late_fee_for_book("12345", 1)
    
    assert fee_dict["fee_amount"] == -1
    assert fee_dict["days_overdue"] == -1
    assert fee_dict["status"] == "Unknown"


def test_calculate_late_fee_invalid_patron_too_long():
    """Test calculating late fee with patron ID too long."""
    fee_dict = calculate_late_fee_for_book("1234567", 1)
    
    assert fee_dict["fee_amount"] == -1
    assert fee_dict["days_overdue"] == -1
    assert fee_dict["status"] == "Unknown"


def test_calculate_late_fee_invalid_patron_not_number():
    """Test calculating late fee with patron ID being a non-number."""
    fee_dict = calculate_late_fee_for_book("123abc", 1)
    
    assert fee_dict["fee_amount"] == -1
    assert fee_dict["days_overdue"] == -1
    assert fee_dict["status"] == "Unknown"


def test_calculate_late_fee_invalid_book_not_found():
    """Test calculating late fee with book not existing."""
    fee_dict = calculate_late_fee_for_book("123456", 100000)
    
    assert fee_dict["fee_amount"] == -1
    assert fee_dict["days_overdue"] == -1
    assert fee_dict["status"] == "Unknown"


def test_return_book_invalid_book_not_borrowed():
    """Test returning a book with book not currently borrowed."""
    fee_dict = calculate_late_fee_for_book("123456", 2)
    
    assert fee_dict["fee_amount"] == -1
    assert fee_dict["days_overdue"] == -1
    assert fee_dict["status"] == "Unknown"
