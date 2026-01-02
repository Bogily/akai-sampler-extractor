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

1. Place your Akai `.iso` files (e.g., _Spectrasonics - Distorted Reality_) in the same directory as the script.
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

## Technical Details

### How it handles files

- **WAV Files**: Preserved and organized by partition/volume.
- **Metadata**: Files ending in `.P1`, `.P3`, or `.DAT` are deleted.
- **Stereo Pairs**: The script identifies matching filenames with `-L` and `-R` suffixes, combines them, and removes the original mono files to save space.
