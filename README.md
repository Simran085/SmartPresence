# 🎓 SmartPresence – AI-Powered Facial Recognition Attendance System

> ✅ **Automated. Accurate. Real-time.** Built to replace manual attendance systems with a secure, efficient face recognition solution.

---

## 📌 Overview

**SmartPresence** is a Python-based student attendance system that automates the entire attendance process using **facial recognition technology**. Designed for educational institutions, the system eliminates manual errors, reduces time wastage, and prevents proxy attendance.

Built using **OpenCV**, **LBPH algorithm**, and a **MySQL backend**, it provides an efficient, real-time, and secure attendance marking process — while being easy to operate even for non-technical users.

Developed as part of UCS503 Software Engineering Lab @ TIET (April–July 2024).

---

## 🚀 Key Features

### 🧠 Intelligent Attendance Automation
- Detects and recognizes student faces with **92.4% accuracy** using the LBPH (Local Binary Pattern Histogram) algorithm.
- Uses Haar cascades for real-time face detection with minimal processing delay.

### ⏱️ Time-Saving & Efficient
- Reduces manual attendance input effort by over **40%**.
- Attendance is auto-logged and stored in **under 1 second per student**.

### 🔐 Secure Authentication
- Admin-only access for training, recognition, and attendance viewing.
- MySQL backend prevents unauthorized data modification.

### 📸 Real-Time Camera Feed
- Captures facial input live from webcam.
- Capable of handling varying light and environmental conditions.

### 📄 Database-Backed Logs
- Attendance is stored in **MySQL** and also exported to **CSV** for reporting and backup.
- Easy retrieval of student-wise logs and statistics.

### 🧑‍🏫 Simple GUI Interface (Tkinter)
- Instructor-friendly, clean, and intuitive GUI — minimal training required.
- Role-based navigation for Admin vs Operator.

### 💡 Additional Highlights
- **Face registration** module: capture and store multiple samples per student.
- **Training module**: updates the facial model using new student data.
- **Scalable**: Can be extended for employee/visitor attendance, biometric integration, or classroom analytics.
- Designed with **modular Python scripts** for each functionality — separation of concerns ensured.

---

## 🧭 Application Workflow

1. **Admin Login**  
   → Secure credentials-based access.

2. **Register Student**  
   → Capture multiple images via webcam and assign a unique ID.

3. **Train Model**  
   → Automatically generates LBPH facial features and saves the trained model.

4. **Mark Attendance**  
   → Real-time recognition with automatic timestamped logging into MySQL & CSV.

5. **View Records**  
   → Instructor can fetch attendance by student ID/date as needed.

---
