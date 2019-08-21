# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reactome_analysis_api.models.base_model_ import Model
from reactome_analysis_api import util


class DataType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, description: str=None):  # noqa: E501
        """DataType - a model defined in Swagger

        :param id: The id of this DataType.  # noqa: E501
        :type id: str
        :param name: The name of this DataType.  # noqa: E501
        :type name: str
        :param description: The description of this DataType.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'description': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description'
        }

        self._id = id
        self._name = name
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'DataType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataType of this DataType.  # noqa: E501
        :rtype: DataType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this DataType.


        :return: The id of this DataType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this DataType.


        :param id: The id of this DataType.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this DataType.

        Nice name of the data type  # noqa: E501

        :return: The name of this DataType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this DataType.

        Nice name of the data type  # noqa: E501

        :param name: The name of this DataType.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this DataType.


        :return: The description of this DataType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this DataType.


        :param description: The description of this DataType.
        :type description: str
        """

        self._description = description
