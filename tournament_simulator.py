import math
import random
import tournament

# register tournaments
chess_tournament = tournament.registerTournament('Chess Master Tournament')

# register players
a = tournament.registerPlayer('Adam')
b = tournament.registerPlayer('Bogdan')
c = tournament.registerPlayer('Cristina')
d = tournament.registerPlayer('Daniel')
e = tournament.registerPlayer('Elena')

# register tournaments players
tournament.registerTournamentPlayer(chess_tournament, a)
tournament.registerTournamentPlayer(chess_tournament, b)
tournament.registerTournamentPlayer(chess_tournament, c)
tournament.registerTournamentPlayer(chess_tournament, d)
tournament.registerTournamentPlayer(chess_tournament, e)

# number of rounds for chess tournament
rounds = int(math.ceil(math.log(tournament.countTournamentPlayers(chess_tournament), 2)))

# record matches
for round in range(0, rounds):
    print "\nROUND", round + 1
    print "".rjust(10, "_"), "\n"
    # generate pairs  for chess tournament
    pairs = tournament.swissPairings(chess_tournament)
    for pair in pairs:
        if pair[2] == None:
            result = 1
        elif pair[0] == None:
            result = 2
        else:
            result = random.randint(0, 2)
        tournament.reportMatch(chess_tournament, pair[0], pair[2], result)
        print pair[1].ljust(8), "vs ", pair[3].ljust(8), "->", result

standings = tournament.playerTournamentStandings(chess_tournament)
print "\n________\n\nRESULTS:\n________\n"
for player in standings:
    print player[2].ljust(10), str(player[6]).rjust(2) + " pts"
print "\n"
