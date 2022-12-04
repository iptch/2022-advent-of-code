# Advent of Code

## Building

> This will require at least Rust version `1.67.0-nightly` to compile. It uses experimental iterator
> functions.

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
