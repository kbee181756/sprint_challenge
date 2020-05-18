from random import randomint, uniform
from acme import Product

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_products(products=30):
    products = []
    for x in range(products):
        name = adjectives[randomint(0, len(adjectives)] + ' ' + noun[randomint(0, len(noun)-1)]
        price = randomint(5, 100)
        weight = randomint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight,
                                flammability=flamability))
    return products


