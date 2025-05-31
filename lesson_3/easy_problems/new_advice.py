advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

stop = advice.find('house')

print(advice[:stop])
print(advice.split("house")[0])
