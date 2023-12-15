# import random 


# # function to generate 
# # a random string 
# def generateOne(strlen): 
	
# 	# string with all the alphabets 
# 	# and a space 
# 	alphabet = "abcdefghijklmnopqrstuvwxyz "
# 	res ="" 
	
# 	for i in range(strlen): 
# 		res+= alphabet[random.randrange(27)] 
		
# 	return res 

# # function to determine the 
# # score of the generated string 
# def score(goal, testString): 
# 	numSame = 0
	
# 	for i in range(len(goal)): 
# 		if goal[i] == testString[i]: 
# 			numSame+= 1
			
# 	return numSame / len(goal) 

# # main function to call the previous 
# # two functions until the goal is achieved 
# def main(): 
# 	goalString = "a computer science portal for geeks"
# 	newString = generateOne(35) 
# 	best = 0
# 	newScore = score(goalString, newString) 
	
# 	while newScore<1: 
# 		if newScore>best: 
# 			print(newString) 
# 			best = newScore 
# 		newString = generateOne(35) 
# 		newScore = score(goalString, newString) 

# # Driver code 
# main()

# def test_1(string =""): 
	
# 	# initializing the substring 
# 	substring = "" 
# 	testList = [] 
# 	initial = 0
	
# 	for char in string: 
		
# 		for i in range(initial, len(string)): 
# 			substring+= string[i] 
			
# 			# checking conditions 
# 			if substring.count(string[i])>1: 
# 				testList.append(substring[:-1]) 
# 				initial+= 1
# 				substring = "" 
# 				break
# 	maxi ="" 
	
# 	for word in testList: 
		
# 		if len(word)>len(maxi): 
# 			maxi = word 
			
# 	if len(maxi)<3: 
# 		return "-1"
# 	else: 
# 		return maxi 
	
# # Driver code 
# print(test_1("character")) 
# print(test_1("standfan")) 
# print(test_1("class"))

# import random 


# # generates a four-digit code 
# def gen_code(): 
# 	set_code = [] 
	
# 	for i in range(4): 
# 		val = random.randint(0, 9) 
# 		set_code.append(val) 
		
# 	return set_code 
	
# # asks for input from the user 
# def input_code(): 
# 	code = input("Enter your four digit guess code: ") 
# 	return code 


# plays the game 
# def mastermind(): 
	
# 	genCode = gen_code() 
# 	i = 0
	
# 	while i < 10: 
# 		result = "" 
# 		inputCode = [int(c) for c in input_code()] 
		
# 		if len(inputCode) != 4: 
# 			print("Enter only 4 digit number") 
# 			continue
		
# 		if inputCode == genCode: 
# 			print("You guessed it !", genCode) 
# 			break
			
# 		for element in inputCode: 
			
# 			if element in genCode: 
				
# 				if inputCode.index(element) == genCode.index(element): 
# 					result+="R"
# 				else: 
# 					result+="Y"
# 			else: 
# 				result+="B"
# 		print(result) 
		
# 		i += 1
# 	else:	 
# 		print("You ran out of trys !", genCode)	 
		
		
# # Driver Code 
# mastermind()

