class goa:
    name="adca"
    drink=""
    def party(self):
        print("Lets Party")
    def beach(self):
        print("Lets Beach")

ramesh=goa()
suresh=goa()


ramesh.name="Ramesh"
suresh.name="Suresh"
ramesh.drink="Yes"
suresh.drink="No"
print(ramesh.name)
print(suresh.name)
print(ramesh.drink)
print(suresh.drink)

ramesh.party()
suresh.beach()