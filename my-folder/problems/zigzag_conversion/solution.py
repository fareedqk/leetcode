class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Initialize a list to hold the rows
        rows = [""] * numRows

        # Variables to track the current row and the direction of movement
        current_row = 0
        direction = 1  # 1 means moving down, -1 means moving up

        # Iterate over each character in the string
        for char in s:
            # Add the character to the current row
            rows[current_row] += char

            # If we are at the top or bottom row, reverse the direction
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            # Move to the next row
            current_row += direction

        # Join all the rows to form the final string
        return "".join(rows)
