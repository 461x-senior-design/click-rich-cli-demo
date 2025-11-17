"""Rich console utilities for beautiful terminal output.

This module provides helper functions for consistent Rich formatting
throughout the CLI application.
"""

from typing import Optional
from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
)
from rich.panel import Panel
from rich.text import Text


# Singleton console instance for consistent output
_console: Optional[Console] = None


def get_console() -> Console:
    """Get or create the Rich Console instance.

    Returns:
        Console: Configured Rich Console instance

    Example:
        >>> console = get_console()
        >>> console.print("Hello, world!")
    """
    global _console
    if _console is None:
        _console = Console()
    return _console


def print_success(message: str) -> None:
    """Print a success message with green styling.

    Args:
        message: The success message to display

    Example:
        >>> print_success("Processing complete!")
    """
    console = get_console()
    text = Text(f"✓ {message}", style="bold green")
    console.print(text)


def print_error(message: str) -> None:
    """Print an error message with red styling.

    Args:
        message: The error message to display

    Example:
        >>> print_error("File not found!")
    """
    console = get_console()
    text = Text(f"✗ {message}", style="bold red")
    console.print(text)


def print_info(message: str) -> None:
    """Print an info message with blue styling.

    Args:
        message: The info message to display

    Example:
        >>> print_info("Processing audio file...")
    """
    console = get_console()
    text = Text(f"ℹ {message}", style="bold blue")
    console.print(text)


def print_panel(message: str, title: str = "", style: str = "green") -> None:
    """Print a message inside a Rich panel.

    Args:
        message: The message to display in the panel
        title: Optional title for the panel
        style: Color style for the panel border

    Example:
        >>> print_panel("Success!", title="Result", style="green")
    """
    console = get_console()
    panel = Panel(message, title=title, border_style=style)
    console.print(panel)


def create_progress_bar() -> Progress:
    """Create a configured Rich Progress bar.

    Returns:
        Progress: Configured Rich Progress instance with multiple columns

    Example:
        >>> with create_progress_bar() as progress:
        ...     task = progress.add_task("Processing...", total=100)
        ...     progress.update(task, advance=10)
    """
    return Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=get_console(),
    )
