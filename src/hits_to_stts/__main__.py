"""Command-line validation of the bundled HiTS mapping."""

from importlib.resources import files

from . import map_tag, unknown_pos


def _read_tagset(filename: str) -> list[str]:
    resource = files("hits_to_stts").joinpath("data", filename)
    return resource.read_text(encoding="utf-8").splitlines()


def main() -> None:
    """Map the bundled HiTS tagset and compare it with the STTS tagset."""
    hits = _read_tagset("HiTS-tagset.txt")
    stts = set(_read_tagset("Tiger_v8_tagset.txt"))
    invalid_tags = set(map(map_tag, hits)) - stts

    print(invalid_tags)
    print("fehler: ", len(invalid_tags))
    print("Unknown POS list:", unknown_pos)


if __name__ == "__main__":
    main()
