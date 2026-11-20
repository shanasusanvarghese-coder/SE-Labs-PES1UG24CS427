# Static Code Analysis Issues

The following issues were identified from the original election system code and its static-analysis reports.

| Issue | Type | Severity | Description | Fix |
|---|---|---|---|---|
| Bidirectional Unicode characters | Security | High | Hidden directional characters could make code misleading. | Removed the confusing characters and used an explicit role comparison. |
| Weak MD5 hashing | Security | High | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Duplicate voting | Logic | High | A voter could potentially cast more than one vote. | Check the voter's voted status before accepting a ballot. |
| Unsafe XML parsing | Security | Medium | The original XML parser could expose the program to unsafe XML input. | Used defusedxml and handled parsing errors. |
| Age eligibility boundary | Logic | Medium | Voters who were exactly 18 could be rejected. | Allowed voters aged 18 and above. |
| Division by zero | Reliability | Medium | Vote percentages could fail when no votes existed. | Handle empty ballot lists before dividing. |
| Incorrect announcement output | Logic | Medium | Late-bound lambdas could produce incorrect candidate announcements. | Generate announcement strings directly. |
| Insecure random numbers | Security | Low | The standard random generator was used for receipt identifiers. | Replaced it with secrets.randbelow. |
| Broad exception handling | Reliability | Low | A bare exception handler could silently hide errors. | Catch specific XML-related exceptions. |
| Style and unused code | Code quality | Low | Tools reported unused names, missing docstrings, naming problems, and formatting issues. | Removed unused code and improved naming, documentation, and formatting. |
