import pytest
from services.library_service import (
    refund_late_fee_payment
)
from services.payment_service import PaymentGateway


def test_successful_refund(mocker):
    """Test a successful refund."""
    mock_gateway = mocker.Mock(spec=PaymentGateway)
    mock_gateway.refund_payment.return_value = (True, "Refund of $1.00 processed successfully. Refund ID: txn_123")

    success, message = refund_late_fee_payment("txn_123", 1.0, mock_gateway)

    assert success == True
    assert "processed successfully" in message
    mock_gateway.refund_payment.assert_called_once_with(
        "txn_123", 1.0
    )


def test_refund_invalid_id(mocker):
    """Test an invalid transaction ID."""
    mock_gateway = mocker.Mock(spec=PaymentGateway)
    mock_gateway.refund_payment.return_value = (False, "Invalid transaction ID")

    success, message = refund_late_fee_payment("txn_1234", 1.0, mock_gateway)

    assert success == False
    assert "Refund failed: Invalid transaction ID" in message
    mock_gateway.refund_payment.assert_called_once_with(
        "txn_1234", 1.0
    )


def test_refund_amount_negative(mocker):
    """Test a negative refund amount."""
    mock_gateway = mocker.Mock(spec=PaymentGateway)
    
    success, message = refund_late_fee_payment("txn_123", -1.0, mock_gateway)

    assert success == False
    assert "Refund amount must be greater" in message
    mock_gateway.refund_payment.assert_not_called()


def test_refund_amount_zero(mocker):
    """Test a refund amount of 0."""
    mock_gateway = mocker.Mock(spec=PaymentGateway)
    
    success, message = refund_late_fee_payment("txn_123", 0.0, mock_gateway)

    assert success == False
    assert "Refund amount must be greater" in message
    mock_gateway.refund_payment.assert_not_called()


def test_refund_amount_exceeds_15(mocker):
    """Test a refund amount over 15."""
    mock_gateway = mocker.Mock(spec=PaymentGateway)
    
    success, message = refund_late_fee_payment("txn_123", 16.0, mock_gateway)

    assert success == False
    assert "Refund amount exceeds" in message
    mock_gateway.refund_payment.assert_not_called()