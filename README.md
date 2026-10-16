# Image Emotion Detection

A small Python application that analyzes an image for facial emotions using [DeepFace](https://github.com/serengil/deepface) and displays the dominant emotion on the image.

## Features

- Detects the dominant emotion in an image.
- Prints the confidence score for each detected emotion.
- Displays the image with the dominant emotion overlaid.
- Includes `emo_img.avif` as a sample image.

## Requirements

- Python 3.8 or newer
- OpenCV
- DeepFace

Install the Python packages:

```bash
python -m pip install opencv-python deepface
```

## Run

Clone the repository, change into the project directory, and run:

```bash
python emo_img.py
```

The script uses `emo_img.avif` by default. To analyze another image, update the `image_path` value in `emo_img.py`. The image must be readable by your OpenCV installation.

The detected dominant emotion and emotion confidence scores are printed in the terminal. A window then displays the image with the dominant emotion overlaid; press any key to close it.
