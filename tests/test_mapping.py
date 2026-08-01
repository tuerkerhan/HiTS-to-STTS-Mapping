import unittest

from hits_to_stts import get_pos, map_tag


class MappingTests(unittest.TestCase):
    def test_get_pos(self) -> None:
        self.assertEqual(get_pos("ADJN.Masc.Nom.Sg"), "ADJN")

    def test_maps_adjective_features(self) -> None:
        self.assertEqual(map_tag("ADJN.Masc.Nom.Sg"), "ADJA.Nom.Sg.Masc")

    def test_maps_accusative_pronoun_features(self) -> None:
        self.assertEqual(map_tag("PPER.Masc.Akk.Sg.3"), "PPER.3.Acc.Sg.Masc")

    def test_preserves_unknown_tag(self) -> None:
        self.assertEqual(map_tag("UNKNOWN.Value"), "UNKNOWN.Value")


if __name__ == "__main__":
    unittest.main()
