# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class QuadrilateralType(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "SimpleQuadrilateral": "SIMPLE_QUADRILATERAL",
            }
        )
    
    @schemas.classproperty
    def SIMPLE_QUADRILATERAL(cls) -> QuadrilateralType[str]:
        return cls("SimpleQuadrilateral") # type: ignore
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "quadrilateralType": typing.Type[QuadrilateralType],
    }
)
DictInput = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            QuadrilateralType[str],
            str
        ],
        schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ]
]


class _1(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quadrilateralType"]) -> QuadrilateralType[str]: ...
    
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
            typing_extensions.Literal["quadrilateralType"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg: typing.Union[
            DictInput,
            _1[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> _1[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg,
            configuration=configuration,
        )
        inst = typing.cast(
            _1[frozendict.frozendict],
            inst
        )
        return inst

DictInput2 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class SimpleQuadrilateral(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        all_of: AllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf)) # type: ignore


    def __new__(
        cls,
        arg: typing.Union[
            DictInput2,
            schemas.INPUT_TYPES_ALL_INCL_SCHEMA
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> SimpleQuadrilateral[
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
            SimpleQuadrilateral[
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


from petstore_api.components.schema import quadrilateral_interface
AllOf = typing.Tuple[
    typing.Type[quadrilateral_interface.QuadrilateralInterface],
    typing.Type[_1[schemas.U]],
]
