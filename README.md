# InTheGreen

**InTheGreen** is an AIoT (Artificial Intelligence of Things) project designed to assist visually impaired or blind individuals in recognizing the state of pedestrian traffic lights through an intelligent and accessible solution.

## 🎯 Project Goal

To enable visually impaired or blind individuals to move safely by detecting the state of pedestrian traffic lights (red or green) and providing appropriate feedback through a buzzer or a mobile application.

---

## ⚙️ Features

### 1. **ESP32 with a Camera and AI Model**

- Detects the state of traffic lights (red or green) using an embedded AI model.
- Processes images captured by the camera to determine the light's state.

### 2. **User-Adapted Feedback**

- **For visually impaired/blind users**:
  - A **buzzer** connected to the microcontroller emits distinct sounds:
    - Short and rapid beeps for a **red** light.
    - Long and spaced beeps for a **green** light.
- **SwiftUI application**:
  - Displays the traffic light state for sighted users.

---

## 🛠️ Technologies Used

### Hardware:

- **ESP32**: Microcontroller.
- **ESP32-CAM**: For image capture.
- **Buzzer**: Provides auditory feedback.

### Software:

- **TinyML AI Model**: Detects traffic light colors (red or green).
- **SwiftUI**: Develops a user-friendly mobile app.
- **Arduino IDE**: For programming the ESP32 firmware.

---

## 🧩 System Architecture

1. **Image Capture**:  
   The ESP32-CAM captures images of the traffic light.

2. **AI Analysis**:  
   The TinyML model embedded in the ESP32 analyzes the image and determines the light's state.

3. **User Feedback**:
   - **Auditory feedback** via the buzzer.
   - **Visual feedback** on the SwiftUI application.

---

## 📐 AI Model

- **Architecture:** Lightweight model optimized for microcontrollers (TinyML).
- **Input:** Images captured by the camera.
- **Output:**
  - `0`: **Red** light.
  - `1`: **Green** light.

---

## 📚 Contributions

**Contributions are welcome!**

- **Fork** the project.
- **Create a branch** for your feature `(git checkout -b my-feature)`.
- **Make your changes.**
- **Submit** a pull request.

---

## ✨ Authors

`Oscar FRANK` – `Younès BOUFRIOUA` – `Romain REYNAERT` – `Théotime SCHMELTZ​`

**All contributions are acknowledged in the releases.**

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
