import argparse
import json
from .analyzer import analyze

def main():
    parser = argparse.ArgumentParser(description="Sanskrit Morphological Engine & Reverse-Lookup")
    parser.add_argument("word", help="The word to search for (in SLP1 transliteration)")
    parser.add_argument("--verb", action="store_true", help="Only show verbal conjugations (Tiṅanta)")
    parser.add_argument("--participle", action="store_true", help="Only show uninflected participle bases")
    parser.add_argument("--declension", action="store_true", help="Only show declined nouns/adjectives (Subanta)")
    parser.add_argument("--namadhatu", action="store_true", help="Only show denominative verbs (Nāmadhātu)")
    parser.add_argument("--pronoun", action="store_true", help="Only show pronouns (Sarvanāma)")
    parser.add_argument("--taddhita", action="store_true", help="Only show secondary derivatives (Taddhita)")
    parser.add_argument("--numeral", action="store_true", help="Only show numerals (Saṃkhyā)")
    parser.add_argument("--comparative", action="store_true", help="Only show comparative/superlative degrees")
    parser.add_argument("--irregular", action="store_true", help="Only show highly irregular nouns")
    
    args = parser.parse_args()
    results = analyze(args.word)
    filtered_results = {}
    
    show_all = not any([args.verb, args.participle, args.declension, args.namadhatu, args.pronoun, args.taddhita, args.numeral, args.comparative, args.irregular])
    
    if show_all or args.verb: filtered_results["verbs"] = results.get("verbs", [])
    if show_all or args.participle: filtered_results["participles"] = results.get("participles", [])
    if show_all or args.declension: filtered_results["declensions"] = results.get("declensions", [])
    if show_all or args.namadhatu: filtered_results["namadhatus"] = results.get("namadhatus", [])
    if show_all or args.pronoun: filtered_results["pronouns"] = results.get("pronouns", [])
    if show_all or args.taddhita: filtered_results["taddhitas"] = results.get("taddhitas", [])
    if show_all or args.numeral: filtered_results["numerals"] = results.get("numerals", [])
    if show_all or args.comparative: filtered_results["comparatives"] = results.get("comparatives", [])
    if show_all or args.irregular: filtered_results["irregulars"] = results.get("irregulars", [])

    print(json.dumps(filtered_results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
