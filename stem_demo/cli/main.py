"""Main CLI entry point for stem-demo.

This module defines the main Click group and coordinates all subcommands.
"""

import click
from stem_demo.utils.console import get_console


@click.group()
@click.version_option(version="0.1.0")
def cli() -> None:
    """Audio stem separation demo CLI tool.

    This tool demonstrates audio processing with beautiful terminal output
    using Click for the CLI framework and Rich for formatting.

    \b
    Example Usage:
        $ stem-demo separate song.mp3
        $ stem-demo separate /path/to/audio.wav
        $ stem-demo --help

    \b
    Supported Audio Formats:
        .mp3, .wav, .flac, .ogg, .m4a
    """
    pass


# Import and register subcommands
# This is done after the cli group is defined to avoid circular imports
from stem_demo.cli.separate import separate

cli.add_command(separate)


if __name__ == "__main__":
    cli()
