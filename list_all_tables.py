"""
List all table names from all databases
"""
import sqlite3
import os

def list_tables(db_path, db_name):
    """Get all table names from a database"""
    if not os.path.exists(db_path):
        return []
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = cursor.fetchall()
        conn.close()
        return [table[0] for table in tables]
    except:
        return []

def main():
    print("\n" + "="*80)
    print("ALL DATABASE TABLES")
    print("="*80 + "\n")
    
    databases = {
        'users.db': 'data/users.db',
        'predictions.db': 'data/predictions.db',
        'appointments.db': 'data/appointments.db',
        'audit.db': 'data/audit.db'
    }
    
    all_tables = []
    
    for db_name, db_path in databases.items():
        if os.path.exists(db_path):
            tables = list_tables(db_path, db_name)
            
            print(f"📁 {db_name}")
            print("-" * 80)
            
            if tables:
                for i, table in enumerate(tables, 1):
                    print(f"   {i}. {table}")
                    all_tables.append(f"{db_name}.{table}")
            else:
                print("   (no tables)")
            print()
    
    print("="*80)
    print(f"Total tables: {len(all_tables)}")
    print("="*80 + "\n")
    
    # Save to file
    with open('all_tables_list.txt', 'w', encoding='utf-8') as f:
        f.write("All Database Tables\n")
        f.write("="*80 + "\n\n")
        for table in all_tables:
            f.write(f"{table}\n")
    
    print("✓ Table list saved to: all_tables_list.txt\n")

if __name__ == "__main__":
    main()
