# Binfinity ♻️🔍  
**Real-time waste detection & classification using YOLO (Ultralytics)**

Binfinity is a computer-vision project that detects and classifies waste into **metal**, **paper**, and **plastic** using a custom-trained **YOLO** model from the **Ultralytics** framework.  
It supports inference on **images**, **folders**, **videos**, and **live camera/webcam feeds**.

---

## Features
- Custom YOLO model trained for 3 waste categories:
  - `metal`
  - `paper`
  - `plastic`
- Real-time detection using webcam (live feed)
- CLI-based detection script with multiple input options
- Optional FPS display and recording support (video/webcam)
- Dataset training workflow (Google Colab notebook)

---

## Repository Structure
- `yolo_model.ipynb` — Google Colab notebook for:
  - dataset preparation (train/val split)
  - generating `data.yaml`
  - training YOLO with Ultralytics
- `yolo_detect.py` — full detection pipeline for:
  - images / folders / video files / USB camera / PiCamera
  - bounding box drawing + confidence + FPS + object count
- `live.py` — quick live webcam inference script
- `notes.json` — label/category metadata (Label Studio export-style)

---

## Classes / Labels
The project is trained to detect the following categories:

| Class ID | Name    |
|---------:|---------|
| 0        | metal   |
| 1        | paper   |
| 2        | plastic |

(See `notes.json` for reference.)

---

## Installation

### 1) Create a virtual environment (recommended)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install ultralytics opencv-python numpy
```

---

## Model Weights
This repo expects trained YOLO weights (a `.pt` file).

Examples referenced in code:
- `best220.pt` (used in `live.py`)
- any custom path you pass via `--model` in `yolo_detect.py`

Place your weights file in the repo root or update the filename/path in scripts.

---

## Usage

### Option A — Quick Live Webcam Detection
`live.py` runs inference directly on your webcam:

```bash
python live.py
```

Make sure `best220.pt` is present (or edit `live.py` to point to your weights file):
```python
model = YOLO("best220.pt")
```

---

### Option B — Flexible Detection Script (Recommended)
Use `yolo_detect.py` for images, videos, folders, or cameras.

#### 1) Run on a single image
```bash
python yolo_detect.py --model best220.pt --source test.jpg
```

#### 2) Run on a folder of images
```bash
python yolo_detect.py --model best220.pt --source path/to/images_folder
```

#### 3) Run on a video file
```bash
python yolo_detect.py --model best220.pt --source testvid.mp4 --resolution 640x480
```

#### 4) Run on a USB webcam
Use `usb0`, `usb1`, etc.
```bash
python yolo_detect.py --model best220.pt --source usb0 --resolution 640x480
```

#### 5) Record output (video/webcam only)
Recording requires `--resolution`:
```bash
python yolo_detect.py --model best220.pt --source usb0 --resolution 640x480 --record
```
This will save an output file named `demo1.avi`.

---

## Training (Colab)
Training is documented in **`yolo_model.ipynb`**, including:
- GPU check (`nvidia-smi`)
- dataset zip extraction
- train/val splitting
- generating `data.yaml`
- training with Ultralytics YOLO

Typical training command pattern used:
- installs `ultralytics`
- creates `data.yaml` from `classes.txt`
- trains a YOLO model for detection

If you use your own dataset, ensure you have:
- images in `train/images` and `validation/images`
- labels in YOLO format in `train/labels` and `validation/labels`
- a valid `data.yaml`

---

## Notes / Tips
- If you see warnings like **“non-normalized or out of bounds”** during training, it usually means some label files have invalid bounding box values (YOLO requires normalized coordinates between 0 and 1).
- If webcam doesn’t open, try changing camera index (`usb0` → `usb1`) or verify permissions.

---

## Tech Stack
- **Python**
- **Ultralytics YOLO**
- **OpenCV**
- **NumPy**
- (Training) **Google Colab + NVIDIA GPU**


