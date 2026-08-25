# Use-Case Flow Specification

## Use Case: Submit Adoption Application

**Actor(s):** Adoption Applicant (primary), Shelter Staff (secondary — receives the application)
**Related Requirement(s):** FR-002, FR-003
**Includes:** Fill Screening Questionnaire

### Preconditions
1. The applicant has an active account or has provided valid contact details.
2. The animal being applied for exists in the system and its status is "Ready for Adoption".
3. The applicant has not already submitted an open (pending) application for this animal.

### Postconditions
**Success:**
1. A new application record is created with status "Submitted" and linked to the selected animal.
2. The screening questionnaire responses are stored against the application.
3. The animal's status changes from "Ready for Adoption" to "Application Pending".
4. Shelter staff receive a notification that a new application is awaiting review.

**Failure:**
1. No application record is created, and the animal's status remains unchanged.

### Main Success Scenario
1. The applicant browses the pet catalog and selects an animal marked "Ready for Adoption".
2. The applicant selects "Apply to Adopt" for that animal.
3. The system displays the adoption application form, including the screening questionnaire (<<include>> Fill Screening Questionnaire).
4. The applicant completes all mandatory questionnaire fields (household type, other pets, experience, work schedule, etc.).
5. The applicant reviews a summary of their answers and confirms submission.
6. The system validates that all mandatory fields are complete and the animal is still available.
7. The system creates the application record with status "Submitted" and timestamps it.
8. The system updates the animal's status to "Application Pending".
9. The system sends a confirmation notification to the applicant and an alert to shelter staff.
10. The use case ends successfully.

### Alternate Flow A1: Incomplete Questionnaire on Submission
Triggered at step 6, when validation fails because one or more mandatory fields are empty or invalid.

1. The system halts submission and highlights the missing or invalid fields on the form.
2. The system displays an inline message: "Please complete all required fields before submitting."
3. The applicant corrects the flagged fields.
4. The applicant re-submits the form.
5. The flow resumes at step 6 of the Main Success Scenario.

*(If the applicant abandons the form instead of correcting it, no application record is created and the use case ends without changing the animal's status — this satisfies the Failure Postcondition.)*

### Alternate Flow A2: Animal No Longer Available
Triggered at step 6, when another applicant's application has already changed the animal's status before this submission is validated.

1. The system detects that the animal's status is no longer "Ready for Adoption".
2. The system rejects the submission and informs the applicant that the animal is no longer available.
3. The system suggests similar animals from the catalog (same species/breed/age range).
4. The use case ends without creating an application record.

---
*Note: Alternate Flow A1 is the flow required by the assignment. A2 is included as a bonus to show you can identify more than one alternate path — check your rubric on whether multiple alternate flows are wanted or exactly one.*
