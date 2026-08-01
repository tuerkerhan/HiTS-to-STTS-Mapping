# HiTS to STTS Tagset Conversion

> [!NOTE]
> This repository is a fork of
> [tuerkerhan/HiTS-to-STTS-Mapping](https://github.com/tuerkerhan/HiTS-to-STTS-Mapping).

Convert HiTS (Historical Tagset) part-of-speech tags to STTS
(Stuttgart-Tuebingen Tagset) tags. The project requires Python 3.13 or newer
and uses [uv](https://docs.astral.sh/uv/) for project and package management.

## Development

Clone the repository and create the locked development environment:

```bash
uv sync
```

Run the tests:

```bash
uv run python -m unittest discover -s tests
```

## Library usage

Install the project from a local checkout:

```bash
uv add --editable ../HiTS-to-STTS-Mapping
```

It can then be imported like any other dependency:

```python
from hits_to_stts import map_tag

mapped_tag = map_tag("ADJN.Masc.Nom.Sg")
assert mapped_tag == "ADJA.Nom.Sg.Masc"
```

To build installable source and wheel distributions:

```bash
uv build
```

The artifacts are written to `dist/`.

## CLI usage

The bundled HiTS tagset can be mapped and checked against the bundled STTS
tagset with:

```bash
uv run hits-to-stts
```

Unknown tags and mapped tags that are absent from the STTS tagset are printed.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
