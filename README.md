# Image Resizer

This Python script resizes images to a specified percentage using OpenCV. It's a simple tool for quickly adjusting image dimensions while maintaining the aspect ratio.

## Features

- Resize images by a specified percentage
- Supports various image formats
- User-friendly with minimal setup

## Requirements

- Python 3.x
- OpenCV (`cv2` library)

To install the required library, run:

```bash
pip install opencv-python
```

## How It Works

This script reads an image, resizes it by a given percentage (default: 50%), and saves the resized image as a new file.

### Parameters

- **source**: The path to the original image.
- **destination**: The filename for the resized image.
- **scale_percent**: The percentage to resize the image (default: 50%).

## How to Run

1. Place your image in the same directory as the script.
2. Update the `source` and `destination` variables if needed.
3. Run the script:

   ```bash
   python image_resizer.py
   ```

## Example

To resize an image named `input.jpg` to 50% and save it as `output.jpg`, modify the variables in the script:

```python
source = 'input.jpg'
destination = 'output.jpg'
scale_percent = 50  # Resize to 50%
```

## License

This project is licensed under the MIT License. Feel free to modify and use it as you wish!
```

