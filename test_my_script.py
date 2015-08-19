import math
import random
import tournament

# register tournaments
chess_tournament = tournament.registerTournament('Chess Master Tournament')

# register players
a = tournament.registerPlayer('A')
b = tournament.registerPlayer('B')
c = tournament.registerPlayer('C')
d = tournament.registerPlayer('D')
e = tournament.registerPlayer('E')
f = tournament.registerPlayer('F')
g = tournament.registerPlayer('G')
h = tournament.registerPlayer('H')
i = tournament.registerPlayer('I')
j = tournament.registerPlayer('J')

# register tournaments players
tournament.registerTournamentPlayer(chess_tournament, a)
tournament.registerTournamentPlayer(chess_tournament, b)
tournament.registerTournamentPlayer(chess_tournament, c)
tournament.registerTournamentPlayer(chess_tournament, d)
tournament.registerTournamentPlayer(chess_tournament, e)
tournament.registerTournamentPlayer(chess_tournament, f)
tournament.registerTournamentPlayer(chess_tournament, g)
tournament.registerTournamentPlayer(chess_tournament, h)
tournament.registerTournamentPlayer(chess_tournament, i)
tournament.registerTournamentPlayer(chess_tournament, j)

# number of rounds for chess tournament
rounds = int(math.ceil(math.log(tournament.countTournamentPlayers(chess_tournament), 2)))

# record matches
for round in range(0, rounds):
    # generate pairs  for chess tournament
    pairs = tournament.swissPairings(chess_tournament)
    print pairs
    for pair in pairs:
        if pair[0] < pair[2] or pair[2] == None:
            result = 1
        else:
            result = 2
        tournament.reportMatch(chess_tournament, pair[0], pair[2], result)
