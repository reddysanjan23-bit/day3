contects = {
    "Preeti": "9112867023",
    "Sanjana": "827867898",
    "Ankita":"9911234902",

}
contects["Kiran"] = '9910254786'
contects["ravi"] = ' 9987373892'
contects["Ankita"] = '9788667889'

print("Lookup Preeti:", contects.get("Preeti","Not found"))
print("Lookup Ankita:", contects.get("Ankita","Not found"))

for name, number in contects.items():
    print("contect:",name,"number:",number)

    raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
is_id05_present = "ID05" in unique_users
original_count = len(raw_logs)
unique_count = len(unique_users)

print("Unique User IDs:", unique_users)
print("Is 'ID05' present?:", is_id05_present)
print("Original log count:", original_count)
print("Unique user count:", unique_count)
print("Duplicates removed:", original_count - unique_count)

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
shared_interests = friend_a & friend_b
all_interests = friend_a | friend_b
unique_to_a = friend_a - friend_b

print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Interests Unique to Friend A:", unique_to_a)