apt-get -qqy update
apt-get -qqy install git
apt-get -qqy install postgresql python-psycopg2
apt-get -qqy install python-flask python-sqlalchemy
apt-get -qqy install python-pip
pip install networkx
su postgres -c 'createuser -dRS vagrant'
su vagrant -c 'createdb'
su vagrant -c 'psql -f /vagrant/tournament.sql'

vagrantTip="[35m[1mThe shared directory is located at /vagrant\nTo access your shared files: cd /vagrant(B[m"
echo -e $vagrantTip > /etc/motd
