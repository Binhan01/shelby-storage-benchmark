# Shelby Storage Benchmark

Benchmarking and stress testing tools for the Shelby decentralized storage network using the Shelby CLI.

## Overview

This project provides experimental benchmarking tools designed to evaluate performance characteristics of Shelby storage such as:

- upload throughput
- download latency
- concurrent read performance
- storage reliability under stress workloads

The goal is to explore how Shelby performs in real-world data-intensive applications.

## Repository Structure

shelby-storage-benchmark
│
├── benchmark
│   ├── benchmark.py
│   ├── stress_test.py
│   └── shelby_cli_auto_benchmark.py
│
├── dashboard
│   └── plot_results.py
│
├── results
│
└── README.md


#
## Benchmark Features

### Upload Benchmark
Measures time required to upload files and calculates throughput.

### Download Benchmark
Tests retrieval speed and latency from the Shelby storage network.

### Stress Testing
Simulates multiple concurrent operations to test performance under load.

### Result Visualization
Benchmark results can be visualized using the dashboard scripts.

## Example Use Case

Possible workloads tested with this project include:

- AI dataset storage
- large file distribution
- media streaming workloads
- decentralized data hosting

## Quick Start

Follow these steps to quickly run the benchmark.

### 1. Install Shelby CLI
Make sure the Shelby CLI is installed and configured on your machine.

### 2. Clone this repository

```bash
git clone https://github.com/Binhan01/shelby-storage-benchmark.git
cd shelby-storage-benchmark