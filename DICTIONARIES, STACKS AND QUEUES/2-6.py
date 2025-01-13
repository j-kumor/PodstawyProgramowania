required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# Sprawdzamy, czy użytkownik ma wszystkie wymagane uprawnienia
has_permissions = required_permissions <= user_permissions  # Używamy operatora <=, aby sprawdzić, czy brakuje uprawnień

print(has_permissions) # Will return False because "execute" is missing.
