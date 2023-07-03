#!/usr/bin/env python3

from whenx.database import db
from sqlalchemy import MetaData


def delete_all_data():
    meta = MetaData()
    meta.reflect(bind=db.get_bind())  # Get the engine associated with the session

    # First, delete child table data
    child_tables = [table for table in meta.sorted_tables if table.foreign_keys]

    for table in child_tables:
        db.execute(table.delete())

    # Then, delete parent table data
    parent_tables = [table for table in meta.sorted_tables if not table.foreign_keys]

    for table in parent_tables:
        db.execute(table.delete())

    db.commit()


if __name__ == "__main__":
    delete_all_data()
