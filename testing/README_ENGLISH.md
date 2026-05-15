# Manual Testing Documentation - Complete Guide

## 📋 Overview
This folder contains comprehensive manual testing documentation for Breast Care +, following professional IT industry standards.

## 📁 Files and Their Purpose

### 1. **MANUAL_TESTING_GUIDE_ENGLISH.md** ⭐ MAIN GUIDE
**What it is:** Complete testing guide with all instructions and methodology
**How to use:** 
- Read this first before starting testing
- Understand testing approach and methodology
- Learn how to set up test environment
- Reference for all testing procedures

**Contents:**
- Testing approach and methodology
- Test environment setup
- Test case structure
- Bug reporting guidelines
- Testing workflow
- Severity and priority definitions
- Test execution process
- Reporting and metrics

### 2. **Test_Cases_English.csv** ⭐ MAIN TEST CASES
**What it is:** 60+ detailed test cases covering all features
**How to use:**
- Open in Excel or Google Sheets
- Execute test cases one by one
- Record results in the sheet
- Mark Pass/Fail

**Columns Explained:**
- `Test_ID`: Unique test case number (TC001, TC002...)
- `Module`: Feature module (Authentication, Prediction, etc.)
- `Feature`: Specific feature being tested
- `Test_Case_Title`: Brief descriptive title
- `Test_Case_Description`: Detailed description
- `Preconditions`: Requirements before testing
- `Test_Steps`: Step-by-step instructions
- `Expected_Result`: What should happen
- `Test_Data`: Data to use for testing
- `Priority`: How important (Critical/High/Medium/Low)
- `Test_Type`: Category (Functional/Negative/Security/Performance)
- `Status`: Execution status
- `Executed_By`: Tester name
- `Execution_Date`: When tested
- `Actual_Result`: What actually happened
- `Pass_Fail`: Pass or Fail
- `Comments`: Additional notes

### 3. **Bug_Tracking_English.csv** ⭐ BUG REPORTING
**What it is:** Template for reporting and tracking bugs
**How to use:**
- When you find a bug, add a new row
- Fill in all details
- Attach screenshots (save file names)
- Update status as bug progresses (Open → Fixed → Verified → Closed)

**Important Columns:**
- `Bug_ID`: Unique bug number (BUG001, BUG002...)
- `Bug_Title`: Short bug description
- `Steps_to_Reproduce`: How to reproduce the bug
- `Expected_Behavior`: What should happen
- `Actual_Behavior`: What actually happens
- `Severity`: How serious (Critical/High/Medium/Low)
- `Priority`: How urgent (High/Medium/Low)
- `Status`: Bug status (Open/In Progress/Fixed/Verified/Closed)
- `Screenshots`: Screenshot file names
- `Related_Test_Case`: Link to test case

### 4. **Test_Execution_Tracker_English.csv**
**What it is:** Daily test execution progress tracker
**How to use:**
- Record daily test execution
- Track time spent on each test
- Track Pass/Fail count
- Link to bugs found

### 5. **Test_Summary_English.csv**
**What it is:** Overall testing metrics and summary
**How to use:**
- Update daily or weekly
- Calculate totals and percentages
- Track bug statistics
- Monitor test coverage
- Use for management reporting

### 6. **Test_Scenarios_English.csv**
**What it is:** High-level test scenarios checklist
**How to use:**
- Test complete flows (end-to-end)
- Group multiple test cases together
- Track overall progress

### 7. **QUICK_START_GUIDE_ENGLISH.md**
**What it is:** 5-minute quick start guide
**How to use:**
- Read this to get started quickly
- Follow step-by-step instructions
- Execute your first test case

---

## 🚀 How to Start Testing

### Step 1: Setup (5 minutes)
```bash
# Start the application
python src/app.py

# Open in browser
http://localhost:5000
```

### Step 2: Prepare Test Data (5 minutes)
```bash
# Create admin account
python create_admin.py

# Create doctor account
python create_doctor.py

# Generate test samples
python generate_test_samples.py
```

### Step 3: Open Excel Files (2 minutes)
1. Open `Test_Cases_English.csv` in Excel
2. Open `Bug_Tracking_English.csv` in Excel
3. Arrange them side by side

### Step 4: Start Testing (Ongoing)
1. **Select a test case** (start with TC001)
2. **Check preconditions** - ensure everything is ready
3. **Follow test steps** - execute each step exactly
4. **Record results**:
   - `Status` column: "Executed"
   - `Actual_Result` column: Write what happened
   - Mark "Pass" or "Fail"
5. **If bug found**:
   - Go to Bug Tracking sheet
   - Add new row
   - Fill all details
   - Take screenshot
   - Save screenshot with proper name

---

## 📊 How to Report Bugs

### When You Find a Bug:

1. **Take a Screenshot**
   - Capture the error or issue
   - File name: `bug_001_description.png`
   - Save in: `testing/screenshots/` folder

2. **Fill Bug Tracking Sheet**:
   ```
   Bug_ID: BUG001
   Date_Reported: 2026-05-12
   Reported_By: Your Name
   Module: Authentication
   Feature: Login
   Bug_Title: Login button not responding
   Bug_Description: When clicking login button with valid credentials, no action is taken
   
   Steps_to_Reproduce:
   1. Navigate to http://localhost:5000/login
   2. Enter username: patient1
   3. Enter password: Patient@123
   4. Click Login button
   
   Expected_Behavior: User should be logged in and redirected to dashboard
   Actual_Behavior: Button does not respond; No action taken
   Severity: High
   Priority: High
   Status: Open
   Environment: Development
   Browser: Chrome
   OS: Windows 11
   Screenshots: bug001_login_error.png
   Related_Test_Case: TC006
   ```

