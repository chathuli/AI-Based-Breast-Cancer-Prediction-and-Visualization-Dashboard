# Quick Start Guide - Manual Testing

## 5 Minutes වලින් Testing Start කරන්න

### Step 1: Files Open කරන්න (1 minute)
```
1. Excel open කරන්න
2. testing/test_cases_data.csv open කරන්න
3. testing/bug_tracking_template.csv open කරන්න
4. දෙකම side by side තියාගන්න
```

### Step 2: Application Start කරන්න (1 minute)
```bash
# Terminal එකේ run කරන්න
python src/app.py

# Browser එකෙන් open කරන්න
http://localhost:5000
```

### Step 3: First Test Case Execute කරන්න (3 minutes)

#### Test Case: TC001 - User Registration

**කරන්න ඕන දේවල්:**

1. Browser එකෙන් යන්න: `http://localhost:5000/register`

2. Fill කරන්න:
   - Username: `testuser123`
   - Email: `test@example.com`
   - Password: `Test@1234`
   - Confirm Password: `Test@1234`

3. Click කරන්න: **Register** button

4. බලන්න:
   - ✅ Success message එකක් පෙන්වනවාද?
   - ✅ Login page එකට redirect වෙනවාද?
   - ✅ User account create වෙලාද?

5. Excel sheet එකේ record කරන්න:
   - `Status` column: "Executed"
   - `Executed_By`: Your name
   - `Execution_Date`: Today's date
   - `Actual_Result`: මොකද වුණේ ලියන්න
   - Pass නම්: "Pass", Fail නම්: "Fail"

**Pass Example:**
```
Actual_Result: User successfully registered. Redirected to login page. Success message displayed.
Pass_Fail: Pass
```

**Fail Example (Bug හම්බ වුණොත්):**
```
Actual_Result: Registration button not working. No response on click.
Pass_Fail: Fail
Defects_Found: 1
Bug_IDs: BUG001
```

### Bug හම්බ වුණොත් කරන්න ඕන දේ:

1. **Screenshot එකක් ගන්න** (Windows: Win + Shift + S)

2. **Bug Tracking Sheet එකට යන්න**

3. **New row එකක් add කරලා fill කරන්න:**
```
Bug_ID: BUG001
Date_Reported: 2026-05-12
Reported_By: Your Name
Module: Authentication
Feature: User Registration
Bug_Title: Registration button not responding
Bug_Description: Register button click කරද්දී කිසිම response එකක් නෑ

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

4. **Screenshot එක save කරන්න:** `testing/screenshots/bug001_registration.png`

---

## Next Steps

### ඊළඟට කරන්න ඕන දේවල්:

1. **TC002 Test කරන්න** - Duplicate username registration
2. **TC003 Test කරන්න** - Weak password validation
3. **TC004 Test කරන්න** - Invalid email format
4. **TC005 Test කරන්න** - Empty fields validation

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
- එක එක test case හොඳින් කියවන්න
- Steps හරියටම follow කරන්න
- Results record කරන්න
- Screenshots ගන්න bugs සඳහා
- Clear bug descriptions ලියන්න

❌ **DON'T:**
- Test steps skip කරන්න එපා
- Results record කරන්න අමතක කරන්න එපා
- Bugs report කරන්න අමතක කරන්න එපා
- Incomplete information දාන්න එපා

---

## Need Help?

📖 **Detailed Guide**: `testing/README_SINHALA.md` කියවන්න
📋 **Full Manual**: `testing/Manual_Testing_Guide.md` බලන්න
🐛 **Bug Examples**: Bug tracking sheet එකේ example row බලන්න

---

**Happy Testing! 🚀**
