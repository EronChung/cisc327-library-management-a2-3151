import pytest
from library_service import (
    calculate_late_fee_for_book
)


def test_calculate_late_fee_valid_input():
    """Test calculating late fee with valid input."""
    success, message = calculate_late_fee_for_book("123456", 1)
    
    assert success == True
    # No return message yet to assert on


def test_calculate_late_fee_invalid_no_patron():
    """Test calculating late fee with no patron."""
    success, message = calculate_late_fee_for_book("", 1)
    
    assert success == False
    # No return message yet to assert on


def test_calculate_late_fee_invalid_patron_too_short():
    """Test calculating late fee with patron ID too short."""
    success, message = calculate_late_fee_for_book("12345", 1)
    
    assert success == False
    # No return message yet to assert on


def test_calculate_late_fee_invalid_patron_too_long():
    """Test calculating late fee with patron ID too long."""
    success, message = calculate_late_fee_for_book("1234567", 1)
    
    assert success == False
    # No return message yet to assert on


def test_calculate_late_fee_invalid_patron_not_number():
    """Test calculating late fee with patron ID being a non-number."""
    success, message = calculate_late_fee_for_book("123abc", 1)
    
    assert success == False
    # No return message yet to assert on


def test_calculate_late_fee_invalid_book_not_found():
    """Test calculating late fee with book not existing."""
    success, message = calculate_late_fee_for_book("123456", 100000)
    
    assert success == False
    # No return message yet to assert on