# stem-demo: Audio Stem Separation CLI Tool

A quick demo CLI application showcasing how to build sleek command-line tools using **Click** and **Rich** in Python.

## Overview

This project demonstrates best practices for building modern CLI applications with:
- **Click**: Elegant command-line interface framework
- **Rich**: Beautiful terminal formatting, progress bars, and styled output
- Clean project structure with separation of concerns
- Type hints and comprehensive documentation
- Progress tracking for long-running operations

## Features

- Audio file stem separation (simulated for demo)
- Beautiful terminal output with colors and formatting
- Real-time progress bars with time estimates
- Comprehensive error handling and validation
- Rich help text and documentation
- Modular, maintainable code structure

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Quick Install

```bash
# Clone or navigate to the project directory
cd ai_stem_cli_research

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Usage

### Basic Usage

```bash
# Show help
stem-demo --help

# Show separate command help
stem-demo separate --help

# Process an audio file
stem-demo separate song.mp3

# Process with verbose output
stem-demo separate song.mp3 --verbose

# Specify output directory
stem-demo separate song.mp3 --output-dir ./output
```

### Example Output

```
ℹ Processing: song.mp3

⠹ Writing output files ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

╭─────────── ✓ Complete ────────────╮
│ Successfully separated audio into │
│ 4 stems                           │
│ Processing time: 3.50 seconds     │
╰───────────────────────────────────╯
```

## Project Structure

```
ai_stem_cli_research/
├── stem_demo/              # Main package directory
│   ├── __init__.py        # Package initialization
│   ├── cli/               # CLI command modules
│   │   ├── __init__.py
│   │   ├── main.py        # Main CLI entry point
│   │   └── separate.py    # Separate subcommand
│   ├── core/              # Core business logic
│   │   ├── __init__.py
│   │   └── processor.py   # Audio processing logic
│   └── utils/             # Shared utilities
│       ├── __init__.py
│       └── console.py     # Rich console helpers
├── setup.py               # Package setup configuration
├── pyproject.toml         # Modern Python project config
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Step-by-Step Build Guide

This section provides a detailed walkthrough for building this CLI tool from scratch. Follow these steps to learn how to create your own professional CLI applications.

### Step 1: Project Setup

First, create the project directory structure:

```bash
# Create main project directory
mkdir ai_stem_cli_research
cd ai_stem_cli_research

# Create package structure
mkdir -p stem_demo/cli
mkdir -p stem_demo/core
mkdir -p stem_demo/utils
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### Step 3: Define Dependencies

Create `requirements.txt`:

```txt
# CLI Framework
click>=8.1.0

# Terminal Formatting and Progress Bars
rich>=13.0.0
```

### Step 4: Configure Package Metadata

Create `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "stem-demo"
version = "0.1.0"
description = "A demo CLI tool for audio stem separation"
requires-python = ">=3.10"
dependencies = [
    "click>=8.1.0",
    "rich>=13.0.0",
]

[project.scripts]
stem-demo = "stem_demo.cli.main:cli"
```

**Key Points:**
- `[project.scripts]` defines the CLI command name and entry point
- Entry point format: `command-name = "package.module:function"`
- This makes `stem-demo` available as a shell command after installation

### Step 5: Create Rich Console Utilities

Create `stem_demo/utils/console.py`:

This module provides reusable helper functions for Rich output:

```python
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, ...

def get_console() -> Console:
    """Singleton console instance"""
    # Implementation...

def print_success(message: str) -> None:
    """Print green success message"""
    # Implementation...

def create_progress_bar() -> Progress:
    """Create configured progress bar"""
    # Implementation...
```

**Key Concepts:**
- **Singleton pattern**: One shared Console instance prevents output conflicts
- **Helper functions**: Encapsulate Rich formatting for consistency
- **Type hints**: Improve code clarity and enable IDE autocomplete

### Step 6: Create Core Business Logic

Create `stem_demo/core/processor.py`:

This contains the audio processing logic (simulated):

```python
class AudioProcessor:
    SUPPORTED_EXTENSIONS = {".mp3", ".wav", ".flac", ".ogg", ".m4a"}

    def validate_audio_file(self, file_path: str) -> tuple[bool, str]:
        """Validate file exists and has supported extension"""
        # Implementation...

    def process_audio(self, file_path: str,
                     progress_callback: Callable) -> Dict:
        """Process audio with progress updates"""
        # Implementation...
```

**Key Concepts:**
- **Separation of concerns**: Business logic separate from CLI code
- **Callback pattern**: Pass progress updates to the UI layer
- **Type hints**: Document expected inputs and outputs
- **Validation**: Check preconditions before processing

### Step 7: Create Main CLI Entry Point

Create `stem_demo/cli/main.py`:

```python
import click

