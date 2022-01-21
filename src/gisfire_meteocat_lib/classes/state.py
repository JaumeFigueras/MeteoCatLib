#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

import datetime
import dateutil.parser
import json

from . import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import func

from typing import Dict
from typing import Optional
from typing import Any


class State(Base):
    """
    Class container for a state. Implements a base abstract class with common properties between states. Will be used in
    variables and weather stations

    :type id: int or Column
    :type from_date: datetime.datetime or Column or None
    :type to_date: datetime.datetime or Column or None
    :type ts: datetime.datetime or Column
    """
    __abstract__ = True  # SQLAlchemy directive for abstract classes
    id = Column(Integer, primary_key=True)
    from_date = Column('_data_inici', DateTime(timezone=True), nullable=False)
    to_date = Column('_data_fi', DateTime(timezone=True))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, from_date: Optional[datetime.datetime, None] = None,
                 to_date: Optional[datetime.datetime, None] = None) -> None:
        """
        Class constructor

        :param from_date: Date the state begins to be valid
        :type from_date: datetime
        :param to_date: Date when the state finishes its validity
        :type to_date: datetime
        """
        self.from_date = from_date
        self.to_date = to_date

    @staticmethod
    def object_hook_abstract(dct: Dict[str, Any], dest: State) -> None:
        """
        Decodes a JSON originated dict from the Meteocat API and stores in the destination object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :param dest: Destination object were the data wil be stored. Must be a subclass of State
        :type dest: State
        :return: None
        """
        try:
            dest.from_date = dateutil.parser.isoparse(dct['dataInici'])
        except ValueError as e:
            raise e
        if dct['dataFi'] is None:
            dest.to_date = None
        else:
            try:
                dest.to_date = dateutil.parser.isoparse(dct['dataFi'])
            except ValueError as e:
                raise e

    class JSONEncoder(json.JSONEncoder):
        """
        JSON Encoder to convert a States to JSON
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj: Object to encode to JSON
            :type obj: State
            :return: dict
            """
            if isinstance(obj, State):
                obj: State
                dct = dict()
                dct['from_date'] = obj.from_date.strftime("%Y-%m-%dT%H:%MZ")
                dct['to_date'] = obj.to_date.strftime("%Y-%m-%dT%H:%MZ") if obj.to_date is not None else None
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover
