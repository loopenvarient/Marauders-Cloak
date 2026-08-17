# Marauders-Cloak
### ⬇️ 
### ⬇️ which basically is
### ⬇️ 
# Harry Potter — Invisibility Cloak

> *"I solemnly swear that I am up to no good."* 🗺️

A small computer vision project inspired by one of my favorite things from childhood **Harry Potter**.

This project uses **Python, OpenCV, and NumPy** to recreate the illusion of an invisibility cloak using a webcam.

I'm building this project primarily as a **learning exercise** to understand the basics of computer vision, image processing, color detection, masking, and real-time video processing.

---

## 🧙 Why I Made This

I've been a **Harry Potter fan since childhood**, so when I started learning computer vision, I wanted to build something that was more than just another tutorial project.

Instead of simply following an OpenCV example, I decided to turn one of the most iconic Harry Potter objects into a small computer vision project.

The goal isn't to build something production-ready.

The goal is to **learn by building something I actually care about.**

And honestly, making myself disappear on camera seemed like a pretty good way to start. 🪄

---

## 🎯 What This Project Does

The program uses your webcam to create an **invisibility cloak effect**.

The basic idea is:

1. Capture the background without the person in the frame.
2. Start capturing the live webcam feed.
3. Detect the cloak based on its color.
4. Create a mask around the detected cloak.
5. Replace the cloak region with the previously captured background.
6. Combine everything into a final frame.

The result looks like the person is disappearing behind an invisible cloak.

---

## 🧠 What I'm Learning

This project is helping me understand the fundamentals of:

- 📷 Webcam / video capture
- 🎨 Color detection
- 🌈 HSV color space
- 🖼️ Image processing
- 🎭 Image masking
- 🔀 Bitwise operations
- 🧹 Noise reduction
- 🔄 Real-time frame processing
- 🧮 NumPy arrays
- ⚡ Basic computer vision concepts

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 👁️ OpenCV | Computer vision & image processing |
| 🔢 NumPy | Image/frame manipulation |
| 📷 Webcam | Real-time video input |

---

## 📁 Project Structure

```text
Harry-Potter-Invisibility-Cloak/
│
├── main.py
├── requirements.txt
├── README.md
│
└── assets/
    └── demo.gif
