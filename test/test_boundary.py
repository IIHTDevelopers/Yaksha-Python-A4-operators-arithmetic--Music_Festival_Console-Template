import pytest
from test.TestUtils import TestUtils
from music_festival_console import *

test_obj = TestUtils()

def test_revenue_and_seats_boundary():
    """Test revenue and remaining seats with boundary values"""
    try:
        # Revenue tests
        revenue_empty = calculate_ticket_revenue(0, 0, 0) == 0
        revenue_full = calculate_ticket_revenue(200, 300, 500) == (200*5000 + 300*3000 + 500*1500)
        
        # Seats remaining tests
        seats_empty = calculate_seats_remaining(0, 0, 0) == (200, 300, 500)
        seats_full = calculate_seats_remaining(200, 300, 500) == (0, 0, 0)
        
        all_passed = revenue_empty and revenue_full and seats_empty and seats_full
        test_obj.yakshaAssert("TestRevenueAndSeatsBoundary", all_passed, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestRevenueAndSeatsBoundary", False, "boundary")

def test_occupancy_and_rows_boundary():
    """Test occupancy and row calculations with boundary values"""
    try:
        # Occupancy tests
        occupancy_empty = calculate_zone_occupancy(0, 200) == 0
        occupancy_full = calculate_zone_occupancy(200, 200) == 100
        
        # Rows tests
        rows_empty = calculate_seats_per_row(0) == (0, 0)
        rows_full = calculate_seats_per_row(20) == (1, 0)
        rows_partial = calculate_seats_per_row(25) == (1, 5)
        
        all_passed = occupancy_empty and occupancy_full and rows_empty and rows_full and rows_partial
        test_obj.yakshaAssert("TestOccupancyAndRowsBoundary", all_passed, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestOccupancyAndRowsBoundary", False, "boundary")