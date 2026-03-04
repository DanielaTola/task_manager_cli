# definición de Task (dataclass) + (de)serialización.
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Literal, List, Optional, Dict, Any
import uuid

Priority = Literal ["Low", "Medium", "High"]
Status = Literal ["Done", "In Progress", "ToDo"]

#estandariza fechas, facilita parseo y comparaciones sin ambigüedades de zona horaria.
def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
    
@dataclass #para tener un modelo claro, tipado y fácil de serializar.
class Task: 
    id: str
    title: str
    status: Status = "ToDo"
    priority: Priority ="Medium"
    tags: List[str] = field(default_factory=list)
    description: str
    responsible: str
    create_at: str = field(default_factory= now_iso)
    update_att: Optional[str] = field(default_factory= now_iso)
    
    def to_dict(self)-> Dict[str, Any]:
        return asdict(self)
    
    @staticmethod
    def new(title: str,
            priority: Priority = "medium",
            status: Status = "ToDo",
            tags: Optional[List[str]] = None) -> "Task":
        return Task(
            id=str(uuid.uuid4()),
            title=title.strip(),
            status=status,
            priority=priority,
            tags=tags or [],
            created_at=now_iso(),
            updated_at=None,
        )

    @staticmethod
    def from_dict (data: Dict[str, Any]) -> "Task": 
        return Task(
            id=data.get("id", str(uuid.uuid4())), 
            title=str(data.get("title", "")).strip(), 
            priority=data.get("priority", "Medium"),
            status=data.get("status", "ToDo"),
            tags=list(data.get("tags", [])),
            responsible=(data.get("responsible", "")).strip(),
            description=(data.get("description", "")).strip(),
            created_at=data.get("created_at", now_iso()),
            updated_at=data.get("updated_at")
        )

    
    def migrate_legacy_record(rec: Any) -> Dict[str, Any]:
        """
            Compatibilidad: si tu JSON anterior era ['tarea1', 'tarea2', ...],
            lo convertimos a objetos Task con título = string y resto por defecto.
        """
        if isinstance(rec, str):
            return Task.new(title=rec).to_dict()
        if isinstance(rec, dict):
            return Task.from_dict(rec).to_dict()
        # Si viene algo inesperado, lo ignoramos (o podríamos levantar error)
        return Task.new(title=str(rec)).to_dict()
        
        