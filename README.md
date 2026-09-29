# Student Attendance & Eligibility Tracker

A lightweight, human-readable Python command-line application designed to track classroom attendance, validate session entries, and calculate exam eligibility based on the 75% attendance rule[cite: 1].

## Overview
This project provides a clean Input-Output system to replace physical roll-call rosters[cite: 1]. Built using straightforward Python functions, loops, and basic file input/output, it stores records in plain text files and offers instant status checks and defaulter reports.

## Features
- **Student Registration:** Enroll students with basic validation (length and uniqueness).
- **Attendance Ingestion (Input System):** Record daily attendance with built-in validation for date format (`YYYY-MM-DD`) and safeguards against marking a student twice on the same day[cite: 1].
- **Summary & Analytics (Output System):** View total classes conducted, days attended, days absent, and percentage attendance[cite: 1].
- **Defaulter Filtering:** Filter and display all enrolled students with attendance below 75%[cite: 1].
- **Plain-Text Data Persistence:** Stores records locally across runs in `students.txt` and `attendance.txt`.

## Technologies Used
- **Language:** Python 3.x[cite: 1]
- **Libraries:** Python standard library (no third-party packages required)
- **Data Storage:** Flat text files (`.txt`)

## Project Structure
```text
attendance-tracker/
├── main.py          # Main application code containing all functions and the CLI loop
├── README.md        # Project overview, installation, and usage instructions
├── statement.md     # Problem statement, scope, and feature breakdown
├── students.txt     # Persistent storage for student records (auto-generated)
└── attendance.txt   # Persistent storage for attendance logs (auto-generated)
