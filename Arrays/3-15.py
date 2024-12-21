original_tuple = (10, 20, 30, 40, 50)

print("Tuple:", ','.join(map(str, original_tuple)))

reversed_tuple = original_tuple[::-1]
print("Reverse order:", ','.join(map(str, reversed_tuple)))
