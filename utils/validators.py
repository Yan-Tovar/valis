def required(value, field_name):

    if value is None:
        return f"{field_name} es obligatorio"

    if str(value).strip() == "":
        return f"{field_name} es obligatorio"

    return None



def min_length(value, size, field_name):

    if len(value) < size:
        return f"{field_name} debe tener mínimo {size} caracteres"

    return None