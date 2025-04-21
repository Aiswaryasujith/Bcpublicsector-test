# Bcpublicsector-test

Case Management
The Prevention and Loss Management Services (PLMS) branch reviews employment and assistance
cases following standard procedures established within the branch. Among other outcomes, these
reviews could lead to turning off cheque production for income assistance cases after which the case
can be either closed or cheque production turned back on based on clients meeting specific conditions
of eligibility. There is also a possibility to reopen closed cases during a review cycle.
You have been presented with four (4) tables in csv format (named in the format 1_* to 4_*, and
attached in the csv.zip file) from an oracle data warehouse, containing the case review data for
answering the following questions. Data field definitions are also provided below.
Disclaimer: The data provided for this question is fictitious and is solely intended for this assignment.
• 1_case_table-csv CASE_ID – unique identifier for each case
o CASE_TYPE – some of the case type the ministry handles- Emp and Assistance, Bus Pass etc.
o CASE_CLOSED_DATE – the date a case was closed
o CASE_OPEN_DATE – the date a case was opened
o DISAB_FLG – a flag on the disability status of a client
• 2_case_audit_prev-csv (contains records from June 01, 2022 – December 31, 2022) A_ID – unique
identifier for each audit instance
o CASE_ID – unique identifier for each case
o FIELD – defines the dimension through which the data can be sliced (e.g., Chq Prod Flag,
Status, Closed Date, Reopened Date)
o VALUE_OLD – attribute associated with the FIELD attribute, which determines the previous
value of FIELD attribute
o VALUE_NEW – attribute associated with the FIELD attribute, which determines the current
value of FIELD attribute
o OPERATION – attribute associated with the FIELD attribute, which defines what operation is
performed on the FIELD attribute
o OPERATION_DATE – attribute associated with the FIELD attribute, which captures the date
the operation was performed on the FIELD attribute

• 3_case_audit_current-csv (contains records from January 1, 2023 – June 30, 2023) A_ID – unique
identifier for each audit instance
o CASE_ID – unique identifier for each case
o FIELD – defines the dimension through which the data can be sliced (e.g., Chq Prod Flag,
Status, Closed Date, Reopened Date)

Service Delivery Division Ministry of Social Development and Poverty Reduction

2 | P a g e
o VALUE_OLD – attribute associated with the FIELD attribute, which determines the previous
value of FIELD attribute
o VALUE_NEW – attribute associated with the FIELD attribute, which determines the current
value of FIELD attribute
o OPERATION – attribute associated with the FIELD attribute, which defines what operation is
performed on the FIELD attribute
o OPERATION_DATE – attribute associated with the FIELD attribute, which captures the date
the operation was performed on the FIELD attribute

• 4_srvreq_table-csv
o S_ID – unique identifier for each service review (PK)
o CASE_ID – unique identifier for each case (FK)
o REVIEW_START_DATE – the date a review was started on a case
o REVIEW_CLOSED_DATE – the date a review was closed on a case
o REVIEW_TYPE – some of the review types that the enterprise does (e.g., Gen Enquiry, PLMS
Review)

Answer the following questions using either R or Python and please provide a copy of your scripts (for
example in a jupyter notebook)
a) How long did cases with disability (PWD Cases) receive assistance from June 1st
, 2022, to
June 1st, 2023? (Hint: cheque production is on for receiving assistance) (25 marks)
b) Calculate the number of non-PWD cases and the average of their total SR duration for those
who received assistance since June 1st, 2022, to June 1st, 2023, for:
i. Less than or equal to 3 months
ii. Less than or equal to 6 months
iii. Less than or equal to 9 months
iv. Less than or equal to 12 months


c) In the period from June 1st, 2022, to June 1st, 2023:
i. What is the proportion of case closure operations by PLMS Review to the total
number of case closure operations? (Hint: Assume the case is closed by PLMS on the
same day as the PLMS Review Closure in the 4_srvreq_table).
ii. What is the proportion of number of cases closed by PLMS to the total number of
closed cases in the same period?

d) Assume these csv files are tables within an oracle data warehouse, provide SQL scripts that
would appropriately join the tables, filter, and extract data to answer each of the questions
above. Use file names as table names.
