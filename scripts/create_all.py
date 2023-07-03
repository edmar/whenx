from whenx.database import engine, Base
from whenx.models import *
Base.metadata.create_all(engine)

