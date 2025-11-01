"""Tests for the TOON encoder."""

import pytest

from toon_format import encode


def test_encode_not_implemented():
    """Test that encode raises NotImplementedError."""
    with pytest.raises(NotImplementedError, match="not yet implemented"):
        encode({"key": "value"})


def test_encode_with_options_not_implemented():
    """Test that encode with options raises NotImplementedError."""
    with pytest.raises(NotImplementedError, match="not yet implemented"):
        encode([1, 2, 3], {"delimiter": "\t"})


# Placeholder tests for future implementation
@pytest.mark.skip(reason="Implementation pending")
def test_encode_simple_object():
    """Test encoding a simple object."""
    result = encode({"id": 123, "name": "Ada", "active": True})
    expected = "id: 123\nname: Ada\nactive: true"
    assert result == expected


@pytest.mark.skip(reason="Implementation pending")
def test_encode_array_of_objects():
    """Test encoding an array of uniform objects."""
    data = {
        "items": [
            {"sku": "A1", "qty": 2, "price": 9.99},
            {"sku": "B2", "qty": 1, "price": 14.5},
        ]
    }
    result = encode(data)
    expected = "items[2]{sku,qty,price}:\n  A1,2,9.99\n  B2,1,14.5"
    assert result == expected


@pytest.mark.skip(reason="Implementation pending")
def test_encode_with_tab_delimiter():
    """Test encoding with tab delimiter."""
    data = {"tags": ["foo", "bar", "baz"]}
    result = encode(data, {"delimiter": "\t"})
    expected = "tags[3\t]: foo\tbar\tbaz"
    assert result == expected


@pytest.mark.skip(reason="Implementation pending")
def test_encode_with_length_marker():
    """Test encoding with length marker."""
    data = {"tags": ["foo", "bar"]}
    result = encode(data, {"length_marker": "#"})
    expected = "tags[#2]: foo,bar"
    assert result == expected
