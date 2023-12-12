# BinSight

BinSight is a Python-based computer vision tool designed for accurate dustbin detection and cropping within images. Leveraging NumPy, OpenCV (cv2), and YOLOv8's powerful machine learning algorithms, this application offers efficient and precise identification of dustbins.

## Features

- **Dustbin Detection:** Utilizes YOLOv8 for pinpointing and isolating dustbins within images.
- **Image Cropping:** Efficiently crops identified bins using OpenCV.
- **Automated Organization:** Systematically saves cropped dustbin images in a designated folder.

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/BinSight.git


2. Install required dependencies:
pip install -r requirements.txt


## Usage

1. Add images for processing into the `input_images` directory.
2. Run the main script:

python detect_bins.py

3. Cropped dustbin images will be saved in the `cropped_bins` folder.

## Requirements

- Python 3.x
- NumPy
- OpenCV (cv2)
- YOLOv8 model weights (downloaded automatically upon first run)

## Contributions

Contributions are welcome! Fork the repository and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

