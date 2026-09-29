# Problem & Scope Statement: Student Attendance & Eligibility Tracker

## 1. Problem Statement
Maintaining paper-based attendance registers in educational environments is time-consuming, prone to human calculation mistakes, and susceptible to loss or damage[cite: 1]. Additionally, manually determining whether each student meets mandatory academic regulations (such as the standard 75% attendance criterion) requires substantial administrative effort. There is a need for a lightweight, reliable, offline-first command-line application that ensures unique record logging per date, prevents duplicate marks, and automatically computes exam eligibility metrics.

## 2. Scope of the Project
The application manages basic academic records by allowing users to enroll students, log daily classroom attendance (`PRESENT` or `ABSENT`), compute percentage attendance, and detect defaulters[cite: 1]. It relies strictly on Python standard constructs, loops, functions, and persistent flat text-file storage without needing external database drivers or third-party web frameworks[cite: 1]. The scope covers local execution suitable for classroom-level tracking.

## 3. Target Users
- Course instructors and faculty members conducting roll calls[cite: 1].
- Academic mentors monitoring absenteeism trends[cite: 1].
- Students checking their current semester attendance percentages and exam qualification status.

## 4. High-Level Features
- **Student Enrollment:** Register students with unique IDs, full names, and enrolled courses.
- **Daily Attendance Marking (Input System):** Mark students as `PRESENT` or `ABSENT` with ISO date formatting checks and same-day duplicate mark prevention[cite: 1].
- **Student Attendance Ledger:** Retrieve individual summaries including total sessions, present days, absent days, and net attendance percentages.
- **Automated Defaulter Detection (Output System):** Automatically filter and display all enrolled students falling below the 75% attendance threshold[cite: 1].
- **Persistent Flat-File Storage:** Maintain records across application restarts using comma-separated text files (`students.txt` and `attendance.txt`).
