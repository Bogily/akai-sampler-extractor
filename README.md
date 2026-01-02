# Akai ISO to Stereo WAV Extractor

A Python-based TUI tool designed to bridge the gap between legacy Akai S1000/S3000 sampler images and modern Filesystems. This script automates the extraction, merging, and cleaning process of the akai iso.

## Prerequisites

1. **Python 3.x**
2. **FFmpeg**: Must be installed and added to your System PATH (required for the `pydub` library to export audio).
3. **akaiutil.exe**: Ensure the [akaiutil](https://sourceforge.net/projects/akaiutil/) executable is in the same folder as the script.

## Installation

Install the necessary Python dependencies via pip:

```bash
pip install pick pydub

```

## Usage

1. Place your Akai `.iso` files in the same directory as the script.
2. Run the tool:

```bash
python akai_util_helper.py

```

3. Use the **Arrow Keys** to navigate and **Enter** to select your ISO.
4. The script will:

- Create a folder named after the ISO.
- Extract all samples into their original folder structure.
- Merge all stereo pairs.
- Delete all "junk" files (anything not a `.wav`).


## Disclaimer

This project is an independent utility and is not affiliated with, authorized, or endorsed by Akai Professional or Spectrasonics. All trademarks (AKAI, S1000, S3000) are the property of their respective owners. This tool is intended for personal use in converting legally owned backup images.
