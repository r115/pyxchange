# $changer = new PyChanger();
# $moneychanger = new PyChanger();
#
# enter you currency
# $changer->setCurrency();
# Set amount
# $changer->setAmount()
# Convert 
# $changer->setNewCurrency()
# $changer->convert()
from exchangers.changer import PyChanger

changer = PyChanger(base_currency="tzs", exchange_rate=50)

converted_value = changer.convert()

# print(converted_value)
