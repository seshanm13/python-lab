ages = (15, 21, 18, 45, 12, 30)

def check_voting_eligibility(age_tuple):
    eligible_count = 0
    print("Voting Status Check:")
    for age in age_tuple:
        if age >= 18:
            print(f"Age {age}: Eligible")
            eligible_count += 1
        else:
            print(f"Age {age}: Not Eligible")
    print(f"Total eligible voters: {eligible_count}")

check_voting_eligibility(ages)