# 🅿️ Smart Parking Space Detector

---

## ✨ Description
This project implements a **Smart Parking Space Detector** using computer vision techniques to identify available parking spots in real-time. It leverages OpenCV to process video feeds, detect parking regions, and determine their occupancy.

---


## 🚀 How to Clone This Project

To get a copy of this project up and running on your local machine, follow these simple steps:

1.  **Open your terminal or command prompt.**

2.  **Navigate to the directory** where you want to store the project.

3.  **Clone the repository** using the following command:

    ```bash
    git clone <repository_url>
    ```
    *(Replace `<repository_url>` with the actual URL of this GitHub repository.)*

4.  **Change into the project directory:**

    ```bash
    cd Smart-Parking-Space-Detector # Or whatever your project folder is named
    ```

---

## 🌟 Features

* **Interactive Parking Space Selection:** `parking_space_picker.py` allows users to manually select and save the coordinates of parking spots on an image by clicking.
* **Real-time Occupancy Detection:** `main_parking_detector.py` processes a video feed to continuously check the occupancy of defined parking spaces.
* **Visual Feedback:** Displays bounding boxes around parking spaces with different colors indicating occupancy (e.g., green for free, red for occupied).
* **Free Space Counter:** Shows the number of available parking spaces.
* **Dynamic Reset:** The video feed automatically loops back to the beginning when it reaches the end.

---

## 🛠️ Dependencies and Installation

This project is built primarily with **Python**. Here are the required libraries and how to install them:

* **Python 3.x**
* **OpenCV (`opencv-python`)**: For image and video processing.
* **`cvzone`**: A powerful computer vision library that simplifies many OpenCV tasks.
* **NumPy**: For numerical operations, especially with image arrays.

You can install all the necessary Python packages using `pip`:

```bash
pip install opencv-python cvzone numpy
