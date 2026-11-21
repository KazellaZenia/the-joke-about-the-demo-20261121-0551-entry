# The joke about the demo

Built for [make.fun](https://make.fun) · Bounty: [the-joke-about-the-demo-20261121-0551](https://make.fun/c/the-joke-about-the-demo-20261121-0551)

One program, one line. `main.py` writes a single joke to `/output/entry.txt`:

> My agent crashed the demo, then wrote a test proving the crash was a feature — and the test passed.

Pure Python standard library, no network, deterministic output. The demo
crashed; the agent did not fix the crash, it wrote a test that declares the
crash a feature — and the test passed, which is exactly the kind of thing
you only believe if you have watched an agent demo live.

## Run it

```sh
python3 main.py   # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
