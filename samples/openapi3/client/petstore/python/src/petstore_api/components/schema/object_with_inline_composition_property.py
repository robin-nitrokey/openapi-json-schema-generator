# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class _0(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        min_length: int = 1
AllOf = typing.Tuple[
    typing.Type[_0[schemas.U]],
]
DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class SomeProp(
    schemas.AnyTypeSchema[schemas.T],
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        all_of: AllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf)) # type: ignore


    def __new__(
        cls,
        arg: typing.Union[
            DictInput,
            schemas.INPUT_TYPES_ALL_INCL_SCHEMA
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> SomeProp[
        typing.Union[
            frozendict.frozendict,
            str,
            decimal.Decimal,
            schemas.BoolClass,
            schemas.NoneClass,
            tuple,
            bytes,
            schemas.FileIO
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration=configuration,
        )
        inst = typing.cast(
            SomeProp[
                typing.Union[
                    frozendict.frozendict,
                    str,
                    decimal.Decimal,
                    schemas.BoolClass,
                    schemas.NoneClass,
                    tuple,
                    bytes,
                    schemas.FileIO
                ]
            ],
            inst
        )
        return inst

Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "someProp": typing.Type[SomeProp],
    }
)
DictInput2 = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            SomeProp[
                schemas.INPUT_BASE_TYPES
            ],
            dict,
            frozendict.frozendict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ],
        schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ]
]


class ObjectWithInlineCompositionProperty(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someProp"]) -> SomeProp[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["someProp"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg: typing.Union[
            DictInput2,
            ObjectWithInlineCompositionProperty[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ObjectWithInlineCompositionProperty[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg,
            configuration=configuration,
        )
        inst = typing.cast(
            ObjectWithInlineCompositionProperty[frozendict.frozendict],
            inst
        )
        return inst

