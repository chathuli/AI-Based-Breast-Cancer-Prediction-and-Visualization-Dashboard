"""
Quick test to demonstrate SQLite browser functionality
"""
import sqlite3
from tabulate import tabulate

# Test connection to users database
print("\n" + "="*80)
print("TESTING SQLite DATABASE ACCESS")
print("="*80)

db_path = 'data/users.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Show tables
print("\n📋 Tables in users.db:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
tables = cursor.fetchall()
for table, in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table};")
    count = cursor.fetchone()[0]
    print(f"  - {table:<20} ({count} rows)")

# Show sample data from users table
print("\n📊 Sample Users:")
cursor.execute("SELECT id, username, email, role, is_active FROM users LIMIT 5;")
results = cursor.fetchall()
headers = ['ID', 'Username', 'Email', 'Role', 'Active']
print(tabulate(results, headers=headers, tablefmt='grid'))

conn.close()

print("\n✓ Database access working correctly!")
print("\n" + "="*80)
print("HOW TO USE YOUR DATABASES:")
print("="*80)
print("\n1. INTERACTIVE BROWSER (Recommended):")
print("   python sqlite_browser.py")
print("\n2. OPEN SPECIFIC DATABASE:")
print("   python open_database.py users")
print("   python open_database.py predictions")
print("   python open_database.py appointments")
print("   python open_database.py audit")
print("\n3. DOUBLE-CLICK BATCH FILE:")
print("   open_sqlite.bat")
print("\n4. USE EXTERNAL TOOLS:")
print("   - DB Browser for SQLite: https://sqlitebrowser.org/")
print("   - VS Code SQLite extension")
print("="*80 + "\n")
