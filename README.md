# Student Records Persistence and Export System

A lightweight, modular command-line application built in **Python** designed for efficient student record management, reliable data persistence, and flexible data export options (JSON and CSV). It also includes a built-in activity logging feature to track system operations.

## Features

* **Data Management:** Add, view, update, and manage student profiles seamlessly.
* **Persistent Storage:** Safely saves student records across sessions.
* **Export Capabilities:** Export your records instantly into standard formats like [students.json](https://github.com/uzma0786/Student_records_persistance_and_export_system/blob/main/students.json) and [students.csv](https://github.com/uzma0786/Student_records_persistance_and_export_system/blob/main/students.csv).
* **Activity Tracking:** Automatically records operational history and changes in [activity_log.txt](https://github.com/uzma0786/Student_records_persistance_and_export_system/blob/main/activity_log.txt).

## Project Structure

```text
Student_records_persistance_and_export_system/
│
├── main.py             # Core script containing the application logic
├── students.json       # JSON-based data store for student records
├── students.csv        # CSV-based export/data store file
└── activity_log.txt    # Log file tracking system activity and updates
