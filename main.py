from sokwe_game import sokwe_game


if(__name__ == "__main__"):
    sokwe_game()



continue_response = input("\n\tUshaka kubandanya? ishura ego/oya: ")

# while the respond ego(yes) we re-executed the code
# hosted in the sokwe_game function
while(continue_response.lower() == "ego"):
    sokwe_game()
    continue_response = input("\n\tUshaka kubandanya? ishura ego/oya: ")

print("\n\tUrakoze gukina Bye Bye!!!")
