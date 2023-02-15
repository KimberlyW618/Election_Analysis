count = 7
while count < 1:
    print("Hello World")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
{"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

print(voting_data)

for vd in voting_data:
    print(f'{vd["county"]} has {vd["registered_voters"]} registered voters')







