from sqlalchemy import Column, String, Text

from app.core.db import BaseModel


class Document(BaseModel):
    __tablename__ = "documents"
    
    text = Column(Text, nullable=False, default='')
    url = Column(String, nullable=False, server_default='')
    summary = Column(Text, nullable=False, server_default='')
