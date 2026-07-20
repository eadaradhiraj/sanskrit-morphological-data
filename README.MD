# skt-morph (Sanskrit Morphological Engine)

`skt-morph` is a lightning-fast, offline Sanskrit morphological analyzer, generator, and reverse-lookup. It is built by scraping the highly accurate WebAssembly-generated morphological tables from [Ashtadhyayi.com](https://ashtadhyayi.com) and structuring them into an optimized local SQLite database.

## 🏗️ Architecture: JSON Transport -> SQLite Engine

To bypass GitHub file-size limits and ensure blazing-fast query speeds (under 1 millisecond), this package uses a unique two-step architecture:
1. **The Distribution:** The raw grammatical data is stored in the repository as thousands of tiny, human-readable `.json` files.
2. **The Compilation:** When a user installs and imports the package for the first time, it automatically reads the bundled JSON files and compiles them into a highly-indexed SQLite database (`skt_morphology.db`) in the user's home directory (`~/.skt_morph/`). 

This gives users the ease of a `pip install` with the speed of a local SQL database, using virtually 0MB of RAM.

## 🚀 Features
* **Comprehensive Scraping:** Automatically parses verbs (*tiṅanta*), participles (*kṛdanta*), *upasarga* combinations, and classical literature usages (*prayoga*) directly from the source.
* **Grammar Filtering:** Intelligently hides raw generative templates if they violate standard grammar rules (e.g., hiding *Ātmanepadam* participles if the verb + upasarga combination is strictly *Parasmaipadam*).
* **Avyaya Recognition:** Automatically identifies non-declining suffixes (`-tumun`, `-ktvā`, `-lyap`, etc.) and classifies them as *Avyayas* (indeclinables).
* **Universal Reverse-Stemmer:** An algorithmic engine that mathematically strips 21 *Sup* affixes across *a, i, u,* and *ṛ* paradigms (applying reverse-*ṇatva* rules) to identify the base stem of any declined noun or participle.
* **Dynamic Sandhi Stripper:** If a word with a sandhi-fused Upasarga (e.g., *vyākaroti* -> *vi + ā + karoti*) is searched and isn't explicitly in the database, the engine dynamically strips the sandhi, identifies the bare root, and seamlessly rebuilds the grammatical metadata.
* **Forward Subanta Generator:** Mathematically generates the full 24-case declension grids for *a, ā, i, ī, u, ṛ,* and *at* ending nouns/participles on the fly, correctly applying internal *ṇatva* (n -> ṇ) rules.
* **Foreign Word Fallback:** Gracefully parses modern or foreign names (e.g., *ṭrampeṇa* -> *ṭrampa*, *neharūṇām* -> *neharu*) by guessing the stem and case, even if no Pāṇinian root exists.
* **CLI Built-in:** Search for words directly from your terminal.
* **100% Test Coverage:** Core analyzer, generator, and sandhi logic are strictly tested against mathematical edge cases.

## 📦 Installation

You can install the package directly from this GitHub repository using pip:

```bash
pip install git+https://github.com/eadaradhiraj/sanskrit-morphological-data.git
```

## 💻 Usage

### 1. Python API
The engine will compile the database the first time you import it.

```python
import skt_morph
import json

# Reverse lookup for a conjugated verb
result = skt_morph.analyze("prakaroti")
print(json.dumps(result["verbs"], indent=2))

# Dynamic Sandhi Resolution
result = skt_morph.analyze("vyAkftena")
print(json.dumps(result["declensions"], indent=2))

# Forward Declension Generation (e.g. guru in masculine)
from skt_morph.generator import get_participle_declension
from skt_morph.declension import decline_noun

forms = decline_noun("guru", "masculine")
print(json.dumps(forms, indent=2))
```

### 2. Command Line Interface (CLI)
You can query the engine directly from your terminal using SLP1 transliteration.

```bash
# Search for a word
python -m skt_morph prakaroti

# Filter by grammatical type
python -m skt_morph kartum --participle
python -m skt_morph kftena --declension
```

## 🗺️ Future Roadmap
- [ ] **Consonant Stems (Halanta):** Expand the declension generator to support complex consonant-ending nouns (e.g. *rājan*, *vāc*, *gīr*).
- [ ] **Avyaya Database:** Integrate a static lookup list of common indeclinable particles and conjunctions (e.g., *ca*, *vā*, *api*).
- [ ] **PyPI Release:** Publish as an official pip package for easier installation (`pip install skt-morph`).

---
*Data sourced with gratitude from [Ashtadhyayi.com](https://ashtadhyayi.com).*