3. **Set Severity and Priority**:

   **Severity Levels:**
   - **Critical**: Application crash, data loss, security breach
   - **High**: Major feature not working, incorrect predictions
   - **Medium**: Minor feature issues, UI problems
   - **Low**: Cosmetic issues, spelling mistakes

   **Priority Levels:**
   - **High**: Fix immediately
   - **Medium**: Fix in current sprint
   - **Low**: Fix when time permits

---

## 📈 Daily Testing Workflow

### Morning (9:00 AM - 12:00 PM)
1. Add today's date in Test Execution Tracker
2. Select 5-10 test cases to execute
3. Execute tests and record results
4. Report any bugs found

### Afternoon (1:00 PM - 5:00 PM)
1. Continue executing test cases
2. Retest any fixed bugs
3. Update bug status
4. Organize screenshots

### End of Day (5:00 PM)
1. Update Test Summary sheet
2. Calculate Pass/Fail count
3. Plan tomorrow's testing
4. Backup all files

---

## 🎯 Testing Priorities

### Phase 1: Critical Features (Week 1)
- Authentication (TC001-TC014)
- Prediction System (TC015-TC021)
- Security Testing (TC041-TC045)

### Phase 2: Core Features (Week 2)
- Dashboard Features (TC022-TC027)
- Appointments (TC028-TC033)
- API Testing (TC038-TC040)

### Phase 3: Additional Features (Week 3)
- Profile Management (TC034-TC037)
- Performance Testing (TC046-TC048)
- Usability Testing (TC049-TC052)

### Phase 4: Integration & Reports (Week 4)
- Database Testing (TC053-TC054)
- Audit Logging (TC055-TC056)
- Reports (TC057-TC058)
- Email Integration (TC059-TC060)

---

## 📝 Tips & Best Practices

### Testing Tips:
1. ✅ Complete one test case before moving to next
2. ✅ Write actual results for every test case
3. ✅ Take screenshots for bugs
4. ✅ Write clear steps to reproduce
5. ✅ Document test data used

### Bug Reporting Tips:
1. ✅ Use clear bug titles
2. ✅ Write detailed steps to reproduce
3. ✅ Clearly mention expected vs actual behavior
4. ✅ Attach screenshots
5. ✅ Set severity and priority correctly

### Common Mistakes to Avoid:
1. ❌ Testing without following steps
2. ❌ Not recording results
3. ❌ Not taking screenshots
4. ❌ Incomplete bug reports
5. ❌ Not documenting test data

---

## 📞 Support

### Need Help?
1. Read `MANUAL_TESTING_GUIDE_ENGLISH.md` for detailed information
2. Check `QUICK_START_GUIDE_ENGLISH.md` for quick start
3. See example rows in Bug Tracking sheet

### Questions?
- Review the test case examples
- Check bug report examples
- Refer to the complete guide

---

## 🎓 Learning Resources

### Testing Concepts:
- **Functional Testing**: Testing if features work correctly
- **Negative Testing**: Testing with invalid inputs to check error handling
- **Security Testing**: Testing for security vulnerabilities
- **Performance Testing**: Testing speed and load handling
- **Usability Testing**: Testing user experience

### Bug Life Cycle:
```
New → Open → Assigned → In Progress → Fixed → Retest → Verified → Closed
```

---

## 📊 Metrics to Track

### Daily Metrics:
- Total test cases executed
- Pass count
- Fail count
- Bugs found
- Bugs fixed
- Test coverage %
- Pass percentage

### Weekly Metrics:
- Total test cases executed
- Overall pass percentage
- Total bugs found
- Bugs by severity
- Bugs by status
- Test coverage

---

## ✅ Testing Complete Checklist

### Before Sign-off:
- [ ] All 60 test cases executed
- [ ] All bugs reported
- [ ] Critical bugs fixed and verified
- [ ] High priority bugs fixed
- [ ] Regression testing done
- [ ] Test summary report complete
- [ ] Final test report prepared
- [ ] All deliverables ready

### Quality Gates:
- [ ] Pass percentage > 95%
- [ ] No critical bugs open
- [ ] No high priority bugs open
- [ ] All features working
- [ ] Performance acceptable
- [ ] Security verified
- [ ] Usability acceptable

---

## 📌 Quick Reference

### File Locations:
- Test Cases: `testing/Test_Cases_English.csv`
- Bug Tracking: `testing/Bug_Tracking_English.csv`
- Test Execution: `testing/Test_Execution_Tracker_English.csv`
- Test Summary: `testing/Test_Summary_English.csv`
- Test Scenarios: `testing/Test_Scenarios_English.csv`
- Screenshots: `testing/screenshots/`

### Test Account Credentials:
- **Patient**: username: patient1, password: Patient@123
- **Doctor**: username: doctor1, password: Doctor@123
- **Admin**: username: admin, password: Admin@123

### Application URLs:
- **Home**: http://localhost:5000
- **Register**: http://localhost:5000/register
- **Login**: http://localhost:5000/login
- **Dashboard**: http://localhost:5000/dashboard

---

## 📦 Deliverables

### Testing Deliverables:
- ✅ Test Cases Document (60 test cases)
- ✅ Bug Tracking Sheet
- ✅ Test Execution Tracker
- ✅ Test Summary Report
- ✅ Test Scenarios Checklist
- ✅ Screenshots (Bug evidences)
- ✅ Complete Testing Guide
- ✅ Quick Start Guide

---

**Document Version**: 1.0  
**Last Updated**: May 12, 2026  
**Status**: Final  

**Good Luck with Testing! 🚀**
