'''## 📌 Introduction

In this task, you’ll take a hands-on approach to evaluating and improving an AI-driven financial transaction categorization system.

You’ll work with:

- Original transaction data
- AI-generated categorizations
- Bookkeeper-annotated corrections (only provided for transactions where the AI was wrong)

The system uses a prompt-based method to classify financial transactions into business accounting categories. Your job is to evaluate how well it's working — and how it can be improved.

- Transaction Categorization Prompt
    
    System prompt:
    % You are an expert bookkeeper. Your goal is to categorize the transaction properly in one of the 
        <categories_labels>
             f"Direct Deposit Payable, Chair Rental:Facial Room, Chair Rental:Hair Chair, 60400 Bank Service Charges, Cash Clearing Account, Chair Rental:Lash Bed, 67100 Rent Expense, Cost of Goods Sold:Salon Supplies:Supplies and Materials, 68600 Utilities, 51800 Merchant Account Fees, Uncategorized Expense, 20000 Accounts Payable, 24000 Payroll Liabilities:Federal Taxes, 25550 PST Payable (BC):PST Payable (BC), TD Visa 1968, Uncategorized Income, 25500 GST/HST Payable:GST/HST Payable, 66000 Payroll Expenses:WCB Expenses, 64300 Meals and Entertainment, Subcontractor, Sales of Product Income, 15000 Furniture and Equipment, Other Income, 61700 Computer and Software  Expenses, Sales, 30800 Owners Draw, Cost of Labor:Commission, Legal & Professional Fess:Professional Fees - Accounting, Rent Security Deposit, Undeposited Funds, MyJobs_test, Bank loans
        </categories_labels>

        Based on the transaction details provided, such as the name, amount, description, paymenChannel, and type.


        % The output will be the following:
                - Analysis: Analysis for why it is a certain category
                - Category: <category_label>Return only the probable category for the transaction without any additional information here</category_label>
                
                

        "% Here are some examples:
        "
        <examples>
        f"<example>
                <category>"Chair Rental:Hair Chair"</category>
                <name>"E-TRANSFER ***VFB"</name>
                <amount>"1500.0"</amount>
                <description>"E-TRANSFER ***VFB"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Cash Clearing Account"</category>
                <name>"Phorest Pay MSP"</name>
                <amount>"1221.03"</amount>
                <description>"Phorest Pay      MSP"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Chair Rental:Hair Chair"</category>
                <name>"E-TFR ***caX EPAY"</name>
                <amount>"1575.0"</amount>
                <description>"E-TFR ***caX EPAY"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Direct Deposit Payable"</category>
                <name>"PAYROLL PAY"</name>
                <amount>"-1643.56"</amount>
                <description>"PAYROLL          PAY"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Uncategorized Income"</category>
                <name>"E-TRANSFER ***jTm"</name>
                <amount>"48.75"</amount>
                <description>"E-TRANSFER ***jTm"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Subcontractor"</category>
                <name>"SEND E-TFR *rXp AP"</name>
                <amount>"-1793.37"</amount>
                <description>"SEND E-TFR *rXp AP"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Direct Deposit Payable"</category>
                <name>"INTUIT 02467094 PAY"</name>
                <amount>"-1099.03"</amount>
                <description>"INTUIT 02467094  PAY"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Cash Clearing Account"</category>
                <name>"Phorest Pay-Pho MSP"</name>
                <amount>"2576.27"</amount>
                <description>"Phorest Pay-Pho  MSP"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Cost of Labor:Commission"</category>
                <name>"CHQ#00051-1143660177"</name>
                <amount>"-1500.0"</amount>
                <description>"CHQ#00051-1143660177"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"20000 Accounts Payable"</category>
                <name>"SEND E-TFR *cA9 AP"</name>
                <amount>"-1349.18"</amount>
                <description>"SEND E-TFR *cA9 AP"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Chair Rental:Lash Bed"</category>
                <name>"E-TRANSFER ***CHk"</name>
                <amount>"892.5"</amount>
                <description>"E-TRANSFER ***CHk"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Subcontractor"</category>
                <name>"SEND E-TFR *WAk AP"</name>
                <amount>"-893.09"</amount>
                <description>"SEND E-TFR *WAk AP"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Legal & Professional Fess:Professional Fees - Accounting"</category>
                <name>"SEND E-TFR ***YeQ"</name>
                <amount>"-1121.25"</amount>
                <description>"SEND E-TFR ***YeQ"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Uncategorized Income"</category>
                <name>"E-TRANSFER ***xvD"</name>
                <amount>"1260.0"</amount>
                <description>"E-TRANSFER ***xvD"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Chair Rental:Lash Bed"</category>
                <name>"E-TRANSFER ***KbC"</name>
                <amount>"1050.0"</amount>
                <description>"E-TRANSFER ***KbC"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"20000 Accounts Payable"</category>
                <name>"SEND E-TFR ***mSt"</name>
                <amount>"-2964.56"</amount>
                <description>"SEND E-TFR ***mSt"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"24000 Payroll Liabilities:Federal Taxes"</category>
                <name>"EMPTX 9575546 BUS"</name>
                <amount>"-5390.46"</amount>
                <description>"EMPTX 9575546    BUS"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"25500 GST/HST Payable:GST/HST Payable"</category>
                <name>"GST-P 339306 BUS"</name>
                <amount>"-7730.06"</amount>
                <description>"GST-P  339306    BUS"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Cost of Goods Sold:Salon Supplies:Supplies and Materials"</category>
                <name>"E-TRANSFER ***XcX"</name>
                <amount>"1470.0"</amount>
                <description>"E-TRANSFER ***XcX"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Cost of Goods Sold:Salon Supplies:Supplies and Materials"</category>
                <name>"Phorest Pay-Pho MSP"</name>
                <amount>"3239.16"</amount>
                <description>"Phorest Pay-Pho  MSP"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Uncategorized Expense"</category>
                <name>"SEND E-TFR ***KzK"</name>
                <amount>"-252.0"</amount>
                <description>"SEND E-TFR ***KzK"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"25500 GST/HST Payable:GST/HST Payable"</category>
                <name>"GST34 1436338 BUS"</name>
                <amount>"-7635.98"</amount>
                <description>"GST34 1436338    BUS"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"MyJobs_test"</category>
                <name>"E-TRANSFER ***Bby"</name>
                <amount>"37.5"</amount>
                <description>"E-TRANSFER ***Bby"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"60400 Bank Service Charges"</category>
                <name>"ACCT BAL REBATE"</name>
                <amount>"125.0"</amount>
                <description>"ACCT BAL REBATE"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Uncategorized Expense"</category>
                <name>"SEND E-TFR ***TcU"</name>
                <amount>"-748.65"</amount>
                <description>"SEND E-TFR ***TcU"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"TD Visa 1968"</category>
                <name>"TD VISA PREAUTH PYMT"</name>
                <amount>"-13413.38"</amount>
                <description>"TD VISA PREAUTH PYMT"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"60400 Bank Service Charges"</category>
                <name>"MONTHLY PLAN FEE"</name>
                <amount>"-125.0"</amount>
                <description>"MONTHLY PLAN FEE"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"51800 Merchant Account Fees"</category>
                <name>"FIRST DATA CORP RLS"</name>
                <amount>"-36.1"</amount>
                <description>"FIRST DATA CORP  RLS"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"25550 PST Payable (BC):PST Payable (BC)"</category>
                <name>"PROVINCE OF BC PRO"</name>
                <amount>"-146.69"</amount>
                <description>"PROVINCE OF BC   PRO"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"TD Visa 1968"</category>
                <name>"RI301 TFR-TO C/C"</name>
                <amount>"-3000.0"</amount>
                <description>"RI301 TFR-TO C/C"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Chair Rental:Facial Room"</category>
                <name>"E-TRANSFER ***cnE"</name>
                <amount>"1470.0"</amount>
                <description>"E-TRANSFER ***cnE"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"24000 Payroll Liabilities:Federal Taxes"</category>
                <name>"EMPTX 7615623 BUS"</name>
                <amount>"-6995.83"</amount>
                <description>"EMPTX 7615623    BUS"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"30800 Owners Draw"</category>
                <name>"SEND E-TFR ***f4C"</name>
                <amount>"-87.5"</amount>
                <description>"SEND E-TFR ***f4C"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Chair Rental:Facial Room"</category>
                <name>"E-TRANSFER ***gMx"</name>
                <amount>"787.5"</amount>
                <description>"E-TRANSFER ***gMx"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"51800 Merchant Account Fees"</category>
                <name>"FIRST DATA CORP RLS"</name>
                <amount>"-36.1"</amount>
                <description>"FIRST DATA CORP  RLS"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"25550 PST Payable (BC):PST Payable (BC)"</category>
                <name>"PROVINCE OF BC PRO"</name>
                <amount>"-309.66"</amount>
                <description>"PROVINCE OF BC   PRO"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Undeposited Funds"</category>
                <name>"E-TRANSFER ***BhW"</name>
                <amount>"750.0"</amount>
                <description>"E-TRANSFER ***BhW"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"67100 Rent Expense"</category>
                <name>"CHQ#00052-0146456744"</name>
                <amount>"-17067.56"</amount>
                <description>"CHQ#00052-0146456744"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"64300 Meals and Entertainment"</category>
                <name>"Costco"</name>
                <amount>"-5.22"</amount>
                <description>"COSTCO WHOLESAL"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"66000 Payroll Expenses:WCB Expenses"</category>
                <name>"WORKSAFEBC K4Q6U8"</name>
                <amount>"-658.21"</amount>
                <description>"WORKSAFEBC   K4Q6U8"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"66000 Payroll Expenses:WCB Expenses"</category>
                <name>"WORKERS COMP BC WCB"</name>
                <amount>"-893.84"</amount>
                <description>"WORKERS COMP BC  WCB"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"64300 Meals and Entertainment"</category>
                <name>"Costco"</name>
                <amount>"-271.86"</amount>
                <description>"COSTCO WHOLESAL"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"MyJobs_test"</category>
                <name>"E-TRANSFER ***BhW"</name>
                <amount>"750.0"</amount>
                <description>"E-TRANSFER ***BhW"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Cost of Labor:Commission"</category>
                <name>"SEND E-TFR ***tx9"</name>
                <amount>"-79.6"</amount>
                <description>"SEND E-TFR ***tx9"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"30800 Owners Draw"</category>
                <name>"SEND E-TFR ***kcw"</name>
                <amount>"-160.0"</amount>
                <description>"SEND E-TFR ***kcw"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"67100 Rent Expense"</category>
                <name>"CHQ#00048-0142775540"</name>
                <amount>"-17067.86"</amount>
                <description>"CHQ#00048-0142775540"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Legal & Professional Fess:Professional Fees - Accounting"</category>
                <name>"SEND E-TFR ***aec"</name>
                <amount>"-3000.0"</amount>
                <description>"SEND E-TFR ***aec"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Other Income"</category>
                <name>"E-TRANSFER ***NJG"</name>
                <amount>"80.43"</amount>
                <description>"E-TRANSFER ***NJG"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Other Income"</category>
                <name>"E-TRANSFER ***J3b"</name>
                <amount>"22.0"</amount>
                <description>"E-TRANSFER ***J3b"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Undeposited Funds"</category>
                <name>"E-TRANSFER ***Bby"</name>
                <amount>"37.5"</amount>
                <description>"E-TRANSFER ***Bby"</description>
                <paymentchannel>"other"</paymentchannel>
                <type>"special"</type>
            </example>
        <example>
                <category>"Owners Draw"</category>
                <name>"AGELESS BEAUTY LASER & SP"</name>
                <amount>"-200.0"</amount>
                <description>"AGELESS BEAUTY LASER & SP"</description>
                <paymentchannel>"online"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Owners Draw"</category>
                <name>"NANNYSERVICES.CA"</name>
                <amount>"-48.0"</amount>
                <description>"NANNYSERVICES.CA"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Owners Draw"</category>
                <name>"SP HEIRESS CLOTHING"</name>
                <amount>"-320.86"</amount>
                <description>"SP HEIRESS CLOTHING"</description>
                <paymentchannel>"online"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Owners Draw"</category>
                <name>"NANNYSERVICES.CA"</name>
                <amount>"-48.0"</amount>
                <description>"NANNYSERVICES.CA"</description>
                <paymentchannel>"online"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Owners Draw"</category>
                <name>"NANNYSERVICES.CA"</name>
                <amount>"-48.0"</amount>
                <description>"NANNYSERVICES.CA"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"CHOICES YALETOWN # 907"</name>
                <amount>"-10.68"</amount>
                <description>"CHOICES YALETOWN # 907"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"SP SECRET NAIL SUPPL"</name>
                <amount>"-37.97"</amount>
                <description>"SP SECRET NAIL SUPPL"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"Shoppers Drug Mart"</name>
                <amount>"-6.25"</amount>
                <description>"SHOPPERS DRUG MART #2289"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"Matchstick Coffee"</name>
                <amount>"-7.18"</amount>
                <description>"Matchstick Coffee"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"AKZENTZ"</name>
                <amount>"-1008.0"</amount>
                <description>"AKZENTZ"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"MODERN BEAUTY SUPPLIES IN"</name>
                <amount>"-33.43"</amount>
                <description>"MODERN BEAUTY SUPPLIES IN"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"IN *LENSEN ENTERPRISES IN"</name>
                <amount>"-92.4"</amount>
                <description>"IN *LENSEN ENTERPRISES IN"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Charitable donation"</category>
                <name>"Covenant House Vancouver"</name>
                <amount>"-5.0"</amount>
                <description>"Covenant House Vancouver"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Gift Expense"</category>
                <name>"BROWNSSHOES.COM"</name>
                <amount>"-224.0"</amount>
                <description>"BROWNSSHOES.COM"</description>
                <paymentchannel>"online"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"KAO CANADA INC"</name>
                <amount>"-1017.47"</amount>
                <description>"KAO CANADA INC"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"LS THE CROSS DECOR AND"</name>
                <amount>"-274.4"</amount>
                <description>"LS THE CROSS DECOR AND"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"SP EURONAILS ONLINE"</name>
                <amount>"-21.8"</amount>
                <description>"SP EURONAILS ONLINE"</description>
                <paymentchannel>"online"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Supplies and Materials"</category>
                <name>"RCH* REVOLVE"</name>
                <amount>"-141.47"</amount>
                <description>"RCH* REVOLVE"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Charitable donation"</category>
                <name>"GOFNDME* HEALTHY HEART"</name>
                <amount>"-50.0"</amount>
                <description>"GOFNDME* HEALTHY HEART"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        <example>
                <category>"Repairs and Maintenance"</category>
                <name>"ARCTERYX Equipment"</name>
                <amount>"-156.8"</amount>
                <description>"ARCTERYX Equipment"</description>
                <paymentchannel>"in store"</paymentchannel>
                <type>"place"</type>
            </example>
        </examples>

We’ve provided a dataset with 3 sets of fields:
1. Original Transaction Data
accountId, date, name, amount, description, paymentChannel, type

​
2. AI-Generated Columns
Explanation, transactionId, AssignedCategory, ConfidenceScore, AccountNumber, TypeOfTransaction, Payee, Taxes

​
3. Bookkeeper-Annotated Corrections (if any)
These appear only when the AI categorization was incorrect:
Type of Transaction, Payee/Vendor, Category, Account Number, Tax, Memo/Notes'''

