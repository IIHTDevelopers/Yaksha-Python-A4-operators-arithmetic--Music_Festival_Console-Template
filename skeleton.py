def calculate_ticket_revenue(zone_a_sold, zone_b_sold, zone_c_sold):
    """Calculate total revenue from ticket sales across all zones
    Uses multiplication (*) for zone revenue and addition (+) for total"""
    # TODO: Define constants for zone prices
    # ZONE_A_PRICE = ?
    # ZONE_B_PRICE = ?
    # ZONE_C_PRICE = ?
    
    if not all(isinstance(x, int) for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets must be whole numbers")
    if any(x < 0 for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets cannot be negative")
    
    # TODO: Calculate revenue for each zone using multiplication (*)
    # zone_a_revenue = ?
    # zone_b_revenue = ?
    # zone_c_revenue = ?
    
    # TODO: Calculate and return total revenue using addition (+)
    # total_revenue = ?
    pass

def calculate_seats_remaining(zone_a_sold, zone_b_sold, zone_c_sold):
    """Calculate remaining seats in each zone
    Uses subtraction (-)"""
    # TODO: Define constants for zone capacities
    # ZONE_A_CAPACITY = ?
    # ZONE_B_CAPACITY = ?
    # ZONE_C_CAPACITY = ?
    
    if not all(isinstance(x, int) for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets must be whole numbers")
    if any(x < 0 for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets cannot be negative")
    if zone_a_sold > ZONE_A_CAPACITY or zone_b_sold > ZONE_B_CAPACITY or zone_c_sold > ZONE_C_CAPACITY:
        raise ValueError("Tickets sold cannot exceed zone capacity")
    
    # TODO: Calculate remaining seats using subtraction (-)
    # zone_a_left = ?
    # zone_b_left = ?
    # zone_c_left = ?
    
    # TODO: Return the remaining seats for all zones
    pass

def calculate_zone_occupancy(zone_sold, zone_capacity):
    """Calculate occupancy percentage for a zone
    Uses multiplication (*) and division (/)"""
    if not isinstance(zone_sold, int) or not isinstance(zone_capacity, int):
        raise ValueError("Values must be whole numbers")
    if zone_sold < 0:
        raise ValueError("Tickets sold cannot be negative")
    if zone_capacity <= 0:
        raise ValueError("Capacity must be positive")
    if zone_sold > zone_capacity:
        raise ValueError("Sold tickets cannot exceed capacity")
    
    # TODO: Calculate and return occupancy percentage using multiplication (*) and division (/)
    # return ?
    pass

def calculate_seats_per_row(total_seats):
    """Calculate complete rows and remaining seats
    Uses floor division (//) and modulus (%)"""
    # TODO: Define constant for seats per row
    # SEATS_PER_ROW = 20
    
    if not isinstance(total_seats, int):
        raise ValueError("Seats must be a whole number")
    if total_seats < 0:
        raise ValueError("Seats cannot be negative")
    
    # TODO: Calculate complete rows using floor division (//)
    # complete_rows = ?
    
    # TODO: Calculate remaining seats using modulus (%)
    # remaining_seats = ?
    
    # TODO: Return both values
    pass

if __name__ == "__main__":
    # Display header
    print("Concert Management System")

    # Get input for tickets sold in each zone
    # TODO: Get zone_a_sold using input()
    # TODO: Get zone_b_sold using input()
    # TODO: Get zone_c_sold using input()

    # TODO: Calculate total revenue using calculate_ticket_revenue()
    # TODO: Calculate remaining seats using calculate_seats_remaining()
    # TODO: Calculate occupancy for each zone using calculate_zone_occupancy()
    # TODO: Calculate row distribution for each zone using calculate_seats_per_row()

    # TODO: Display results according to the specified format:
    # Show "Sales Summary"
    # Show "Total Revenue: ₹{value}"
    # Show "Seating Status"
    # For each zone (A, B, C):
    #   Show "Zone [X]:"
    #   Show "Remaining Seats: {value}"
    #   Show "Occupancy: {value}%"
    #   Show "Complete Rows: {value}"
    #   Show "Extra Seats: {value}"