from gisfire_meteocat_lib.database import db
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import UniqueConstraint
from sqlalchemy import func
from geoalchemy2 import Geometry


class Area(db.Base):
    __tablename__ = 'meteocat_reference'
    id = Column(Integer, primary_key=True)
    _codi = Column(String, nullable=False)
    _nom = Column(String, nullable=False)
    admin_level = Column(Integer, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    geom = Column(Geometry('MULTIPOLYGON', srid=25831))
    __table_args__ = UniqueConstraint('admin_level', '_codi')

    def __init__(self, _codi, _nom, admin_level, geom=None):
        self._codi = _codi
        self._nom = _nom
        self.admin_level = admin_level
        self.geom = geom
