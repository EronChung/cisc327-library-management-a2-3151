import pytest
from services.library_service import (
    pay_late_fees
)
from services.payment_service import PaymentGateway


def test_successful_payment(mocker):
    """Test a successful payment."""
    mocker.patch("services.library_service.calculate_late_fee_for_book",
                 return_value={
                    "fee_amount"    : 0.5,
                    "days_overdue"  : 1,
                    "status"        : "Late"
                 })

    mock_gateway = mocker.Mock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = (True, "txn_123", "Success")

    success, message, transaction_id = pay_late_fees("123456", 1, mock_gateway)

    assert success == True
    assert "Payment successful" in message
    assert transaction_id == "txn_123"


def test_payment_declined_by_gateway_limit_exceeded(mocker):
    """Test getting declined by payment service (limit exceeded)."""
    mocker.patch("services.library_service.calculate_late_fee_for_book",
                 return_value={
                    "fee_amount"    : 1001,
                    "days_overdue"  : 1,
                    "status"        : "Late"
                 })

    mock_gateway = mocker.Mock(spec=PaymentGateway)
    mock_gateway.process_payment.return_value = (False, "", "Payment declined: amount exceeds limit")

    success, message, transaction_id = pay_late_fees("123456", 1, mock_gateway)

    assert success == False
    assert "Payment failed: Payment declined" in message
    assert transaction_id == None


def test_payment_invalid_patron(mocker):
    """Test invalid patron ID."""
    mocker.patch("services.library_service.calculate_late_fee_for_book",
                 return_value={
                    "fee_amount"    : 0.5,
                    "days_overdue"  : 1,
                    "status"        : "Late"
                 })

    mock_gateway = mocker.Mock(spec=PaymentGateway)

    success, message, transaction_id = pay_late_fees("12345", 1, mock_gateway)

    assert success == False
    assert "Invalid patron ID" in message
    assert transaction_id == None
    mock_gateway.assert_not_called()


def test_payment_zero_late_fees(mocker):
    """Test with no late fees."""
    mocker.patch("services.library_service.calculate_late_fee_for_book",
                 return_value={
                    "fee_amount"    : 0,
                    "days_overdue"  : 0,
                    "status"        : "Not late"
                 })

    mock_gateway = mocker.Mock(spec=PaymentGateway)

    success, message, transaction_id = pay_late_fees("123456", 1, mock_gateway)

    assert success == False
    assert "No late fees" in message
    assert transaction_id == None
    mock_gateway.assert_not_called()


def test_payment_network_error(mocker):
    """Test gateway network error exception."""
    mocker.patch("services.library_service.calculate_late_fee_for_book",
                 return_value={
                    "fee_amount"    : 0.5,
                    "days_overdue"  : 1,
                    "status"        : "Late"
                 })

    mock_gateway = mocker.Mock(side_effect=KeyError())

    success, message, transaction_id = pay_late_fees("123456", 1, mock_gateway)

    assert success == False
    assert "Payment processing error" in message
    assert transaction_id == None