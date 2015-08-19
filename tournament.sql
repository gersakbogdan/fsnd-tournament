--
-- Table definitions for the tournament project.
--

--
-- Drop database
--
DROP DATABASE IF EXISTS tournament;

--
-- Tournament database
--
CREATE DATABASE tournament;
\c tournament;

--
-- Tournaments table
--
CREATE TABLE tournaments (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

--
-- Players table
--
CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

--
-- Tournaments Players table
--
CREATE TABLE tournaments_players (
  tournament INTEGER REFERENCES tournaments (id),
  player INTEGER REFERENCES players (id),
  PRIMARY KEY (tournament, player)
);

--
-- Matches table
--
CREATE TABLE matches (
	id SERIAL PRIMARY KEY,
  tournament INTEGER NOT NULL,
  first_player INTEGER NOT NULL,
  second_player INTEGER,
  result SMALLINT NOT NULL,
  FOREIGN KEY (tournament, first_player) REFERENCES tournaments_players (tournament, player),
  FOREIGN KEY (tournament, second_player) REFERENCES tournaments_players (tournament, player),
  CHECK (first_player > second_player),
  CHECK (result >= 0 AND result <= 2)
);

--
-- Matches table unique constraints
--
CREATE UNIQUE INDEX tournament_player_unique
  ON matches (tournament, first_player, second_player);

CREATE UNIQUE INDEX tournament_player_bye_unique
  ON matches (tournament, first_player)
  WHERE second_player IS NULL;

--
-- Players matches view (helper view to easy retrieve players games and results)
--
CREATE VIEW players_matches AS
  SELECT m.id, m.tournament,
         CASE
          WHEN p.id = m.first_player THEN m.first_player ELSE m.second_player
         END as player,
         CASE
          WHEN p.id = m.first_player THEN m.second_player ELSE m.first_player
         END as opponent,
         CASE
          WHEN p.id = m.second_player AND m.result = 2 THEN 1 ELSE m.result
         END as result
  FROM players p
  INNER JOIN matches m ON m.first_player = p.id OR m.second_player = p.id;

--
-- Players stats view
--
CREATE VIEW players_stats AS
  SELECT pm.tournament,
         pm.player,
         COUNT(pm.player) AS matches,
         SUM(CASE result WHEN 1 THEN 1 ELSE 0 END) as wins,
         SUM(CASE result WHEN 0 THEN 1 ELSE 0 END) as draws
  FROM players_matches pm
  GROUP BY pm.tournament, pm.player;

--
-- Opponents view
--
CREATE VIEW opponents as
  SELECT pm.tournament, pm.player, array_agg(pm.opponent) as opponents
  FROM players_matches pm
  GROUP BY pm.tournament, pm.player;

--
-- Opponents matches wins (https://www.wizards.com/dci/downloads/tiebreakers.pdf)
--
CREATE VIEW opponents_matches_wins AS
  SELECT o.tournament, o.player, SUM((ps.wins::float * 3 + ps.draws)/(ps.matches * 3)) / COUNT(o.opponents) as omw
  FROM opponents o
  INNER JOIN players_stats ps ON ps.player = ANY(o.opponents)
  GROUP BY o.tournament, o.player;

--
-- Standings view
--
CREATE VIEW standings AS
  SELECT tp.tournament, p.id as player, p.name, coalesce(ps.matches, 0) as matches,
         coalesce(ps.wins, 0) as wins, coalesce(ps.draws, 0) as draws,
         coalesce(ps.wins * 3 + ps.draws, 0) as points,
         omw.omw
  FROM players p
  LEFT JOIN tournaments_players tp ON tp.player = p.id
  LEFT JOIN players_stats ps ON tp.tournament = ps.tournament AND ps.player = p.id
  LEFT JOIN opponents_matches_wins omw ON omw.tournament = tp.tournament AND omw.player = ps.player
  ORDER BY tp.tournament ASC, points DESC, omw.omw DESC NULLS LAST;
