import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

# Позитивные тесты
def test_capitalize(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("SkyPro") == "Skypro"
    assert string_utils.capitalize("123") == "123"
    assert string_utils.capitalize("04 апреля 2023") == "04 апреля 2023"

def test_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   skypro   ") == "skypro   "
    assert string_utils.trim("  123  ") == "123  "

def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("Тест,123,04 апреля 2023") == ["Тест", "123", "04 апреля 2023"]

def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("123", "1") is True

def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("12345", "3") == "1245"

def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S") is True
    assert string_utils.starts_with("SkyPro", "P") is False
    assert string_utils.starts_with("123", "1") is True

def test_ends_with(string_utils):
    assert string_utils.ends_with("SkyPro", "o") is True
    assert string_utils.ends_with("SkyPro", "y") is False
    assert string_utils.ends_with("123", "3") is True

def test_is_empty(string_utils):
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True
    assert string_utils.is_empty("SkyPro") is False

def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string([]) == ""

# Негативные тесты
def test_capitalize_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)

def test_trim_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.trim(None)

def test_to_list_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.to_list(None)

def test_contains_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.contains(None, "S")
    with pytest.raises(AttributeError):
        string_utils.contains("SkyPro", None)

def test_delete_symbol_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "k")
    with pytest.raises(AttributeError):
        string_utils.delete_symbol("SkyPro", None)

def test_starts_with_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.starts_with(None, "S")
    with pytest.raises(AttributeError):
        string_utils.starts_with("SkyPro", None)

def test_ends_with_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.ends_with(None, "o")
    with pytest.raises(AttributeError):
        string_utils.ends_with("SkyPro", None)

def test_is_empty_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.is_empty(None)

def test_list_to_string_with_non_list(string_utils):
    with pytest.raises(AttributeError):
        string_utils.list_to_string(None)

if __name__ == "__main__":
    pytest.main()
