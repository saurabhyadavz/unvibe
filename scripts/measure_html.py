#!/usr/bin/env python3
"""Measure a standalone HTML page so an audit reports counts, not adjectives.

Usage: python3 scripts/measure_html.py page.html [other.html ...]
With two files it prints a before/after table. Pure standard library; reads only the files named.
"""
import re, sys, json, pathlib

GENERIC = {"sans-serif","serif","monospace","system-ui","ui-sans-serif","ui-serif","ui-monospace","-apple-system",
           "blinkmacsystemfont","segoe ui","roboto","helvetica neue","helvetica","arial","inherit","cursive","emoji",
           "apple color emoji","segoe ui emoji","segoe ui symbol","noto color emoji","times new roman","times",
           "courier new","courier","menlo","consolas","monaco","sfmono-regular","liberation mono","liberation sans","noto sans"}
STATE_WORDS = r"loading|skeleton|spinner|empty state|no data|nothing here|no results|first week|not found|try again|retry|offline|failed|error|stale|undo"
TECH = re.compile(r"\b(ai|a\.i\.|llm|gpt|engine|platform|revolutioni[sz]e|powered|machine learning)\b", re.I)
HYPE = re.compile(r"\b(supercharge|seamless|unlock|magic(al)?|game.?changing|revolutioni[sz]e|next.?gen|cutting.?edge|effortless)\b", re.I)

def measure(path):
    html = pathlib.Path(path).read_text(errors="replace"); low = html.lower()
    css = " ".join(re.findall(r"<style.*?</style>", html, flags=re.S | re.I)) + " " + " ".join(re.findall(r'style="([^"]*)"', html))
    cssl = css.lower()
    body = re.sub(r"<style.*?</style>|<script.*?</script>", "", html, flags=re.S | re.I)
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))
    fams = set()
    for m in re.finditer(r"font-family\s*:\s*([^;}\"]+)", cssl):
        for f in m.group(1).split(","):
            f = f.strip().strip("'\"")
            if f and f not in GENERIC and not f.startswith("var("): fams.add(f)
    for m in re.finditer(r"fonts\.googleapis\.com/css2?\?[^\"']*", low):
        for fm in re.findall(r"family=([^&:]+)", m.group(0)): fams.add(fm.replace("+", " ").lower())
    sizes = sorted(set(re.findall(r"font-size\s*:\s*([\d.]+(?:px|rem|em))", cssl)))
    weights = sorted(set(re.findall(r"font-weight\s*:\s*(\d{3})", cssl)))
    hexes = set(c.lower() for c in re.findall(r"#[0-9a-fA-F]{6}\b", css))
    grads = re.findall(r"linear-gradient\([^)]*\)", cssl)
    purple_blue = sum(1 for g in grads if re.search(r"#(6a11cb|7c3aed|8b5cf6|a855f7|9333ea|6d28d9|5b21b6|4c1d95|c084fc|7e22ce)", g) and re.search(r"#(2575fc|3b82f6|2563eb|1d4ed8|60a5fa|0ea5e9|06b6d4|38bdf8|1e40af|4f46e5|6366f1|818cf8)", g))
    gradient_text = len(re.findall(r"background-clip\s*:\s*text", cssl))
    dead = len(re.findall(r'href="#"', html)) + len(re.findall(r'href="javascript:void', html))
    anchors = len(re.findall(r"<a\b", html, flags=re.I)); buttons = len(re.findall(r"<button\b", html, flags=re.I))
    emoji = len(re.findall(r"[\U0001F300-\U0001FAFF☀-➿⭐✨]", body))
    upper_tracked = len(re.findall(r"text-transform\s*:\s*uppercase", cssl))
    glows = len(re.findall(r"box-shadow\s*:[^;]*rgba\(\s*(?:1[2-9]\d|2\d\d)\s*,\s*(?:[0-9]\d?|1[0-4]\d)\s*,\s*(?:2\d\d)", cssl))
    states = len(re.findall(STATE_WORDS, html, flags=re.I))
    h1 = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<h1\b[^>]*>(.*?)</h1>", html, flags=re.S | re.I)]
    arbitrary = sorted(set(v for v in re.findall(r"(?:margin|padding|gap|top|left|right|bottom)(?:-[a-z]+)?\s*:\s*(\d+)px", cssl) if int(v) % 4 != 0 and int(v) > 2))
    maxw = sorted(set(int(x) for x in re.findall(r"max-width\s*:\s*(\d+)px", cssl)))
    return {
        "file": str(path), "kb": round(len(html) / 1024, 1),
        "font_families": sorted(fams), "font_sizes": len(sizes), "font_weights": weights,
        "hex_colours": len(hexes), "gradients": len(grads), "purple_blue_gradients": purple_blue, "gradient_text": gradient_text,
        "glow_shadows": glows, "uppercase_tracked_rules": upper_tracked, "emoji_in_markup": emoji,
        "links": anchors, "buttons": buttons, "dead_links": dead,
        "state_mentions": states, "off_grid_spacing_values": arbitrary[:12],
        "max_widths_px": maxw, "h1": h1[:3],
        "h1_leads_with_tech": bool(h1) and bool(TECH.search(h1[0][:60])),
        "hype_words": len(HYPE.findall(text)), "exclamations_in_ui": text.count("!"),
        "viewport_meta": 'name="viewport"' in low, "media_queries": low.count("@media"),
    }

KEYS = ["font_families","font_sizes","font_weights","hex_colours","gradients","purple_blue_gradients","gradient_text","glow_shadows",
        "uppercase_tracked_rules","emoji_in_markup","dead_links","links","buttons","state_mentions","off_grid_spacing_values",
        "hype_words","exclamations_in_ui","h1","viewport_meta","media_queries"]

def fmt(v):
    if isinstance(v, list): return str(len(v)) + (" (" + ", ".join(map(str, v))[:60] + ")" if v and len(", ".join(map(str, v))) < 60 else "")
    return str(v)

if __name__ == "__main__":
    files = sys.argv[1:]
    if not files: print(__doc__); sys.exit(1)
    results = [measure(f) for f in files]
    if len(results) == 1: print(json.dumps(results[0], indent=2, ensure_ascii=False)); sys.exit(0)
    print("| measure | " + " | ".join(pathlib.Path(r["file"]).name for r in results) + " |")
    print("|---|" + "---|" * len(results))
    for k in KEYS: print(f"| {k} | " + " | ".join(fmt(r[k]) for r in results) + " |")
