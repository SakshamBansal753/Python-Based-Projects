bid_data={}
maxout_bid={}
continue_bid=True
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to IPL Mega Auction I am Saksham Bansal Your Auctioneer Lets Start Bidding With Virat Kohli")
while continue_bid:
    name = input("What Is Your Name?\n").lower()
    bid = int(input("What is YOur Bid?\n $"))
    bid_data[name]=bid
    is_continue=input("For Continue Bid Enter (y) For Exit (n)?\n").lower()
    if is_continue=="y":
        print("\n"*25)
    else:
        continue_bid=False
max_bid=0
max_bidder=""
for key in bid_data:

    if bid_data[key] >max_bid:
        max_bid=bid_data[key]
        max_bidder=key
maxout_bid[max_bidder]=max_bid
print(f"The Item Auctioned or You say now is off {maxout_bid} Thank YOU")
