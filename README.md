# TOON Format for Python

[![PyPI version](https://img.shields.io/pypi/v/toon-format.svg)](https://pypi.org/project/toon-format/)
[![Python versions](https://img.shields.io/pypi/pyversions/toon-format.svg)](https://pypi.org/project/toon-format/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

**Token-Oriented Object Notation** is a compact, human-readable serialization format designed for passing structured data to Large Language Models with significantly reduced token usage. It's intended for LLM input, not output.

> [!TIP]
> Think of TOON as a translation layer: use JSON programmatically, convert to TOON for LLM input.

## Status

🚧 **This package is currently a namespace reservation.** Full implementation coming soon!

### Example

**JSON** (verbose):

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

**TOON** (compact):

```toon
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

## Installation

Make sure [`uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) is installed. Then install the `toon-format` package:

```shell
uv pip install toon-format
# or
uv add toon-format  # adds to your pyproject.toml
```


## Future Usage

Once implemented, the package will provide:

```python
from toon_format import encode, decode

data = "id: 123" # your data structure
toon_string = encode(data)
decoded = decode(toon_string)

assert data == decoded
```

## Resources

- [TOON Specification](https://github.com/johannschopplich/toon/blob/main/SPEC.md)
- [Main Repository](https://github.com/johannschopplich/toon)
- [Benchmarks & Performance](https://github.com/johannschopplich/toon#benchmarks)
- [Other Language Implementations](https://github.com/johannschopplich/toon#other-implementations)


## Contributing

Interested in implementing TOON for Python? Check out the [specification](https://github.com/johannschopplich/toon/blob/main/SPEC.md) and feel free to contribute!

## License

MIT License © 2025-PRESENT [Johann Schopplich](https://github.com/johannschopplich)
