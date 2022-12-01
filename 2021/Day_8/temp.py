#     if all([char in signal for char in pattern_8]):
#         return 8
#     elif all([char in signal for char in pattern_9]):
#         return 9
#     elif all([char in signal for char in pattern_6]):
#         return 6
#     elif all([char in signal for char in pattern_0]):
#         return 0
#     elif all([char in signal for char in pattern_5]):
#         return 5
#     elif all([char in signal for char in pattern_3]):
#         return 3
#     elif all([char in signal for char in pattern_2]):
#         return 2
#     elif all([char in signal for char in pattern_4]):
#         return 4
#     elif all([char in signal for char in pattern_7]):
#         return 7
#     elif all([char in signal for char in pattern_1]):
#         return 1



# def translate_pattern(signal):

#     # unique
#     pattern_8 = ['a','c','e','d','g','f','b']
#     pattern_4 = ['e','a','f','b']
#     pattern_7 = ['d','a','b']
#     pattern_1 = ['a','b']
    
#     # to be determined
#     pattern_9 = ['c','e','f','a','b','d']
#     pattern_6 = ['c','d','f','g','e','b']
#     pattern_0 = ['c','a','g','e','d','b']
    
#     pattern_5 = ['c','d','f','b','e']
#     pattern_3 = ['f','b','c','a','d']
#     pattern_2 = ['g','c','d','f','a']
    


    # #  3 = top + left bottom corner + mid left corner
    # pattern_3 = []
    # for char in mid_left_corner:
    #     if char not in pattern_3:
    #         pattern_3.append(char)
    # for char in bottom_left_corner:
    #     if char not in pattern_3:
    #         pattern_3.append(char)
    # for char in top_line:
    #     if char not in pattern_3:
    #         pattern_3.append(char)
    
    # print("pattern 3", pattern_3)
    # decoded_patterns[3] = pattern_3
