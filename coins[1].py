# name of student: 
# number of student: 
# purpose of program: 
# function of program:
# structure of program: 


toPay = int(float(input('Amount to pay: '))* 100) #hier voer je in wat je moet betalen
paid = int(float(input('Paid amount: ')) * 100) #hier voer je in wat je betaald heb 
change = paid - toPay #hier bereken je het wisselgeld

if change > 0: #wisselgeld
  coinValue = 500 #waarde van het geld
  
  while change > 0 and coinValue > 0: #dit zorgt ervoor dat de lijn hieronder uitgevoerd wordt
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cent!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    elif coinValue == 1:
      coinValue = 0.5
    elif coinValue == 0.5:
      coinValue = 0.2
    elif coinValue == 0.2:
      coinValue = 0.1
    else:
      coinValue = 0

if change > 0: #als er geld over is dat niet terug gegeven is wordt dat hier toegeleid
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')