@click.group()
@click.version_option(version="0.1.0")
def cli() -> None:
    """Audio stem separation demo CLI tool.

    This tool demonstrates audio processing with
    beautiful terminal output.
    """
    pass

# Import and register subcommands
from stem_demo.cli.separate import separate
cli.add_command(separate)
```

**Key Concepts:**
- **`@click.group()`**: Creates a CLI with subcommands
- **`@click.version_option()`**: Adds `--version` flag automatically
- **Docstring**: Becomes the help text (`--help`)
- **Dynamic registration**: Add subcommands after group definition

### Step 8: Create Separate Subcommand

Create `stem_demo/cli/separate.py`:

```python
@click.command()
@click.argument("audio_file", type=click.Path(exists=False))
@click.option("--output-dir", "-o", type=click.Path(...))
@click.option("--verbose", "-v", is_flag=True)
def separate(audio_file: str, output_dir: str, verbose: bool) -> None:
    """Separate audio file into individual stems."""

    # 1. Validate input
    processor = AudioProcessor()
    is_valid, error = processor.validate_audio_file(audio_file)

    if not is_valid:
        print_error(error)
        sys.exit(1)

    # 2. Process with progress bar
    with create_progress_bar() as progress:
        task = progress.add_task("Processing...", total=100)

        def update_progress(description: str, fraction: float):
            progress.update(task, description=description,
                          completed=int(fraction * 100))

        result = processor.process_audio(audio_file, update_progress)

    # 3. Display results
    print_panel("Success!", style="green")
```

**Key Concepts:**
- **`@click.command()`**: Defines a CLI command
- **`@click.argument()`**: Required positional arguments
- **`@click.option()`**: Optional flags and parameters
- **Context manager**: `with create_progress_bar()` ensures cleanup
- **Callback function**: Updates UI as processing progresses
- **Exit codes**: `sys.exit(1)` for errors, `0` for success

### Step 9: Create Package __init__ Files

Create `__init__.py` in each package directory:

```bash
# stem_demo/__init__.py
"""stem-demo: Audio stem separation CLI tool."""
__version__ = "0.1.0"

# stem_demo/cli/__init__.py
"""CLI commands module."""

# stem_demo/core/__init__.py
"""Core business logic module."""

# stem_demo/utils/__init__.py
"""Utilities module."""
```

**Key Points:**
- Makes directories into Python packages
- Can define package-level variables and imports
- Docstrings document package purpose

### Step 10: Create setup.py

Create `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="stem-demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click>=8.1.0", "rich>=13.0.0"],
    entry_points={
        "console_scripts": [
            "stem-demo=stem_demo.cli.main:cli",
        ],
    },
)
```

**Key Concepts:**
- **`find_packages()`**: Automatically discovers all packages
- **`entry_points`**: Defines CLI commands (same as pyproject.toml)
- **`console_scripts`**: Creates executable shell commands

### Step 11: Install and Test

```bash
# Install in development mode (-e = editable)
pip install -e .

# Test the installation
stem-demo --help
stem-demo separate --help

# Create a test file
touch test_song.mp3

# Run the command
stem-demo separate test_song.mp3 --verbose
```

**Development Mode (`-e`) Benefits:**
- Code changes are immediately available
- No need to reinstall after edits
- Perfect for iterative development

## How Click and Rich Work Together

### Click's Role

Click handles the command-line interface structure:

1. **Command parsing**: Converts `stem-demo separate song.mp3 --verbose` into function calls
2. **Argument validation**: Checks types, required values, etc.
3. **Help generation**: Creates beautiful `--help` text from docstrings
4. **Error handling**: Displays user-friendly error messages

### Rich's Role

Rich handles terminal output and formatting:

1. **Styled text**: Colors, bold, italic, etc.
2. **Progress bars**: Real-time updates with spinners and ETAs
3. **Panels**: Bordered boxes for important messages
4. **Tables**: Formatted data display (not used in this demo)

### Integration Pattern

```python
@click.command()  # Click decorator
def my_command(file: str):
    # Click handles parsing

    # Rich handles output
    with create_progress_bar() as progress:
        # Your logic here
        pass

    print_success("Done!")  # Rich formatting
```

## Architecture Patterns

### 1. Separation of Concerns

- **CLI layer** (`cli/`): User interaction, Click decorators
- **Core layer** (`core/`): Business logic, algorithms
- **Utils layer** (`utils/`): Shared helpers, formatting

### 2. Callback Pattern

The processor doesn't know about Rich or progress bars:

```python
# Core layer: accepts generic callback
def process_audio(self, file_path, progress_callback):
    progress_callback("Loading...", 0.1)
    # Do work...
    progress_callback("Done", 1.0)

