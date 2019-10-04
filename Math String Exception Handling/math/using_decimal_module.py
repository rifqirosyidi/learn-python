from decimal import Decimal as D

jumlah = D(0)
jumlah += D("0.1")
jumlah += D("0.1")
jumlah += D("0.1")
jumlah -= D("0.3")

print(jumlah)

# this Result below is not what we wanted
print(.1 + .1 + .1 - .3)