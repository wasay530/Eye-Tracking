# 👁️ Real-Time Eye Tracking & fMRI Correlation Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Computer Vision](https://img.shields.io/badge/Computer_Vision-FF6F00?style=for-the-badge&logo=computer-vision&logoColor=white)
![Research](https://img.shields.io/badge/Research-00599C?style=for-the-badge&logo=googlescholar&logoColor=white)

> **A low-cost, computer vision-based approach to track eye gaze during comprehension tasks and correlate ocular movements with fMRI brain activity.**

---

## 📌 Overview

Real-time gaze tracking provides crucial input for **psychophysics studies**, **neuromarketing**, and **human-computer interaction (HCI)**. Traditional solutions often rely on expensive hardware and specialized infrared cameras. 

This project implements a cost-effective **vision-based eye-tracking system** using standard webcams. It utilizes **Haar Cascade classifiers** and image processing techniques to detect:
* Pupil center coordinates $(x, y)$.
* Gaze direction (Left, Right, Up, Down).
* Blink detection.
* **Correlation with fMRI:** Comparing eye movement patterns with functional MRI data during cognitive tasks.

---

## 📊 Results & Visualization

### 1. Real-Time Pupil Detection
The system identifies the eye region and pinpoints the pupil center in real-time video feeds.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60351044/212671363-f3cc2826-742e-4f7a-aac3-f3f6b02a62eb.png" alt="Eye Tracking Output" width="70%">
</p>

### 2. Gaze Movement Analysis
We generate time-series data for eye movements, allowing for statistical analysis of blink rates and saccades.

<p align="center">
  <img src="https://user-images.githubusercontent.com/60351044/212672823-33ef1fd1-919d-499c-897a-796f91ae512d.png" alt="Eye Movement Graph" width="70%">
</p>

---

## 📂 Repository Structure

```bash
├── code/           # Main Python scripts for tracking and analysis
├── input_data/     # Raw video samples or fMRI datasets
├── report/         # Project documentation and final reports
├── research/       # Literature review and reference papers
├── Results/        # Generated graphs, logs, and output images
└── README.md       # Project documentation
