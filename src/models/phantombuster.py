from pydantic import BaseModel
from typing import Dict, List, Optional, Any

class Argument(BaseModel):
    """Modelo para los argumentos de un phantom"""
    name: str
    value: Any

class Phantom(BaseModel):
    """Modelo para un phantom de PhantomBuster"""
    id: str
    name: str
    description: Optional[str] = None
    script: Optional[str] = None
    arguments: Optional[List[Argument]] = None

class Container(BaseModel):
    """Modelo para un contenedor de ejecución de PhantomBuster"""
    id: str
    status: str
    phantomId: str
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    resultObject: Optional[Dict] = None
