# coding: utf-8

"""
    Listing Data Storage

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from listing_data_storage_client.models.pagination_schema import PaginationSchema
from listing_data_storage_client.models.sold_info import SoldInfo
from listing_data_storage_client.models.tickemaster_sold_group_schema import TickemasterSoldGroupSchema
from typing import Optional, Set
from typing_extensions import Self

class TicketmasterSoldGroupResponseSchema(BaseModel):
    """
    TicketmasterSoldGroupResponseSchema
    """ # noqa: E501
    pagination: PaginationSchema
    info: SoldInfo
    sold_data: Optional[Dict[str, List[TickemasterSoldGroupSchema]]] = None
    __properties: ClassVar[List[str]] = ["pagination", "info", "sold_data"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TicketmasterSoldGroupResponseSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in sold_data (dict of array)
        _field_dict_of_array = {}
        if self.sold_data:
            for _key_sold_data in self.sold_data:
                if self.sold_data[_key_sold_data] is not None:
                    _field_dict_of_array[_key_sold_data] = [
                        _item.to_dict() for _item in self.sold_data[_key_sold_data]
                    ]
            _dict['sold_data'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TicketmasterSoldGroupResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pagination": PaginationSchema.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "info": SoldInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "sold_data": dict(
                (_k,
                        [TickemasterSoldGroupSchema.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("sold_data", {}).items()
            )
        })
        return _obj