# CLI layer: provides Rich-specific callback
def update_progress(description, fraction):
    progress.update(task, description=description,
                   completed=int(fraction * 100))

processor.process_audio(file, update_progress)
```

### 3. Configuration Over Code

Rich Progress is configured once in `utils/console.py`:

```python
def create_progress_bar() -> Progress:
    return Progress(
        SpinnerColumn(),      # Spinning animation
        TextColumn(...),      # Task description
        BarColumn(),          # Progress bar
        TaskProgressColumn(), # Percentage
        TimeRemainingColumn() # Time estimate
    )
```

Then used everywhere without repetition.

## Extending the Tool

### Add a New Subcommand

1. Create `stem_demo/cli/analyze.py`:

```python
import click
from stem_demo.utils.console import print_info

@click.command()
@click.argument("audio_file")
def analyze(audio_file: str):
    """Analyze audio file characteristics."""
    print_info(f"Analyzing {audio_file}...")
    # Implementation...
```

2. Register in `stem_demo/cli/main.py`:

```python
from stem_demo.cli.analyze import analyze
cli.add_command(analyze)
```

3. Test it:

```bash
stem-demo analyze song.mp3
```

### Add a New Option

Add to the `@click.option()` decorators:

```python
@click.option(
    "--format",
    type=click.Choice(["wav", "mp3", "flac"]),
    default="wav",
    help="Output format for stems"
)
def separate(audio_file: str, format: str, ...):
    # Use the format parameter
    print_info(f"Output format: {format}")
```

## Learning Resources

### Click Documentation
- **Official Docs**: https://click.palletsprojects.com/
- **Key Topics**: Commands, arguments, options, context

### Rich Documentation
- **Official Docs**: https://rich.readthedocs.io/
- **Key Topics**: Console, Progress, Panel, Table, Syntax

### Python Packaging
- **PEP 517/518**: Modern build system
- **setuptools**: Package building
- **entry_points**: CLI command registration

## Common Patterns Reference

### Error Handling

```python
try:
    result = processor.process_audio(file)
    print_success("Processing complete!")
except KeyboardInterrupt:
    print_error("Cancelled by user")
    sys.exit(130)
except Exception as e:
    print_error(f"Error: {e}")
    sys.exit(1)
```

### Progress Tracking

```python
with create_progress_bar() as progress:
    task = progress.add_task("Working...", total=100)

    for i in range(100):
        # Do work
        progress.update(task, advance=1)
```

### Validation

```python
def validate_input(value: str) -> tuple[bool, str]:
    """Return (is_valid, error_message)"""
    if not value:
        return False, "Value cannot be empty"
    return True, ""

is_valid, error = validate_input(user_input)
if not is_valid:
    print_error(error)
    sys.exit(1)
```

## Testing Your CLI

### Manual Testing

```bash
# Test help text
stem-demo --help
stem-demo separate --help

# Test with valid input
touch test.mp3
stem-demo separate test.mp3

# Test error handling
stem-demo separate nonexistent.mp3
stem-demo separate test.txt  # Invalid extension

# Test options
stem-demo separate test.mp3 --verbose
stem-demo separate test.mp3 --output-dir ./output
```

### Automated Testing (Optional)

Use Click's testing utilities:

```python
from click.testing import CliRunner
from stem_demo.cli.main import cli

def test_separate_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['separate', 'test.mp3'])
    assert result.exit_code == 0
```

## Troubleshooting

### Command Not Found After Install

```bash
# Make sure you're in the virtual environment
which stem-demo  # Should show path in .venv/

# If not, activate venv
source .venv/bin/activate

# Reinstall
pip install -e .
```

### Import Errors

```bash
# Check package is installed
pip list | grep stem-demo

# Verify all __init__.py files exist
find stem_demo -name "__init__.py"
```

### Progress Bar Not Showing

- Rich requires a TTY (terminal)
- Redirect to file may hide progress: `stem-demo separate file.mp3 > output.txt`
- Use `--verbose` for more visibility

## Next Steps

Now that you understand the basics, try:

1. **Add real audio processing**: Integrate Spleeter or Demucs
2. **Add more options**: Quality settings, stem selection, etc.
3. **Improve error messages**: More helpful suggestions
4. **Add configuration file**: YAML/TOML for user preferences
5. **Add logging**: Track processing history
6. **Build documentation**: Sphinx or MkDocs
7. **Publish to PyPI**: Share your tool with the world

## License

MIT License - Feel free to use this as a template for your own projects!

## Acknowledgments

- **Click**: Elegant CLI framework by Pallets
- **Rich**: Beautiful terminal formatting by Will McGugan
- Python community for excellent documentation and examples
