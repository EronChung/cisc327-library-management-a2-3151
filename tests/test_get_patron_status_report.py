import pytest
from library_service import (
    get_patron_status_report
)


def test_patron_status_valid_input():
    """Test getting status report for a patron with valid input."""
    success, message = get_patron_status_report("123456")
    
    assert success == True
    # No return message yet to assert on


def test_patron_status_invalid_no_patron():
    """Test getting status report for a patron with no ID."""
    success, message = get_patron_status_report("")
    
    assert success == False
    # No return message yet to assert on


def test_patron_status_invalid_patron_too_short():
    """Test getting status report for a patron with ID being too short."""
    success, message = get_patron_status_report("12345")
    
    assert success == False
    # No return message yet to assert on


def test_patron_status_invalid_patron_too_long():
    """Test getting status report for a patron with ID being too long."""
    success, message = get_patron_status_report("1234567")
    
    assert success == False
    # No return message yet to assert on


def test_patron_status_invalid_patron_not_number():
    """Test getting status report for a patron with ID not being a number."""
    success, message = get_patron_status_report("1a2b3c")
    
    assert success == False
    # No return message yet to assert on