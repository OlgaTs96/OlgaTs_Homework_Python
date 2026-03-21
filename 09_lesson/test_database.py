from sqlalchemy import create_engine, inspect

db_connection_string = "postgresql://postgres:Olga1996@localhost:5433/postgres"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'users'
