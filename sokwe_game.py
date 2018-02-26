# """
# ***************************************************************
# *               SOKWE GAME                                    *
# ***************************************************************
# """


# import random module especially the sample method
from random import sample

def sokwe_game():
    # start the game by asking him / her sokwe
    # if is not respoding niruze we have  to redemand
    #  inorder to get the *niruze* response
    niruze_response = input("Sokwe:")

    while(niruze_response.lower() != "niruze" ):
        print("Ntibishura", "*"+niruze_response+"*", "Bishura *Niruze* ")
        niruze_response = input("Sokwe: ")

    try:
        # get ibisokozos for files/ibisokozo.txt file
        with open("files/ibisokozo.txt") ibisokozos_file:

        # empty dictionnary to store ibisokozo
        ibisokozo  = {}

        for ibisokozo_file in ibisokozos_file:
            # split igisokozo with the equal symbol and store it in tuple
            (igisokozo, inyishu) = ibisokozo_file.split("=")

            # format the igisokozo and inyishu by
            # removing rounded spaces and lowercased them
            # after store in the in an empty dictionnary created
            igisokozo = igisokozo.strip().lower()
            inyishu = inyishu.strip().lower()

            ibisokozo[igisokozo] = inyishu

        # Demand the user the number of questions he wants
        # if he demands the number which won't surpass the number of ibisoko we have
        # then we accept it else we give he all ibisokozo we have
        question = int(input("Ushaka ibisokozo bingahe? :"))

        if(question <= len(ibisokozo)):
            question = question
        else:
            question = len(ibisokozo)

        ibisokozo_list = sample(list(ibisokozo), question)

        for igisokozo in ibisokozo_list:
            user_response = input(igisokozo + ":")
            print(user_response)

    except FileNotFoundError:
        print("Sorry ububiko bwibisokozo ntabuhari tugiye kubikosora")


sokwe_game()
# try:
#     # get ibisokozo
#     ibisokozo_file = open('files/ibisokozo.txt')

#     # a empty dict which will store all ibisokozo
#     ibisokozo = {}


#     #start the game
#     niruze_response = input("Sokwe:")

#     if(niruze_response.lower() == 'niruze'):
#         for line in ibisokozo_file:
#             # split the file in two parts by an equal symbol
#             # and format the result
#             (igisokozo, inyishu) = line.split('=')
#             igisokozo = igisokozo.lower().strip()
#             inyishu = inyishu
#             # .lower().strip().replace('\'', '')

#             # store ibisokozo in a dictionnary
#             ibisokozo[igisokozo] = inyishu

#         # asking the user number of questions
#         # if he demand a number of ibisokozo which is lower than what we hava accept it
#         # else asking  him the number of ibisokozo we have
#         try:
#             questions = int(input("Ushaka ibisokozo bingahe:"))

#             if(questions <= len(ibisokozo)):
#                 questions = questions
#             else:
#                 questions = len(ibisokozo)

#             score = 0

#             ibisokozo_list = sample(list(ibisokozo), questions)

#             for igisokozo in ibisokozo_list:
#                 user_response = input(igisokozo + ':')
#                 user_response = user_response

#                 if(user_response.strip().lower().replace('\'', '').replace(' ', '') == ibisokozo[igisokozo].lower().strip().replace('\'', '').replace(' ', '')):
#                     score += 1
#                     print("\n\tWell Done\n")
#                 else:
#                     print("\n\toya warikwishura ati: ", ibisokozo[igisokozo], "\n")

#             print("*************************************")
#             print( "Finish ! << score : ", score , '/' , questions )
#             print("*************************************")

#         except ValueError:
#             print("please andika igiharuro apana ijambo ")

#     else:
#         print("Oya ntibishura", '***',niruze_response,'***' , '***bishura niruze***')


# except FileNotFoundError:
#     print("Sorry ububiko bwibisokozo ntabuhari tugiye kubikosora")

# finally:
#     ibisokozo_file.close()