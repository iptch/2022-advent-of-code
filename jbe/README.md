# Advent of Code

## Building

To build the entire code base use:

```bash
cargo build --all
# for optimized code
cargo build --all --release
```

This will use incremental builds, hence caching sub-builds.

## Running

You can run the exercise of a specific day using its package name:

```bash
cargo run -p day1-1
# for optimized code
cargo run --release -p day1-1
```
