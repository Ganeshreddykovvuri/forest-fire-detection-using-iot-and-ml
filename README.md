# 🌲🔥 Forest Fire Detection System

A computer vision-based forest fire detection system built using a custom dataset and the YOLOv8 object detection model. This project allows users to detect fires in forest images and videos in real-time through a user-friendly Streamlit web interface.

## 🚀 Features

- 🔥 Detects forest fires in images and videos
- 📦 Built with YOLOv8 for high-speed, accurate inference
- 🖼️ Streamlit app for simple drag-and-drop file upload
- 🧠 Trained on a custom forest fire dataset
- 💡 Real-time visualization of detection results

## 🧰 Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Streamlit
- PIL (Pillow)

## 📂 Project Structure

forest-fire-detection-system-/
│
├── best.pt                   # Trained YOLOv8 model
├── app.py                    # Streamlit app
├── requirements.txt          # Required Python packages
└── README.md                 # Project documentation

## ✅ Getting Started
### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

> Ensure you have Python 3.7 or above and `ultralytics` installed.

### 2. Download the YOLOv8 Model

Place your trained YOLOv8 model (`best.pt`) inside the project directory.

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

## 📁 Input Types

- Image: `jpg`, `jpeg`, `png`
- Video: `mp4`, `avi`, `mov`, `mkv`

## 📌 Usage

1. Choose between **Image** or **Video** upload in the dropdown.
2. Upload your file.
3. View detection results with fire areas highlighted.

## 🔮 Future Improvements

- Integrate live drone camera feeds
- Add SMS/Email alert system
- Expand dataset for better generalization

## 🙋‍♂️ Author

Developed by Ganesh

## 📃 License

This project is licensed under the MIT License. Feel free to use and modify it for your own applications.

---

> Feel free to ⭐️ this repo if you found it helpful!
```
