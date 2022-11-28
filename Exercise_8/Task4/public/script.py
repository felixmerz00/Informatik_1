#!/usr/bin/env python3

class MagicDrawingBoard:

    def __init__(self, x, y):
        self.__size = [x, y]
        self.reset()

        try: 
            if x < 1 or y < 1:
                raise Warning("Invalid size of drawing board: Too small.")
        except:
            raise Warning("This is a Warning.")

    def pixel(self, coordinates):
        try: 
            if coordinates[0] < 0 or coordinates[1] < 0: 
                raise Warning("Pixel out of bounds.")
            self.__board[coordinates[1]][coordinates[0]] = "1"
        except: 
            raise Warning("Pixel out of bounds.")

    def rect(self, coordinate_top_left, coordinate_bottom_right):
        try:
            # Add minus 1 because the end coordinates should be "exclusive".
            width = coordinate_bottom_right[0] - coordinate_top_left[0] - 1
            height = coordinate_bottom_right[1] - coordinate_top_left[1] - 1
        except:
            raise Warning("Invalid Coordinates.")

        # Check if the rectangle is positive.
        if width < 0 or height < 0 or coordinate_top_left[0] < 0 or coordinate_top_left[1] < 0 or coordinate_bottom_right[0] < 0 or coordinate_bottom_right[1] < 0: 
            raise Warning("This is a Warning.")

        try:
            for y in range(height+1):
                for x in range(width+1):
                    self.__board[coordinate_top_left[1] + y][coordinate_top_left[0] + x] = "1"
        except: 
            # Raise warning if the rectangle is too large.
            raise Warning("The recatangle is too large.")

    def reset(self):
        self.__board = []
        row = []
        for i in range(self.__size[0]): # Create one row of desired length
            row.append("0")
        for i in range(self.__size[1]): # Add desired number of rows to the board
            self.__board.append(row.copy())
    
    def img(self):
        out = ""
        for row in self.__board:
            out += "".join(row) + "\n"
        return out[:-1]

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6,4) # instantiation of a specific size
    db.pixel((2,1)) # draw at one coordinate
    db.rect((2,2), (5,4)) # draw a rectangle
    img = db.img() # return the drawn image
    print(img)
    db.reset() # reset the field again
