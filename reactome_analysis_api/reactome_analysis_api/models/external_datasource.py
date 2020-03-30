# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reactome_analysis_api.models.base_model_ import Model
from reactome_analysis_api.models.external_datasource_parameters import ExternalDatasourceParameters  # noqa: F401,E501
from reactome_analysis_api import util


class ExternalDatasource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, parameters: List[ExternalDatasourceParameters]=None):  # noqa: E501
        """ExternalDatasource - a model defined in Swagger

        :param id: The id of this ExternalDatasource.  # noqa: E501
        :type id: str
        :param name: The name of this ExternalDatasource.  # noqa: E501
        :type name: str
        :param parameters: The parameters of this ExternalDatasource.  # noqa: E501
        :type parameters: List[ExternalDatasourceParameters]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'parameters': List[ExternalDatasourceParameters]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'parameters': 'parameters'
        }

        self._id = id
        self._name = name
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'ExternalDatasource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExternalDatasource of this ExternalDatasource.  # noqa: E501
        :rtype: ExternalDatasource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ExternalDatasource.

        A unique identifier for the data source.  # noqa: E501

        :return: The id of this ExternalDatasource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ExternalDatasource.

        A unique identifier for the data source.  # noqa: E501

        :param id: The id of this ExternalDatasource.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this ExternalDatasource.

        A human readable name for the data source  # noqa: E501

        :return: The name of this ExternalDatasource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ExternalDatasource.

        A human readable name for the data source  # noqa: E501

        :param name: The name of this ExternalDatasource.
        :type name: str
        """

        self._name = name

    @property
    def parameters(self) -> List[ExternalDatasourceParameters]:
        """Gets the parameters of this ExternalDatasource.


        :return: The parameters of this ExternalDatasource.
        :rtype: List[ExternalDatasourceParameters]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: List[ExternalDatasourceParameters]):
        """Sets the parameters of this ExternalDatasource.


        :param parameters: The parameters of this ExternalDatasource.
        :type parameters: List[ExternalDatasourceParameters]
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters