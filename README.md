Na-ovoce.cz
===========

Na ovoce aims to become a web community platform that maps fruit trees, fruit bushes and 
herbs in wild and public spaces. At the same time its activities increase awareness 
of traditional varieties among the general public and contribute to their retention 
in the landscape.

## Installation

Prerequisities:

* Python3.4+
* PostgreSQL 9+
* CoffeeScript
* Less
* Bower

You may also need to install Cairo (eg. `brew install cairo`) if it's not already in your system.


Very basic local installation example:

	# Create and activate virtualenv with the latest Python 3 you have:
	mkdir ~/.env
	python3[.5] -m venv ~/.env/naovoce
	source ~/.env/naovoce/bin/activate

	# Upgrade pip:
	pip install --upgrade pip
	
	# If you don't have (or want) node.js, you can install it into your virtualenv:
	pip install nodeenv
	nodeenv -p --prebuilt
	npm install -g coffee-script less bower

	# Install site and dependencies:
	git clone https://github.com/jsmesami/naovoce.git
	cd naovoce
	pip install -r requirements.txt [-b ~/tmp]
	bower install

	# Create and edit local settings to match your setup: 
	cd src
	cp naovoce/settings/local_[deploy|devel]_example.py naovoce/settings/local.py
	vim naovoce/settings/local.py

	# Create datbase to match your settings, eg.:
	psql -c "CREATE DATABASE naovoce OWNER=naovoce"
	
	# Populate database:
	# If your DB user is not superuser, you my have to install HStore extension by hand
	# in case it does not exist yet: CREATE EXTENSION IF NOT EXISTS hstore;
	chmod u+x manage.py
	./manage.py migrate
	./manage.py loaddata naovoce/fixtures/sites.json
	./manage.py loaddata fruit/fixtures/kinds.json
	./manage.py createsuperuser
	
	# You may need to run collectstatic, if you point your STATIC_ROOT outside of the project:
	./manage.py collectstatic
