# coding: utf-8

"""
    Example
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import json_schema_api
from json_schema_api.components.schema.any_type_unevaluated_properties_true import AnyTypeUnevaluatedPropertiesTrue


class TestAnyTypeUnevaluatedPropertiesTrue(unittest.TestCase):
    """AnyTypeUnevaluatedPropertiesTrue unit test stubs"""

    def test_succeeds_with_no_unevaluated_properties(self):
        inst = AnyTypeUnevaluatedPropertiesTrue.validate({})
        assert inst == {}

    def test_succeeds_with_unevaluated_property(self):
        inst = AnyTypeUnevaluatedPropertiesTrue.validate({'foo': True})
        assert inst == {'foo': True}


if __name__ == '__main__':
    unittest.main()
