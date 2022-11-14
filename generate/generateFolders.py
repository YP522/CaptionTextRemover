from system import utils as u
from pathlib import Path

def create_folders():
    """
    Create folders for the project
    """
    Path(u.dt_string+"/").mkdir(parents=True, exist_ok=True)
