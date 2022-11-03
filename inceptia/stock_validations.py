import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado",
"Limon", "Dulce de Leche"], "quantity": [3,10,0,5]})

def is_product_available(product_name:str, quantity:int) -> bool:
    """
        True: 
            ->Available Product\n
        False:\n 
            ->Product not Avilable\n
    """
    try:
        product_name = product_name.replace(product_name[0], product_name[0].upper(), 1)
        validate_product = _PRODUCT_DF.where(_PRODUCT_DF.product_name == product_name)
        df_separation = validate_product.dropna()
        quantity_validate = int(df_separation.quantity.values[0])
        product_name_validate = str(df_separation.product_name.values[0])
        for i in product_name_validate: 
            if i != product_name: product_name_validate.split(i) 
        
        if quantity_validate >= quantity: return True
        elif quantity_validate < quantity: return False
    except Exception:
        return False
    
if __name__ == '__main__':
    product_in_stock = is_product_available("Chocolate", 2)
    print(product_in_stock)