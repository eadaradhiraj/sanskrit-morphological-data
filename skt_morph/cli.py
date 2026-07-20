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
    
    args = parser.parse_args()
    results = analyze(args.word)
    filtered_results = {}
    
    show_all = not (args.verb or args.participle or args.declension or args.namadhatu)
    
    if show_all or args.verb: filtered_results["verbs"] = results.get("verbs", [])
    if show_all or args.participle: filtered_results["participles"] = results.get("participles", [])
    if show_all or args.declension: filtered_results["declensions"] = results.get("declensions", [])
    if show_all or args.namadhatu: filtered_results["namadhatus"] = results.get("namadhatus", [])

    print(json.dumps(filtered_results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
