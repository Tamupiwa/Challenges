#coding challenges
'''
overlapping rectangles probelem

given the bottom left and top right coodinates of two rectangles
find the coodinates where they overlap
'''
#rec_one and rec_two is respectuve bottom left and top right coodinates
#.. for the first and second rectangles as a 2d list
def overlapping_rectangles(rect_one, rec_two):
    #tracks the starting point of rectangle one on x axis that is overlapping
    #.. with rectangle two
    start_point_x = ''
    #tracks the end point of rectangle one on x axis that is overlapping
    #.. with rectangle two
    end_point_x = ''
    #tracks the starting point of rectangle one on y axis that is overlapping
    #.. with rectangle two
    start_point_y = ''
    #tracks the end point of rectangle one on y axis that is overlapping
    #.. with rectangle two
    end_point_y = ''
    #lowest x point of rectangle two
    left_plane = rec_two[0][0]
    #lowest y point of rectangle two
    bottom_plane = rect_two[0,1]
    #highest x point of rectangle two
    right_plane = rec_two[1][0]
    #highest y point of rectangle two
    top_plane = rect_two[1][1]
    #iterate the bottom x plane of first triangle to find overlap from left to right
    for x in rangex(rec_one[0][0], rec_one[1][0], 1):
        for y in rangex(rec[0][1], rec_one[1][1])
            #check if x and y are within the x and y plane boundaries of rectangle two
            if x >= bottom_plane and y >= left_plane and
            x =< top_plane and y =< right_plane:

                #if theres no start point make this point the start point
                if not start_point:
                    start_point = [x,y]

                #otherwise make it the end point
                else:
                    end_point =  [x,y]

    #if there were no starting and ending points there is no overlap
    if not start_point and not end_point:
        return False

    return [start_point, end_point]


#could use recursion instead of iteration
def factorial(num):
    num = 0
    for n in range(1, num + 1)
        if n == 1:
            num = n * n+1
        else:
            num = n * num
    return num

#;)
def factorial(num):
    multiples = range(1, num + 1)
    return eval('*'.join(str(n) for n in multiples))

def is_positive_dominant(lst):
    pos_dict = {}
    neg_dict = {}
    for l in lst:
        if l < 0:
            neg_dict[l] += 1
        else:
            pos_dict[l] += 1

    return max(pos_dict, key=dict.get) > max(neg_dict, key=dict.get)

#A consecutive-run is a list of adjacent, consecutive integers. This list can be either
#increasing or decreasing. Create a function that takes a list of numbers and returns
#the length of the longest consecutive
#longest_run([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
# Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
#*** this only works for runs counting upwards and not downwards
def longest_run(lst):
    longest_run = 0
    curr_run = 1
    for n in lst:
        #stop if last element has been reached
        if n == lst[-1]:
            break
        if curr_run > longest_run:
            longest_run = curr_run
        #if the next number is plus one of the previous add to the run
        if lst[n+1] == n + 1:
            curr_run += 1
            #otherwise start run again
        else:
            curr_run = 1
    return longest_run

#Create a function that returns True if two strings share the same letter pattern, and False otherwise.
#same_letter_pattern("ABCBA", "BCDCB") ➞ True
#same_letter_pattern("FFGG", "CDCD") ➞ False
def same_letter_pattern(txt1, txt2):




#If the list is [3, 5, 2, -4, 8, 11] and the sum is 7,
#... this function returns [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
def two_sum(lst, s):
    last_number = 0
    for n in lst:
        if last_number -
    return sums


#checks how many days and consecutive losing days its takes for ruin given a coin toss
#with assymetric payoff (lose/win $5), starting with $100
def survival():
  counter = 0
  balance = 100
  coin = ['heads', 'tails']
  for x in range(300000):
    counter = counter + 1
    toss = random.choice(coin)
    if toss == 'heads':
      balance = balance - 5
    else:
      balance = balance + 5
    if balance == 100:
      counter = 0
    if balance == 0:
      print 'bankrupt after: ' + str(x) + ' bets'
      print 'After: ' + str(counter) + ' consecutive losses'
      break
