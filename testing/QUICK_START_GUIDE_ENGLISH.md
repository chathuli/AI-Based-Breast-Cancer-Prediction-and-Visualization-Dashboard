# Quick Start Guide - Manual Testing

## Get Started in 5 Minutes

### Step 1: Open the Files (1 minute)
```
1. Open Excel or Google Sheets
2. Open: testing/Test_Cases_English.csv
3. Open: testing/Bug_Tracking_English.csv
4. Arrange them side by side
```

### Step 2: Start the Application (1 minute)
```bash
# Run in terminal
python src/app.py

# Open in browser
http://localhost:5000
```

### Step 3: Execute Your First Test Case (3 minutes)

#### Test Case: TC001 - User Registration

**What to do:**

1. Go to: `http://localhost:5000/register`

2. Fill in the form:
   - Username: `testuser123`
   - Email: `test@example.com`
   - Password: `Test@1234`
   - Confirm Password: `Test@1234`

3. Click: **Register** button

4. Check if:
   - ✅ Success message is displayed?
   - ✅ Redirected to login page?
   - ✅ User account is created?

5. Record in Excel sheet:
   - `Status` column: "Executed"
   - `Executed_By`: Your name
   - `Execution_Date`: Today's date
   - `Actual_Result`: Write what happened
   - `Pass_Fail`: "Pass" or "Fail"

**Pass Example:**
```
Actual_Result: User successfully registered. Redirected to login page. Success message displayed.
Pass_Fail: Pass
```

**Fail Example (if bug found):**
```
Actual_Result: Registration button not working. No response on click.
Pass_Fail: Fail
Defects_Found: 1
Bug_IDs: BUG001
```

### What to Do If You Find a Bug:

1. **Take a Screenshot** (Windows: Win + Shift + S)

2. **Go to Bug Tracking Sheet**

3. **Add a new row and fill in:**
```
Bug_ID: BUG001
Date_Reported: 2026-05-12
Reported_By: Your Name
Module: Authentication
Feature: User Registration
Bug_Title: Registration button not responding
Bug_Description: Register button does not respond when clicked

Steps_to_Reproduce:
1. Go to /register
2. Fill all fields
3. Click Register button

Expected_Behavior: User should be registered and redirected to login
Actual_Behavior: Button does not respond
Severity: High
Priority: High
Status: Open
Screenshots: bug001_registration.png
Related_Test_Case: TC001
```

4. **Save Screenshot:** `testing/screenshots/bug001_registration.png`

---

## Next Steps

### Continue Testing:

1. **TC002** - Duplicate username registration
2. **TC003** - Weak password validation
3. **TC004** - Invalid email format
4. **TC005** - Empty fields validation

### Daily Target:
- **Morning**: 5-10 test cases
- **Afternoon**: 5-10 test cases
- **Total per day**: 10-20 test cases

### Weekly Target:
- **Week 1**: Authentication + Prediction (TC001-TC021)
- **Week 2**: Dashboard + Appointments (TC022-TC033)
- **Week 3**: Profile + Performance (TC034-TC052)
- **Week 4**: Database + Reports (TC053-TC060)

---

## Important Reminders

✅ **DO:**
- Read each test case carefully
- Follow steps exactly
- Record results
- Take screenshots for bugs
- Write clear bug descriptions

❌ **DON'T:**
- Skip test steps
- Forget to record results
- Forget to report bugs
- Provide incomplete information

---

## Need Help?

📖 **Detailed Guide**: Read `testing/MANUAL_TESTING_GUIDE_ENGLISH.md`
📋 **Full Documentation**: Check all CSV files
🐛 **Bug Examples**: See example row in Bug Tracking sheet

---

**Happy Testing! 🚀**
