from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from app import models, schemas, database
import os
from app.database import get_db

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# --- Configuración JWT ---
SECRET_KEY = os.getenv("SECRET_KEY", "supersecreto123")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# --- Dependencia de seguridad ---
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

# --- ENDPOINTS PROTEGIDOS ---
@router.post("/", response_model=schemas.UsuarioOut)
def crear_usuario(
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    if db.query(models.Usuario).filter_by(cedula=usuario.cedula).first():
        raise HTTPException(status_code=400, detail="La cédula ya existe")
    
    nuevo_usuario = models.Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/", response_model=list[schemas.UsuarioOut])
def listar_usuarios(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return db.query(models.Usuario).all()

@router.get("/{cedula}", response_model=schemas.UsuarioOut)
def obtener_usuario(
    cedula: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    usuario = db.query(models.Usuario).filter_by(cedula=cedula).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{cedula}", response_model=schemas.UsuarioOut)
def actualizar_usuario(
    cedula: str,
    datos: schemas.UsuarioBase,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    usuario = db.query(models.Usuario).filter_by(cedula=cedula).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in datos.dict().items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/{cedula}")
def eliminar_usuario(
    cedula: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    usuario = db.query(models.Usuario).filter_by(cedula=cedula).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}