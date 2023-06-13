# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class EnumString(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "UPPER": "UPPER",
                "lower": "LOWER",
                "": "EMPTY",
            }
        )
    
    @schemas.classproperty
    def UPPER(cls) -> EnumString[str]:
        return cls("UPPER") # type: ignore
    
    @schemas.classproperty
    def LOWER(cls) -> EnumString[str]:
        return cls("lower") # type: ignore
    
    @schemas.classproperty
    def EMPTY(cls) -> EnumString[str]:
        return cls("") # type: ignore


class EnumStringRequired(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "UPPER": "UPPER",
                "lower": "LOWER",
                "": "EMPTY",
            }
        )
    
    @schemas.classproperty
    def UPPER(cls) -> EnumStringRequired[str]:
        return cls("UPPER") # type: ignore
    
    @schemas.classproperty
    def LOWER(cls) -> EnumStringRequired[str]:
        return cls("lower") # type: ignore
    
    @schemas.classproperty
    def EMPTY(cls) -> EnumStringRequired[str]:
        return cls("") # type: ignore


class EnumInteger(
    schemas.Int32Schema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            decimal.Decimal,
        })
        format: str = 'int32'
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                1: "POSITIVE_1",
                -1: "NEGATIVE_1",
            }
        )
    
    @schemas.classproperty
    def POSITIVE_1(cls) -> EnumInteger[decimal.Decimal]:
        return cls(1) # type: ignore
    
    @schemas.classproperty
    def NEGATIVE_1(cls) -> EnumInteger[decimal.Decimal]:
        return cls(-1) # type: ignore


class EnumNumber(
    schemas.Float64Schema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            decimal.Decimal,
        })
        format: str = 'double'
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                1.1: "POSITIVE_1_PT_1",
                -1.2: "NEGATIVE_1_PT_2",
            }
        )
    
    @schemas.classproperty
    def POSITIVE_1_PT_1(cls) -> EnumNumber[decimal.Decimal]:
        return cls(1.1) # type: ignore
    
    @schemas.classproperty
    def NEGATIVE_1_PT_2(cls) -> EnumNumber[decimal.Decimal]:
        return cls(-1.2) # type: ignore


class EnumTest(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        required: typing.FrozenSet[str] = frozenset({
            "enum_string_required",
        })
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    
    @property
    def enum_string_required(self) -> EnumStringRequired[str]:
        return self.__getitem__("enum_string_required")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_string_required"]) -> EnumStringRequired[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_string"]) -> EnumString[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_integer"]) -> EnumInteger[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_number"]) -> EnumNumber[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stringEnum"]) -> string_enum.StringEnum[typing.Union[
        schemas.NoneClass,
        str
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IntegerEnum"]) -> integer_enum.IntegerEnum[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StringEnumWithDefaultValue"]) -> string_enum_with_default_value.StringEnumWithDefaultValue[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IntegerEnumWithDefaultValue"]) -> integer_enum_with_default_value.IntegerEnumWithDefaultValue[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IntegerEnumOneValue"]) -> integer_enum_one_value.IntegerEnumOneValue[decimal.Decimal]: ...
    
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
            typing_extensions.Literal["enum_string_required"],
            typing_extensions.Literal["enum_string"],
            typing_extensions.Literal["enum_integer"],
            typing_extensions.Literal["enum_number"],
            typing_extensions.Literal["stringEnum"],
            typing_extensions.Literal["IntegerEnum"],
            typing_extensions.Literal["StringEnumWithDefaultValue"],
            typing_extensions.Literal["IntegerEnumWithDefaultValue"],
            typing_extensions.Literal["IntegerEnumOneValue"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg: typing.Union[
            DictInput,
            EnumTest[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> EnumTest[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg,
            configuration=configuration,
        )
        inst = typing.cast(
            EnumTest[frozendict.frozendict],
            inst
        )
        return inst


from petstore_api.components.schema import integer_enum
from petstore_api.components.schema import integer_enum_one_value
from petstore_api.components.schema import integer_enum_with_default_value
from petstore_api.components.schema import string_enum
from petstore_api.components.schema import string_enum_with_default_value
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "enum_string": typing.Type[EnumString],
        "enum_string_required": typing.Type[EnumStringRequired],
        "enum_integer": typing.Type[EnumInteger],
        "enum_number": typing.Type[EnumNumber],
        "stringEnum": typing.Type[string_enum.StringEnum],
        "IntegerEnum": typing.Type[integer_enum.IntegerEnum],
        "StringEnumWithDefaultValue": typing.Type[string_enum_with_default_value.StringEnumWithDefaultValue],
        "IntegerEnumWithDefaultValue": typing.Type[integer_enum_with_default_value.IntegerEnumWithDefaultValue],
        "IntegerEnumOneValue": typing.Type[integer_enum_one_value.IntegerEnumOneValue],
    }
)
DictInput = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            EnumStringRequired[str],
            str
        ],
        typing.Union[
            EnumString[str],
            str
        ],
        typing.Union[
            EnumInteger[decimal.Decimal],
            decimal.Decimal,
            int
        ],
        typing.Union[
            EnumNumber[decimal.Decimal],
            decimal.Decimal,
            int,
            float
        ],
        typing.Union[
            string_enum.StringEnum[typing.Union[
                schemas.NoneClass,
                str
            ]],
            None,
            str
        ],
        typing.Union[
            integer_enum.IntegerEnum[decimal.Decimal],
            decimal.Decimal,
            int
        ],
        typing.Union[
            string_enum_with_default_value.StringEnumWithDefaultValue[str],
            str
        ],
        typing.Union[
            integer_enum_with_default_value.IntegerEnumWithDefaultValue[decimal.Decimal],
            decimal.Decimal,
            int
        ],
        typing.Union[
            integer_enum_one_value.IntegerEnumOneValue[decimal.Decimal],
            decimal.Decimal,
            int
        ],
        schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ]
]
