class purchase(object):
    def __init__(self, amount):
        self.amount = amount

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

purchase = purchase(100.0)

taxPercent = 7.5
tipPercent = 20.0

tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

print('tax:', tax)
print('tip:', tip)
print('total:', purchase.calculateTotal(taxPercent, tipPercent))

#missybernskoetter