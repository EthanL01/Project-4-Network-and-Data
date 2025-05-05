def decrypt_rail_fence(cipher, key):
    n = len(cipher)
    pattern = [['' for _ in range(n)] for _ in range(key)]
    
    # Create zigzag path
    idx = 0
    direction = 1
    for col in range(n):
        pattern[idx][col] = '*'
        idx += direction
        if idx == 0 or idx == key - 1:
            direction *= -1

    # Fill in the cipher text row-by-row
    idx = 0
    for i in range(key):
        for j in range(n):
            if pattern[i][j] == '*' and idx < len(cipher):
                pattern[i][j] = cipher[idx]
                idx += 1

    # Read it diagonally
    result = ''
    row = 0
    direction = 1
    for col in range(n):
        result += pattern[row][col]
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1

    return result
