# 🗄️ Database Access - Complete Guide

## 📋 All Your Tables

Your project has **12 tables** across **4 databases**:

```
users.db
├── users (10 rows)
├── sessions (0 rows)
├── api_tokens (1 row)
└── sqlite_sequence

predictions.db
├── predictions (56 rows)
└── sqlite_sequence

appointments.db
├── appointments (8 rows)
├── doctor_availability (57 rows)
├── doctor_locations (13 rows)
└── sqlite_sequence

audit.db
├── audit_log (49 rows)
└── sqlite_sequence
```

---

## ⚡ Quick Commands

### See All Tables
```bash
python list_all_tables.py
```

### Interactive Browser (Recommended)
```bash
python sqlite_browser.py
```

### Quick Query
```bash
python quick_query.py users "SELECT * FROM users LIMIT 5"
```

### View All Schemas
```bash
python show_all_schemas.py
```

---

## 📚 Documentation

| File | Description |
|------|-------------|
| **DATABASE_INDEX.md** | Central hub - start here |
| **TABLES_QUICK_REFERENCE.md** | Quick table overview |
| **TABLES_SUMMARY.md** | Complete table details |
| **DATABASE_GUIDE.md** | Full usage guide |
| **SQLITE_TOOLS_README.md** | Tools documentation |

---

## 🛠️ Tools Available

| Tool | Command |
|------|---------|
| Interactive Browser | `python sqlite_browser.py` |
| Direct Access | `python open_database.py users` |
| Quick Query | `python quick_query.py users "SQL"` |
| Schema Viewer | `python show_all_schemas.py` |
| Table Lister | `python list_all_tables.py` |
| Windows Menu | `show_tables.bat` |

---

## 📊 Database Summary

| Database | Size | Tables | Records |
|----------|------|--------|---------|
| users.db | 36 KB | 4 | 13 |
| predictions.db | 68 KB | 2 | 57 |
| appointments.db | 20 KB | 4 | 81 |
| audit.db | 40 KB | 2 | 50 |
| **TOTAL** | **164 KB** | **12** | **201** |

---

## 🎯 Common Queries

### View Users
```bash
python quick_query.py users "SELECT username, email, role FROM users"
```

### Recent Predictions
```bash
python quick_query.py predictions "SELECT * FROM predictions ORDER BY timestamp DESC LIMIT 10"
```

### Pending Appointments
```bash
python quick_query.py appointments "SELECT * FROM appointments WHERE status='pending'"
```

### Audit Logs
```bash
python quick_query.py audit "SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT 20"
```

---

## 🚀 Getting Started

1. **List all tables:**
   ```bash
   python list_all_tables.py
   ```

2. **Explore interactively:**
   ```bash
   python sqlite_browser.py
   > connect 1
   > tables
   > view users 10
   ```

3. **Read documentation:**
   - Start with **DATABASE_INDEX.md**
   - Check **TABLES_QUICK_REFERENCE.md** for quick info

---

**Need Help?** Check **DATABASE_INDEX.md** for complete documentation index.
