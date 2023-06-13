# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


import decimal
import unittest

import petstore_api
from petstore_api.components.schema.date_with_validations import DateWithValidations
from petstore_api.components.schema.date_time_with_validations import DateTimeWithValidations
from petstore_api.components.schema.string_with_validation import StringWithValidation
from petstore_api.components.schema.integer_enum_one_value import IntegerEnumOneValue
from petstore_api.components.schema.integer_enum import IntegerEnum
from petstore_api.components.schema.integer_enum_big import IntegerEnumBig
from petstore_api.components.schema.integer_max10 import IntegerMax10
from petstore_api.components.schema.integer_min15 import IntegerMin15
from petstore_api.components.schema.nullable_string import NullableString
from petstore_api.schemas import AnyTypeSchema, Schema, NoneSchema, StrSchema, Singleton


class TestCombineNonObjectSchemas(unittest.TestCase):

    def test_valid_enum_plus_prim(self):
        class EnumPlusPrim(IntegerEnumOneValue, IntegerMax10):
            pass

        enum_value = EnumPlusPrim.POSITIVE_0
        assert isinstance(enum_value, EnumPlusPrim)
        assert isinstance(enum_value, Singleton)
        assert isinstance(enum_value, decimal.Decimal)
        # we can access this enum from our class
        assert EnumPlusPrim.POSITIVE_0 == 0

        # invalid value throws an exception
        with self.assertRaises(petstore_api.ApiValueError):
            EnumPlusPrim(9)

        # valid value succeeds
        val = EnumPlusPrim(0)
        assert val == 0
        assert isinstance(val, EnumPlusPrim)
        assert isinstance(val, Singleton)
        assert isinstance(val, decimal.Decimal)

    def test_valid_enum_plus_enum(self):
        class IntegerOneEnum(IntegerEnum, IntegerEnumOneValue):
            pass

        enum_value = IntegerOneEnum.POSITIVE_0
        assert isinstance(enum_value, IntegerOneEnum)
        assert isinstance(enum_value, Singleton)
        assert isinstance(enum_value, decimal.Decimal)
        # we can access this enum from our class
        assert IntegerOneEnum.POSITIVE_0 == 0


if __name__ == '__main__':
    unittest.main()
