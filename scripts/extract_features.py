#!/usr/bin/env python
"""
Driver script to extract features from TranscribeMe transcripts.
"""

import sys
from pathlib import Path

file = Path(__file__).resolve()
parent = file.parent
ROOT = None
for parent in file.parents:
    if parent.name == "dpfluency":
        ROOT = parent
sys.path.append(str(ROOT))

# remove current directory from path
try:
    sys.path.remove(str(parent))
except ValueError:
    pass

import argparse
import logging

from rich.console import Console
from rich.logging import RichHandler

from dptools import disfluencies
from dptools.disfluencies import constants

MODULE_NAME = "formsdb.runners.imports.export_mongo_to_psql"

console = Console(color_system="standard")

logger = logging.getLogger(MODULE_NAME)
logargs = {
    "level": logging.DEBUG,
    # "format": "%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s",
    "format": "%(message)s",
    "handlers": [RichHandler(rich_tracebacks=True)],
}
logging.basicConfig(**logargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="extract_features",
        description="Extract features from TranscribeMe transcripts",
    )
    parser.add_argument(
        "-t",
        "--transcript",
        type=Path,
        required=True,
        help="Path to the transcript file",
    )
    parser.add_argument(
        "-l",
        "--language",
        type=str,
        required=True,
        help="Language of the transcript",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        required=True,
        help="Path to the output file",
    )

    console.rule("[bold red]ClarityQuantifier: Extract Features")
    logger.info(f"Supported languages: {constants.supported_languages}")

    args = parser.parse_args()
    logger.debug(f"Arguments: {args}")

    if args.language not in constants.supported_languages:
        logger.error(f"Language '{args.language}' not supported")
        raise ValueError(f"Language '{args.language}' not supported")

    logger.info(f"Extracting features from {args.transcript}")
    df = disfluencies.get_features_df(args.transcript, args.language)
    df.to_csv(args.output, index=False)
    logger.info(f"Features extracted and saved to {args.output}")

    logger.info("Done!")
