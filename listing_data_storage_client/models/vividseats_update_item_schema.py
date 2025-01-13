# coding: utf-8

"""
    Listing Data Storage

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class VividseatsUpdateItemSchema(str, Enum):
    """
    VividseatsUpdateItemSchema
    """

    """
    allowed enum values
    """
    PRICE = 'PRICE'
    QUANTITY = 'QUANTITY'
    SELLABLE_QUANTITIES = 'SELLABLE_QUANTITIES'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VividseatsUpdateItemSchema from a JSON string"""
        return cls(json.loads(json_str))


