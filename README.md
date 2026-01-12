# ANAV Drone – Autonomous Safe Landing Detection (Vision-Based)

This project implements a vision-based autonomous landing detection system for drones operating in GPS-denied environments. The system uses real-time camera input to identify safe and unsafe landing zones using classical computer vision techniques, inspired by planetary exploration scenarios such as Mars landings.

---

## Problem Statement
Enable a drone to autonomously identify safe landing zones without relying on GPS or external positioning systems, using only onboard visual input.

---

## Solution Overview
A real-time computer vision pipeline processes live camera feed to:
- Detect obstacles and hazardous regions
- Identify obstacle-free (safe) landing zones
- Output precise bounding box coordinates for navigation and landing decisions

---

## System Pipeline
1. Capture live video feed (webcam / drone camera)
2. Image preprocessing (resize, grayscale, blur)
3. Edge detection using Canny
4. Contour extraction for obstacle detection
5. Safe zone identification using grid-based mask analysis
6. Bounding box generation for safe and unsafe regions

---



