from sqlalchemy import MetaData, Column, Text
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class UrlAssociation(Base):
    __tablename__ = 'urlassociation'

    fullurl = Column(Text)
    shorturl = Column(Text, primary_key=True)
