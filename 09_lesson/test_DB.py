from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

db_connection_string = (
    "postgresql://postgres:Olga1996@localhost:5433/postgres"
)
db = create_engine(db_connection_string)


def test_insert_subject():
    connection = db.connect()
    transaction = connection.begin()

    try:
        sql = text(
            "INSERT INTO subject(subject_id, subject_title) "
            "VALUES (:id, :title)"
        )
        new_id = 1234
        new_title = "Mathematics"
        connection.execute(sql, {"id": new_id, "title": new_title})

        # Проверка, что запись добавилась
        result = connection.execute(
            text(
                "SELECT subject_title FROM subject WHERE subject_id = :id"
            ),
            {"id": new_id},
        )
        subject = result.fetchone()
        assert subject is not None, "Запись не найдена"
        assert subject[0] == new_title, (
            f"Ожидалось '{new_title}', получено '{subject[0]}'"
        )

        transaction.rollback()  # Откат изменений после теста

    except SQLAlchemyError as e:
        transaction.rollback()
        raise e  # Проброс ошибки, чтобы тест упал

    finally:
        connection.close()


def test_update_subject():
    connection = db.connect()
    transaction = connection.begin()

    try:
        # ID существующей записи, которую хотим изменить
        subject_id_to_update = 1
        new_title = "Physics"

        # Выполняем обновление
        sql_update = text(
            "UPDATE subject SET subject_title = :new_title "
            "WHERE subject_id = :id"
        )
        connection.execute(
            sql_update,
            {"new_title": new_title, "id": subject_id_to_update},
        )

        # Проверяем, что обновление прошло успешно
        sql_select = text(
            "SELECT subject_title FROM subject WHERE subject_id = :id"
        )
        result = connection.execute(sql_select, {"id": subject_id_to_update})
        updated = result.fetchone()
        assert updated is not None, "Запись для обновления не найдена"
        assert updated[0] == new_title, (
            f"Ожидался заголовок '{new_title}', получен '{updated[0]}'"
        )

        transaction.rollback()  # Откат, чтобы не менять базу после теста

    except SQLAlchemyError as e:
        transaction.rollback()
        raise e  # Проброс ошибки, чтобы тест упал

    finally:
        connection.close()


def test_delete_subject():
    connection = db.connect()
    transaction = connection.begin()

    try:
        test_id = 15
        test_title = "Test Subject to Delete"

        # Вставляем тестовую запись
        insert_sql = text(
            "INSERT INTO subject(subject_id, subject_title) "
            "VALUES (:id, :title)"
        )
        connection.execute(insert_sql, {"id": test_id, "title": test_title})

        # Удаляем запись
        delete_sql = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(delete_sql, {"id": test_id})

        # Проверяем, что записи нет
        select_sql = text(
            "SELECT subject_id FROM subject WHERE subject_id = :id"
        )
        result = connection.execute(select_sql, {"id": test_id})
        deleted = result.fetchone()
        assert deleted is None, "Запись не удалена"

        transaction.rollback()  # Откат всех изменений после теста

    except SQLAlchemyError as e:
        transaction.rollback()
        raise e

    finally:
        connection.close()
