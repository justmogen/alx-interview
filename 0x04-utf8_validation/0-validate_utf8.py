# /usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    num_bytes_to_follow = 0

    for num in data:
        # Check if it's a continuation byte
        if num_bytes_to_follow > 0:
            if (num >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1
        else:
            # Determine the number of bytes for the current character
            if (num >> 7) == 0b0:
                num_bytes_to_follow = 0
            elif (num >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (num >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (num >> 3) == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False

    # All characters have correct continuation bytes
    return num_bytes_to_follow == 0
