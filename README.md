# ERP System - Purchase Order (PO) Management System

A comprehensive microservices-based Purchase Order (PO) Management System built to integrate Vendors, Products, and Orders.

## Architecture

This system has been built using a Docker Compose microservices architecture:
1. **Frontend**: Static HTML/CSS/JS served via Nginx (Port 80).
2. **PO Service**: Python / FastAPI backend focusing on Products, POs, and AI descriptions (Port 8000).
3. **Vendor Service (Bonus)**: Java / Spring Boot backend managing Vendor resources (Port 8080).
4. **Notification Service (Bonus)**: Node.js / Socket.io server to broadcast real-time PO creation events (Port 3000).
5. **Database Layer**:
   - **PostgreSQL**: Primary relational database handling Vendors, Products, and POs (Port 5432).
   - **MongoDB (Bonus)**: Document store logging all generated AI marketing descriptions (Port 27017).

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- **Docker**: Specifically, Docker Desktop (Mac/Windows) or Docker Engine (Linux).
- **Docker Compose**: Included with most modern Docker Desktop installations.

---

## How to Run from Scratch

**Step 1. Clone/Navigate to the Directory**
Ensure your terminal is in the root directory where the `docker-compose.yml` file is located:
```bash
cd iv-innovations-task
```

**Step 2. Build and Start the Containers**
This powerful command will download the necessary base images, execute all the multi-stage compilations (like building the Spring Boot `.jar` via Maven and installing Python packages), and boot up the system cleanly:
```bash
docker compose up --build
```
*Note: The first compilation might take a couple of minutes depending on your internet speed.*

**Step 3. Verify the Services are Running**
Wait until the terminal stops scrolling heavily and indicates the services have started. You are good to go!
- Access the **Frontend Dashboard**: `http://localhost:80` (or simply `http://localhost`)
- Access the **FastAPI Swagger UI**: `http://localhost:8000/docs`
- Access the **Vendor API**: `http://localhost:8080/vendors`

**Step 4. Shutting Down**
To cleanly shut down the services, press `Ctrl+C` in your terminal. You can also run:
```bash
docker compose down
```

---

## Database Design Logic (PostgreSQL)

The primary relational database is designed using three main interconnected entities to ensure data integrity and normalized interactions:

1. **Vendors Table**:
   - `id` (Primary Key), `name`, `contact`, `rating`.
   - Used for the Java microservice independently.

2. **Products Table**:
   - `id` (Primary Key), `name`, `sku` (Unique), `unit_price`, `stock_level`.
   - Central repository fetched iteratively to dynamically list options in the Create PO Form.

3. **PurchaseOrders & PurchaseOrderItems Tables**:
   - **`PurchaseOrders`**: `id`, `reference_no` (Unique), `vendor_id` (Foreign Key linking to Vendors), `total_amount`, `status`.
   - **`PurchaseOrderItems`**: `id`, `po_id` (Foreign Key -> PurchaseOrders ON DELETE CASCADE), `product_id` (Foreign Key -> Products), `quantity`, `unit_price`.
   - *Logic flow*: A `PurchaseOrder` has a one-to-many relationship with `PurchaseOrderItems`. When a PO is submitted from the frontend, the FastAPI backend iterates over the selected item rows, binds their associated primary product IDs to the overarching `po_id`, and calculates the 5% tax iteratively to determine and insert the final `total_amount`.

---

## Extra Features Showcased
- **AI Auto-Description Integration**: Using a simulated API prompt to formulate dynamic responses and dumping raw JSON copies to the NoSQL MongoDB instance asynchronously.
- **Dynamic Frontend Row Handling**: Real-time stock visibility and auto-calc row additions in pure Vanilla Javascript.
