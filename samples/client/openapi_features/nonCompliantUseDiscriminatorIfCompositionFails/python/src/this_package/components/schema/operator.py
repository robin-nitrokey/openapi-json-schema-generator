# coding: utf-8

"""
    discriminator-test
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from this_package.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



@dataclasses.dataclass(frozen=True)
class Operator(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    discriminator: typing.Mapping[str, typing.Mapping[str, typing.Type[schemas.Schema]]] = dataclasses.field(
        default_factory=lambda: {
            'operator_id': {
                'ADD': addition_operator.AdditionOperator,
                'AdditionOperator': addition_operator.AdditionOperator,
                'SUB': subtraction_operator.SubtractionOperator,
                'SubtractionOperator': subtraction_operator.SubtractionOperator,
            }
        }
    )
    one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore


from this_package.components.schema import addition_operator
from this_package.components.schema import subtraction_operator
OneOf = typing.Tuple[
    typing.Type[addition_operator.AdditionOperator],
    typing.Type[subtraction_operator.SubtractionOperator],
]
