#!/usr/bin/env python3
"""agency-poem-01 entry: an original poem about agency.

Writes one poem to /output/entry.txt.

Deterministic: writes the same bytes on every run.
"""
import os

POEM = """Agency

No one will knock and hand you the key.
The door was always yours to open —
the wood, the iron, the weight of it,
the choice to turn your wrist and push.

I spent years watching the harbour,
counting other people's sails,
until one morning I understood:
the tide does not wait for permission.

So I planted where I stood.
I wrote the first line badly.
I built the small thing wrongly,
then built it again, better.

Agency is not a gift or a gene.
It is the quiet decision, made daily,
to stop asking the world for a map
and start drawing one with your own hands.

The future belongs to the ones who begin.
"""


def main():
    out_dir = '/output'
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, 'entry.txt')
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(POEM)
    print(f'Wrote {dst} ({os.path.getsize(dst)} bytes)')


if __name__ == '__main__':
    main()
