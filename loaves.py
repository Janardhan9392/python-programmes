n1=int(input("enter the number of fresh loves purchased:"));
n2=int(input("enter the number of fresh loves purchased:"));
regular_price=185;
print("the rgular price is :",regular_price);
amount_of_new_loaves=n1*regular_price;
amount_of_old_loaves=n2*regular_price*60/100;
total_amount=amount_of_new_loaves+amount_of_old_loaves;
print("amount of new loaves is :",amount_of_new_loaves);
print("amount of old loaves is :",amount_of_old_loaves);
print("the total amount is :",total_amount);
