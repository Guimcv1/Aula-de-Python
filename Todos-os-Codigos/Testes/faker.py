from faker import Faker

fk = Faker()

for i in fk.profile:
    print(fk.profile, ':', fk.profile[i])