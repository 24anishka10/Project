# Bank Management System

# Problem Statement
Traditional banking operations, when handled manually, are time-consuming, prone to human error, and inefficient. Customers often face long delays for simple operations like balance inquiries or fund transfers, while bank administrators struggle with maintaining accurate paper-based records. There is a need for a digital, automated system to streamline these operations, ensuring data integrity, security, and faster transaction processing.

# Scope of the Project
The Bank Management System is a Python-based application designed to simulate core banking activities. 
* **In Scope:** The system covers the lifecycle of a user account (creation to deletion), handles monetary transactions (deposits, withdrawals, transfers), performs validations, and maintains a persistent log of transaction history using file handling/database connectivity.
* **Out of Scope:** This project does not involve real-time monetary processing with actual banking networks, physical ATM hardware integration, or complex loan approval algorithms.

# Target Users
* **Bank Administrators:** Staff members responsible for creating new accounts, removing inactive users, and viewing overall bank statistics.
* **Bank Customers:** End-users who interact with the system to deposit money, withdraw funds, transfer to other accounts, and view their personal transaction history.

# High-Level Features
The project focuses on three major functional areas:
1.  **User Management Module:** Secure account creation, authentication (login/logout), and profile management (updating customer details).
2.  **Transaction Processing Module:** Real-time handling of deposits and withdrawals, including logic to prevent overdrafts (withdrawing more than the available balance).
3.  **Reporting & Auditing Module:** Generation of "Mini-Statements" (transaction history) for users and summary reports for administrators to track total deposits/withdrawals.
