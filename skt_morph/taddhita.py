import re

# Reverses Vṛddhi (first vowel lengthening)
def reverse_vriddhi(word):
    if not word: return word
    # If word starts with a vowel
    if word[0] == 'A': return 'a' + word[1:]
    if word[0] == 'E': return 'i' + word[1:] # Maps to i/I/e, we default to i
    if word[0] == 'O': return 'u' + word[1:] # Maps to u/U/o, we default to u
    
    # If word starts with a consonant, find the first vowel
    vowel_match = re.search(r'[aAiIuUfFeEoO]', word)
    if not vowel_match: return word
    
    idx = vowel_match.start()
    v = word[idx]
    
    new_v = v
    if v == 'A': new_v = 'a'
    elif v == 'E': new_v = 'i'
    elif v == 'O': new_v = 'u'
    elif v == 'ar': new_v = 'f'
    
    return word[:idx] + new_v + word[idx+1:]

TADDHITA_RULES = [
    # Patronymics (Apatya) requiring Vriddhi
    (r'i$', 'iY', 'a', True, "Descendant of "),           # dASaraTi -> daSaraTa
    (r'eya$', 'Qak', 'I', True, "Descendant of "),        # kOnteya -> kuntI
    (r'Aya[nR]a$', 'PaY', 'a', True, "Descendant of "),   # gArgyAyaRa -> gArgya
    (r'a$', 'aR', 'a', True, "Descendant/Relation of "),  # vAsudeva -> vasudeva
    
    # Abstract/State (Bhava) - No Vriddhi
    (r'tva$', 'tva', '', False, "State/nature of "),      # gurutva -> guru
    (r'tA$', 'tal', '', False, "State/nature of "),       # gurutA -> guru
    (r'mat$', 'matup', '', False, "Possessing "),         # DImat -> DI
    (r'vat$', 'vatup', '', False, "Possessing "),         # Bagavat -> Baga
    (r'in$', 'ini', '', False, "Possessing ")             # Danin -> Dana
]

def analyze_taddhita(word_slp1):
    results = []
    for pattern, pratyaya, fallback_vowel, apply_vriddhi, meaning in TADDHITA_RULES:
        if re.search(pattern, word_slp1):
            stem = re.sub(pattern, '', word_slp1)
            
            # Reconstruct the base word
            if apply_vriddhi:
                stem = reverse_vriddhi(stem)
                
            base_noun = stem + fallback_vowel
            
            # Clean up slight phonetic overlaps (e.g., if fallback adds 'a' but stem already ends in 'a')
            if base_noun.endswith('aa'): base_noun = base_noun[:-1]

            results.append({
                "type": "taddhita",
                "base_noun": base_noun,
                "pratyaya": pratyaya,
                "meaning_hint": meaning + base_noun
            })
    return results
