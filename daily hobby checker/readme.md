# Hello Young Guns, I am Saksham 🚴‍♂️

Welcome to my Pixela-based Python project! This script helps you track your daily cycling activity using the Pixela API.

## 📌 What Does This Project Do?

This project allows you to:
1. **Create a user account** on [Pixela](https://pixe.la).
2. **Create a graph** to track a habit (like cycling).
3. **Log daily activity** (e.g., how many kilometers you cycled).
4. **Update past entries** in case you made a mistake or changed your workout.

                                         
##  🚀 How to Use It

###  Follow all the steps i commented

# 🧠 Example Output
```bash
Copy code
How many km You cycle today? 12.4
{"message":"Success","isSuccess":true}
```
# How Date is Handled
The script automatically takes today’s date using:
````
python
Copy code
from datetime import datetime
today = datetime.now().strftime("%Y%m%d")
````
## TO see the page i shared screenshot with you go to [https://pixe.la/v1/users/{YOUR_USERNAME}/graphs/{YOUR_GRAPH_ID}.html]
# 📸Preview
<img src="https://github.com/SakshamBansal753/Python-Based-Projects/blob/main/daily%20hobby%20checker/Screenshot%202025-05-11%20115403.png"/>
