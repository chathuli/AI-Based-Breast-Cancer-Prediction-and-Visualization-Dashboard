"""
Quick SQL Query Runner
Usage: python quick_query.py <database> "<SQL query>"
Example: python quick_query.py users "SELECT * FROM users LIMIT 5"
"""
import sqlite3
import sys
from tabulate import tabulate

def run_query(db_name, query):
    """Execute a quick query on specified database"""
    databases = {
        'users': 'data/users.db',
        'predictions': 'data/predictions.db',
        'appointments': 'data/appointments.db',
        'audit': 'data/audit.db'
    }
    
    if db_name not in databases:
        print(f"❌ Unknown database: {db_name}")
        print(f"Available: {', '.join(databases.keys())}")
        return
    
    db_path = databases[db_name]
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print(f"\n📊 Executing on {db_name}.db:")
        print(f"Query: {query}\n")
        
        cursor.execute(query)
        
        if query.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
            if results:
                columns = [desc[0] for desc in cursor.description]
                print(tabulate(results, headers=columns, tablefmt='grid'))
                print(f"\n✓ {len(results)} rows returned")
            else:
                print("✓ No results")
        else:
            conn.commit()
            print(f"✓ Query executed. Rows affected: {cursor.rowcount}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ SQL Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python quick_query.py <database> \"<SQL query>\"")
        print("\nExamples:")
        print('  python quick_query.py users "SELECT * FROM users LIMIT 5"')
        print('  python quick_query.py predictions "SELECT COUNT(*) FROM predictions"')
        print('  python quick_query.py appointments "SELECT * FROM appointments WHERE status=\'pending\'"')
        print("\nAvailable databases: users, predictions, appointments, audit")
    else:
        db_name = sys.argv[1]
        query = sys.argv[2]
        run_query(db_name, query)
