#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

from .lightnings import Lightning
from .lightnings import LightningAPIRequest
import dateutil.parser


def get_lightning_api_requests(db_session, date_from, date_to=None):
    """
    Get a list of the requests results performed to the remote MeteoCat API. This list is useful to know if there were
    lightnings in a particular time interval. The dates minimum precision is the hour. So any minute, second or
    millisecond is truncated. The query is performed using the following comparison: date_from <= date < date_to

    :param db_session: SQL Alchemy database session to work with
    :type db_session: sqlalchemy.orm.Session
    :param date_from: Date to ask requests from
    :type date_from: Union[datetime.datetime|str]
    :param date_to: Date to finish the asking of requests
    :type date_to: Union[datetime.datetime|str]
    :return: A list LightningAPIRequest objects or None if no requests were found between the dates
    :rtype: Union[list[LightningAPIRequest] | None]
    """
    if type(date_from) is str:
        date_from = dateutil.parser.isoparse(date_from).replace(minute=0, second=0)
    else:
        date_from = date_from.replace(minute=0, second=0)
    if not(date_to is None):
        if type(date_to) is str:
            date_to = dateutil.parser.isoparse(date_to).replace(minute=0, second=0)
        else:
            date_to = date_to.replace(minute=0, second=0)
        requests = db_session.query(LightningAPIRequest)\
            .filter(LightningAPIRequest.date >= date_from)\
            .filter(LightningAPIRequest.date < date_to)\
            .order_by(LightningAPIRequest.date)\
            .all()
    else:
        requests = db_session.query(LightningAPIRequest)\
            .filter(LightningAPIRequest.date == date_from)\
            .all()
    return requests


def get_lightnings(db_session, date_from, date_to=None):
    """
    Get a list of Lightnings registered by the MeteoCat system between the specified dates. The dates minimum precision
    is the hour. So any minute, second or millisecond is truncated. The query is performed using the following
    comparison: date_from <= date < date_to

    :param db_session: SQL Alchemy database session to work with
    :type db_session: sqlalchemy.orm.Session
    :param date_from:
    :type date_from: Union[datetime.datetime|str]
    :param date_to:
    :type date_to: Union[datetime.datetime|str]
    :return: A list Lightning objects or None if no lightnings were found between the dates
    :rtype: Union[list[Lightning] | None]
    """
    if type(date_from) is str:
        date_from = dateutil.parser.isoparse(date_from).replace(minute=0, second=0)
    else:
        date_from = date_from.replace(minute=0, second=0)
    if not(date_to is None):
        if type(date_to) is str:
            date_to = dateutil.parser.isoparse(date_to).replace(minute=0, second=0)
        else:
            date_to = date_to.replace(minute=0, second=0)
        lightnings = db_session.query(Lightning)\
            .filter(Lightning.date >= date_from)\
            .filter(Lightning.date < date_to)\
            .order_by(Lightning.date)\
            .all()
    else:
        lightnings = db_session.query(Lightning)\
            .filter(Lightning.date == date_from)\
            .all()
    return lightnings

