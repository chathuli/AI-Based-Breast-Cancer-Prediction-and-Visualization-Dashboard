"""
Script to display all database schemas from the project
"""
import sqlite3
import os
from pathlib import Path

def get_table_schema(db_path, db_name):
    """Get schema information for all tables in a database"""
    if not os.path.exists(db_path):
        print(f"\n❌ Database not found: {db_name}")
        return
    
    print(f"\n{'='*80}")
    print(f"DATABASE: {db_name}")
    print(f"Path: {db_path}")
    print(f"{'='*80}")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = cursor.fetchall()
        
        if not tables:
            print("  No tables found in this database.")
            return
        
        for (table_name,) in tables:
            print(f"\n📋 TABLE: {table_name}")
            print("-" * 80)
            
            # Get table schema
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            print(f"{'Column':<25} {'Type':<15} {'Not Null':<10} {'Default':<15} {'PK':<5}")
            print("-" * 80)
            
            for col in columns:
                cid, name, col_type, not_null, default_val, pk = col
                not_null_str = "YES" if not_null else "NO"
                default_str = str(default_val) if default_val is not None else "NULL"
                pk_str = "YES" if pk else "NO"
                print(f"{name:<25} {col_type:<15} {not_null_str:<10} {default_str:<15} {pk_str:<5}")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"\n  📊 Total rows: {count}")
            
            # Get indexes
            cursor.execute(f"PRAGMA index_list({table_name});")
            indexes = cursor.fetchall()
            if indexes:
                print(f"\n  🔑 Indexes:")
                for idx in indexes:
                    print(f"    - {idx[1]} (Unique: {bool(idx[2])})")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"  ❌ Error reading database: {e}")

def main():
    """Main function to display all database schemas"""
    print("\n" + "="*80)
    print("DATABASE SCHEMA VIEWER")
    print("="*80)
    
    # Define all databases in the project
    databases = {
        'users.db': 'data/users.db',
        'predictions.db': 'data/predictions.db',
        'appointments.db': 'data/appointments.db',
        'audit.db': 'data/audit.db'
    }
    
    # Check which databases exist
    existing_dbs = []
    for name, path in databases.items():
        if os.path.exists(path):
            existing_dbs.append((name, path))
    
    if not existing_dbs:
        print("\n❌ No databases found in the data/ folder.")
        return
    
    print(f"\nFound {len(existing_dbs)} database(s):")
    for name, path in existing_dbs:
        size = os.path.getsize(path) / 1024  # Size in KB
        print(f"  ✓ {name} ({size:.2f} KB)")
    
    # Display schema for each database
    for name, path in existing_dbs:
        get_table_schema(path, name)
    
    print("\n" + "="*80)
    print("SCHEMA DISPLAY COMPLETE")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
