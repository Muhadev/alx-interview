#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.
    Args:
    data : List[int] - A list of integers representing bytes
    Returns:
    bool - True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for byte in data:
        # Get the binary representation of the byte
        bin_rep = format(byte, '#010b')[-8:]

        if num_bytes == 0:
            # Determine how many bytes the current UTF-8 character should have
            if bin_rep[0] == '0':
                continue
            elif bin_rep[:3] == '110':
                num_bytes = 1
            elif bin_rep[:4] == '1110':
                num_bytes = 2
            elif bin_rep[:5] == '11110':
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte is of the form '10xxxxxx'
            if bin_rep[:2] != '10':
                return False
            num_bytes -= 1

    return num_bytes == 0
