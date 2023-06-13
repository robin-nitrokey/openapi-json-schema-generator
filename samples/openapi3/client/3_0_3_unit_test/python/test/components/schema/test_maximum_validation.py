# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.maximum_validation import MaximumValidation
from unit_test_api.configurations import schema_configuration


class TestMaximumValidation(unittest.TestCase):
    """MaximumValidation unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_below_the_maximum_is_valid_passes(self):
        # below the maximum is valid
        MaximumValidation(
            2.6,
            configuration=self.configuration
        )

    def test_boundary_point_is_valid_passes(self):
        # boundary point is valid
        MaximumValidation(
            3.0,
            configuration=self.configuration
        )

    def test_above_the_maximum_is_invalid_fails(self):
        # above the maximum is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MaximumValidation(
                3.5,
                configuration=self.configuration
            )

    def test_ignores_non_numbers_passes(self):
        # ignores non-numbers
        MaximumValidation(
            "x",
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()
