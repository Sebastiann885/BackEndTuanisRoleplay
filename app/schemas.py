from pydantic import BaseModel
from typing import Literal

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    nacionalidad: str
    estatura: str
    fecha_nacimiento: str
    edad: str
    sexo: Literal["Hombre", "Mujer"]
    usuario_discord: int
    usuario_roblox: str

class UsuarioCreate(UsuarioBase):
    cedula: str

class UsuarioOut(UsuarioBase):
    id: int
    cedula: str

    class Config:
        from_attributes = True