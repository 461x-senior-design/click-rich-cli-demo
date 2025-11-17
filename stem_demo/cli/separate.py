"""Separate subcommand for audio stem separation.

This module implements the 'separate' subcommand that processes
audio files and separates them into individual stems.
"""

import sys
from pathlib import Path
import click
from stem_demo.core.processor import AudioProcessor
from stem_demo.utils.console import (
    get_console,
    print_success,
    print_error,
    print_info,
    print_panel,
    create_progress_bar,
)


@click.command()
@click.argument(
    "audio_file",
    type=click.Path(exists=False),  # We'll do custom validation
    required=True,
)
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(file_okay=False, dir_okay=True),
    help="Output directory for separated stems (default: same as input file)",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Show detailed processing information",
)
def separate(audio_file: str, output_dir: str, verbose: bool) -> None:
    """Separate audio file into individual stems.

    This command takes an audio file and separates it into individual
    instrumental stems (vocals, drums, bass, and other instruments).

    \b
    Arguments:
        AUDIO_FILE: Path to the audio file to process

    \b
    Example Usage:
        $ stem-demo separate song.mp3
        $ stem-demo separate /path/to/audio.wav --output-dir ./output
        $ stem-demo separate music.flac --verbose

    \b
    Supported Formats:
        .mp3, .wav, .flac, .ogg, .m4a
    """
    console = get_console()
    processor = AudioProcessor()

    # Display header
    if verbose:
        console.print("\n[bold cyan]═══ Audio Stem Separator ═══[/bold cyan]\n")
        print_info(f"Input file: {audio_file}")
        if output_dir:
            print_info(f"Output directory: {output_dir}")

    # Validate audio file
    is_valid, error_message = processor.validate_audio_file(audio_file)
    if not is_valid:
        print_error(error_message)

        # Show helpful hint about supported formats
        formats = processor.get_supported_formats()
        console.print(
            f"\n[dim]Supported formats: {', '.join(formats)}[/dim]\n",
            style="yellow",
        )
        sys.exit(1)

    # Process the audio file with progress bar
    try:
        print_info(f"Processing: {Path(audio_file).name}")
        console.print()  # Empty line for spacing

        # Create progress bar and process audio
        with create_progress_bar() as progress:
            # Task for tracking overall progress
            task = progress.add_task(
                "[cyan]Initializing...",
                total=100
            )

            def update_progress(description: str, progress_fraction: float) -> None:
                """Callback to update the progress bar.

                Args:
                    description: Current processing step description
                    progress_fraction: Progress from 0.0 to 1.0
                """
                # Convert fraction to percentage
                percentage = int(progress_fraction * 100)

                # Update progress bar
                progress.update(
                    task,
                    description=f"[cyan]{description}",
                    completed=percentage,
                )

            # Process the audio file
            result = processor.process_audio(audio_file, update_progress)

        # Display success message
        console.print()  # Empty line for spacing

        duration = result["duration"]
        stems = result["stems"]

        # Create success panel with generated stem filenames
        stem_lines = "\n".join(
            f"[white]- [cyan]{Path(stem).name}[/cyan]"
            for stem in stems
        )
        success_message = (
            f"[green]Successfully separated audio into {len(stems)} stems[/green]\n"
            f"[dim]Processing time: {duration:.2f} seconds[/dim]\n\n"
            f"[bold]Generated files:[/bold]\n{stem_lines}"
        )

        print_panel(
            success_message,
            title="✓ Complete",
            style="green",
        )

        # Show generated stems if verbose (with full paths)
        if verbose:
            console.print("\n[bold]Generated stems (full paths):[/bold]")
            for i, stem in enumerate(stems, 1):
                console.print(f"  {i}. [cyan]{stem}[/cyan]")
            console.print()

    except KeyboardInterrupt:
        console.print("\n")
        print_error("Processing cancelled by user")
        sys.exit(130)  # Standard exit code for SIGINT

    except Exception as e:
        console.print("\n")
        print_error(f"An error occurred during processing: {str(e)}")

        if verbose:
            console.print_exception()

        sys.exit(1)
