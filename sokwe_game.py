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
        print("Ntibishura *{}* Bishura *Niruze* ".format(niruze_response))
        niruze_response = input("Sokwe: ")

    try:

        # empty dictionnary to store ibisokozo
        ibisokozo  = {}

        # get ibisokozos for files/ibisokozo.txt file
        with open("files/ibisokozo.txt") as ibisokozos_file:

            for ibisokozo_file in ibisokozos_file:
                # split igisokozo with the equal symbol and store it in tuple
                (igisokozo, inyishu) = ibisokozo_file.split("=")

                # format the igisokozo and inyishu by
                # removing rounded spaces and lowercased them
                # after store in the in an empty dictionnary created
                igisokozo = igisokozo
                inyishu = inyishu

                ibisokozo[igisokozo] = inyishu

        # if for the question the user enter the string value throw an exception
        try:
            # Demand the user the number of questions he wants
            # if he demands the number which won't surpass the number of ibisoko we have
            # then we accept it else we give he all ibisokozo we have
            questions = int(input("Ushaka ibisokozo bingahe?: "))

            if(questions <= len(ibisokozo)):
                questions = questions
            else:
                questions = len(ibisokozo)

            # initialize the user_score and the device score
            # at the start they equal to zero but they'll increment when they guess
            # the answer
            user_score = 0
            device_score = 0

            # get ibisokozo randomely with sample method from the random module
            ibisokozo_list = sample(list(ibisokozo), questions)


            for igisokozo in ibisokozo_list:
                user_response = input(igisokozo + ": ")

                # format the user_response and the device response as the same
                # inorder to have the same values from the device response and user_response
                user_response = user_response.strip().lower().replace(' ', '').replace('\'', '')

                device_response = ibisokozo[igisokozo].strip().lower().replace(' ', '').replace('\'', '')

                # while the user_response is not equals to the device response
                # and while the user response is not equals
                # to "ndaguhaye"(because the user should want to reply ndaguhaye directly
                # and because we have the condition of this iteration block below
                # it'll be valuated to True)
                # looping until the user get the response or replies ndaguhaye if he replies
                # ndaguhaye get out of the iteration block and continue
                while(user_response != device_response and user_response != "ndaguhaye"):

                    user_response = input("Uhh!! inyishu siyo ushaka kugerageza kandi? canke wishure *ndaguhaye*: ")

                    user_response = user_response.strip().lower().replace(' ', '').replace('\'', '')

                    if(user_response == "ndaguhaye"):
                        break

                if(user_response == "ndaguhaye"):

                    print("\n\t Warikwishura ati: {} \n".format(ibisokozo[igisokozo]))

                else:
                    user_score += 1
                    print("\n\tWell Done\n")

            print("*************************************")
            print( "Finish ! << score : ", user_score , '/' , questions )
            print("*************************************")


        except ValueError:
            print("Please andika igiharuro apana ijambo")


    except FileNotFoundError:
        print("Sorry ububiko bwibisokozo ntabuhari tugiye kubikosora")


sokwe_game()