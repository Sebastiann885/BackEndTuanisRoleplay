from sqlalchemy import Column, Integer, String, BigInteger, Enum
from .database import Base

class Usuario(Base):
    __tablename__ = "cedulas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cedula = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100))
    apellido = Column(String(100))
    nacionalidad = Column(String(100))
    estatura = Column(String(10))
    fecha_nacimiento = Column(String(15))
    edad = Column(String(3))
    sexo = Column(Enum("Hombre", "Mujer"))
    usuario_discord = Column(BigInteger)
    usuario_roblox = Column(String(100))