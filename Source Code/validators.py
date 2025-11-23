def validate_pin(pin):
    """Checks if PIN is exactly 4 digits"""
    return len(pin) == 4 and pin.isdigit()

def validate_amount(amount):
    """Checks if amount is a positive number"""
    try:
        val = float(amount)
        return val > 0
    except ValueError:
        return False

def validate_name(name):
    """Checks if name is not empty"""
    return len(name.strip()) > 0
