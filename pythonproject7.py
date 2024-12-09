#F-L-A-M-E-S G-A-M-E 
def remove_match(list_1,list_2):
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i]==list_2[j]:
                char=list_1[i]
                list_1.remove(char)
                list_2.remove(char)

                list_3=list_1+["*"]+list_2
                return [list_3,True]
        
    list_3=list_1+["*"]+list_2
    return [list_3,False]
    



if __name__=="__main__":
    p1=input("name of the player 1: ")
    # converted all letters into lower case
    p1 = p1.lower()
 
    # replace any space with empty string
    p1.replace(" ", "")
 
    # make a list of letters or characters
    p1_list = list(p1)
 
    # take 2nd name
    p2 = input("Player 2 name : ")
    p2 = p2.lower()
    p2.replace(" ", "")
    p2_list = list(p2)

    proceed=True 

    while proceed:

        return_list = remove_match(p1_list,p2_list) 

        con_list = return_list[0]
 
        # take out flag value from return list
        proceed = return_list[1]
 
        # find the index of "*" / border mark
        star_index = con_list.index("*")
 
        # list slicing perform
 
        # all characters before * store in p1_list
        p1_list = con_list[: star_index]
 
        # all characters after * store in p2_list
        p2_list = con_list[star_index + 1:]
 
    # count total remaining characters
    count = len(p1_list) + len(p2_list)
 
    # list of FLAMES acronym
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:
 
        # store that index value from
        # where we have to perform slicing.
        split_index = (count % len(result) - 1)
 
        # this steps is done for performing
        # anticlock-wise circular fashion counting.
        if split_index >= 0:
 
            # list slicing
            right = result[split_index + 1:]
            left = result[: split_index]
 
            # list concatenation
            result = right + left
 
        else:
            result = result[: len(result) - 1]
 
    # print final result
    print("Relationship status :", result[0])
