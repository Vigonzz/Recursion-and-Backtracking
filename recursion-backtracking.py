# Violet Gonzalez 

# Assignment 5

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    
    # Create to record the exact character counts from a matching window
    need = {}
    for character in s1:
        if character not in need:
            need[character] = 1
        else:
            need[character] += 1

    # Building the first window
    window = {}
    for character in s2[:len(s1)]:
        if character not in window:
            window[character] = 1
        else:
            window[character] += 1
    
    # Compare the first window
    if window == need:
        return True
    
    # Slide the window
    for i in range(len(s1), len(s2)):
        entering = s2[i]
        leaving = s2[i - len(s1)]
        if entering not in window:
            window[entering] = 1
        else:
            window[entering] += 1
        window[leaving] -= 1
        # remove empty counts
        if window[leaving] == 0:
            del window[leaving]
        if window == need:
            return True
    return False
# Task 2:
def generate_solutions():
    board = []
    solutions = []
    rows = set()
    diag1 = set()
    diag2 = set()
    
    def place_queen(col):
        """ Tries to place a queen in the given column, calls itself for the next column"""
        # base case 
        if col == 8:
            solutions.append(board[:])
            return 
    
        for row in range(1,9):
            d1 = row - col
            d2= row + col
            if row in rows or d1 in diag1 or d2 in diag2:
                continue
            board.append(row)
            # Place the queen
            rows.add(row)
            diag1.add(d1)
            diag2.add(d2)

            # Go to the next column
            place_queen(col + 1)

            # undo the placements
            board.pop()
            rows.remove(row)
            diag1.remove(d1)
            diag2.remove(d2)
    # Start at the first column
    place_queen(0)
    return solutions

# Parse the input 
def parse_input(line):
    """ takes a line of text then returns a list of ints """
    parts = line.split()
    positions = []
    # Conversion
    for part in parts:
        part = int(part)
        positions.append(part)
    # check length 
    if len(positions) != 8:
        raise ValueError("input must contain 8 integer")
    for position in positions:
        if position < 1 or position > 8:
            raise ValueError("The rows must be between 1-8")
    return positions

def min_moves(positions, solutions):
    """ Find the min moves """
    best = 8
    # loop through the solutions 
    for solution in solutions:
        moves = 0
        for col in range(8):
            if positions[col] != solution[col]:
                moves += 1
        if moves < best:
            best = moves
    return best

# Testing

# Test our check inclusion function
print("---Test Task 1---")

print("\n---Test 1---")
print(check_inclusion("ab", "eidbaooo"))

print("\n---Test 2---")
print(check_inclusion("ab", "eidboaoo"))

print("\n---Test 3---")
print(check_inclusion("abc", "ab"))

print("\n---Test 4---")
print(check_inclusion("abc", "cabxxx"))

print("\n---Test 5---")
print(check_inclusion("abc", "xxxcab"))

print("\n---Test 6---")
print(check_inclusion("aab", "abbab"))

print("\n---Test 7---")
print(check_inclusion("a", "b"))

print("\n---Test 8: Repeated Letters---")
print(check_inclusion("aab", "aaab"))

print("\n---Test Task 2---")

print("\n---Test 1: Diagonal---")
solutions = generate_solutions()
test1 = parse_input("1 2 3 4 5 6 7 8")
print(min_moves(test1, solutions))

print("\n---Test 2: All Queens, Same Row---")
solutions1 = generate_solutions()
test2 = parse_input("1 1 1 1 1 1 1 1")
print(min_moves(test2, solutions1))

print("\n---Test 3: Already Valid---")
solutions3 = generate_solutions()
test3 = parse_input("1 5 8 6 3 7 2 4")
print(min_moves(test3, solutions3))

print("\n---Test 4: One Move form Valid---")
solutions4 = generate_solutions()
test4 = parse_input("1 5 8 6 3 7 2 1")
print(min_moves(test4, solutions4))

print("\n---Test 5: Reverse Diagonal---")
solutions5 = generate_solutions()
test5 = parse_input("8 7 6 5 4 3 2 1")
print(min_moves(test5, solutions5))

print("\n---Test generat sol---")
print(len(generate_solutions()))

print("\n---Test parse input---")
print(generate_solutions()[0])