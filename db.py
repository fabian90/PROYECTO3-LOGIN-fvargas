# db.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.ingrediente import Ingrediente
from models.tipoVaso import TipoVaso