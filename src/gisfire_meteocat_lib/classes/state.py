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
    TODO
    Class container for the weather station status table.  Provides the SQL Alchemy access to the different status of
    the timeline of a weather station. A weather station status informs of the presence of a certain weather station in
    the system.

    The weather station status information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/metadades-estacions/#metadades-de-totes-les-estacions

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
        self.from_date = from_date
        self.to_date = to_date

    @staticmethod
    def object_hook_abstract(dct: Dict[str, Any], dest: State) -> None:
        """
        TODO
        Decodes a JSON originated dict from the Meteocat API to a WeatherStationStatus object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        TODO
        :param dest:
        :type dest:
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
        JSON Encoder to convert a database WeatherStationStatus to JSON
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: Lightning
            :return: dict
            """
            if isinstance(obj, State):
                obj: State
                dct = dict()
                dct['from_date'] = obj.from_date.strftime("%Y-%m-%dT%H:%MZ")
                dct['to_date'] = obj.to_date.strftime("%Y-%m-%dT%H:%MZ") if obj.to_date is not None else None
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover
