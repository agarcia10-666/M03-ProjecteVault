def check_password(pwd):
    # 1. Validación de longitud (Mínimo 8 caracteres)
    if len(pwd) < 8:
        return False
    
    # 2. Debe contener al menos un número
    if not any(char.isdigit() for char in pwd):
        return False
    
    # 3. Debe contener al menos una letra mayúscula
    if not any(char.isupper() for char in pwd):
        return False
    
    # 4. No debe contener la palabra "admin" (insensible a mayúsculas)
    if "admin" in pwd.lower():
        return False
    
    # Si pasa todos los filtros, es segura
    return True
