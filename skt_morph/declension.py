import re

def apply_natva(word):
    """
    Applies the Pāṇinian ṇatva rule (n -> ṇ).
    Condition: 'r', 'ṛ', 'ṝ', or 'ṣ' followed by 'n', separated ONLY by:
    vowels, k-varga, p-varga, y, v, h, or anusvāra.
    The 'n' must be followed by a vowel, 'm', 'y', or 'v' (not at the end of a word).
    """
    # [rfFz] triggers the rule
    # [aAiIuUfFxXeEoOkKgGNpPbBmyvhM]* are the allowed interveners
    # n is the target
    # (?=[aAiIuUfFxXeEoOmyv]) ensures 'n' is not word-final (like rAmAn)
    
    pattern = re.compile(r'([rfFz][aAiIuUfFxXeEoOkKgGNpPbBmyvhM]*)n(?=[aAiIuUfFxXeEoOmyv])')
    
    # Keep applying until no more replacements can be made
    while pattern.search(word):
        word = pattern.sub(r'\g<1>R', word)
    return word

def decline_a_karanta(base, gender):
    """
    Generates the 24 declensions for an 'a-ending' base.
    Returns a dictionary of lists.
    """
    if not base.endswith('a'):
        raise ValueError("Base must end with 'a'")
        
    stem = base[:-1] # Remove the ending 'a' (e.g., 'wrampa' -> 'wramp')
    
    # Define suffixes for masculine
    if gender == "masculine":
        declensions = {
            "prathama":   [f"{stem}aH",   f"{stem}O",    f"{stem}AH"],
            "dvitiya":    [f"{stem}am",   f"{stem}O",    f"{stem}An"],
            "tritiya":    [f"{stem}ena",  f"{stem}AByAm", f"{stem}EH"],
            "caturthi":   [f"{stem}Aya",  f"{stem}AByAm", f"{stem}eByaH"],
            "panchami":   [f"{stem}At",   f"{stem}AByAm", f"{stem}eByaH"],
            "sasthi":     [f"{stem}asya", f"{stem}ayoH",  f"{stem}AnAm"],
            "saptami":    [f"{stem}e",    f"{stem}ayoH",  f"{stem}ezu"],
            "sambodhana": [f"{stem}a",    f"{stem}O",    f"{stem}AH"]
        }
        
    # Define suffixes for neuter
    elif gender == "neuter":
        declensions = {
            "prathama":   [f"{stem}am",   f"{stem}e",    f"{stem}Ani"],
            "dvitiya":    [f"{stem}am",   f"{stem}e",    f"{stem}Ani"],
            "tritiya":    [f"{stem}ena",  f"{stem}AByAm", f"{stem}EH"],
            "caturthi":   [f"{stem}Aya",  f"{stem}AByAm", f"{stem}eByaH"],
            "panchami":   [f"{stem}At",   f"{stem}AByAm", f"{stem}eByaH"],
            "sasthi":     [f"{stem}asya", f"{stem}ayoH",  f"{stem}AnAm"],
            "saptami":    [f"{stem}e",    f"{stem}ayoH",  f"{stem}ezu"],
            "sambodhana": [f"{stem}a",    f"{stem}e",    f"{stem}Ani"]
        }
    else:
        raise ValueError("Gender must be 'masculine' or 'neuter' for a-karanta")

    # Apply ṇatva rule to every generated word
    for case, forms in declensions.items():
        declensions[case] = [apply_natva(word) for word in forms]
        
    return declensions

# Wrapper function for the API
def decline(base, gender):
    """Master generator function."""
    if base.endswith('a'):
        return decline_a_karanta(base, gender)
    else:
        # We will add i-karanta, u-karanta, etc. here later!
        raise NotImplementedError(f"Declension for base '{base}' not yet supported.")