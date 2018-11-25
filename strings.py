## This is a function that takes the user's input and counts how many lower or
##upper case letters, integer numbers and other type of characters there are
##in your input. It's a good way for working with conditional statements and
##for loops.

def string_counter(urinput):
	
	count_lower = 0
	count_upper = 0
	count_numbers = 0
	count_other = 0
	
	for c in urinput: #It goes through each characters in your input and
                            #compares it to the conditional statements below.
		if c.islower() == True: ##.islower() is a Python method
                                        ##that checks if a character is lower
                                        ##case. It turns True or False answers.
			count_lower+=1   ##The counter we've set up there
                                        ##receives one more unit every time
                                        ##there is a match.
		elif c.isupper() == True: ##Now, we check character by character
                                          ##looking for upper case letters.
			count_upper+=1    ##Nah! You don't need a comment on
                                            ##this line. You already got it.
		elif c.isdigit() == True: ##.isdigit() is a method that checks
                                            ##for a number. And now you ask what
                                            ##the difference is between
                                            ##.isdigit() and .isnumeric().
                                            #The difference is the way those
                                            ##methods deal with UNICODE characters.
			count_numbers+=1
		else: ##if the character does not fit in any of the above categories,
                    ##it will fall in this category.
			count_other+=1

			
	print("The number of lower case characters is: ", count_lower,
              "\n The number of upper case characters is: ", count_upper,
              "\n The number of numbers in your string is: ", count_numbers,
              "\n All the other things you typed accoun for: ", count_other)
