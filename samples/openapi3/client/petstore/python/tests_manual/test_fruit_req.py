# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


import unittest

import petstore_api
from petstore_api.components.schema import apple_req
from petstore_api.components.schema import banana_req
from petstore_api.components.schema.fruit_req import FruitReq
from petstore_api import schemas


class TestFruitReq(unittest.TestCase):
    """FruitReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFruitReq(self):
        """Test FruitReq"""

        # make an instance of Fruit, a composed schema oneOf model
        # banana test
        length_cm = 20.3
        fruit = FruitReq({'lengthCm': length_cm})
        # check its properties
        assert isinstance(fruit, banana_req.BananaReq)
        self.assertEqual(fruit.lengthCm, length_cm)
        self.assertEqual(fruit['lengthCm'], length_cm)
        self.assertEqual(getattr(fruit, 'lengthCm'), length_cm)
        # check the dict representation
        self.assertEqual(
            fruit,
            {
                'lengthCm': length_cm,
            }
        )
        # setting values after instance creation is not allowed
        with self.assertRaises(TypeError):
            fruit['lengthCm'] = 'some value'

        # setting values after instance creation is not allowed
        with self.assertRaises(AttributeError):
            setattr(fruit, 'lengthCm', 'some value')

        # getting a value that doesn't exist raises an exception
        # with a key
        with self.assertRaises(KeyError):
            fruit['cultivar']
        with self.assertRaises(AttributeError):
            fruit.cultivar
        assert fruit.get('cultivar', schemas.unset) is schemas.unset

        # with getattr
        self.assertEqual(getattr(fruit, 'cultivar', 'some value'), 'some value')

        with self.assertRaises(AttributeError):
            getattr(fruit, 'cultivar')

        # including extra parameters raises an exception
        with self.assertRaises(petstore_api.ApiValueError):
            FruitReq({
                'length_cm': length_cm,
                'unknown_property': 'some value'
            })

        # including input parameters for two oneOf instances raise an exception
        with self.assertRaises(petstore_api.ApiValueError):
            FruitReq({
                'length_cm': length_cm,
                'cultivar': 'granny smith'
            })

        # make an instance of Fruit, a composed schema oneOf model
        # apple test
        cultivar = 'golden delicious'
        fruit = FruitReq({'cultivar': cultivar})
        # check its properties
        assert isinstance(fruit, apple_req.AppleReq)
        self.assertEqual(fruit.cultivar, cultivar)
        self.assertEqual(fruit['cultivar'], cultivar)
        self.assertEqual(getattr(fruit, 'cultivar'), cultivar)
        # check the dict representation
        self.assertEqual(
            fruit,
            {
                'cultivar': cultivar
            }
        )

        # we can pass in None
        fruit = FruitReq(None)
        assert isinstance(fruit, schemas.Singleton)
        assert isinstance(fruit, FruitReq)
        assert isinstance(fruit, schemas.NoneSchema)
        assert fruit.is_none_() is True


if __name__ == '__main__':
    unittest.main()
