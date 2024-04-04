import json

from betterproto.lib.google.protobuf import Struct, NullValue, Value, ListValue


def test_struct_roundtrip():
    data2 = {
        "foo": Value(string_value="bar"),
        "baz": Value(),
        "quux": Value(number_value=123.0),
        "zap": Value(list_value=ListValue(values=[
            Value(number_value=1),
            Value(struct_value=Struct(fields={
                "two": Value(number_value=3),
            })),
            Value(string_value="four"),
        ])),
    }
    # data = {
    #     "foo": "bar",
    #     "baz": None,
    #     "quux": 123,
    #     "zap": [1, {"two": 3}, "four"],
    # }

    data = {
        "fields": {
            "foo": { "stringValue": "bar" },
            "baz": {},
            "quux": { "numberValue": 123.0 },
            "zap": {
                "listValue": {
                    "values": [
                        { "numberValue": 1.0 },
                        { "structValue": { "fields": {
                            "two": { "numberValue": 3.0 },
                        } } },
                        { "stringValue": "four" },
                    ],
                },
            },
        },
    }

    data_json = json.dumps(data)

    struct_from_dict = Struct().from_dict(data)
    assert struct_from_dict.fields == data2
    assert struct_from_dict.to_dict() == data
    # assert struct_from_dict.to_json() == data_json

    struct_from_json = Struct().from_json(data_json)
    assert struct_from_json.fields == data2
    assert struct_from_json.to_dict() == data
    assert struct_from_json == struct_from_dict
    # assert struct_from_json.to_json() == data_json

test_struct_roundtrip()