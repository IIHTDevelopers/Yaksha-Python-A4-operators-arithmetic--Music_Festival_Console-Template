def calculate_ticket_revenue(zone_a_sold, zone_b_sold, zone_c_sold):
    """Calculate total revenue from ticket sales across all zones
    Uses multiplication (*) for zone revenue and addition (+) for total"""
    ZONE_A_PRICE = 5000
    ZONE_B_PRICE = 3000
    ZONE_C_PRICE = 1500
    
    if not all(isinstance(x, int) for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets must be whole numbers")
    if any(x < 0 for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets cannot be negative")
    
    zone_a_revenue = zone_a_sold * ZONE_A_PRICE
    zone_b_revenue = zone_b_sold * ZONE_B_PRICE
    zone_c_revenue = zone_c_sold * ZONE_C_PRICE
    
    total_revenue = zone_a_revenue + zone_b_revenue + zone_c_revenue
    return total_revenue

def calculate_seats_remaining(zone_a_sold, zone_b_sold, zone_c_sold):
    """Calculate remaining seats in each zone
    Uses subtraction (-)"""
    ZONE_A_CAPACITY = 200
    ZONE_B_CAPACITY = 300
    ZONE_C_CAPACITY = 500
    
    if not all(isinstance(x, int) for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets must be whole numbers")
    if any(x < 0 for x in [zone_a_sold, zone_b_sold, zone_c_sold]):
        raise ValueError("Number of tickets cannot be negative")
    if zone_a_sold > ZONE_A_CAPACITY or zone_b_sold > ZONE_B_CAPACITY or zone_c_sold > ZONE_C_CAPACITY:
        raise ValueError("Tickets sold cannot exceed zone capacity")
    
    zone_a_left = ZONE_A_CAPACITY - zone_a_sold
    zone_b_left = ZONE_B_CAPACITY - zone_b_sold
    zone_c_left = ZONE_C_CAPACITY - zone_c_sold
    
    return zone_a_left, zone_b_left, zone_c_left

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
    
    return (zone_sold * 100) / zone_capacity

    
def calculate_seats_per_row(total_seats):
    """Calculate complete rows and remaining seats
    Uses floor division (//) and modulus (%)"""
    SEATS_PER_ROW = 20
    
    if not isinstance(total_seats, int):
        raise ValueError("Seats must be a whole number")
    if total_seats < 0:
        raise ValueError("Seats cannot be negative")
    
    complete_rows = total_seats // SEATS_PER_ROW
    remaining_seats = total_seats % SEATS_PER_ROW
    
    return complete_rows, remaining_seats

if __name__ == "__main__":
    # Display header
    print("Concert Management System")

    # Get tickets sold
    zone_a_sold = int(input("Enter Zone A tickets sold: "))
    zone_b_sold = int(input("Enter Zone B tickets sold: "))
    zone_c_sold = int(input("Enter Zone C tickets sold: "))

    # Calculate results
    total_revenue = calculate_ticket_revenue(zone_a_sold, zone_b_sold, zone_c_sold)
    a_left, b_left, c_left = calculate_seats_remaining(zone_a_sold, zone_b_sold, zone_c_sold)
    a_occupancy = calculate_zone_occupancy(zone_a_sold, 200)
    b_occupancy = calculate_zone_occupancy(zone_b_sold, 300)
    c_occupancy = calculate_zone_occupancy(zone_c_sold, 500)
    a_rows, a_extra = calculate_seats_per_row(zone_a_sold)
    b_rows, b_extra = calculate_seats_per_row(zone_b_sold)
    c_rows, c_extra = calculate_seats_per_row(zone_c_sold)

    # Display results
    print("\nSales Summary")
    print(f"Total Revenue: ₹{total_revenue}")

    print("\nSeating Status")
    print("Zone A:")
    print(f"Remaining Seats: {a_left}")
    print(f"Occupancy: {a_occupancy}%")
    print(f"Complete Rows: {a_rows}")
    print(f"Extra Seats: {a_extra}")

    print("\nZone B:")
    print(f"Remaining Seats: {b_left}")
    print(f"Occupancy: {b_occupancy}%")
    print(f"Complete Rows: {b_rows}")
    print(f"Extra Seats: {b_extra}")

    print("\nZone C:")
    print(f"Remaining Seats: {c_left}")
    print(f"Occupancy: {c_occupancy}%")
    print(f"Complete Rows: {c_rows}")
    print(f"Extra Seats: {c_extra}")