# Reflection — Static Code Analysis

**Note:** The exact four reflection questions from the lecturer's handout were not available. The following answers cover four relevant reflection topics and are not claimed to reproduce the original questions word for word.

## 1. What issues did I find in the original program?

The original program contained security issues and functional bugs. Bandit identified weak MD5 hashing, unsafe XML parsing, insecure random-number generation, and suspicious bidirectional Unicode characters. Pylint and Flake8 identified unused imports and variables, missing documentation, naming problems, and formatting issues. Reviewing the program also revealed potential duplicate voting, an incorrect age boundary, division by zero when there were no ballots, and incorrect candidate announcements.

## 2. How did Pylint, Bandit, and Flake8 differ?

Pylint examined overall code quality, including naming, documentation, unused variables, and possible programming mistakes. Flake8 focused on style and common errors, such as unused imports and long lines. Bandit focused on security-sensitive code patterns, including weak hashing, unsafe XML parsing, and insecure random-number generation. Using all three provided a broader review.

## 3. Which fixes were most important, and why?

The most important fixes addressed election integrity and security. These included removing confusing Unicode characters, replacing MD5, using a safer XML parser, and preventing duplicate votes. I also corrected the age eligibility boundary, handled empty vote totals safely, and fixed candidate announcements. These changes made the program more reliable and easier to maintain.

## 4. What did I learn, and what are the limitations of static analysis?

I learned that static-analysis tools can identify suspicious code without executing the program, but they cannot guarantee that every logical bug will be found. Code review and testing are still necessary. The saved reports showed no Bandit findings, no Flake8 findings, and a Pylint score of 9.78/10 after the changes. Pylint still reported a missing module docstring and a missing docstring for main.
