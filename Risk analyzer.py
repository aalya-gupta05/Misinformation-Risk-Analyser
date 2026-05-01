"""
============================================================================
  Misinformation Risk Analyzer Rule-Based Text Credibility Assessment Module

============================================================================
"""

import re


# ──────────────────────────────────────────────
#  RULE DEFINITIONS
# ──────────────────────────────────────────────

# Indicator 1: Emotional manipulation words
EMOTIONAL_WORDS = [
    "shocking", "outrage", "terrifying", "disgusting",
    "horrifying", "explosive", "exposed", "breaking",
    "unbelievable", "scandalous", "alarming", "devastating"
]

# Indicator 2: Clickbait phrases
CLICKBAIT_PHRASES = [
    "you won't believe",
    "this will shock you",
    "share before it's deleted",
    "they don't want you to know",
    "watch before it's banned",
    "what they are hiding",
    "the truth they don't want",
    "must watch",
    "share now"
]

# Indicator 3: Vague / unsupported claim phrases
VAGUE_CLAIMS = [
    "sources say",
    "experts believe",
    "many people say",
    "insiders claim",
    "anonymous sources",
    "some say",
    "people are saying",
    "rumor has it",
    "word is that"
]

# Indicator 4: Strong claim words (that imply evidence but give none)
CLAIM_WORDS = [
    "proves", "confirmed", "leaked", "officially admitted",
    "undeniable proof", "caught on camera", "100% confirmed",
    "absolute truth"
]

# Indicator 5: Credibility signals (reduce suspicion if present)
CREDIBLE_SIGNALS = [
    "according to", "study by", "reported by", "published in",
    "source:", "cited by", "per ", "reuters", "bbc", "who",
    "university", "research shows", "data shows", "survey"
]


# ──────────────────────────────────────────────
#  CORE ANALYSIS FUNCTION
# ──────────────────────────────────────────────

def analyze_risk(text):
    """
    Analyzes the given text and returns:
      - score       : integer risk score
      - risk_level  : "LOW", "MEDIUM", or "HIGH"
      - indicators  : list of detected issues (strings)
    """
    score = 0
    indicators = []
    text_lower = text.lower()

    # --- Check 1: Emotional manipulation ---
    found_emotional = [w for w in EMOTIONAL_WORDS if w in text_lower]
    if found_emotional:
        score += 2
        indicators.append(
            "Emotional language detected: " + ", ".join(found_emotional)
        )

    # --- Check 2: Clickbait phrases ---
    found_clickbait = [p for p in CLICKBAIT_PHRASES if p in text_lower]
    if found_clickbait:
        score += 2
        indicators.append(
            "Clickbait phrase detected: " + "; ".join(found_clickbait)
        )

    # --- Check 3: Excessive punctuation (!!, ??) ---
    if re.search(r"[!?]{2,}", text):
        score += 1
        indicators.append(
            "Excessive punctuation found (!! or ??)"
        )

    # --- Check 4: No credible references ---
    has_credible = any(signal in text_lower for signal in CREDIBLE_SIGNALS)
    if not has_credible:
        score += 1
        indicators.append(
            "No credible source or reference found in text"
        )

    # --- Check 5: Vague / anonymous attribution ---
    found_vague = [p for p in VAGUE_CLAIMS if p in text_lower]
    if found_vague:
        score += 1
        indicators.append(
            "Vague attribution detected: " + "; ".join(found_vague)
        )

    # --- Check 6: Claim-evidence mismatch ---
    has_claim = any(w in text_lower for w in CLAIM_WORDS)
    has_evidence = any(w in text_lower for w in ["because", "data shows",
                                                   "study found", "evidence",
                                                   "research", "report"])
    if has_claim and not has_evidence:
        score += 2
        indicators.append(
            "Strong claim made but no supporting evidence provided"
        )

    # --- Determine risk level ---
    if score <= 2:
        risk_level = "LOW"
    elif score <= 5:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return score, risk_level, indicators


# ──────────────────────────────────────────────
#  DISPLAY FUNCTION
# ──────────────────────────────────────────────

def display_result(text, score, risk_level, indicators):
    """
    Prints the analysis result in a clean, formatted layout.
    """
    # Choose a label for context
    level_labels = {
        "LOW":    "Likely credible. No major red flags.",
        "MEDIUM": "Needs verification. Some suspicious signals.",
        "HIGH":   "Likely misleading. Multiple red flags detected."
    }
    verdict = level_labels[risk_level]

    print()
    print("=" * 50)
    print("          MISINFORMATION RISK ANALYSIS")
    print("=" * 50)
    print(f"  Input Text : {text[:60]}{'...' if len(text) > 60 else ''}")
    print("-" * 50)
    print(f"  Risk Score : {score} / 9")
    print(f"  Risk Level : {risk_level}")
    print(f"  Verdict    : {verdict}")
    print("-" * 50)

    if indicators:
        print("  Indicators Detected:")
        for item in indicators:
            print(f"    - {item}")
    else:
        print("  Indicators Detected: None")

    print("=" * 50)
    print()


# ──────────────────────────────────────────────
#  MAIN PROGRAM
# ──────────────────────────────────────────────

def main():
    print()
    print("=" * 50)
    print("   MISINFORMATION RISK ANALYZER v1.0")
    print("   Academic Project | Rule-Based Module")
    print("=" * 50)
    print("  Type your news text and press Enter.")
    print("  Type 'quit' to exit.")
    print("=" * 50)

    while True:
        print()
        user_input = input("  Enter news text: ").strip()

        if user_input.lower() == "quit":
            print("\n  Exiting analyzer. Goodbye!\n")
            break

        if not user_input:
            print("  [!] Please enter some text to analyze.")
            continue

        score, risk_level, indicators = analyze_risk(user_input)
        display_result(user_input, score, risk_level, indicators)


if __name__ == "__main__":
    main()
