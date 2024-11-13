# Rust commands
rust-version:
	echo "Rust command-line utility versions:"
	rustc --version              # Rust compiler
	cargo --version              # Rust package manager
	rustfmt --version            # Rust code formatter
	rustup --version             # Rust toolchain manager
	clippy-driver --version      # Rust linter

rust_install:
	cargo install --path ./sqlite

rust_format:
	cargo fmt --quiet --manifest-path ./sqlite/Cargo.toml

rust_lint:
	cargo clippy --quiet --manifest-path ./sqlite/Cargo.toml

rust_test:
	cargo test --quiet --manifest-path ./sqlite/Cargo.toml

rust_run:
	cd sqlite && cargo run --release


rust_build:
	cargo build --release --manifest-path ./sqlite/Cargo.toml

rust_release:
	cargo build --release --manifest-path ./sqlite/Cargo.toml

rust_all: rust_format rust_lint rust_test rust_run

# Python commands
python_install:
	pip install --upgrade pip
	pip install -r requirements.txt

python_format:
	black *.py

python_lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

python_test:
	python -m pytest --cov=main test.py


python_all: python_install python_format python_lint python_test

# Run all checks
check: python_all rust_all

