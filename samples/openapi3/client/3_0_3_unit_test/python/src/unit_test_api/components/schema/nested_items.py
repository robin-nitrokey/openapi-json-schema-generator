# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *

Items4: typing_extensions.TypeAlias = schemas.NumberSchema[U]


class Items3(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items4] = dataclasses.field(default_factory=lambda: Items4) # type: ignore

    def __new__(
        cls,
        arg: typing.Sequence[
            typing.Union[
                Items4[decimal.Decimal],
                decimal.Decimal,
                int,
                float
            ]
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items3[tuple]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )

    def __getitem__(self, name: int) -> Items4[decimal.Decimal]:
        return super().__getitem__(name)



class Items2(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items3] = dataclasses.field(default_factory=lambda: Items3) # type: ignore

    def __new__(
        cls,
        arg: typing.Sequence[
            typing.Union[
                Items3[tuple],
                list,
                tuple
            ]
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items2[tuple]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )

    def __getitem__(self, name: int) -> Items3[tuple]:
        return super().__getitem__(name)



class Items(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items2] = dataclasses.field(default_factory=lambda: Items2) # type: ignore

    def __new__(
        cls,
        arg: typing.Sequence[
            typing.Union[
                Items2[tuple],
                list,
                tuple
            ]
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items[tuple]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )

    def __getitem__(self, name: int) -> Items2[tuple]:
        return super().__getitem__(name)



class NestedItems(
    schemas.ListSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore

    def __new__(
        cls,
        arg: typing.Sequence[
            typing.Union[
                Items[tuple],
                list,
                tuple
            ]
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> NestedItems[tuple]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )

    def __getitem__(self, name: int) -> Items[tuple]:
        return super().__getitem__(name)

