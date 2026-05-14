"""
Quick script to open and query a specific SQLite database
Usage: python open_database.py [database_name]
Example: python open_database.py users.db
"""
import sqlite3
import sys
import os
from tabulate import tabulate

def open_database(db_path):
    """Open database and start interactive session"""
    if not os.path.exists(db_path):
        print(f"❌ Database not found: {db_path}")
        return
    
    print(f"\n{'='*80}")
    print(f"Opening: {db_path}")
    print(f"Size: {os.path.getsize(db_path)/1024:.2f} KB")
    print(f"{'='*80}\n")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Show tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    tables = cursor.fetchall()
    
    print("📋 Available Tables:")
    for i, (table,) in enumerate(tables, 1):
        cursor.execute(f"SELECT COUNT(*) FROM {table};")
        count = cursor.fetchone()[0]
        print(f"  {i}. {table:<30} ({count} rows)")
    
    print(f"\n{'='*80}")
    print("Enter SQL queries (or 'exit' to quit)")
    print("Quick commands:")
    print("  .tables              - List all tables")
    print("  .schema <table>      - Show table structure")
    print("  SELECT * FROM <table> LIMIT 10;  - View data")
    print(f"{'='*80}\n")
    
    while True:
        try:
            query = input(f"[{os.path.basename(db_path)}]> ").strip()
            
            if not query:
                continue
            
            if query.lower() in ['exit', 'quit', '.exit', '.quit']:
                break
            
            # Handle special commands
            if query == '.tables':
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
                tables = cursor.fetchall()
                print("\nTables:")
                for table, in tables:
                    print(f"  - {table}")
                continue
            
            if query.startswith('.schema'):
                parts = query.split()
                if len(parts) > 1:
                    table_name = parts[1]
                    cursor.execute(f"PRAGMA table_info({table_name});")
                    columns = cursor.fetchall()
                    headers = ['ID', 'Column', 'Type', 'Not Null', 'Default', 'PK']
                    print(f"\nStructure of {table_name}:")
                    print(tabulate(columns, headers=headers, tablefmt='grid'))
                else:
                    print("Usage: .schema <table_name>")
                continue
            
            # Execute query
            cursor.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                if results:
                    columns = [desc[0] for desc in cursor.description]
                    print(f"\n📊 Results ({len(results)} rows):")
                    print(tabulate(results, headers=columns, tablefmt='grid'))
                else:
                    print("✓ No results")
            else:
                conn.commit()
                print(f"✓ Query executed. Rows affected: {cursor.rowcount}")
        
        except sqlite3.Error as e:
            print(f"❌ SQL Error: {e}")
        except KeyboardInterrupt:
            print("\n")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    conn.close()
    print("\n👋 Database closed.\n")

if __name__ == "__main__":
    # Database paths
    databases = {
        'users': 'data/users.db',
        'predictions': 'data/predictions.db',
        'appointments': 'data/appointments.db',
        'audit': 'data/audit.db'
    }
    
    if len(sys.argv) > 1:
        db_name = sys.argv[1].lower().replace('.db', '')
        if db_name in databases:
            open_database(databases[db_name])
        else:
            # Try as direct path
            if os.path.exists(sys.argv[1]):
                open_database(sys.argv[1])
            else:
                print(f"❌ Unknown database: {sys.argv[1]}")
                print(f"\nAvailable databases:")
                for name in databases.keys():
                    print(f"  - {name}")
    else:
        print("Usage: python open_database.py <database_name>")
        print("\nAvailable databases:")
        for name, path in databases.items():
            exists = "✓" if os.path.exists(path) else "✗"
            print(f"  - {name:<15} {exists}")
        print("\nExample: python open_database.py users")
