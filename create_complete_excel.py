"""
Generate Complete Excel File with All Testing Sheets
All sheets in one Excel file - English version
"""

import pandas as pd
from datetime import datetime
import os

def create_complete_testing_excel():
    """Create one Excel file with all testing sheets"""
    
    # Excel file name
    excel_file = 'testing/Complete_Testing_Documentation.xlsx'
    
    print("🚀 Creating Complete Excel Testing Documentation...")
    print("=" * 60)
    
    # Create Excel writer
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        
        # ==================== SHEET 1: Test Cases ====================
        print("📋 Sheet 1: Test Cases (60+ test cases)...")
        
        # Read from CSV
        test_cases_df = pd.read_csv('testing/Test_Cases_English.csv')
        test_cases_df.to_excel(writer, sheet_name='Test Cases', index=False)
        
        # ==================== SHEET 2: Bug Tracking ====================
        print("🐛 Sheet 2: Bug Tracking...")
        
        bug_tracking_df = pd.read_csv('testing/Bug_Tracking_English.csv')
        bug_tracking_df.to_excel(writer, sheet_name='Bug Tracking', index=False)
        
        # ==================== SHEET 3: Test Execution ====================
        print("📊 Sheet 3: Test Execution Tracker...")
        
        execution_df = pd.read_csv('testing/Test_Execution_Tracker_English.csv')
        execution_df.to_excel(writer, sheet_name='Test Execution', index=False)
        
        # ==================== SHEET 4: Test Summary ====================
        print("📈 Sheet 4: Test Summary...")
        
        summary_df = pd.read_csv('testing/Test_Summary_English.csv')
        summary_df.to_excel(writer, sheet_name='Test Summary', index=False)
        
        # ==================== SHEET 5: Test Scenarios ====================
        print("🎯 Sheet 5: Test Scenarios...")
        
        scenarios_df = pd.read_csv('testing/Test_Scenarios_English.csv')
        scenarios_df.to_excel(writer, sheet_name='Test Scenarios', index=False)
        
        # ==================== SHEET 6: Instructions ====================
        print("📖 Sheet 6: Instructions...")
        
        instructions_data = [
            ['SECTION', 'CONTENT'],
            ['', ''],
            ['🎯 OVERVIEW', 'This Excel file contains complete manual testing documentation for Breast Care +'],
            ['', ''],
            ['📋 SHEETS IN THIS FILE', ''],
            ['Sheet 1', 'Test Cases - 60+ detailed test cases with all information'],
            ['Sheet 2', 'Bug Tracking - Report and track bugs found during testing'],
            ['Sheet 3', 'Test Execution - Track daily test execution progress'],
            ['Sheet 4', 'Test Summary - Overall testing metrics and statistics'],
            ['Sheet 5', 'Test Scenarios - High-level test scenarios (end-to-end flows)'],
            ['Sheet 6', 'Instructions - This sheet with usage guidelines'],
            ['', ''],
            ['🚀 QUICK START', ''],
            ['Step 1', 'Start the application: python src/app.py'],
            ['Step 2', 'Open browser: http://localhost:5000'],
            ['Step 3', 'Go to Test Cases sheet'],
            ['Step 4', 'Start with TC001 (User Registration)'],
            ['Step 5', 'Follow test steps and record results'],
            ['Step 6', 'If bug found, report in Bug Tracking sheet'],
            ['', ''],
            ['📝 HOW TO USE TEST CASES SHEET', ''],
            ['1', 'Select a test case to execute (start with TC001)'],
            ['2', 'Read Preconditions and ensure they are met'],
            ['3', 'Follow Test Steps exactly as written'],
            ['4', 'Compare actual result with Expected Result'],
            ['5', 'Fill in: Status, Executed_By, Execution_Date, Actual_Result'],
            ['6', 'Mark Pass or Fail in Pass_Fail column'],
            ['7', 'If test fails, create bug report in Bug Tracking sheet'],
            ['', ''],
            ['🐛 HOW TO REPORT BUGS', ''],
            ['1', 'Take a screenshot of the error/issue'],
            ['2', 'Go to Bug Tracking sheet'],
            ['3', 'Add a new row'],
            ['4', 'Assign Bug_ID (BUG001, BUG002, etc.)'],
            ['5', 'Fill in all required fields'],
            ['6', 'Enter screenshot filename in Screenshots column'],
            ['7', 'Link to related test case in Related_Test_Case column'],
            ['8', 'Update Status as bug progresses (Open → Fixed → Verified → Closed)'],
            ['', ''],
            ['⚠️ SEVERITY LEVELS', ''],
            ['Critical', 'Application crash, data loss, security breach - Stop testing and report immediately'],
            ['High', 'Major feature not working, incorrect predictions - Report immediately'],
            ['Medium', 'Minor feature issues, UI problems - Report and continue testing'],
            ['Low', 'Cosmetic issues, spelling mistakes - Report for future fix'],
            ['', ''],
            ['🎯 PRIORITY LEVELS', ''],
            ['High', 'Fix immediately (blocks testing or critical functionality)'],
            ['Medium', 'Fix in current sprint (important but has workaround)'],
            ['Low', 'Fix when time permits (minor issues, nice-to-have)'],
            ['', ''],
            ['📊 DAILY WORKFLOW', ''],
            ['Morning', '1. Add today\'s date in Test Execution sheet'],
            ['', '2. Select 5-10 test cases to execute'],
            ['', '3. Execute tests and record results'],
            ['', '4. Report any bugs found'],
            ['Afternoon', '1. Continue executing test cases'],
            ['', '2. Retest any fixed bugs'],
            ['', '3. Update bug status'],
            ['', '4. Organize screenshots'],
            ['End of Day', '1. Update Test Summary sheet'],
            ['', '2. Calculate Pass/Fail count'],
            ['', '3. Plan tomorrow\'s testing'],
            ['', '4. Save and backup this file'],
            ['', ''],
            ['✅ TESTING TIPS', ''],
            ['Tip 1', 'Complete one test case before moving to next'],
            ['Tip 2', 'Write actual results for every test case'],
            ['Tip 3', 'Take screenshots for all bugs'],
            ['Tip 4', 'Write clear steps to reproduce bugs'],
            ['Tip 5', 'Document test data used'],
            ['Tip 6', 'Follow test steps exactly as written'],
            ['Tip 7', 'Don\'t skip preconditions'],
            ['Tip 8', 'Update Test Summary sheet daily'],
            ['', ''],
            ['🎯 TEST COVERAGE', ''],
            ['Total Test Cases', '60'],
            ['Authentication', '14 test cases (23.3%)'],
            ['Prediction', '7 test cases (11.7%)'],
            ['Dashboard', '6 test cases (10.0%)'],
            ['Appointments', '6 test cases (10.0%)'],
            ['Security', '5 test cases (8.3%)'],
            ['Profile', '4 test cases (6.7%)'],
            ['Usability', '4 test cases (6.7%)'],
            ['API', '3 test cases (5.0%)'],
            ['Performance', '3 test cases (5.0%)'],
            ['Database', '2 test cases (3.3%)'],
            ['Audit', '2 test cases (3.3%)'],
            ['Reports', '2 test cases (3.3%)'],
            ['Integration', '2 test cases (3.3%)'],
            ['', ''],
            ['📈 TESTING SCHEDULE', ''],
            ['Week 1', 'Authentication (TC001-TC014), Prediction (TC015-TC021), Security (TC041-TC045)'],
            ['Week 2', 'Dashboard (TC022-TC027), Appointments (TC028-TC033), API (TC038-TC040)'],
            ['Week 3', 'Profile (TC034-TC037), Performance (TC046-TC048), Usability (TC049-TC052)'],
            ['Week 4', 'Database (TC053-TC054), Audit (TC055-TC056), Reports (TC057-TC058), Integration (TC059-TC060)'],
            ['', ''],
            ['📞 NEED HELP?', ''],
            ['Documentation', 'Read testing/README_ENGLISH.md for complete guide'],
            ['Quick Start', 'Read testing/QUICK_START_GUIDE_ENGLISH.md for quick start'],
            ['Complete Guide', 'Read testing/MANUAL_TESTING_GUIDE_ENGLISH.md for detailed methodology'],
            ['', ''],
            ['✅ QUALITY GATES (Release Criteria)', ''],
            ['Ready for Release', 'Pass percentage > 95%, No critical bugs, No high priority bugs'],
            ['Conditional Release', 'Pass percentage > 85%, Critical bugs fixed, High bugs have workarounds'],
            ['Not Ready', 'Pass percentage < 85%, Critical bugs open, Major features not working'],
            ['', ''],
            ['🎓 TEST TYPES', ''],
            ['Functional', 'Testing if features work correctly (35 test cases)'],
            ['Negative', 'Testing with invalid inputs to check error handling (15 test cases)'],
            ['Security', 'Testing for security vulnerabilities (5 test cases)'],
            ['Performance', 'Testing speed and load handling (3 test cases)'],
            ['Usability', 'Testing user experience and interface (4 test cases)'],
            ['', ''],
            ['📦 TEST ACCOUNTS', ''],
            ['Patient', 'Username: patient1, Password: Patient@123'],
            ['Doctor', 'Username: doctor1, Password: Doctor@123'],
            ['Admin', 'Username: admin, Password: Admin@123'],
            ['', ''],
            ['🌐 APPLICATION URLS', ''],
            ['Home', 'http://localhost:5000'],
            ['Register', 'http://localhost:5000/register'],
            ['Login', 'http://localhost:5000/login'],
            ['Dashboard', 'http://localhost:5000/dashboard'],
            ['', ''],
            ['✨ GOOD LUCK WITH TESTING!', ''],
            ['', 'This Excel file contains everything you need for professional manual testing.'],
            ['', 'Start with Test Cases sheet and begin testing with TC001.'],
            ['', 'Report bugs in Bug Tracking sheet.'],
            ['', 'Track progress in Test Execution sheet.'],
            ['', 'Monitor metrics in Test Summary sheet.'],
            ['', ''],
            ['📄 Version', '1.0'],
            ['📅 Created', '2026-05-12'],
            ['✅ Status', 'Complete and Ready to Use'],
        ]
        
        instructions_df = pd.DataFrame(instructions_data)
        instructions_df.to_excel(writer, sheet_name='Instructions', index=False, header=False)
    
    print("=" * 60)
    print(f"\n✅ Excel file successfully created!")
    print(f"\n📂 File location: {os.path.abspath(excel_file)}")
    print(f"\n📊 Sheets included:")
    print("   1. Test Cases (60+ test cases)")
    print("   2. Bug Tracking (Bug reporting)")
    print("   3. Test Execution (Execution tracking)")
    print("   4. Test Summary (Overall metrics)")
    print("   5. Test Scenarios (Test scenarios)")
    print("   6. Instructions (How to use)")
    print("\n🎉 Open the Excel file and start testing!")
    print("=" * 60)
    
    return excel_file

if __name__ == "__main__":
    try:
        # Generate Excel file
        excel_file = create_complete_testing_excel()
        
        print("\n" + "="*60)
        print("🎯 NEXT STEPS:")
        print("="*60)
        print("1. Open the Excel file: Complete_Testing_Documentation.xlsx")
        print("2. Start application: python src/app.py")
        print("3. Go to 'Test Cases' sheet")
        print("4. Start testing with TC001")
        print("5. Report bugs in 'Bug Tracking' sheet")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure pandas and openpyxl are installed:")
        print("pip install pandas openpyxl")
