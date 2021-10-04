from gisfire_meteocat_lib.database import db
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func


class Variable(db.Base):
    __tablename__ = 'meteocat_metadata_variables'
    id = Column(Integer, primary_key=True)
    _codi = Column(String, nullable=False, unique=True)
    _nom = Column(String, nullable=False)
    _unitat = Column(String, nullable=False)
    _acronim = Column(String, nullable=False)
    _tipus = Column(String, nullable=False)
    _decimals = Column(String, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, _codi, _nom, _unitat, _acronim, _tipus, _decimals):
        self._codi = _codi
        self._nom = _nom
        self._unitat = _unitat
        self._acronim = _acronim
        self._tipus = _tipus
        self._decimals = _decimals
