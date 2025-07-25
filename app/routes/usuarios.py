from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    if db.query(models.Usuario).filter_by(cedula=usuario.cedula).first():
        raise HTTPException(status_code=400, detail="La cédula ya existe")
    nuevo_usuario = models.Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/", response_model=list[schemas.UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@router.get("/{cedula}", response_model=schemas.UsuarioOut)
def obtener_usuario(cedula: str, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter_by(cedula=cedula).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{cedula}", response_model=schemas.UsuarioOut)
def actualizar_usuario(cedula: str, datos: schemas.UsuarioBase, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter_by(cedula=cedula).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in datos.dict().items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/{cedula}")
def eliminar_usuario(cedula: str, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter_by(cedula=cedula).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}