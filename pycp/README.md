# PyCP

PyCP is a python library for competitive programming, 
developed by Rodrigo Llanes for the [Advent of code](https://adventofcode.com) contest.

This library contains commonly used data structures and algorithms, and also basic input reading and parsing for 
the AOC.

### Features:
- [Heap](./pycp/structures/heap.py): wrapper for the heapq python built-in module.
- [Point](./pycp/structures/point.py): basic N dimensional point class.
- [Grid](./pycp/structures/grid.py): basic grid class, indexable with `Point`.
- [cache](./pycp/cache.py): custom cache function, with key arguments selection.
- [aoc](./pycp/aoc.py): automatic AOC input downloading and reading.
