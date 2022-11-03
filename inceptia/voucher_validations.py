_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code:str) -> bool:
    """
        True: 
            ->Voucher Accepted\n
        False:\n 
            ->Voucher Rejected\n
    """
    differences = []
    list_input_discount = []
    list_available_discount_codes = []
    
    for codes in _AVAILABLE_DISCOUNT_CODES:
        if discount_code.lower() in codes.lower():
            for i in discount_code: list_input_discount.append(i)
            for i in codes: list_available_discount_codes.append(i)
            for i in range(len(discount_code)):
                if list_input_discount[i] != list_available_discount_codes[i]: 
                    differences.append(discount_code[i])
            
            quantity_differences = len(differences) * 2
            if quantity_differences >= 3: return False
            elif quantity_differences < 3: return True

if __name__ == '__main__':
    voucher_accepted = validate_discount_code("Primavera2021")
    print(voucher_accepted)