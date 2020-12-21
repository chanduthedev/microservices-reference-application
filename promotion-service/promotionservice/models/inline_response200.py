# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from promotionservice.models.base_model_ import Model
from promotionservice.models.promotion import Promotion
from promotionservice import util

from promotionservice.models.promotion import Promotion  # noqa: E501

class InlineResponse200(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status_code=None, message=None, promotions=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI

        :param status_code: The status_code of this InlineResponse200.  # noqa: E501
        :type status_code: int
        :param message: The message of this InlineResponse200.  # noqa: E501
        :type message: str
        :param promotions: The promotions of this InlineResponse200.  # noqa: E501
        :type promotions: Promotion
        """
        self.openapi_types = {
            'status_code': int,
            'message': str,
            'promotions': Promotion
        }

        self.attribute_map = {
            'status_code': 'statusCode',
            'message': 'message',
            'promotions': 'promotions'
        }

        self._status_code = status_code
        self._message = message
        self._promotions = promotions

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status_code(self):
        """Gets the status_code of this InlineResponse200.


        :return: The status_code of this InlineResponse200.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this InlineResponse200.


        :param status_code: The status_code of this InlineResponse200.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def message(self):
        """Gets the message of this InlineResponse200.


        :return: The message of this InlineResponse200.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse200.


        :param message: The message of this InlineResponse200.
        :type message: str
        """

        self._message = message

    @property
    def promotions(self):
        """Gets the promotions of this InlineResponse200.


        :return: The promotions of this InlineResponse200.
        :rtype: Promotion
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this InlineResponse200.


        :param promotions: The promotions of this InlineResponse200.
        :type promotions: Promotion
        """

        self._promotions = promotions
