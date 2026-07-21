Here is the pure Markdown for your `README.md`. You can copy and paste this directly into the file.

***

# skt-morph (Sanskrit Morphological Engine)

`skt-morph` is a lightning-fast, offline Sanskrit morphological analyzer, generator, and reverse-lookup dictionary. It combines highly accurate scraped data from [Ashtadhyayi.com](https://ashtadhyayi.com) with a powerful mathematical stemming engine to dynamically parse classical Sanskrit words.

## 🏗️ Architecture: JSON Transport -> SQLite Engine

To ensure blazing-fast query speeds (under 1 millisecond) with near-zero RAM usage, this package uses a unique two-step architecture:
1. **The Distribution:** The raw generative data is stored as thousands of tiny `.json` files.
2. **The Compilation:** On first import, it compiles the bundled JSON files into a highly-indexed SQLite database (`skt_morphology.db`) in the user's home directory (`~/.skt_morph/`).

## 🚀 Features
* **Comprehensive Root Scraping:** Parses verbs (*tiṅanta*), participles (*kṛdanta*), and classical usages directly from Pāṇinian generative tables.
* **Universal Reverse-Stemmer (Ajanta & Halanta):** Mathematically strips 21 *Sup* affixes across *a, i, u, ṛ* vowel paradigms, as well as complex **consonant stems** (*-an, -in, -as, -t, -c, -j*), applying reverse-*ṇatva* rules.
* **Dynamic Sandhi Stripper:** If a word with a sandhi-fused prefix (e.g., *vyākaroti* -> *vi + ā + karoti*) isn't explicitly in the database, the engine dynamically strips the sandhi, identifies the bare root, and seamlessly rebuilds the metadata.
* **Secondary Derivatives (Taddhita):** Algorithmically parses patronymics by executing **reverse-vṛddhi** (*vāsudeva* -> *vasudeva*) and abstract nouns (*gurutva* -> *guru*).
* **Denominative Verbs (Nāmadhātu):** Identifies nouns acting as verbs (e.g., *putrīyati* -> *putra* + *kyac*).
* **Pronouns (Sarvanāma):** Built-in support for highly irregular, hyper-common pronouns (*tad, kim, asmad, yuṣmad*).
* **Forward Subanta Generator:** Mathematically generates full 24-case declension grids on the fly for both vowel and consonant ending nouns/participles.
* **100% Test Coverage:** Core analyzer, generator, sandhi, vṛddhi, and ṇatva logic are strictly tested against mathematical edge cases.

## 💻 Usage

### 1. Python API
The engine will compile the database the first time you import it.

```python
import skt_morph
import json

# Master Analyzer (Handles verbs, nouns, taddhitas, namadhatus, and pronouns)
result = skt_morph.analyze("vAsudevam")
print(json.dumps(result, indent=2))

# Forward Declension Generation (e.g., Consonant stem 'manas' in neuter)
from skt_morph.declension import decline_noun
forms = decline_noun("manas", "neuter")
print(json.dumps(forms, indent=2))
```

### 2. Command Line Interface (CLI)
You can query the engine directly from your terminal using SLP1 transliteration. Use flags to filter the massive JSON output.

```bash
# Search for a word (shows everything)
python -m skt_morph prakaroti

# Filter by grammatical category
python -m skt_morph kartum --participle
python -m skt_morph rAjAnam --declension
python -m skt_morph kOnteya --taddhita
python -m skt_morph putrIyati --namadhatu
python -m skt_morph tasmE --pronoun
```