def encrypt_rail_fence(text, key):
    rails = ['' for _ in range(key)]
    rail = 0
    direction = 1  # 1 for down, -1 for up

    for char in text:
        rails[rail] += char
        rail += direction

        if rail == 0 or rail == key - 1:
            direction *= -1

    return ''.join(rails)
