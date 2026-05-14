# 📊 SQLite Database Access Guide

## Your Databases

Your project has 4 SQLite databases in the `data/` folder:

1. **users.db** - User accounts, sessions, API tokens
2. **predictions.db** - Breast cancer prediction records
3. **appointments.db** - Patient appointments and doctor schedules
4. **audit.db** - System audit logs

---

## 🚀 Quick Start Methods

### Method 1: Interactive Browser (Recommended)
The easiest way to explore your databases with a command-line interface.

```bash
python sqlite_browser.py
```

**Features:**
- Browse all databases
- View table structures
- Execute custom SQL queries
- Quick data preview
- Interactive command prompt

**Example Session:**
```
> connect 1              # Connect to users.db
> tables                 # List all tables
> view users 5           # View first 5 users
> describe users         # Show table structure
> query SELECT * FROM users WHERE role='admin';
> exit
```

---

### Method 2: Open Specific Database
Directly open a specific database for quick queries.

```bash
python open_database.py users
python open_database.py predictions
python open_database.py appointments
python open_database.py audit
```

**Features:**
- Direct access to specific database
- SQL query execution
- Special commands (.tables, .schema)

**Example Commands:**
```sql
SELECT * FROM users LIMIT 10;
SELECT COUNT(*) FROM predictions;
SELECT * FROM appointments WHERE status='pending';
.tables                  # List all tables
.schema users           # Show table structure
```

---

### Method 3: Batch File Launcher
Double-click `open_sqlite.bat` for a menu-driven interface.

**Menu Options:**
1. Interactive Browser
2. Open Users Database
3. Open Predictions Database
4. Open Appointments Database
5. Open Audit Database

---

### Method 4: View All Schemas
See the structure of all databases at once.

```bash
python show_all_schemas.py
```

---

## 📝 Common SQL Queries

### Users Database
```sql
-- View all users
SELECT * FROM users;

-- Find admin users
SELECT * FROM users WHERE role='admin';

-- Count users by role
SELECT role, COUNT(*) FROM users GROUP BY role;

-- View active sessions
SELECT * FROM sessions WHERE expires_at > datetime('now');

-- Check API tokens
SELECT * FROM api_tokens WHERE is_active=1;
```

### Predictions Database
```sql
-- View recent predictions
SELECT * FROM predictions ORDER BY timestamp DESC LIMIT 10;

-- Count predictions by result
SELECT prediction_label, COUNT(*) 
FROM predictions 
GROUP BY prediction_label;

-- View high-confidence predictions
SELECT * FROM predictions WHERE confidence > 0.9;

-- Predictions by user
SELECT user_id, COUNT(*) as total_predictions
FROM predictions 
GROUP BY user_id;
```

### Appointments Database
```sql
-- View upcoming appointments
SELECT * FROM appointments 
WHERE appointment_date >= date('now')
ORDER BY appointment_date, appointment_time;

-- Appointments by status
SELECT status, COUNT(*) FROM appointments GROUP BY status;

-- Doctor availability
SELECT * FROM doctor_availability WHERE is_active=1;

-- Doctor locations
SELECT * FROM doctor_locations WHERE is_active=1;
```

### Audit Database
```sql
-- Recent audit logs
SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT 20;

-- Failed login attempts
SELECT * FROM audit_log 
WHERE action='login' AND status='failure';

-- User activity
SELECT username, action, COUNT(*) as count
FROM audit_log 
GROUP BY username, action
ORDER BY count DESC;

-- Logs by date
SELECT DATE(timestamp) as date, COUNT(*) as events
FROM audit_log 
GROUP BY DATE(timestamp)
ORDER BY date DESC;
```

---

## 🛠️ External Tools (Optional)

### DB Browser for SQLite (GUI Tool)
**Download:** https://sqlitebrowser.org/

**Features:**
- Visual table browser
- Query builder
- Schema designer
- Data editing
- Export/Import

**How to use:**
1. Download and install DB Browser
2. Open the application
3. Click "Open Database"
4. Navigate to your `data/` folder
5. Select any `.db` file

### VS Code SQLite Extension
**Extension:** SQLite Viewer or SQLite

**How to use:**
1. Install extension from VS Code marketplace
2. Right-click any `.db` file in VS Code
3. Select "Open Database"

---

## 🔍 Database Schema Summary

### users.db
- **users** - User accounts (username, email, password_hash, role)
- **sessions** - Active user sessions
- **api_tokens** - API authentication tokens

### predictions.db
- **predictions** - Prediction records with features, confidence, and results

### appointments.db
- **appointments** - Patient appointments
- **doctor_availability** - Doctor schedule slots
- **doctor_locations** - Doctor practice locations

### audit.db
- **audit_log** - System activity logs (user actions, timestamps, IP addresses)

---

## 💡 Tips

1. **Always use LIMIT** when exploring large tables:
   ```sql
   SELECT * FROM predictions LIMIT 10;
   ```

2. **Check row counts** before querying:
   ```sql
   SELECT COUNT(*) FROM table_name;
   ```

3. **Use WHERE clauses** to filter data:
   ```sql
   SELECT * FROM users WHERE role='doctor';
   ```

4. **Order results** for better readability:
   ```sql
   SELECT * FROM appointments ORDER BY appointment_date DESC;
   ```

5. **Backup before modifications**:
   ```bash
   copy data\users.db data\users_backup.db
   ```

---

## 🚨 Safety Notes

- The scripts open databases in **read-write mode**
- Be careful with UPDATE, DELETE, and DROP commands
- Always backup before making changes
- Use transactions for multiple changes:
  ```sql
  BEGIN TRANSACTION;
  -- your queries here
  COMMIT;  -- or ROLLBACK; to undo
  ```

---

## 📚 Additional Resources

- SQLite Documentation: https://www.sqlite.org/docs.html
- SQL Tutorial: https://www.w3schools.com/sql/
- SQLite Browser: https://sqlitebrowser.org/

---

**Created:** May 9, 2026
**Project:** AI-Based Breast Cancer Prediction Dashboard
