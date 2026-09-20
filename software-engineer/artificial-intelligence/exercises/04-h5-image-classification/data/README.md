# Data Directory

This folder holds the **input images** for Exercise 04. There is no bundled
dataset here: the exercise expects **you** to place a single image file to
classify.

## Expected Input Image

| Property | Expected value |
| --- | --- |
| Format | JPEG or PNG |
| Channels | RGB (color). Grayscale images are converted to RGB automatically by the script. |
| Size | Any size — the image is resized to the model's expected input size (e.g. `224x224`) before inference. |
| Values | Integer pixel values 0–255; the script normalizes them to `[0, 1]`. |
| Orientation | Any — no orientation assumptions are made. |

## What the script does with this image

1. Opens the file with Pillow.
2. Converts it to RGB.
3. Resizes it to the model's expected `(height, width)`.
4. Converts the pixels to `float32` and divides by 255.
5. Adds a batch axis: `(1, height, width, 3)`.
6. Runs inference and prints the top-k class indices.

## Recommendations

- Use a **test image from the same domain** the model was trained on (for
  example, if the model classifies vehicles, use a clear photo of a vehicle).
- The classification **quality depends on the model and on matching its
  training data distribution** — unrelated images will still produce some
  output, but it will not be meaningful.
- Do not place large or copyrighted datasets in this folder; a single
  self-made image is enough for the exercise.

## Filename conventions

Place the file at `data/sample.jpg` (the script default) or pass any path
with `--image`:

```bash
python predict.py --image data/my_photo.png
```