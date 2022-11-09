# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

from petstore_api import schemas, exceptions
from petstore_api.model.object_model_with_arg_and_args_properties import ObjectModelWithArgAndArgsProperties


class TestObjectModelWithArgAndArgsProperties(unittest.TestCase):
    """ObjectModelWithArgAndArgsProperties unit test stubs"""

    def test_ObjectModelWithArgAndArgsProperties(self):
        """Test ObjectModelWithArgAndArgsProperties"""
        model = ObjectModelWithArgAndArgsProperties(arg='a', args='as')
        self.assertTrue(
            isinstance(
                model["arg"],
                ObjectModelWithArgAndArgsProperties.MetaOapg.properties.arg
            )
        )
        self.assertTrue(
            isinstance(
                model["args"],
                ObjectModelWithArgAndArgsProperties.MetaOapg.properties.args
            )
        )
        self.assertTrue(isinstance(model["arg"], schemas.StrSchema))
        self.assertTrue(isinstance(model["args"], schemas.StrSchema))


if __name__ == '__main__':
    unittest.main()