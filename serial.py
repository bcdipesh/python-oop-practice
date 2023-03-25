"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize the start number and setup a sequence number for the generator"""
        self.start = start
        self.next_number = self.start - 1

    def generate(self):
        """Generate a number based on the current sequence number"""
        self.next_number += 1
        return self.next_number

    def reset(self):
        """Reset the current sequence number to original start number"""
        self.next_number = self.start - 1
