## Udacity FSND - Tournament Planner Project
The game tournament is using [Swiss system](https://en.wikipedia.org/wiki/Swiss-system_tournament) for pairing up players in each round.

### Tournament planner features:
  - each player is paired with another player with the same number of points or as close as possible
  - the matching algorithm is based on Blossom Algorithm and provided by an external library [networkx](networkx.github.io)
  - rematches between players are prevented
  - odd/even number of players are supported
  - in the case of odd number of playes "bye" (skipped round) will be assign to one player
  - a player can get maximum one "bye"
  - draw (tied game) is supported
  - players are rank according to OMW (Opponent Match Wins) when they have the same number of points
  - multiple tournaments are supported

### Install

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2. Clone repository: `git clone https://github.com/gersakbogdan/fsnd-tournament fsnd-tournament`
3. Launch the Vagrant VM, from the root `/fsnd-tournament` directory run `vagrant up` in the command line.
4. To connect to Vagrant VM run `vagrant ssh` and go to the shared directory using: `cd /vagrant`
5. Run tournament test units: `python tournament_test.py`

### Running unit tests
```bash
vagrant@vagrant-ubuntu-trusty-32:/vagrant$ python tournament_test.py
1. Old matches can be deleted.
2. Old tournaments players records can be deleted.
3. Old tournament records can be deleted.
4. Old player records can be deleted.
5. After deleting, countPlayers() returns zero.
6. After deleting, countTournaments() returns zero.
7. After registering a player, countPlayers() returns 1.
8. After registering a tournament, countTournaments() returns 1.
9. After registering a player to a tournament, countTournamentPlayers() returns 1.
10. Players can be registered and deleted.
11. Tournaments can be registered and deleted.
12. Tournaments players can be registered and deleted.
13. Newly registered players appear in the standings with no matches.
14. After a match, players have updated standings.
15. After one match, players with one win are paired.
16. Extra - Newly registered players can join a tournament and standings are correct.
17. Extra - Tournaments can have odd number of players.
18. Extra - After one match, players with one win are paired and rematches are prevented (D against C).
19. Extra - After second round players with same number of points are ranked by OMW.
20. Extra - After two matches, players with similar score are paired.
21. Extra - After third round tied are handled by OMW (A, B, D, C, E).
Success!  All tests pass!
```

### Running tournament simulator

### Creators

**Bogdan Gersak**

* <https://twitter.com/gersakbogdan>
* <https://github.com/gersakbogdan>

**Udacity**

* <https://www.udacity.com>
