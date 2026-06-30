#!/usr/bin/env python3
"""Guards atrophy's core privacy promise: zero network. Run: python3 tests/test_no_network.py

The tool reads local transcripts and must never phone home. This fails if a
network-capable import sneaks into the sources — enforcing in CI what the README
and atrophy.py header only state in prose.
"""
import os, re, sys, traceback

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# Sources that must stay offline. The --llm path uses a local gguf, also offline.
SOURCES = ["atrophy.py", "atrophy_llm.py"]
# Modules that can open a socket / fetch a URL. socketserver/asyncio excluded:
# not used here, add only if a real local-only need appears.
FORBIDDEN = ["socket", "urllib", "http", "ftplib", "smtplib", "telnetlib",
             "requests", "httpx", "aiohttp", "websocket", "ssl"]
IMPORT_RE = re.compile(r"^\s*(?:import|from)\s+([a-zA-Z0-9_.]+)", re.M)


def test_no_network_imports():
    for src in SOURCES:
        path = os.path.join(ROOT, src)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            mods = [m.split(".")[0] for m in IMPORT_RE.findall(f.read())]
        hits = sorted(set(mods) & set(FORBIDDEN))
        assert not hits, f"{src} imports network module(s): {hits} — atrophy must stay offline"


def _run():
    tests = [(n, v) for n, v in sorted(globals().items())
             if n.startswith("test_") and callable(v)]
    fails = 0
    for name, fn in tests:
        try:
            fn(); print(f"PASS {name}")
        except Exception as e:
            fails += 1
            print(f"FAIL {name}: {e}")
            traceback.print_exc()
    print(f"\n{len(tests)-fails}/{len(tests)} passed")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    _run()
