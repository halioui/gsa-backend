# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from reactome_analysis_api.models.base_model_ import Model
from reactome_analysis_api.models.dataset import Dataset  # noqa: F401,E501
from reactome_analysis_api.models.parameter import Parameter  # noqa: F401,E501
from reactome_analysis_api import util


class AnalysisInput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, method_name: str=None, datasets: List[Dataset]=None, parameters: List[Parameter]=None, analysis_id: str=None):  # noqa: E501
        """AnalysisInput - a model defined in Swagger

        :param method_name: The method_name of this AnalysisInput.  # noqa: E501
        :type method_name: str
        :param datasets: The datasets of this AnalysisInput.  # noqa: E501
        :type datasets: List[Dataset]
        :param parameters: The parameters of this AnalysisInput.  # noqa: E501
        :type parameters: List[Parameter]
        :param analysis_id: The analysis_id of this AnalysisInput.  # noqa: E501
        :type analysis_id: str
        """
        self.swagger_types = {
            'method_name': str,
            'datasets': List[Dataset],
            'parameters': List[Parameter],
            'analysis_id': str
        }

        self.attribute_map = {
            'method_name': 'methodName',
            'datasets': 'datasets',
            'parameters': 'parameters',
            'analysis_id': 'analysisId'
        }

        self._method_name = method_name
        self._datasets = datasets
        self._parameters = parameters
        self._analysis_id = analysis_id

    @classmethod
    def from_dict(cls, dikt) -> 'AnalysisInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnalysisInput of this AnalysisInput.  # noqa: E501
        :rtype: AnalysisInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def method_name(self) -> str:
        """Gets the method_name of this AnalysisInput.


        :return: The method_name of this AnalysisInput.
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name: str):
        """Sets the method_name of this AnalysisInput.


        :param method_name: The method_name of this AnalysisInput.
        :type method_name: str
        """
        if method_name is None:
            raise ValueError("Invalid value for `method_name`, must not be `None`")  # noqa: E501

        self._method_name = method_name

    @property
    def datasets(self) -> List[Dataset]:
        """Gets the datasets of this AnalysisInput.


        :return: The datasets of this AnalysisInput.
        :rtype: List[Dataset]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets: List[Dataset]):
        """Sets the datasets of this AnalysisInput.


        :param datasets: The datasets of this AnalysisInput.
        :type datasets: List[Dataset]
        """
        if datasets is None:
            raise ValueError("Invalid value for `datasets`, must not be `None`")  # noqa: E501

        self._datasets = datasets

    @property
    def parameters(self) -> List[Parameter]:
        """Gets the parameters of this AnalysisInput.


        :return: The parameters of this AnalysisInput.
        :rtype: List[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: List[Parameter]):
        """Sets the parameters of this AnalysisInput.


        :param parameters: The parameters of this AnalysisInput.
        :type parameters: List[Parameter]
        """

        self._parameters = parameters

    @property
    def analysis_id(self) -> str:
        """Gets the analysis_id of this AnalysisInput.

        This field is only used internally and will be ignored if set in the request.  # noqa: E501

        :return: The analysis_id of this AnalysisInput.
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id: str):
        """Sets the analysis_id of this AnalysisInput.

        This field is only used internally and will be ignored if set in the request.  # noqa: E501

        :param analysis_id: The analysis_id of this AnalysisInput.
        :type analysis_id: str
        """

        self._analysis_id = analysis_id
