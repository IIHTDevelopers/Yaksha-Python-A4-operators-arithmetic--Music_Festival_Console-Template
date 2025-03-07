import pytest
from test.TestUtils import TestUtils
import re
import inspect
from music_festival_console import *

test_obj = TestUtils()

def test_required_variables():
    """Test if all required variables are defined with exact naming"""
    try:
        with open('music_festival_console.py', 'r') as file:
            content = file.read()
        
        required_vars = {
            'zone_a_revenue': r'zone_a_revenue\s*=',
            'zone_b_revenue': r'zone_b_revenue\s*=',
            'zone_c_revenue': r'zone_c_revenue\s*=',
            'total_revenue': r'total_revenue\s*=',
            'zone_a_left': r'zone_a_left\s*=',
            'zone_b_left': r'zone_b_left\s*=',
            'zone_c_left': r'zone_c_left\s*=',
            'complete_rows': r'complete_rows\s*=',
            'remaining_seats': r'remaining_seats\s*='
        }
        
        all_vars_found = True
        for var_name, pattern in required_vars.items():
            if not re.search(pattern, content):
                all_vars_found = False
                break
        
        test_obj.yakshaAssert("TestRequiredVariables", all_vars_found, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestRequiredVariables", False, "functional")

def test_calculation_operators():
    """Test if correct operators are used in calculations"""
    try:
        # Revenue calculation should use * and +
        revenue_code = inspect.getsource(calculate_ticket_revenue)
        has_revenue_operators = "*" in revenue_code and "+" in revenue_code
        
        # Seats remaining should use -
        seats_code = inspect.getsource(calculate_seats_remaining)
        has_seats_operators = "-" in seats_code
        
        # Occupancy should use * and /
        occupancy_code = inspect.getsource(calculate_zone_occupancy)
        has_occupancy_operators = "*" in occupancy_code and "/" in occupancy_code
        
        # Seats per row should use // and %
        rows_code = inspect.getsource(calculate_seats_per_row)
        has_rows_operators = "//" in rows_code and "%" in rows_code
        
        all_operators_used = has_revenue_operators and has_seats_operators and has_occupancy_operators and has_rows_operators
        test_obj.yakshaAssert("TestCalculationOperators", all_operators_used, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestCalculationOperators", False, "functional")

def test_calculation_logic():
    """Test if calculation functions produce correct results"""
    try:
        # Test revenue calculation
        revenue_result = calculate_ticket_revenue(10, 15, 20) == (10*5000 + 15*3000 + 20*1500)
        
        # Test seats remaining
        seats_result = calculate_seats_remaining(50, 100, 200) == (150, 200, 300)
        
        # Test occupancy
        occupancy_result = calculate_zone_occupancy(75, 200) == 37.5
        
        # Test seats per row
        rows_result = calculate_seats_per_row(45) == (2, 5)
        
        all_calculations_correct = revenue_result and seats_result and occupancy_result and rows_result
        test_obj.yakshaAssert("TestCalculationLogic", all_calculations_correct, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestCalculationLogic", False, "functional")