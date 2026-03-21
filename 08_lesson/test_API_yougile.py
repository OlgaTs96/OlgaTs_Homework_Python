import pytest
import requests
import uuid

base_url = "https://yougile.com"


@pytest.fixture(scope='session')
def get_token():
    """Фикстура для получения токена один раз за сессию."""
    company_id = get_company_id()
    creds_auth = {
        'login': 'ucfh4@dollicons.com',
        'password': 'Test1234!',
        'companyId': company_id,
    }

    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.post(
        f"{base_url}/api-v2/auth/keys",
        json=creds_auth,
        headers=headers
    )
    assert resp.status_code == 201, "Не удалось получить API ключ"

    API_key = resp.json()['key']
    return API_key


@pytest.fixture
def headers(get_token):
    """Обновляем HEADERS с актуальным токеном."""
    return {
        'Authorization': f'Bearer {get_token}',
        'Content-Type': 'application/json',
    }


def generate_unique_title():
    """Генерирует уникальное название проекта."""
    return f"Test Project {uuid.uuid4()}"


@pytest.fixture
def created_project(headers):
    """Создаёт проект, удаляет после теста."""
    project_id = None
    try:
        title = generate_unique_title()
        response = requests.post(
            f"{base_url}/api-v2/projects",
            headers=headers,
            json={"title": title}
        )
        assert response.status_code == 201, (
            f"Не удалось создать проект: {response.text}"
        )
        project_id = response.json()['id']
        yield project_id
    finally:
        if project_id:
            delete_response = requests.delete(
                f"{base_url}/api-v2/projects/{project_id}",
                headers=headers
            )
            if delete_response.status_code not in (200, 204):
                print(f"Предупреждение: не удалось удалить проект "
                      f"{project_id}, код {delete_response.status_code}")


# Тест на создание проекта
def test_create_project_positive(created_project, headers):
    """Позитивный тест: создание проекта и проверка его существования."""
    project_id = created_project
    get_response = requests.get(
        f"{base_url}/api-v2/projects/{project_id}",
        headers=headers
    )
    assert get_response.status_code == 200, "Созданный проект не найден"
    data = get_response.json()
    assert 'id' in data, "Ответ не содержит id проекта"


# Негативный тест: пустое тело при создании
def test_create_project_negative_empty_body(headers):
    response = requests.post(
        f"{base_url}/api-v2/projects",
        headers=headers,
        json={}  # пустое тело
    )
    assert response.status_code == 400, (
        f"Ожидался код 400, получен {response.status_code}"
    )


# 2. Тесты на изменение проекта
def test_update_project_positive(created_project, headers):
    """Позитивный тест: изменение названия существующего проекта."""
    project_id = created_project
    new_title = f"Updated {generate_unique_title()}"
    response = requests.put(
        f"{base_url}/api-v2/projects/{project_id}",
        headers=headers,
        json={'title': new_title}
    )
    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}"
    )

    # Проверим, что изменения применились, выполнив GET
    get_response = requests.get(
        f"{base_url}/api-v2/projects/{project_id}",
        headers=headers
    )
    assert get_response.status_code == 200
    assert get_response.json().get('title') == new_title, "Не обновлено"


def test_update_project_negative_no_id(headers):
    """Негативный тест: PUT запрос без указания ID (ожидается 404 или 405)."""
    new_title = generate_unique_title()
    response = requests.put(
        f"{base_url}/api-v2/projects/",
        headers=headers,
        json={'title': new_title}
    )
    assert response.status_code in (404, 405), (
        f"Ожидался 404 или 405, получен {response.status_code}"
    )


# 3. Тесты на получение проекта по ID
def test_get_project_by_id_positive(created_project, headers):
    """Позитивный тест: получение проекта по ID с авторизацией."""
    project_id = created_project
    response = requests.get(
        f"{base_url}/api-v2/projects/{project_id}",
        headers=headers
    )
    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}"
    )
    data = response.json()
    assert data['id'] == project_id, "ID проекта не совпадает"
    assert 'title' in data, "Ответ не содержит названия"


def test_get_project_by_id_negative_no_auth(created_project):
    """Негативный тест: получение проекта без авторизации (ожидается 401)."""
    project_id = created_project
    response = requests.get(
        f"{base_url}/api-v2/projects/{project_id}",
        headers={}  # без токена
    )
    assert response.status_code == 401, (
        f"Ожидался код 401, получен {response.status_code}"
    )


def get_company_id():
    creds = {
        'login': 'ucfh4@dollicons.com',
        'password': 'Test1234!',
    }
    resp = requests.post(f"{base_url}/api-v2/auth/companies", json=creds)
    assert resp.status_code == 200, "Ошибка при получении компании"

    company_id = resp.json()['content'][0]['id']
    return company_id
