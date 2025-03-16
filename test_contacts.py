from contacts import ContactsManager
import pytest


# contacts_manager = ContactsManager()

@pytest.fixture
def contacts_manager():
    return ContactsManager()


def test_add_contact(contacts_manager):
    contacts_manager.add_contact("John", "1234567")
    assert contacts_manager.get_contact(name="John") == {"John", "1234567"}


def test_empty_contact(contacts_manager):
    with pytest.raises(ValueError) as error:
        contacts_manager.add_contact(name="", phone_number="1234567")
    assert error.value == "not empty"
