def f(dice):
    if not dice:  # Return None if input is empty
        return None

    max_count = 1  # Maximum streak count
    max_number = dice[0]  # Number corresponding to the maximum streak
    current_count = 1  # Current streak count

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:  # Check if the current number matches the previous one
            current_count += 1  # Increase the streak
        else:
            if current_count > max_count:  # Update max streak and corresponding number
                max_count = current_count
                max_number = dice[i - 1]
            current_count = 1  # Reset streak

    # Final check at the end of the string
    if current_count > max_count:
        max_count = current_count
        max_number = dice[-1]

    return max_number



print(f("5233165554211"))  
print(f("2133"))           
