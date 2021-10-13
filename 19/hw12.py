#Name:  Xing Tao Shi
#Email:  XingTao.Shi50@myhunter.cuny.edu
#Date: September 30, 2021
#This program DOESNT WORK WOOOOOOO

'''
Ask the user for amount of social media followers they have.
Compute and output the their influencer tier as follows:
  - Error if followers less than 0
  - Hyper Influencer if number of followers less than 1K followers
  - Nano Influencer if number of followers 1K-10K followers (not including 10k)
  - Micro Influencer if number of followers 10K-100K followers (not including 100k)
  - Mid-Tier Influencer if number of followers 100K-500K followers (not including 500k)
  - Macro-Influencer if number of followers 500K-1M followers (not including 1M)
  - Celebrity Influencer if number of followers greater than 1M followers

Enter amount of social media followers: 150
Your influencer tier is: Hyper Influencer
'''

numInfluencers = int(input("Enter amount of social media followers: "))
tier = ""

if numInfluencers < 0:
  tier = "Error"
elif numInfluencers < 1000:
  tier = "Hyper Influencer"
elif numInfluencers < 10000:
  tier = "Nano Influencer"
elif numInfluencers < 100000:
  tier = "Micro Influencer"
elif numInfluencers < 500000:
  tier = "Mid-Tier Influencer"
elif numInfluencers < 1000000:
  tier = "Macro-Influencer"
else:
  tier = "Celebrity Influencer"

print("Your influencer tier is: " + tier)