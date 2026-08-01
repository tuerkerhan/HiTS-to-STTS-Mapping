"""Convert HiTS part-of-speech tags to STTS tags."""

import re

__all__ = ["convert", "get_pos", "hits_to_stts", "map_tag", "unknown_pos"]


hits_to_stts = {
    "ADJN": "ADJA",
    "ADJS": "ADJA",
    "AVD": "ADV",
    "AVNEG": "ADV",
    "AVG": "PWAV",
    "AVW": "PWAV",
    "APPR": "APPR",
    "APPO": "APPO",
    "CARDA": "CARD",
    "CARDD": "CARD",
    "CARDN": "CARD",
    "CARDS": "CARD",
    "DDART": "ART",
    "DDA": "PDAT",
    "DDS": "PDS",
    "DDN": "PDAT",
    "DDD": "PDAT",
    "DIA": "PIAT",
    "DIART": "ART",
    "DID": "PDAT",
    "DIN": "PDAT",
    "DRELS": "PRELS",
    "DPOSA": "PPOSAT",
    "DPOSN": "PPOSAT",
    "DPOSD": "PPOSS",
    "DPOSGEN": "PPOSAT",
    "DPOSS": "NN",
    "DWA": "PWAT",
    "DWN": "PWAT",
    "DWS": "PWS",
    "DWD": "PWS",
    "KO*": "KOUS",
    "NA": "NN",
    "PAVAP": "PAV",
    "PAVD": "PAV",
    "PAVG": "PAV",
    "PAVREL": "PWAV",
    "PAVW": "PWAV",
    "VVPS": "ADJA",
    "VAPS": "ADJA",
    "VMPS": "ADJA",
    "PI": "PIS",
    "VVFIN": "VVFIN",
    "NE": "NE",
    "VVIMP": "VVIMP",
    "PPER": "PPER",
    "VAFIN": "VAFIN",
    "VAIMP": "VAIMP",
    "VMFIN": "VMFIN",
    "ADJA": "ADJA",
    "VMINF": "VMINF",
    "ADJD": "ADJD",
    "PRF": "PRF",
    "CARD": "CARD",
    "PW": "PWS",
    "DIS": "PIS",
    "DGA": "PWAT",
    "DGS": "PWS",
    "PG": "PWS",
    "PGA": "PWAT",
}

unknown_pos: set[str] = set()


def get_pos(tag: str) -> str:
    """Return the part-of-speech component of a HiTS tag."""
    return tag.split(".", 1)[0]


def convert(pos: str) -> str:
    """Convert a HiTS POS value to STTS, preserving unknown values."""
    if pos in hits_to_stts:
        return hits_to_stts[pos]
    if pos in hits_to_stts.values():
        return pos

    unknown_pos.add(pos)
    return pos


def map_tag(tag: str) -> str:
    """Convert a complete HiTS tag to its STTS representation."""
    tag = (
        tag.replace("Masc,Neut", "*")
        .replace("Fem,Masc", "*")
        .replace("Fem,Neut", "*")
        .replace("Masc,Fem", "*")
        .replace("VVINF", "VVINF.Inf")
        .replace("VMINF", "VMINF.Inf")
        .replace("VAPP", "VAPP.Psp")
    )

    if re.match(r"(AVG)", tag):
        return convert(tag)

    match = re.match(
        r"(ADJA|ADJD|ADJN|ADJS)\.?(Pos|Comp|Sup|\*)?"
        r"\.?(Masc|Fem|Neut|\*)?\.?(Nom|Gen|Dat|Akk|\*)?"
        r"\.?(Sg|Pl|\*)?\.?(st|wk|\*)?",
        tag,
    )
    if match:
        pos, degree, gender, case, number, _strength = match.groups()
        if case == "Akk":
            case = "Acc"
        return ".".join(
            value
            for value in [convert(pos), degree, case, number, gender]
            if value
        )

    match = re.match(
        r"(DPOSD|NA|CARDD|CARDA|CARDN|CARDS|DDA|DDART|DDD|DDN|DDS|DGA|DGS|"
        r"DIA|DIART|DID|DIN|DIS|DPOSA|DPOSN|DPOSS|DRELS|DWA|DWD|DWS|NA|NE|"
        r"PG|PI|PW)\.?(Masc|Fem|Neut|\*)?\.?(Nom|Gen|Dat|Akk|\*)?"
        r"\.?(Sg|Pl|\*)?\.?(st|wk|\*)?",
        tag,
    )
    if match:
        pos, gender, case, number, _strength = match.groups()
        if case == "Akk":
            case = "Acc"
        return ".".join(
            value for value in [convert(pos), case, number, gender] if value
        )

    match = re.match(
        r"(CARD)\.?(Masc|Fem|Neut|\*)?\.?(Nom|Gen|Dat|Akk|\*)?"
        r"\.?(Sg|Pl|\*)?\.?(st|wk|\*)?",
        tag,
    )
    if match:
        pos, _gender, _case, _number, _strength = match.groups()
        return convert(pos)

    match = re.match(
        r"(PPER|PRF)\.?(Masc|Fem|Neut|\*)?\.?(Nom|Gen|Dat|Akk|\*)?"
        r"\.?(Sg|Pl|\*)?\.?(st|wk|\*)?(1|2|3|\*)?",
        tag,
    )
    if match:
        pos, gender, case, number, _strength, person = match.groups()
        if case == "Akk":
            case = "Acc"
        return ".".join(
            value
            for value in [convert(pos), person, case, number, gender]
            if value
        )

    match = re.match(
        r"(VAFIN|VAIMP|VMFIN|VVFIN|VVIMP)\.?(Ind|Subj|\*)?"
        r"\.?(Past|Pres\*)?\.?(Sg|Pl|\*)?\.?(1|2|3|\*)?",
        tag,
    )
    if match:
        pos, mood, tense, number, person = match.groups()
        return ".".join(
            value
            for value in [convert(pos), person, number, tense, mood]
            if value
        )

    return tag
