[![Python CI/CD](https://github.com/ailina-aniwan/Ailina_Aniwan_Mini_Project_8/actions/workflows/python.yml/badge.svg)](https://github.com/ailina-aniwan/Ailina_Aniwan_Mini_Project_8/actions/workflows/python.yml) [![Rust CI/CD](https://github.com/ailina-aniwan/Ailina_Aniwan_Mini_Project_8/actions/workflows/rust.yml/badge.svg)](https://github.com/ailina-aniwan/Ailina_Aniwan_Mini_Project_8/actions/workflows/rust.yml)
# IDS706 - Mini Project 8 - Ailina Aniwan

## Rewrite a Python Script in Rust

## ✔️ Project Overview
This project aims to compare the performance of data processing scripts written in Python and Rust. The goal is to rewrite an existing Python script in Rust and demonstrate improvements in execution speed and memory usage. This comparison highlights the efficiency of Rust over Python in handling data-intensive tasks, providing insights into potential benefits when using Rust for similar workloads.

## ✔️ Project Requirements
- **Rewrite Python Script in Rust**: Convert an existing Python data processing script to Rust.
- **Highlight Performance Improvements**: Identify improvements in speed and memory usage when using Rust.

## ✔️ Findings

### Performance Comparison

| Metric            | Python                | Rust                  |
|-------------------|-----------------------|-----------------------|
| Execution Time    | 0.85 ms               | 0.25 ms               |
| Memory Usage      | 52368 KB              | 16384 KB              |
| Average Age       | 49.23                 | 49.23                 |


### Analysis

- **Execution Time**: Rust completes the task faster (0.25 ms) than Python (0.85 ms), showing greater efficiency in handling CPU-intensive operations.
- **Memory Usage**: Rust uses less memory (16,384 KB) than Python (52,368 KB), making it more suitable for resource-constrained environments.
- **Accuracy**: Both implementations produce the same average age (49.23), ensuring that the data processing logic is consistent across languages.
