# ASM Clinic — Clinic Management System

A desktop clinic management system built with **Python (PyQt5)** on a **Microsoft SQL Server** database. It was developed as a DBMS semester project and covers the day-to-day workflow of a small clinic: registering patients, booking visits, doctor checkups with diagnoses and prescriptions, and managing doctors, staff and medicine/test inventory.

## Features

The app opens on a login screen and routes each user to their own panel based on their role.

### Admin
- **Dashboard** — totals for patients, doctors and staff, average daily visits, and Matplotlib charts (e.g. patient gender distribution).
- **Patients** — full patient management (via the reception screens).
- **Doctors** — add, update and view doctors, including license number, salary, address and login credentials.
- **Staff** — add, update and view staff members and their roles.
- **Inventory** — add, update, view and delete medicines and medical tests.

### Receptionist
- Add, update, delete and view patients.
- Look up returning patients and generate a new visit with a doctor.

### Doctor
- Search a patient by **Visit ID**.
- **Patient Data** — view the patient's details.
- **Diagnosis** — searchable lists to record symptoms and diagnoses for the visit.
- **Medicine and Test** — prescribe medicines and order tests.
- **Slip** — view the visit history / prescription slip.

## Tech Stack

| Layer      | Technology                                |
|------------|-------------------------------------------|
| GUI        | PyQt5                                     |
| Charts     | Matplotlib, NumPy                         |
| Database   | Microsoft SQL Server (Express)            |
| DB driver  | pyodbc + ODBC Driver 17 for SQL Server    |
| Packaging  | PyInstaller (`main.spec`)                 |

## Database

`SemesterPRojectDB.sql` creates the `DB_HMS` database with 17 tables, seed data and stored procedures.

- **People:** `TblPatients`, `TblDoctors`, `TblStaff`, `TblRoles`, `TblCredentials`, `TblAddress`, `TblSalary`
- **Visits & billing:** `TblVisits`, `TblPayments`
- **Clinical:** `TblSymptoms`, `TblDiagnoses`, `TblVisitSymptoms`, `TblVisitDiagnoses`
- **Inventory & prescriptions:** `TblMedicines`, `TblTests`, `TblPrescriptions`, `TblTestPrescriptions`
- **Stored procedures:** name search for medicines, tests, symptoms and diagnoses, plus ID/role lookups (`GetDoctors`, `GetRoleID`, `GetMedID`, …)

Roles are seeded as `1 = Admin`, `2 = Receptionist`, `3 = Doctor`.

## Getting Started

### Prerequisites
- Windows with **Python 3.12**
- **SQL Server** (Express is fine) and **SQL Server Management Studio**
- **ODBC Driver 17 for SQL Server**

### 1. Set up the database
Open `SemesterPRojectDB.sql` in SSMS and run it. This creates `DB_HMS` with all tables, seed data and procedures.

The script does not create any login accounts, so add one before signing in, for example an admin:

```sql
USE DB_HMS;
INSERT INTO TblCredentials (Username, PasswordHash, RoleID) VALUES ('admin', 'admin123', 1);
```

> The login screen currently compares the password as entered, so store it as plain text in `PasswordHash`.

### 2. Point the app at your SQL Server
Edit `DatabaseConnection.py` and set `server` to your own instance name:

```python
server = r'YOUR-PC-NAME\SQLEXPRESS'
database = 'DB_HMS'
```

The connection uses Windows Authentication (`Trusted_Connection=yes`), so no password is needed.

### 3. Install dependencies and run

```bash
pip install PyQt5 pyodbc matplotlib numpy
python main.py
```

### Building an .exe (optional)

```bash
pip install pyinstaller
pyinstaller main.spec
```

The executable is written to `dist/`.

## Project Structure

```
├── main.py                  # Entry point
├── mainwindow.py            # Main window, role-based navigation
├── loginpage.py / loginbackend.py
├── DatabaseConnection.py    # SQL Server connection settings
├── AdminScreen.py           # Admin panel and sidebar
├── adminsidebar/            # Admin sidebar buttons
├── dashboard.py             # Admin dashboard with charts
├── ReceptionScreen.py       # Receptionist panel
├── add_/update_/delete_/view_patient_data.py
├── appointment_patient_data.py   # Create visits
├── DoctorScreen.py          # Doctor panel
├── patient_data_page.py, diagnosis_page.py, medicine_page.py, history_page.py
├── DoctorScreenBackend.py, diagnosisBackend.py, medicineBackend.py
├── Doctorsdata/             # Doctor management (admin)
├── Staffdata/               # Staff management (admin)
├── Inventory/               # Medicine and test inventory (admin)
├── Pictures/                # Images used by the UI
├── SemesterPRojectDB.sql    # Database schema, seed data, procedures
└── main.spec                # PyInstaller build config
```

## Author

**Suleman Saleh** — DBMS Semester Project, 4th semester.
