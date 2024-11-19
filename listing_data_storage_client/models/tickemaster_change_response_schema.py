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
from listing_data_storage_client.models.change_info import ChangeInfo
from listing_data_storage_client.models.pagination_schema import PaginationSchema
from listing_data_storage_client.models.ticketmaster_change_schema import TicketmasterChangeSchema
from typing import Optional, Set
from typing_extensions import Self

class TickemasterChangeResponseSchema(BaseModel):
    """
    TickemasterChangeResponseSchema
    """ # noqa: E501
    pagination: PaginationSchema
    info: ChangeInfo
    change_data: Optional[List[TicketmasterChangeSchema]] = None
    __properties: ClassVar[List[str]] = ["pagination", "info", "change_data"]

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
        """Create an instance of TickemasterChangeResponseSchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in change_data (list)
        _items = []
        if self.change_data:
            for _item_change_data in self.change_data:
                if _item_change_data:
                    _items.append(_item_change_data.to_dict())
            _dict['change_data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TickemasterChangeResponseSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pagination": PaginationSchema.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "info": ChangeInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "change_data": [TicketmasterChangeSchema.from_dict(_item) for _item in obj["change_data"]] if obj.get("change_data") is not None else None
        })
        return _obj

