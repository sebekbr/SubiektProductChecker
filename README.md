# Subiekt Product Checker (SPC)

Internal warehouse/product verification system designed for ERP-assisted inventory workflows using Subiekt GT.

The application was created to improve product verification processes in a real warehouse environment by providing fast barcode/SKU/name-based product lookup, inventory validation and ERP data access through a touchscreen terminal.

## 🎯 Business Problem

In daily warehouse operations, employees needed a fast and reliable way to verify products and product metadata directly from the ERP database.

The existing workflow was too slow and required manual navigation through the ERP system.

SPC was designed as a lightweight touchscreen terminal/mobile application to simplify and accelerate this process.

## :white_check_mark: Solution Overview

SPC is a Django-based internal application connected to the Subiekt GT ERP database.

The system allows warehouse employees to:
- scan or search products,
- verify product data,
- access stock information,
- simplify warehouse verification workflows.

The application was deployed on a small touchscreen terminal connected to the local network.
Works also on mobiles via local WiFi.

## ⚙️ How it works

- Connects directly to **MS SQL Server** via **ODBC** (pyodbc)
- Reads product data and images stored as **base64** in the Subiekt GT database
- Decodes and renders images on the fly — no separate image storage needed
- Served via Django on a local network; Currently deployed on a **Lenovo SFF** (i3-4130T, 4GB RAM, 120 GB SSD)
  with 17" touchscreen HP L6017tm (also tested on AWS EC2) - it will work on most devices

## :open_book: Lessons Learned

This project improved my understanding of:
- ERP database structures,
- business process optimization,
- Django-based internal tooling,
- SQL-based integrations,
- decoding images directly from DB
- infrastructure planning for internal systems.

## :soon: Future Improvements
- Docker deployment,
- items history info
- file logging,

## :computer: Screens
- Ready-To-Work
![desription](img/ready_to_work.jpg)
- Main View
![desription](img/spc_main_view.png)
- Search result
![description](img/search_result.png)
- Item details
![description](img/item_details.png)
- spc_service Console
![description](img/spc_service_console.png)

## 🛠 Tech stack

- Windows Server
- Python 3 / Django
- MS SQL Server (Subiekt GT database)
- pyodbc / ODBC connection
- Bootstrap 5
- SQLite3 (local session/config data)

## 📁 Key files

| File | Description |
|------|-------------|
| `SPC.sql` | SQL view/query used to fetch product + image data from Subiekt GT |
| `zdjecie.py` | Base64 image decoding logic |
| `tabele.py` | MS SQL table mapping helpers |
| `spc_service.bat` | Windows batch script to run as a background service |

## 🚀 Setup

1. Configure your ODBC connection to MS SQL Server in `settings.py`
2. Run `pip install -r requirements.txt`
3. Run `python manage.py runserver 0.0.0.0:8000`
4. Access from any device on the local network

> **Note:** Requires access to a Subiekt GT MS SQL database. 
> Not compatible with Subiekt nexo (different schema).

## 📌 Status

Deployed and in active use since 2023.
