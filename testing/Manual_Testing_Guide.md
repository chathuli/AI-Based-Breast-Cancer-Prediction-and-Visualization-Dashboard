# Manual Testing Guide - Breast Cancer Prediction Application

## Overview
මෙම document එක breast cancer prediction application එකේ සියලුම features manual testing කරන්න අවශ්‍ය විස්තර සහිත guide එකකි.

## Testing Approach
- **Black Box Testing**: User perspective එකෙන් functionality test කිරීම
- **Exploratory Testing**: Different scenarios try කිරීම
- **Regression Testing**: Updates වලින් පස්සේ existing features work කරනවාද බැලීම
- **Security Testing**: Authentication, authorization, data security test කිරීම
- **Usability Testing**: User experience සහ UI/UX test කිරීම

## Test Environment Setup
1. Application start කරන්න: `python src/app.py`
2. Browser එකෙන් open කරන්න: `http://localhost:5000`
3. Test data ready කරන්න (users, doctors, admin accounts)
4. Database backup එකක් තියාගන්න testing වලට පෙර

## Testing Modules

### 1. Authentication & Authorization
- User Registration
- User Login (Patient, Doctor, Admin)
- Password Security
- Session Management
- Role-based Access Control

### 2. Prediction System
- Symptom Input
- Image Upload
- Prediction Results
- SHAP Explanations
- Report Generation

### 3. Dashboard Features
- Patient Dashboard
- Doctor Dashboard
- Admin Dashboard
- History View
- Profile Management

### 4. Appointment System
- Book Appointment
- View Appointments
- Cancel Appointment
- Doctor Location Map

### 5. Admin Features
- User Management
- System Monitoring
- Audit Logs
- Database Management

### 6. API Testing
- REST API Endpoints
- Authentication
- Response Validation

## Test Data Requirements
- Valid user credentials
- Invalid credentials (for negative testing)
- Sample medical images
- Various symptom combinations
- Edge case data

## Bug Severity Levels
- **Critical**: Application crash, data loss, security breach
- **High**: Major feature not working, incorrect predictions
- **Medium**: Minor feature issues, UI problems
- **Low**: Cosmetic issues, minor improvements

## Test Execution Process
1. Read test case
2. Setup test data
3. Execute steps
4. Record actual result
5. Compare with expected result
6. Log bug if failed
7. Mark test status

## Reporting
- Daily test execution summary
- Bug reports with screenshots
- Test coverage metrics
- Final test report

---
**Note**: Excel sheets වල detailed test cases සහ bug tracking templates තිබේ.
