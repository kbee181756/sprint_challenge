import random 
from random import uniform
from acme import Product

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_products(n_products=30):
    products = []
    for ii in range(n_products):
        name = adj[random.randint(0, len(adj)-1)] + ' ' + nouns[random.randint(0, len(nouns)-1)]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price, weight=weight,
                                flammability=flammability))
    return products

def inventory_report(products):
    p_names = []
    p_prices = []
    p_weights = []
    p_flamm = []
    for product in products:
        p_names.append(product.name)
        p_prices.append(product.price)
        p_weights.append(product.weight)
        p_flamm.append(product.flammability)
    print('Acme, Inc. Inventory Report')
    print(f'Unique Product Names: {len(set(p_names))}')
    print(f'Average Price: {sum(p_prices)/len(p_prices)}')
    print(f'Average Weight: {sum(p_weights)/len(p_weights)}') 
    print(f'Average Flammabilitiy: {sum(p_flamm)/len(p_flamm)}')


if __name__ == "__main__":
    inventory_report(generate_products())
