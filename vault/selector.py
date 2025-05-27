import json
import random

def load_vault(path="vault/yure_phrase_vault.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def select_phrase(dp_level, emotion_level, phase=None):
    vault = load_vault()
    filtered = [
        p for p in vault
        if abs(p["dp"] - dp_level) <= 0.5
        and p["emotion_weight"] <= emotion_level
        and (phase is None or p["phase"] == phase)
    ]
    return random.choice(filtered)["text"] if filtered else "（詩的構文を見つけられなかった）"
