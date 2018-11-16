####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'query5' # Only 10 chars displayed.
strategy_name = 'brain bot'
strategy_description = 'test and decide'
global times
times = 0   
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    bot1 = 'bbb',
    bot2 = 'ccc',
    bot3 = 'cbb',
    bot4 = 'cbc',
    bot5 = 'ccb',
    bot6 = 'bbc',
    bot7 = 'bcb'
    bot8 = 'bcc'
    global times
    
    while times < 3:
        return 'b'
        times = times + 1
    if their_history[0,1,2] == bot1 or their_history[0,1,2] == bot3 and times ==3:
        return 'c'
        times = times + 1
    elif their_history[0,1,2] == bot1 or their_history[0,1,2] == bot3 and times ==4:
        return 'b'
        times = times + 1
    else:
        times = 7
    if their_history[1,2,3,4] == my_history[0,1,2,3]:
        return 'c'
    else:
        return 'b'
    
            

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             