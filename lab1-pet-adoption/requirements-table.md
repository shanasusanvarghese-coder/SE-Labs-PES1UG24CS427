# Requirements Table — Pet Adoption & Shelter Management System

## Functional Requirements

| ID | Description | Priority | Acceptance Criteria | Rationale |
|----|--------------|----------|----------------------|-----------|
| FR-001 | The system shall allow staff to log animal vaccination and medical intake records, updating animal availability status to "Ready for Adoption". | High | Pass: Adoption application linked to verified animal record. Fail: Animal under medical quarantine marked adopted. | Ensures no animal is placed for adoption before it is medically cleared, protecting adopter and animal welfare. |
| FR-002 | The system shall allow an adoption applicant to submit an adoption application for a specific animal, including a completed screening questionnaire. | High | Pass: Application is only accepted once all mandatory questionnaire fields are filled and an animal is selected. Fail: Application submitted with an incomplete questionnaire or without a linked animal. | Captures the information staff need to assess suitability and prevents incomplete applications from entering the review queue. |
| FR-003 | The system shall allow shelter staff to review a submitted application and record a decision (approve, reject, or request more information), with a mandatory reason for rejection. | High | Pass: Rejected application cannot be closed without a reason field populated. Fail: Application status changes to "Rejected" with no reason recorded. | Provides accountability and an audit trail for adoption decisions, and gives applicants actionable feedback. |
| FR-004 | The system shall allow an applicant or staff member to schedule a meet-and-greet session for an approved or shortlisted animal, checking staff availability before confirming. | Medium | Pass: Session is booked only when a staff calendar slot is free. Fail: Two sessions are booked for the same staff member at the same time. | Prevents scheduling conflicts and ensures a staff member is present to supervise the interaction. |
| FR-005 | The system shall allow staff to create and track a foster home placement, including start date, expected duration, and check-in reminders. | Medium | Pass: A placement record shows current status (Active/Completed/Overdue) based on dates. Fail: An overdue placement is not flagged to staff. | Supports the shelter's duty of care for animals in temporary foster homes and avoids animals being "lost" in the system. |

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|----|------|--------------|----------|----------------------|-----------|
| NFR-001 | Performance & Security | The pet search catalog must support multi-attribute filtering (Species, Age, Breed, Good with Kids) with page response < 200 ms. | High | Pass: Benchmarking tests confirm target latency and security standards under simulated peak load. | A slow or insecure search page discourages adopters and undermines trust in the platform. |
| NFR-002 | Privacy & Security | All adopter personal data (contact details, home visit notes, screening answers) must be encrypted at rest and in transit, and visible only to authenticated shelter staff roles. | High | Pass: Penetration test confirms data is unreadable without valid staff credentials; unauthorized API calls return 403. Fail: Applicant PII is retrievable via an unauthenticated endpoint. | Applicant data is sensitive personal information; a breach would expose adopters to harm and the shelter to legal liability. |
