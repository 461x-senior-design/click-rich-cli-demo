# Quick Start Guide

## Installation (30 seconds)

```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows

# 2. Install the package
pip install -e .
```

## Test It Out

```bash
# Create a test file
touch test.mp3

# Run the CLI
stem-demo separate test.mp3

# Try with verbose output
stem-demo separate test.mp3 --verbose

# See all options
stem-demo separate --help
```

## What You'll See

The CLI will show:
- ✅ Beautiful colored output
- 📊 Animated progress bar with spinner
- ⏱️ Time remaining estimates
- 🎨 Styled success/error messages
- 📝 Detailed help text

## Next Steps

1. **Read the README.md** - Complete walkthrough of how to build this from scratch
2. **Explore the code** - See how Click and Rich integrate
3. **Customize it** - Add your own commands and features
4. **Build something new** - Use this as a template for your own CLI tools

## File Map

| File | Purpose |
|------|---------|
| `stem_demo/cli/main.py` | Main CLI entry point with Click group |
| `stem_demo/cli/separate.py` | Separate subcommand implementation |
| `stem_demo/core/processor.py` | Audio processing business logic |
| `stem_demo/utils/console.py` | Rich formatting helpers |
| `pyproject.toml` | Modern Python package configuration |
| `setup.py` | Package installation configuration |

## Key Concepts Demonstrated

- ✅ Click command groups and subcommands
- ✅ Click arguments and options
- ✅ Rich progress bars with callbacks
- ✅ Rich styled output (colors, panels)
- ✅ Separation of concerns (CLI/Core/Utils)
- ✅ Type hints and documentation
- ✅ Error handling and validation
- ✅ Python packaging and entry points

## Common Commands

```bash
# Show main help
stem-demo --help

# Show command help
stem-demo separate --help

# Process with options
stem-demo separate song.mp3 --verbose
stem-demo separate song.mp3 --output-dir ./stems

# Check version
stem-demo --version
```

## Troubleshooting

**Command not found?**
```bash
# Make sure venv is activated
which stem-demo  # Should show path in .venv/

# If not, activate venv
source .venv/bin/activate
```

**Import errors?**
```bash
# Reinstall in development mode
pip install -e .
```

**Want to make changes?**
- Edit any Python file
- Changes are immediately active (no reinstall needed with -e flag)
- Run `stem-demo` again to test

## Learn More

See **README.md** for:
- Detailed step-by-step build guide
- Architecture explanations
- How to extend the tool
- Best practices and patterns
