def parse_resume(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    return {"summary": text[:500]}  # Basic parser for now
