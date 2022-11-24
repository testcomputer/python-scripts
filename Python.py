print("Welcome to the testcomputer's automated help desk")
name = input("Please enter your first and last name. ")
input("Email:")
input("Phone:")
Task = input('What is your purpose')

if Task == ("To understand everything")
print("Understood")
else: 
  (input("What is your timeline")
   
print(f"Thank you {name} for using Python practice tool")
   
   
   How to create a user in AD using python
   
   
from pyad import *
pyad.set_defaults(ldap_server="dc1.domain.com", username="service_account", password="mypassword")
ou = ADContainer.from_dn("ou=users, dc=domain, dc=com")
new_user = ADUser.create("Daniel", ou, password="Secret")


new_user.set_attribute("mail", "daniel@example.com")
group = ADGroup.from_dn("so-users")
group.add_member(new_user)


new_user.delete()
