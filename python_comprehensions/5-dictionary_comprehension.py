# for loop - Create a new dictionary that contains integers 1-10
# and their squared values
# squared = {}
# for num in range(1, 11):
#     squared[num] = num**2

# dictionary comprehension syntax template
squared = {num: num**2 for num in range(1, 11)}

# for loop - Create a new dictionary that contains the AUD calculated
# from the USD
# products_usd = {'butter': 5.5, 'garlic': 3.5, 'parsley': 1.2}
# products_aud = {}
# usd_to_aud = 1.49
# for product, price in products_usd.items():
#     products_aud[product] = price*usd_to_aud

# dictionary comprehension syntax template
products_aud = {product: price*1.49
                for (product, price)
                in {'butter': 5.5, 'garlic': 3.5, 'parsley': 1.2}.items()
                if price*1.49 < 5}

# print statements
print(squared)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(products_aud)
# {'butter': 8.195, 'garlic': 5.215, 'parsley': 1.788}
# with the if statement:
# {'parsley': 1.788}
