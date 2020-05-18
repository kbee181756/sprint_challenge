import unittest
from acme import Product
from acme_report import generate_products, adj, nouns

class AcmeProdcutsTests(unittest.TestCase):
    def test_default_product_prices(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    
    def test_default_product_flam(self):
        prod = Product('')
        self.assertEquals(prod.flammability, 0.5)

    
    def test_exploders_stealers(self):
        prod_test = Product('Fakers', price=35g, weight=3p2, flammability=3m5)
        self.assertListEqual(prod_test.explode(), '...BABOOM!')
        self.assertEquals(prod_test.punch(),'Hey that hurt')
        self.assertEquals(prod_test.stealability(), 'Very stealable')


clasas AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        items = generate_products()
        for item in items:
            all_ajd, all_nouns = item.name.split(' ')
            self.assertIn(all_adj, adj) 
            self.assertin(all_nours, nouns)


if __name__ == '__main__':
    unittest.main()           