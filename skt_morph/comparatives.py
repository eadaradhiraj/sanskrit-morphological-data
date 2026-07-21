import re

COMPARATIVE_RULES = [
    (r'tara$', 'tarap', 'Comparative'),
    (r'tama$', 'tamap', 'Superlative'),
]

IRREGULAR_MAP = {
    "SrezWa": {"base": "praSasya", "pratyaya": "izWan", "degree": "Superlative"},
    "Sreyas": {"base": "praSasya", "pratyaya": "Iyasun", "degree": "Comparative"},
    "garizWa": {"base": "guru", "pratyaya": "izWan", "degree": "Superlative"},
    "garIyas": {"base": "guru", "pratyaya": "Iyasun", "degree": "Comparative"},
    "pApIyas": {"base": "pApa", "pratyaya": "Iyasun", "degree": "Comparative"},
    "pApizWa": {"base": "pApa", "pratyaya": "izWan", "degree": "Superlative"},
    "jyezWa": {"base": "vfdDa", "pratyaya": "izWan", "degree": "Superlative"},
    "jyAyas": {"base": "vfdDa", "pratyaya": "Iyasun", "degree": "Comparative"},
    "kanizWa": {"base": "alpa", "pratyaya": "izWan", "degree": "Superlative"},
    "kanIyas": {"base": "alpa", "pratyaya": "Iyasun", "degree": "Comparative"},
    "nedizWa": {"base": "antika", "pratyaya": "izWan", "degree": "Superlative"},
    "nedIyas": {"base": "antika", "pratyaya": "Iyasun", "degree": "Comparative"},
    "sADIyas": {"base": "sADu", "pratyaya": "Iyasun", "degree": "Comparative"},
    "sADizWa": {"base": "sADu", "pratyaya": "izWan", "degree": "Superlative"},
}

def analyze_comparative(word_slp1):
    results = []
    if word_slp1 in IRREGULAR_MAP:
        data = IRREGULAR_MAP[word_slp1]
        results.append({"type": "comparative", "base_adjective": data["base"], "pratyaya": data["pratyaya"], "degree": data["degree"]})
    else:
        for pattern, pratyaya, degree in COMPARATIVE_RULES:
            if re.search(pattern, word_slp1):
                base_adj = re.sub(pattern, '', word_slp1)
                results.append({"type": "comparative", "base_adjective": base_adj, "pratyaya": pratyaya, "degree": degree})
    return results
