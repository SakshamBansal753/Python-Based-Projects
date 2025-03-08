print("Hello Welcome To Tip Calculator")
bill=round(float(input("What Is Your Bill? $ ")),2)      #Taking Bill Upto 2 Decimal Point
tip=int(input("How Many Tip You Want To Give? 10,12,20,30= "))
User_Number=int(input("How many of You are Dividing the price?"))
Share_Bill=round((bill*(tip/100)+bill)/User_Number,3)
print(f"Each Of them Has TO Give ${Share_Bill}")         #F-String
