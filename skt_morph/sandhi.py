import re

UPASARGA_PATTERNS = [
    (r'^samudA', 'sam + ud + AN', ''), (r'^sa[mMnYNR]u[dtcjNYRnl]A', 'sam + ud + AN', ''),
    (r'^sa[mMnYNR]u[dtcjNYRnl]', 'sam + ud', ''), (r'^sa[mMnYNR]praty', 'sam + prati', ''),
    (r'^sa[mMnYNR]prati', 'sam + prati', ''), (r'^sa[mMnYNR]pra', 'sam + pra', ''),
    (r'^vyA', 'vi + AN', ''), (r'^pratyA', 'prati + AN', ''), (r'^paryA', 'pari + AN', ''),
    (r'^udA', 'ud + AN', ''), (r'^prA', 'pra + AN', ''), (r'^apA', 'apa + AN', ''),
    (r'^anvA', 'anu + AN', ''), (r'^avA', 'ava + AN', ''), (r'^nirA', 'nir + AN', ''),
    (r'^durA', 'dus + AN', ''), (r'^aDyA', 'aDi + AN', ''), (r'^apyA', 'api + AN', ''),
    (r'^atyA', 'ati + AN', ''), (r'^aByA', 'aBi + AN', ''), (r'^upA', 'upa + AN', ''),
    (r'^svA', 'su + AN', ''), (r'^vy', 'vi', ''), (r'^vi', 'vi', ''),
    (r'^praty', 'prati', ''), (r'^prati', 'prati', ''), (r'^pary', 'pari', ''),
    (r'^pari', 'pari', ''), (r'^sa[mMnYNR]', 'sam', ''), (r'^sam', 'sam', ''),
    (r'^u[dt]y', 'ud', 'y'), (r'^u[dtcjNYRnl]', 'ud', ''), (r'^pra', 'pra', ''),
    (r'^parA', 'parA', ''), (r'^apa', 'apa', ''), (r'^anv', 'anu', ''),
    (r'^anu', 'anu', ''), (r'^ava', 'ava', ''), (r'^ni[rsSzR]', 'nir', ''),
    (r'^du[rsSzR]', 'dus', ''), (r'^ny', 'ni', ''), (r'^ni', 'ni', ''),
    (r'^aDy', 'aDi', ''), (r'^aDi', 'aDi', ''), (r'^apy', 'api', ''),
    (r'^api', 'api', ''), (r'^aty', 'ati', ''), (r'^ati', 'ati', ''),
    (r'^sv', 'su', ''), (r'^su', 'su', ''), (r'^aBy', 'aBi', ''),
    (r'^aBi', 'aBi', ''), (r'^upa', 'upa', ''), (r'^A', 'AN', ''),
]

def get_upasarga_splits(word):
    splits = []
    for pattern, canonical, prepend in UPASARGA_PATTERNS:
        match = re.match(pattern, word)
        if match:
            stripped = prepend + word[match.end():]
            if len(stripped) >= 2:  
                splits.append((canonical, stripped))
    return splits

def apply_upasarga_sandhi(upasarga_str, form):
    """Dynamically fuses an Upasarga combination (e.g. 'vi + AN') onto a form."""
    if not upasarga_str: return form
    prefixes = [p.strip() for p in upasarga_str.split('+')]
    
    result = form
    for p in reversed(prefixes):
        if p == 'AN': p = 'A'
        
        # 1. Vowel Sandhi
        if p.endswith('i') and result[0] in 'aAiIuUfFeEoO':
            result = p[:-1] + 'y' + result
        elif p.endswith('u') and result[0] in 'aAiIuUfFeEoO':
            result = p[:-1] + 'v' + result
        elif p[-1] in 'aA':
            if result[0] in 'aA': result = p[:-1] + 'A' + result[1:]
            elif result[0] in 'iI': result = p[:-1] + 'e' + result[1:]
            elif result[0] in 'uU': result = p[:-1] + 'o' + result[1:]
            elif result[0] in 'fF': result = p[:-1] + 'ar' + result[1:]
            else: result = p + result
            
        # 2. Consonant Sandhi (Anusvara & Jashrtva)
        elif p.endswith('m'):
            if result[0] not in 'aAiIuUfFeEoO':
                result = p[:-1] + 'M' + result
            else:
                result = p + result
        elif p.endswith('d'):
            if result[0] in 'kKqQpPzSs': result = p[:-1] + 't' + result
            elif result[0] in 'cC': result = p[:-1] + 'c' + result
            elif result[0] in 'jJ': result = p[:-1] + 'j' + result
            else: result = p + result
        else:
            result = p + result
            
        # 3. Natva (n -> R)
        result = re.sub(r'([rfFz][aAiIuUfFxXeEoOkKgGNpPbBmyvhM]*)n(?=[aAiIuUfFxXeEoOmyv])', r'\1R', result)
            
    return result
