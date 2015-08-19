#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeleteMatches():
    deleteMatches()
    print "1. Old matches can be deleted."

def testDeleteTournamentsPlayers():
    deleteTournamentsPlayers()
    print "2. Old tournaments players records can be deleted."

def testDeleteTournaments():
    deleteTournaments()
    print "3. Old tournament records can be deleted."

def testDelete():
    deleteMatches()
    deleteTournamentsPlayers()
    deletePlayers()
    print "4. Old player records can be deleted."

def testCount():
    deleteMatches()
    deleteTournamentsPlayers()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. After deleting, countPlayers() returns zero."

def testCountTournaments():
    deleteMatches()
    deleteTournamentsPlayers()
    deleteTournaments()
    c = countTournaments()
    if c == '0':
        raise TypeError(
            "countTournaments() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countTournaments should return zero.")
    print "6. After deleting, countTournaments() returns zero."

def testRegisterPlayer():
    deleteMatches()
    deleteTournamentsPlayers()
    deletePlayers()
    registerPlayer("Chandra Nalaar")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "7. After registering a player, countPlayers() returns 1."

def testRegisterTournament():
    deleteMatches()
    deleteTournaments()
    registerTournament("Chess Tournament")
    c = countTournaments()
    if c != 1:
        raise ValueError(
            "After one tournament is registered, countTournaments() should be 1.")
    print "8. After registering a tournament, countTournaments() returns 1."

def testRegisterTournamentPlayer():
    deleteMatches()
    deleteTournamentsPlayers()
    deletePlayers()
    deleteTournaments()
    player = registerPlayer("Chandra Nalaar")
    tournament = registerTournament("Chess Beginner")
    registerTournamentPlayer(tournament, player)
    c = countTournamentPlayers(tournament)
    if c != 1:
        raise ValueError(
            "After one player registers to a tournament, countTournamentPlayers() should be 1.")
    print "9. After registering a player to a tournament, countTournamentPlayers() returns 1."

def testRegisterCountDelete():
    deleteMatches()
    deleteTournamentsPlayers()
    deletePlayers()
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "10. Players can be registered and deleted."

def testRegisterCountTournamentsDelete():
    deleteMatches()
    deleteTournamentsPlayers()
    deleteTournaments()
    registerTournament("Chess Markov's Tournament")
    registerTournament("Swiss Joe's Tournament")
    registerTournament("Mao Tsu-hsi Tournament")
    c = countTournaments()
    if c != 3:
        raise ValueError(
            "After registering three tournaments, countTournaments should be 3.")
    deleteTournaments()
    c = countTournaments()
    if c != 0:
        raise ValueError("After deleting, countTournaments should return zero.")
    print "11. Tournaments can be registered and deleted."

def testRegisterCountTournamentsPlayersDelete():
    deleteMatches()
    deleteTournamentsPlayers()
    deleteTournaments()
    deletePlayers()
    tournament1 = registerTournament("Chess Markov's Tournament")
    tournament2 = registerTournament("Swiss Joe's Tournament")
    tournament3 = registerTournament("Soccer Tournament")
    player1 = registerPlayer("Markov Chaney")
    player2 = registerPlayer("Joe Malik")
    player3 = registerPlayer("Mao Tsu-hsi")
    player4 = registerPlayer("Atlanta Hope")
    registerTournamentPlayer(tournament1, player1)
    registerTournamentPlayer(tournament1, player2)
    registerTournamentPlayer(tournament1, player3)
    registerTournamentPlayer(tournament2, player4)
    registerTournamentPlayer(tournament2, player2)
    registerTournamentPlayer(tournament3, player1)
    registerTournamentPlayer(tournament3, player2)
    registerTournamentPlayer(tournament3, player3)
    registerTournamentPlayer(tournament3, player4)

    c = countTournamentPlayers(tournament1)
    if c != 3:
        raise ValueError(
            "After three players registers to a tournament, countTournamentPlayers() should be 3.")
    deleteTournamentPlayers(tournament1)
    c = countTournamentPlayers(tournament1)
    if c != 0:
        raise ValueError("After deleting, countTournamentPlayers should return zero.")

    c = countTournamentPlayers(tournament2)
    if c != 2:
        raise ValueError(
            "After two players registers to a tournament, countTournamentPlayers() should be 2.")
    deleteTournamentPlayers(tournament2)
    c = countTournamentPlayers(tournament2)
    if c != 0:
        raise ValueError("After deleting, countTournamentPlayers should return zero.")

    deleteTournamentsPlayers()
    c = countTournamentsPlayers()
    if c != 0:
        raise ValueError("After deleting, countTournamentsPlayers should return zero.")
    print "12. Tournaments players can be registered and deleted."