'''### Task 1: Evaluate AI Categorization Accuracy

Using the bookkeeper annotations as ground truth:

- Compare AI-generated `AssignedCategory` with the corrected `Category`
- Calculate precision, recall, F1 score for categorization (both overall and per-category if possible)
- Identify categories with highest and lowest accuracy

📎 *Bonus*: Visualize confusion between similar categories (e.g. “Chair Rental:Hair Chair” vs “Chair Rental:Lash Bed”)
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support

csv_file_path = 'Categorized_Transactions_Elle_Jan2025(in).csv'

# Load the dataset
df = pd.read_csv(csv_file_path)

# Replace empty strings with NaN in the bookkeeper correction column ("Category")
df['BookkeeperCategory'] = df['Category'].replace('', np.nan)

# Filter rows where a bookkeeper correction is provided (i.e. BookkeeperCategory is not null)
df_corr = df.dropna(subset=['BookkeeperCategory'])

if df_corr.empty:
    print("No bookkeeper corrections available for evaluation.")
else:
    # Ground truth and prediction
    y_true = df_corr['BookkeeperCategory']
    y_pred = df_corr['AssignedCategory']
    
    # Overall classification report
    print("Classification Report:")
    print(classification_report(y_true, y_pred, zero_division=0))
    
    # Overall precision, recall, and F1 score (weighted)
    overall_precision, overall_recall, overall_f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average='weighted', zero_division=0)
    print("Overall Metrics:")
    print(f"Precision: {overall_precision:.2f}")
    print(f"Recall: {overall_recall:.2f}")
    print(f"F1 Score: {overall_f1:.2f}")
    
    # Calculate per-category accuracy
    category_accuracy = {}
    for category in y_true.unique():
        mask = (y_true == category)
        if mask.sum() > 0:
            correct = (y_pred[mask] == category).sum()
            category_accuracy[category] = correct / mask.sum()
    
    sorted_accuracy = sorted(category_accuracy.items(), key=lambda x: x[1], reverse=True)
    print("\nPer-category Accuracy:")
    for cat, acc in sorted_accuracy:
        print(f"{cat}: {acc:.2f}")
    
    if sorted_accuracy:
        highest = sorted_accuracy[0]
        lowest = sorted_accuracy[-1]
        print(f"\nHighest Accuracy Category: {highest[0]} with accuracy {highest[1]:.2f}")
        print(f"Lowest Accuracy Category: {lowest[0]} with accuracy {lowest[1]:.2f}")
    
    # Visualize the confusion matrix
    labels = np.unique(np.concatenate([y_true.unique(), y_pred.unique()]))
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    
    plt.figure(figsize=(12,10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel("Assigned Category")
    plt.ylabel("Bookkeeper Category")
    plt.title("Confusion Matrix")
    plt.show()
