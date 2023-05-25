#a-z
#0-9
#. _ time 1
# @ time 1
# . 2, 3
#Regular expressions, often referred to as regex or regexp,
# are powerful tools for pattern matching and manipulating text
#pattern matching, data validation, text extraction, text manipulation, data cleaning , tokenization.
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input(" Enter your Email :")
if re.search(email_condition, user_email):
    print("Correct Email")
else:
    print("Wrong Email")