def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 7:
        raise ValueError("Each playerStandings row should have seven columns.")
    [(tournament_id1, player_id1, player_name1, matches1, wins1, draws1, points1),
     (tournament_id2, player_id2, player_name2, matches2, wins2, draws2, points2)
    ] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if tournament_id1 != None or tournament_id2 != None:
        raise ValueError(
            "Newly registed players should not be registered to any tournament")
    if set([player_name1, player_name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "13. Newly registered players appear in the standings with no matches."


def testReportMatches():
    deleteMatches()
    deleteTournamentsPlayers()
    deleteTournaments()
    deletePlayers()
    tournament = registerTournament("Chess Tournament")
    player1 = registerPlayer("Bruno Walton")
    player2 = registerPlayer("Boots O'Neal")
    player3 = registerPlayer("Cathy Burton")
    player4 = registerPlayer("Diane Grant")
    registerTournamentPlayer(tournament, player1)
    registerTournamentPlayer(tournament, player2)
    registerTournamentPlayer(tournament, player3)
    registerTournamentPlayer(tournament, player4)

    reportMatch(tournament, player1, player2, 1)
    reportMatch(tournament, player3, player4, 1)
    standings = playerStandings()
    for (ti, i, n, m, w, d, p) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (player1, player3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (player1, player3) and p != 3:
            raise ValueError("Each match winner should have three points recorded.")
        elif i in (player2, player4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
        elif i in (player2, player4) and p != 0:
            raise ValueError("Each match loser should have zero points recorded.")
    print "14. After a match, players have updated standings."


def testPairings():
    deleteMatches()
    deleteTournamentsPlayers()
    deleteTournaments()
    deletePlayers()
    tournament = registerTournament("Chess Tournament")
    player1 = registerPlayer("Twilight Sparkle")
    player2 = registerPlayer("Fluttershy")
    player3 = registerPlayer("Applejack")
    player4 = registerPlayer("Pinkie Pie")
    registerTournamentPlayer(tournament, player1)
    registerTournamentPlayer(tournament, player2)
    registerTournamentPlayer(tournament, player3)
    registerTournamentPlayer(tournament, player4)
    reportMatch(tournament, player1, player2, 1)
    reportMatch(tournament, player3, player4, 1)
    pairings = swissPairings(tournament)
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([player1, player3]), frozenset([player2, player4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "15. After one match, players with one win are paired."

def testTournament():
    deleteMatches()
    deleteTournamentsPlayers()
    deleteTournaments()
    deletePlayers()
    tournament = registerTournament("Chess Tournament")
    # register 5 players.
    # A - best player, E - worst player
    player1 = registerPlayer("A")
    player2 = registerPlayer("B")
    player3 = registerPlayer("C")
    player4 = registerPlayer("D")
    player5 = registerPlayer("E")
    registerTournamentPlayer(tournament, player1)
    registerTournamentPlayer(tournament, player2)
    registerTournamentPlayer(tournament, player3)
    registerTournamentPlayer(tournament, player4)
    registerTournamentPlayer(tournament, player5)

    standings = playerStandings()
    actual_standings = set([(row[1], row[2], row[3], row[4], row[5], row[6]) for row in standings])
    correct_standings = set([
        (player1, 'A', 0, 0, 0, 0), (player2, 'B', 0, 0, 0, 0),
        (player3, 'C', 0, 0, 0, 0), (player4, 'D', 0, 0, 0, 0),
        (player5, 'E', 0, 0, 0, 0)
    ])
    if correct_standings != actual_standings:
        raise ValueError(
            "Extra - Newly registered players should have no matches or wins.")
    print "16. Extra - Newly registered players can join a tournament and standings are correct."

    # round 1 - add matches
    # A -> B = 1, C -> D = X, E -> BYE = 1
    reportMatch(tournament, player1, player2, 1)
    reportMatch(tournament, player3, player4, 0)
    reportMatch(tournament, player5, None, 1)

    # standings after first rounds
    standings = playerStandings()
    actual_standings = [(row[1], row[2], row[3], row[4], row[5], row[6]) for row in standings]
    # because C and D has the same OMW and points number both situations are possible
    # since we didn't force any order by name
    correct_standings = [
        (player1, 'A', 1, 1, 0, 3), (player5, 'E', 1, 1, 0, 3),
        (player3, 'C', 1, 0, 1, 1), (player4, 'D', 1, 0, 1, 1),
        (player2, 'B', 1, 0, 0, 0)
    ]
    correct_standings_2 = [
        (player1, 'A', 1, 1, 0, 3), (player5, 'E', 1, 1, 0, 3),
        (player4, 'D', 1, 0, 1, 1), (player3, 'C', 1, 0, 1, 1),
        (player2, 'B', 1, 0, 0, 0)
    ]
    if correct_standings != actual_standings and correct_standings_2 != actual_standings:
        print actual_standings
        print correct_standings
        print correct_standings_2
        raise ValueError(
            "Extra - After first round standings are incorrect.")
    print "17. Extra - Tournaments can have odd number of players."

    # round 2 - now we can use swissPairings method to generate next round of matches
    pairings = swissPairings(tournament)
    if len(pairings) != 3:
        raise ValueError(
            "For six players, swissPairings should return three pairs.")
    [(pid1, pname1, pid2, pname2),
     (pid3, pname3, pid4, pname4),
     (pid5, pname5, pid6, pname6)
    ] = pairings

    # players with 1 win will be paired together.
    # but each player with 1 draw can be paired with player 2 (which has a lost a game)
    # player 3 can't be paired with player4 because they played already
    correct_pairs = set([
        frozenset([player1, player5]), frozenset([player3, player2]), frozenset([player4, None])
    ])
    correct_pairs_2 = set([
        frozenset([player1, player5]), frozenset([player4, player2]), frozenset([player3, None])
    ])
    actual_pairs = set([
        frozenset([pid1, pid2]), frozenset([pid3, pid4]),
        frozenset([pid5, pid6])
    ])
    if correct_pairs != actual_pairs and correct_pairs_2 != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "18. Extra - After one match, players with one win are paired and rematches are prevented (D against C)."

    # A -> E = 1, C -> B = 2, D -> Bye = 1
    reportMatch(tournament, player1, player5, 1)
    reportMatch(tournament, player3, player2, 2)
    reportMatch(tournament, player4, None, 1)

    # standings after second round
    standings = playerStandings()
    actual_standings = [(row[1], row[2], row[3], row[4], row[5], row[6]) for row in standings]
    # E before B because higher OMW
    # E played agains A and got a bye, so the OWM is calculated only agains 1 opponent, bye is ignored
    correct_standings = [
        (player1, 'A', 2, 2, 0, 6), (player4, 'D', 2, 1, 1, 4),
        (player5, 'E', 2, 1, 0, 3), (player2, 'B', 2, 1, 0, 3),
        (player3, 'C', 2, 0, 1, 1)
    ]
    if correct_standings != actual_standings:
        raise ValueError(
            "Extra - After second round standings are incorrect.")
    print "19. Extra - After second round players with same number of points are ranked by OMW."

    # round 3
    pairings = swissPairings(tournament)
    if len(pairings) != 3:
        raise ValueError(
            "For six players, swissPairings should return three pairs.")
    [(pid1, pname1, pid2, pname2),
     (pid3, pname3, pid4, pname4),
     (pid5, pname5, pid6, pname6)
    ] = pairings

    # based on current standings correct pairs are:
    # A - D, B - E, C - Bye
    correct_pairs = set([
        frozenset([player1, player4]), frozenset([player5, player2]), frozenset([player3, None])
    ])
    actual_pairs = set([
        frozenset([pid1, pid2]), frozenset([pid3, pid4]),
        frozenset([pid5, pid6])
    ])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After two matches, players with similar score should be paired.")
    print "20. Extra - After two matches, players with similar score are paired."

    # A -> D = 1, E -> B = 2, C -> Bye = 1
    reportMatch(tournament, player1, player4, 1)
    reportMatch(tournament, player5, player2, 2)
    reportMatch(tournament, player3, None, 1)

    # standings after third round
    # D needs to be before C because he played with A which has more wins than B (which C played against)
    standings = playerStandings()
    actual_standings = [(row[1], row[2], row[3], row[4], row[5], row[6]) for row in standings]
    correct_standings = [
        (player1, 'A', 3, 3, 0, 9), (player2, 'B', 3, 2, 0, 6),
        (player4, 'D', 3, 1, 1, 4), (player3, 'C', 3, 1, 1, 4),
        (player5, 'E', 3, 1, 0, 3)
    ]
    if correct_standings != actual_standings:
        raise ValueError(
            "Extra - After third round standings are incorrect.")
    print "21. Extra - After third round tied are handled by OMW (A, B, D, C, E)."

    return standings;

if __name__ == '__main__':
    testDeleteMatches()
    testDeleteTournamentsPlayers()
    testDeleteTournaments()
    testDelete()
    testCount()
    testCountTournaments()
    testRegisterPlayer()
    testRegisterTournament()
    testRegisterTournamentPlayer()
    testRegisterCountDelete()
    testRegisterCountTournamentsDelete()
    testRegisterCountTournamentsPlayersDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()
    testTournament()

    print "Success!  All tests pass!"
