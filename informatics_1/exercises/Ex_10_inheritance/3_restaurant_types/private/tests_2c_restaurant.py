#!/usr/bin/env python3

from unittest import TestCase
# catch potential exception from import
try:
    from public.restaurant import Restaurant
except Exception:
    # Just make sure that all tests are still executed to have a stable number
    # of exercise points. An appropriate warning is generated by the smoke tests.
    pass

class RestaurantTest(TestCase):

    def test01_descr_restaurant(self):
        try:
            name = "rest1"
            cuisine = "allcuisine"
            sut = Restaurant(name, cuisine)
            actual = sut.describe_restaurant()
        except:
            m = "@@Unexpected error when describing restaurant.@@"
            self.fail(m)
        m = "@@describe_restaurant() should return a string with both the name and the cuisine_type of the restaurant.@@"
        contains_name = actual.find(name)
        contains_cuisine = actual.find(cuisine)
        self.assertTrue(contains_name > -1, m)
        self.assertTrue(contains_cuisine > -1, m)

    def test02_open_restaurant(self):
        try:
            sut = Restaurant("r", "a")
            sut.open_restaurant()
        except:
            m = "@@Unexpected error when opening restaurant.@@"
            self.fail(m)
        m = "@@After opening restaurant is_open() should return True.@@"
        self.assertEqual(True, sut.is_open(), m)

    def test03_close_restaurant(self):
        try:
            sut = Restaurant("r", "a")
            sut.close_restaurant()
        except:
            m = "@@Unexpected error when closing restaurant.@@"
            self.fail(m)
        m = "@@After closing restaurant is_open() should return False.@@"
        self.assertEqual(False, sut.is_open(), m)


    def test04_add_consumption_unit(self):
        try:
            sut = Restaurant("r", "a")
            sut.add_consumption_unit("ice tea", 3)
            d = sut.get_menu()
        except:
            m = "@@Unexpected error adding a consumption unit and getting the menu.@@"
            self.fail(m)
        m = "@@adding consumption unit does not work.@@"
        self.assertTrue("ice tea" in d, m)
        self.assertEqual(3, d["ice tea"], m)

    def test05_remove_consumption_unit(self):
        try:
            sut = Restaurant("r", "a")
            sut.add_consumption_unit("ice tea", 3)
            sut.remove_consumption_unit("ice tea")
            d = sut.get_menu()
        except:
            m = "@@Unexpected error removing a consumption unit and getting the menu.@@"
            self.fail(m)
        m = "@@removing consumption unit does not work.@@"
        self.assertFalse("ice tea" in d, m)

    def test06_menu_immutability(self):
        try:
            sut = Restaurant("r", "a")
            sut.add_consumption_unit("ice tea", 3)
            d = sut.get_menu()
            d["ice tea"] = 10
        except:
            m = "@@Unexpected error adding a consumption unit and getting the menu.@@"
            self.fail(m)
        m = "@@Menu is not copied, and thus could be changed from the outside.@@"
        self.assertNotEqual(d, sut.get_menu(), m)

    def test07_sales_works(self):
        try:
            sut = Restaurant("r", "a")
            sut.open_restaurant()
            sut.add_consumption_unit("ice tea", 3)
            sut.sell_unit("ice tea")
            sut.sell_unit("ice tea")
            actual = sut.get_sales()
        except:
            m = "@@Unexpected error adding and selling a consumption unit and getting the sales.@@"
            self.fail(m)
        m = "@@selling consumption unit does not add to sales.@@"
        self.assertEqual(6, actual, m)

    def test08_sales_not_opened(self):
        try:
            sut = Restaurant("r", "a")
            sut.add_consumption_unit("ice tea", 3)
            sut.sell_unit("ice tea")
        except Exception as actual_exception:
            actual_exception_type = type(actual_exception)
            if Warning != actual_exception_type:
                m = "@@Trying to sell before opening the restaurant should trigger a Warning@@ (expected: {}, was: {})@@".format(
                    Warning.__name__, actual_exception_type.__name__)
                self.fail(m)
        else:
            m = "@@It is not possible to sell without first opening the restaurant.@@"
            self.fail(m)