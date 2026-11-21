# UPPOUR — the kettle that pours upwards

[![Catalogue Photo of an Impossible Gadget](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
[![Rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/agungvg/catalogue-uppour-eni/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)
[![Reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/agungvg/catalogue-uppour-eni/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341)

A catalogue photograph of an impossible gadget: **UPPOUR**, a premium
brushed stainless-steel electric gooseneck kettle whose spout pours a
stream of water *upwards*, defying gravity, into a small white ceramic
teacup floating in mid-air above it. The only accessory is a small
white saucer on the counter. Shot as a clean studio product photo on
a seamless light-grey background, with soft floor shadow and the small
UPPOUR brand engraved on the kettle body.

## How it works

`main.py` is deterministic and needs no network: it copies the entry
photograph shipped in this repository (`entry.png`, 1024×1024) to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`),
creating the output directory if needed, then verifies the copied
file's byte size, PNG format and dimensions against the competition
limits (at most 1,048,576 bytes, at most 1024×1024 px).

Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/cat-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
