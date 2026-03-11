from __future__ import annotations
from pathlib import Path
import json 
import os
import tempfile
from typing import List, Dict, Any


APP_DIR_NAME="data"
DATA_FILE_NAME = "tasks.json"

def default_data_path () -> Path: 
    home = Path.home() #obtiene el directorio home del usuario de forma segura y multiplataforma.
    data_dir = home / f".{APP_DIR_NAME}" #crea un directorio oculto en el home del usuario para almacenar los datos de la aplicación, evitando conflictos con otros archivos y manteniendo la organización.
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir/DATA_FILE_NAME

class JsonStorage: 
    def __init__(self, path:Path |None=None):
        self.path = path or default_data_path()
        
    
    def load(self) -> List[Dict[str, Any]]:
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
                # Si el archivo no es lista, devolvemos lista vacía por robustez.
                return []
        except json.JSONDecodeError:
            # Archivo corrupto o vacío → devolvemos vacío (otra opción: backup)
            return []
