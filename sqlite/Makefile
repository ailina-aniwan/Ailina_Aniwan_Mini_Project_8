# Rust commands
rust-version:
	echo "Rust command-line utility versions:"
	rustc --version              # Rust compiler
	cargo --version              # Rust package manager
	rustfmt --version            # Rust code formatter
	rustup --version             # Rust toolchain manager
	clippy-driver --version      # Rust linter

rust_install:
	cargo install --path .

rust_format:
	cargo fmt --quiet

rust_lint:
	cargo clippy --quiet

rust_test:
	cargo test --quiet

rust_run:
	cargo run

rust_build:
	cargo build --release

rust_release:
	cargo build --release

rust_all: format lint test run

# Python commands
python_install:
	pip install --upgrade pip
	pip install -r requirements.txt

python_format:
	black *.py

python_lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

python_test:
	python -m pytest --cov=main test_main.py

python_all: python_install python_format python_lint python_test