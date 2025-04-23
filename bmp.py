"""A module for dealing with  BMP bitmap image files."""

def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.
    
    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the 
            range 0-255.

    Raises:
        OSError: If the files cannot be created or written to.
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP file header
        bmp.write(b'BM')
    
        size_bookmark = bmp.tell() # The next four bytes hold the filesize as a  
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for

        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()   # The next four bytes hold the integer offset 
        bmp.write(b'\x00\x00\x00\x00')       # pixel data. Zero placeholder for now. 

        # Image Header 
        bmp.write(b'\x28\x00\x00\x00')   # Image header size in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width)) # Image width in pixels
        bmp.write(_int32_to_bytes(height)) # Image height in pixels
        bmp.write(b'\x01\x00') # Number of image planes - 1
        bmp.write(b'\x08\x00') # Bits per pixel - 8 for grayscale
        bmp.write(b'\x00\x00\x00\x00') # Compression - 0 for none
        bmp.write(b'\x00\x00\x00\x00') # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00') # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00') # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00') # Use whole color table
        bmp.write(b'\x00\x00\x00\x00') # All colors are important
        

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c,c,c,0))) # Blue, Green, Red, Zero
        
        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels): # BMP files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in the size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in the pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

def _int32_to_bytes(i):
    "Convert an integer to bytes in little-endian format."
    return bytes((i & 0xff,
                i >> 8 & 0xff,
                i >> 16 & 0xff,
                i >> 24 & 0xff
                ))