## Udacity FSND - Tournament Planner Project
The game tournament is using [Swiss system](https://en.wikipedia.org/wiki/Swiss-system_tournament) for pairing up players in each round.

### Tournament planner features:
  - each player is paired with another player with the same number of wins or as close as possible (Blossom Algorithm)
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


### Creators

**Bogdan Gersak**

* <https://twitter.com/gersakbogdan>
* <https://github.com/gersakbogdan>

**Udacity**

* <https://www.udacity.com>
