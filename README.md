# HiTS to STTS Tagset Conversion

This project provides a script to convert HiTS (Historical Tagset) tags to STTS (Stuttgart-Tübingen Tagset) tags. The main script `hits_to_stts.py` reads input tags, applies the conversion rules, and outputs the mapped tags, highlighting any unknown tags encountered.

## Table of Contents
- [Project Overview](#project-overview)
- [File Descriptions](#file-descriptions)
- [Installation](#installation)
- [Usage](#usage)
- [Conversion Logic](#conversion-logic)
- [Future Work](#future-work)
- [License](#license)

## Project Overview
This project aims to facilitate the conversion of part-of-speech (POS) tags from the HiTS format, used for Middle High German texts, to the more modern STTS format. This is particularly useful for linguistic research and the development of language processing tools that need to work with historical texts.

## File Descriptions
- `HiTS-tagset.txt`: Contains the HiTS tags to be converted.
- `Tiger_v8_tagset.txt`: Contains the STTS tags for comparison and validation.
- `hits_to_stts.py`: The main script that handles the conversion of tags from HiTS to STTS.

## Installation
To run the script, you need Python installed on your system. Clone this repository and navigate to the project directory.

```bash
git clone https://github.com/yourusername/hits-to-stts.git
cd hits-to-stts
```

## Usage
Run the script using Python:

```bash
python hits_to_stts.py
```

The script reads the tags from `HiTS-tagset.txt`, applies the conversion rules, and outputs the mapped tags, along with any unknown tags encountered during the conversion.

## Conversion Logic
The script `hits_to_stts.py` implements a dictionary-based mapping of tags. Here’s a brief overview of the logic used:

1. **Dictionary Mapping**: A dictionary `hits_to_stts` is used to map HiTS tags to STTS tags.
2. **POS Extraction**: The function `get_pos` extracts the POS component from the tag.
3. **Conversion Function**: The function `convert` uses the dictionary to convert HiTS tags to STTS tags. If a tag is not found in the dictionary, it is added to the `unknown_pos` set.
4. **Tag Mapping**: The `map_tag` function handles more complex mappings, including handling multiple tag features and edge labels.

### Example of Tag Conversion
The tag `ADJN.Masc.Nom.Sg` in HiTS would be converted to `ADJA.Masc.Nom.Sg` in STTS based on the predefined rules in the dictionary.

## Future Work
- **Enhancements in Tagger**: Improve the accuracy of tagging historical texts by refining the tagger.
- **Expanding the Tag Mapping**: Address non-deterministic mappings and collisions more effectively.
- **Integration with Modern Parsers**: Explore further integration with modern parsing tools for better performance and accuracy.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
