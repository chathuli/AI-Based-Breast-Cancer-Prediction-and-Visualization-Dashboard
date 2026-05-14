"""
Interactive SQLite Database Browser
Allows you to query and explore your SQLite databases
"""
import sqlite3
import os
from tabulate import tabulate

class SQLiteBrowser:
    def __init__(self):
        self.databases = {
            '1': ('users.db', 'data/users.db'),
            '2': ('predictions.db', 'data/predictions.db'),
            '3': ('appointments.db', 'data/appointments.db'),
            '4': ('audit.db', 'data/audit.db')
        }
        self.current_db = None
        self.conn = None
        self.cursor = None
    
    def show_databases(self):
        """Display available databases"""
        print("\n" + "="*80)
        print("AVAILABLE DATABASES")
        print("="*80)
        for key, (name, path) in self.databases.items():
            exists = "✓" if os.path.exists(path) else "✗"
            size = f"{os.path.getsize(path)/1024:.2f} KB" if os.path.exists(path) else "N/A"
            print(f"  {key}. {name:<20} {exists} ({size})")
        print("="*80)
    
    def connect_database(self, choice):
        """Connect to selected database"""
        if choice not in self.databases:
            print("❌ Invalid choice!")
            return False
        
        name, path = self.databases[choice]
        if not os.path.exists(path):
            print(f"❌ Database not found: {path}")
            return False
        
        try:
            if self.conn:
                self.conn.close()
            
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
            self.current_db = name
            print(f"\n✓ Connected to: {name}")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error connecting: {e}")
            return False
    
    def show_tables(self):
        """Show all tables in current database"""
        if not self.conn:
            print("❌ No database connected!")
            return
        
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = self.cursor.fetchall()
        
        print(f"\n📋 TABLES IN {self.current_db}:")
        print("-" * 80)
        for i, (table,) in enumerate(tables, 1):
            self.cursor.execute(f"SELECT COUNT(*) FROM {table};")
            count = self.cursor.fetchone()[0]
            print(f"  {i}. {table:<30} ({count} rows)")
        print("-" * 80)
    
    def describe_table(self, table_name):
        """Show table structure"""
        if not self.conn:
            print("❌ No database connected!")
            return
        
        try:
            self.cursor.execute(f"PRAGMA table_info({table_name});")
            columns = self.cursor.fetchall()
            
            print(f"\n📋 TABLE STRUCTURE: {table_name}")
            print("-" * 80)
            headers = ['ID', 'Column', 'Type', 'Not Null', 'Default', 'PK']
            print(tabulate(columns, headers=headers, tablefmt='grid'))
        except sqlite3.Error as e:
            print(f"❌ Error: {e}")
    
    def execute_query(self, query):
        """Execute SQL query"""
        if not self.conn:
            print("❌ No database connected!")
            return
        
        try:
            self.cursor.execute(query)
            
            # If it's a SELECT query, fetch and display results
            if query.strip().upper().startswith('SELECT'):
                results = self.cursor.fetchall()
                if results:
                    # Get column names
                    columns = [description[0] for description in self.cursor.description]
                    print(f"\n📊 QUERY RESULTS ({len(results)} rows):")
                    print("-" * 80)
                    print(tabulate(results, headers=columns, tablefmt='grid'))
                else:
                    print("\n✓ Query executed successfully. No results returned.")
            else:
                self.conn.commit()
                print(f"\n✓ Query executed successfully. Rows affected: {self.cursor.rowcount}")
        
        except sqlite3.Error as e:
            print(f"❌ SQL Error: {e}")
    
    def quick_view(self, table_name, limit=10):
        """Quick view of table data"""
        query = f"SELECT * FROM {table_name} LIMIT {limit};"
        print(f"\n📊 Showing first {limit} rows from {table_name}:")
        self.execute_query(query)
    
    def show_help(self):
        """Show available commands"""
        print("\n" + "="*80)
        print("AVAILABLE COMMANDS")
        print("="*80)
        print("  databases          - Show available databases")
        print("  connect <number>   - Connect to database (e.g., 'connect 1')")
        print("  tables             - Show all tables in current database")
        print("  describe <table>   - Show table structure")
        print("  view <table> [n]   - View first n rows (default 10)")
        print("  query <SQL>        - Execute custom SQL query")
        print("  help               - Show this help message")
        print("  exit               - Exit the browser")
        print("="*80)
        print("\nExample queries:")
        print("  query SELECT * FROM users WHERE role='admin';")
        print("  query SELECT COUNT(*) FROM predictions;")
        print("  query SELECT * FROM appointments WHERE status='pending';")
        print("="*80)
    
    def run(self):
        """Main interactive loop"""
        print("\n" + "="*80)
        print("SQLite DATABASE BROWSER")
        print("="*80)
        print("Type 'help' for available commands")
        
        self.show_databases()
        
        while True:
            try:
                if self.current_db:
                    prompt = f"\n[{self.current_db}]> "
                else:
                    prompt = "\n> "
                
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                parts = command.split(maxsplit=1)
                cmd = parts[0].lower()
                args = parts[1] if len(parts) > 1 else ""
                
                if cmd == 'exit' or cmd == 'quit':
                    print("\n👋 Goodbye!")
                    break
                
                elif cmd == 'help':
                    self.show_help()
                
                elif cmd == 'databases':
                    self.show_databases()
                
                elif cmd == 'connect':
                    if args:
                        self.connect_database(args)
                        if self.conn:
                            self.show_tables()
                    else:
                        print("❌ Usage: connect <number>")
                
                elif cmd == 'tables':
                    self.show_tables()
                
                elif cmd == 'describe':
                    if args:
                        self.describe_table(args)
                    else:
                        print("❌ Usage: describe <table_name>")
                
                elif cmd == 'view':
                    if args:
                        parts = args.split()
                        table = parts[0]
                        limit = int(parts[1]) if len(parts) > 1 else 10
                        self.quick_view(table, limit)
                    else:
                        print("❌ Usage: view <table_name> [limit]")
                
                elif cmd == 'query':
                    if args:
                        self.execute_query(args)
                    else:
                        print("❌ Usage: query <SQL statement>")
                
                else:
                    print(f"❌ Unknown command: {cmd}. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
        
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    try:
        browser = SQLiteBrowser()
        browser.run()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
