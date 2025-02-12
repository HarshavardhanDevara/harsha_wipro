def extract_page_number_and_offset(address: int, page_size: int = 4096):
    # Number of bits for the offset
    offset_bits = int(math.log2(page_size))
    
    # Mask for extracting the offset
    offset_mask = (1 << offset_bits) - 1
    
    # Extract the offset
    offset = address & offset_mask
    
    # Extract the page number
    page_number = address >> offset_bits
    
    return page_number, offset

import math

# Example address (32-bit)
address = 0xABCDEF12  # You can change this to any 32-bit address

page_number, offset = extract_page_number_and_offset(address)

print(f"Address: {hex(address)}")
print(f"Page Number: {page_number} (in decimal)")
print(f"Offset: {offset} (in decimal)")
