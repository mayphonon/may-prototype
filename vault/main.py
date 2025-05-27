from vault.selector import select_phrase

dp = 2.3
emotion = 0.6

print("📤 Mayの出力候補：")
print(select_phrase(dp_level=dp, emotion_level=emotion))
