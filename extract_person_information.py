n = int(input())
final_age = 0
for _ in range(n):

    name_and_age = input()

    while "@" in name_and_age and "#" in name_and_age:
        start_name = name_and_age.find("@") + 1
        end_name = name_and_age.find("|")
        start_age = name_and_age.find("#") + 1
        end_age = name_and_age.find("*")
        final_name = name_and_age[start_name:end_name]
        final_age = int(name_and_age[start_age:end_age])

        print(f"{final_name} is {final_age} years old.")

        name_and_age = name_and_age.replace(f"@{final_name}|", "", 1).replace(f"#{final_age}*", "", 1)
