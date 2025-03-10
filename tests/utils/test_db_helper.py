import pytest
from unittest import mock
from src.models.hcc import HCC
from src.utils.db_helper import insert_data, get_by_code


@pytest.fixture
def mock_database():
    with mock.patch("sqlite3.connect") as mock_connect:
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()

        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        yield mock_connect
        mock_conn.close.assert_called_once()


def test_insert_data(mock_database):
    data = [("E11", "Diabetes", "Endocrinology"), ("J45", "Asthma", "Respiratory")]

    insert_data(data)

    mock_database.return_value.cursor.return_value.executemany.assert_called_once_with(
        "INSERT INTO icd_codes (code, description, tags) VALUES (?, ?, ?)", data
    )

    mock_database.return_value.commit.assert_called_once()


def test_get_by_code(mock_database):
    mock_database.return_value.cursor.return_value.fetchone.return_value = (
        "E11",
        "Diabetes",
        "Endocrinology",
    )

    result = get_by_code("E11")

    assert isinstance(result, HCC)
    assert result.code == "E11"
    assert result.description == "Diabetes"
    assert result.tags == "Endocrinology"

    mock_database.return_value.cursor.return_value.execute.assert_called_once_with(
        "SELECT code, description, tags FROM icd_codes WHERE code = ?", ("E11",)
    )


def test_get_by_code_not_found(mock_database):
    mock_database.return_value.cursor.return_value.fetchone.return_value = None

    result = get_by_code("NON_EXISTENT_CODE")

    assert result is None

    mock_database.return_value.cursor.return_value.execute.assert_called_once_with(
        "SELECT code, description, tags FROM icd_codes WHERE code = ?",
        ("NON_EXISTENT_CODE",),
    )
