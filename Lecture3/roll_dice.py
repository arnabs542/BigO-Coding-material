

dice_chosen = []
def diceRoll(dice, dice_chosen):
	print('diceRoll({}, {})'.format(dice, dice_chosen))
	if dice == 0:
		print(dice_chosen)
		#base case	
	else:
		for i in range(1, 7):
			dice_chosen.append(i)	 #choose
			diceRoll(dice-1, dice_chosen) #explore
			dice_chosen.pop() #un-choose


def diceRollSum(dice, dice_chosen, desired_sum, sum_so_far):
	print('diceRollSum({}, {}, {})'.format(dice, dice_chosen, desired_sum))
	if dice == 0:
		print(dice_chosen)
		#base case	
	else:
		for i in range(1, 7):
			if ((sum_so_far + i + 1*(dice - 1) <= desired_sum) 
				and (sum_so_far + i + 6*(dice - 1) >= desired_sum)):
				print('sum = {}, i = {}, dice {}'.format(sum_so_far, i, dice_chosen))
				dice_chosen.append(i)	 #choose
				diceRollSum(dice-1, dice_chosen, desired_sum, sum_so_far + i) #explore
				dice_chosen.pop() #un-choose




#diceRoll(3, dice_chosen)
diceRollSum(4, dice_chosen, 9, 0)
		
