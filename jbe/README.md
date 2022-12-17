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

## Testing

All exercises implement a test against the sample input given in the question, and the actual input
that was given to me. These can be launched:

```bash
cargo test
# test only a specific day
cargo test -p day10-1
```

## Running

You can run the exercise of a specific day using its package name:

```bash
cargo run -p day1-1
# for optimized code
cargo run --release -p day1-1
```
