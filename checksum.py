# Defining constants
CHECKSUM_NUM = [14, 2, 12, 2, 11, 1]
CHECKSUM_KEY = ["A", "Y", "U", "S", "P", "L", "J", "G", "D", "B", "Z", "X", "T", "R", "M", "K", "H", "E", "C"]



# Converting string into list of integers with A = 1, B = 2...
def alpha_conversion(alpha_list: list[str] ) -> list[int]:
    converted_list: list[int] = []
    for i in alpha_list:
            converted_list.append(ord(i) - 64)
    return converted_list



def plate_check(vehicle_plate: str) -> str:

    # Convert vehicle plate to uppercase
    valid_plate = False
    vehicle_plate: str = vehicle_plate.upper()

    # Check length of input (Vehicle plate length can only be between 4 and 8 characters)
    if len(vehicle_plate) > 8 or len(vehicle_plate) < 4:
        return "Invalid vehicle plate!\n(Vehicle plate length can only be between 4 and 8 characters)", valid_plate

    # Check if vehicle plate is alphanumeric (Vehicle plate can only contain alphabets or numbers)
    if vehicle_plate.isalnum() == False:
        return "Invalid vehicle plate!\n(Vehicle plate can only contain alphabets or numbers)", valid_plate

    # Check if first character is alphabet (Vehicle plate has to start with alphabet)
    if vehicle_plate[0].isalpha() == False:
        return "Invalid vehicle plate!\n(Vehicle plate has to start with alphabet)", valid_plate

    # Seperating prefix and numeral from vehicle plate
    prefix_done: bool = False
    numeral_done: bool = False
    vehicle_plate_prefix: list[str] = []
    vehicle_plate_numeral: str = ""
    vehicle_plate_checksum: str = ""

    for i in vehicle_plate:
        if prefix_done == False:
            if i.isalpha():
                vehicle_plate_prefix.append(i)
            else:
                vehicle_plate_numeral += i
                prefix_done = True
        elif numeral_done == False:
            if i.isdigit():
                vehicle_plate_numeral += i
            else:
                vehicle_plate_checksum = i
                numeral_done = True
        else:
            if i.isnumeric():
                return "Invalid vehicle plate!\n(Vehicle plate cannot have numbers after checksum)", valid_plate

    # Check numeral length
    if len(vehicle_plate_numeral) < 1 or len(vehicle_plate_numeral) > 4:
        return "Invalid vehicle plate!\n(Vehicle plate has to have a numeral value of length between 1 and 4)", valid_plate

    # Prefix logic by length
    if len(vehicle_plate_prefix) > 3:
        return "Invalid vehicle plate!\n(Vehicle plate prefix cannot be more than 3 characters)", valid_plate
    
    elif len(vehicle_plate_prefix) == 3:
        prefix = [vehicle_plate_prefix[1], vehicle_plate_prefix[2]]

    elif len(vehicle_plate_prefix) == 2:
        prefix = [vehicle_plate_prefix[0], vehicle_plate_prefix[1]]

    elif len(vehicle_plate_prefix) == 1:
        prefix = ["@", vehicle_plate_prefix[0]]

    # Converting string into list of integers with A = 1, B = 2...
    prefix_converted: list[int] = alpha_conversion(prefix)

    # Right adjust and convert numeric into integer list
    r_numeric: str = vehicle_plate_numeral.rjust(4, "0")
    vehicle_plate_numeral: list[str] = list(r_numeric)
    numeral_converted: list[int] = [int(i) for i in vehicle_plate_numeral]

    # Joining back converted prefix, numeral, and checksum
    vehicle_plate_converted: list[int] = []
    vehicle_plate_converted.extend(prefix_converted)
    vehicle_plate_converted.extend(numeral_converted)

    # Checksum calculation
    checksum_sum: int = 0
    for i in range(6):
        checksum_sum += (CHECKSUM_NUM[i] * vehicle_plate_converted[i])

    checksum_int: int = checksum_sum % 19
    checksum_alpha: str = CHECKSUM_KEY[checksum_int]

    # Check calculated checksum against given checksum value
    if checksum_alpha != vehicle_plate_checksum:
        e_msg = f"Invalid checksum value! Checksum value should be '{checksum_alpha}'!"
        return e_msg, valid_plate
    else:
        valid_plate = True
        return "Valid vehicle plate!", valid_plate



if __name__ == "__main__":
    vehicle_plate: str = input("Enter plate: ")
    print(plate_check(vehicle_plate))
