import unittest
from acme import Product
from acme_report import generate_products, adj, nouns

class AcmeProdcutsTests(unittest.TestCase):
    def test_default_product_prices(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    
    def test_default_product_flam(self):
        prod = Product('')
        self.assertEqual(prod.flammability, 0.5)

    
    def test_exploders_stealers(self):
        prod_test = Product('Faking Fakers Faking ', price=35, weight=32, flammability=35)
        self.assertListEqual(prod_test.explode, '...BABOOM!')
        self.assertEquals(prod_test.punch(),'Hey that hurt')
        self.assertEquals(prod_test.stealability(), 'Very stealable')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        items = generate_products()
        for item in items:
            all_adj, all_nouns = item.name.split(' ')
            self.assertIn(all_adj, adj) 
            self.assertIn(all_nouns, nouns)


if __name__ == '__main__':
    unittest.main()           