#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
import networkx as nx

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteTournaments():
    """Remove all the tournament records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM tournaments"
    cursor.execute(query)
    db.commit()
    db.close()

def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM matches"
    cursor.execute(query)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM players"
    cursor.execute(query)
    db.commit()
    db.close()

def deleteTournamentsPlayers():
    """Remove all the player records from tournaments_players table."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM tournaments_players"
    cursor.execute(query)
    db.commit()
    db.close()

def deleteTournamentPlayers(tournament):
    """Remove player records from tournaments_players for the given tournament."""
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM tournaments_players WHERE tournament = %s"
    cursor.execute(query, (tournament,))
    db.commit()
    db.close()

def countTournaments():
    """Returns the number of tournaments."""
    db = connect()
    cursor = db.cursor()
    query = "SELECT COUNT(id) FROM tournaments"
    cursor.execute(query)
    results = cursor.fetchone()
    db.close()

    if results:
        return results[0]
    return 0

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    query = "SELECT COUNT(id) FROM players"
    cursor.execute(query)
    results = cursor.fetchone()
    db.close()

    if results:
        return results[0]
    return 0

def countTournamentsPlayers():
    """Returns the number of players currently register for all tournaments."""
    db = connect()
    cursor = db.cursor()
    query = "SELECT COUNT(tournament) FROM tournaments_players"
    cursor.execute(query)
    results = cursor.fetchone()
    db.close()

    if results:
        return results[0]
    return 0

def countTournamentPlayers(tournament):
    """Returns the number of players currently registered for the given tournament"""
    db = connect()
    cursor = db.cursor()
    query = """SELECT COUNT(tournament)
               FROM tournaments_players
               WHERE tournament = %s"""
    cursor.execute(query, (tournament,))
    results = cursor.fetchone()
    db.close()

    if results:
        return results[0]
    return 0

def registerTournament(name):
    """Adds a tournament to the tournament database.

    The database assigns a unique serial id number for the tournament.

    Args:
      name: the tournament's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO tournaments (name) VALUES (%s) RETURNING id"
    cursor.execute(query, (name,))
    db.commit()
    tournament = cursor.fetchone()
    db.close()

    return tournament[0]

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO players (name) VALUES (%s) RETURNING id"
    cursor.execute(query, (name,))
    db.commit()
    player = cursor.fetchone()
    db.close()

    return player[0]

def registerTournamentPlayer(tournament, player):
    """Adds a player to the tournaments players list.

    The given player id is registered to the given tournament.

    Args:
        tournament: the tournament's unique id assigned when tournament was
                    registered
        player: the player's unique id assigned when player was registered
    """
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO tournaments_players (tournament, player) VALUES (%s, %s)"
    cursor.execute(query, (tournament, player))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        tournament: the tournament's unique id (assigned by the database)
        player: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        matches: the number of matches the player has played
        wins: the number of matches the player has won
        draws: the number of draw matches the player has
        points: the number of points the player has
    """
    db = connect()
    cursor = db.cursor()
    query = """SELECT tournament, player, name, matches, wins, draws, points
               FROM standings"""
    cursor.execute(query)
    standings = cursor.fetchall()
    db.close()

    return standings

def playerTournamentStandings(tournament):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Args:
      tournament: the id number of the tournament

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        tournament: the tournament's unique id (assigned by the database)
        player: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        matches: the number of matches the player has played
        wins: the number of matches the player has won
        draws: the number of draw matches the player has
        points: the number of points the player has
    """
    db = connect()
    cursor = db.cursor()
    query = """SELECT tournament, player, name, matches, wins, draws, points
               FROM standings
               WHERE tournament = %s"""
    cursor.execute(query, (tournament,))
    standings = cursor.fetchall()
    db.close()

    return standings

def reportMatch(tournament, first_player, second_player, result):
    """Records the outcome of a single match between two players.

    Args:
      tournament: the id number of the tournament
      first_player:  the id number of the first player
      second_player:  the id number of the second player
      result: the game result, which can be:
                1 - first player won
                0 - draw
                2 - second player won
    """
    if first_player < second_player:
        first_player, second_player = second_player, first_player
        result = (0, 2, 1)[result]

    db = connect()
    cursor = db.cursor()
    query = """INSERT INTO matches (tournament, first_player, second_player, result)
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, (tournament, first_player, second_player, result))
    db.commit()
    db.close()

def playedMatches(tournament):
    """Retrieve a list of played matches."""
    db = connect()
    cursor = db.cursor()
    query = "SELECT player, opponents FROM opponents WHERE tournament = %s"
    cursor.execute(query, (tournament,))
    matches = cursor.fetchall()
    db.close()

    return matches

def swissPairings(tournament):
    """Returns a list of pairs of players for the next round of a match.

    Each player appears exactly once in the pairings. Each player is paired with
    another player with and equal or nearly-equal points record, that is, a player
    adjacent to him or her in the standings.
    For matching resuls Blossom algorithm is used and it is provided by "networkx"
    library (http://networkx.github.io/).

    Args:
      tournament: the id number of the tournament

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairs = []
    players = playerTournamentStandings(tournament)
    players_number = countTournamentPlayers(tournament)
    if players_number % 2 != 0:
        players.append((None, None, 'Bye', 0, 0, 0, 0))
    # use Blossom algorighm to generrate best matches
    graph = nx.complete_graph(len(players))
    player_to_node = {players[key][1]: key for key, row in enumerate(players)}
    # exclude already played games
    for pair in playedMatches(tournament):
        for opponent in pair[1]:
            if graph.has_edge(player_to_node[pair[0]], player_to_node[opponent]):
                graph.remove_edge(player_to_node[pair[0]], player_to_node[opponent])
    #add weight to each pair (edge)
    for n1, n2, data in graph.edges(data=True):
        weight = 1 + min(players[n1][6], players[n2][6])
        if players[n1][6] != players[n2][6]:
            weight += 1
        data['weight'] = weight
    # generate pairs
    for n1, n2 in nx.max_weight_matching(graph).iteritems():
        if n1 < n2: continue
        pairs.append(
            (players[n1][1], players[n1][2], players[n2][1], players[n2][2])
        )

    return pairs
