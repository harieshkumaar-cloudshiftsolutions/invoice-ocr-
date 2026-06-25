from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Template(Base):
    __tablename__ = "templates"
    
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    vendor_category = Column(String(50), nullable=True)
    created_by = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
    usage_count = Column(Integer, default=0)

    # Relationships
    fields = relationship("TemplateField", back_populates="template")
    rules = relationship("ExtractionRule", back_populates="template")

class TemplateField(Base):
    __tablename__ = "template_fields"
    
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(String(50), ForeignKey("templates.template_id"), nullable=False)
    field_name = Column(String(50), nullable=False)
    field_type = Column(String(20), nullable=False) 
    is_required = Column(Boolean, default=True)
    display_order = Column(Integer, default=0)

    template = relationship("Template", back_populates="fields")

class ExtractionRule(Base):
    __tablename__ = "extraction_rules"
    
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(String(50), ForeignKey("templates.template_id"), nullable=False)
    field_name = Column(String(50), nullable=False)
    rule_type = Column(String(20), nullable=False) 
    rule_value = Column(Text, nullable=False)
    fallback_order = Column(Integer, default=1)
    
    template = relationship("Template", back_populates="rules")