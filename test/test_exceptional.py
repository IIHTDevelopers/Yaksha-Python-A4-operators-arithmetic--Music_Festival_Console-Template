import pytest
from test.TestUtils import TestUtils
from music_festival_console import *

test_obj = TestUtils()

def test_invalid_input_exceptions():
    """Test invalid input handling across functions"""
    try:
        # Test invalid type handling
        with pytest.raises(ValueError):
            calculate_ticket_revenue("10", 20, 30)  # String instead of int
        with pytest.raises(ValueError):
            calculate_seats_per_row("20")  # String instead of int
            
        # Test negative values handling
        with pytest.raises(ValueError):
            calculate_ticket_revenue(-5, 10, 20)  # Negative tickets
        with pytest.raises(ValueError):
            calculate_zone_occupancy(-10, 200)  # Negative tickets
            
        test_obj.yakshaAssert("TestInvalidInputExceptions", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInvalidInputExceptions", False, "exception")

def test_capacity_exceptions():
    """Test capacity constraint handling"""
    try:
        # Test exceeding capacity
        with pytest.raises(ValueError):
            calculate_seats_remaining(300, 20, 30)  # Exceeding Zone A capacity
        with pytest.raises(ValueError):
            calculate_zone_occupancy(250, 200)  # Exceeding capacity
            
        # Test invalid capacity
        with pytest.raises(ValueError):
            calculate_zone_occupancy(100, 0)  # Zero capacity
            
        test_obj.yakshaAssert("TestCapacityExceptions", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestCapacityExceptions", False, "exception")