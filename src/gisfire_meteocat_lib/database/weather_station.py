from gisfire_meteocat_lib.database import db
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func


class WeatherStation(db.Base):
    __tablename__ = 'meteocat_metadata_variables'
    id = Column(Integer, primary_key=True)
    _codi = Column(String, nullable=False, unique=True)
    _nom = Column(String, nullable=False)
    _unitat = Column(String, nullable=False)
    _acronim = Column(String, nullable=False)
    _tipus = Column(String, nullable=False)
    _decimals = Column(String, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)