from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "Charlie Brown",
        },
    ]

    expected_users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Alice",
            "last_name": "Smith",
            "full_name": "Alice Smith",
        },
        {
            "first_name": "Charlie",
            "last_name": "Brown",
            "full_name": "Charlie Brown",
        },
    ]

    restore_names(users)
    assert users == expected_users

# if __name__ == "__main__":
#     pytest.main(["-v", "app/restore_names.py"])
