# shelby-storage-benchmark
Benchmark and stress testing tools for Shelby decentralized storage using the Shelby CLI.
# Shelby Storage Benchmark

This repository benchmarks decentralized storage performance using the Shelby CLI.

The goal is to evaluate Shelby's capability for high-throughput data workloads such as AI datasets, media streaming, and large blob retrieval.

## Features

* automated file generation
* CLI upload/download benchmarks
* stress testing with concurrent uploads
* performance visualization
* CI-based reproducible benchmarks

## Installation

Install Shelby CLI

npm install -g @shelby-protocol/cli

Clone repo

git clone https://github.com/username/shelby-storage-benchmark

Generate files

python benchmark/file_generator.py

Run benchmark

python benchmark/benchmark.py

Run stress test

python benchmark/stress_test.py

## Output

Results are saved in:

results/benchmark_results.csv

## Goal

The goal is to explore the performance characteristics of Shelby decentralized storage and contribute benchmarking tools for the developer ecosystem.
