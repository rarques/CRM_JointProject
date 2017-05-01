#!/usr/bin/env bash
# First, install or update to the latest system software.
sudo apt-get update
sudo apt-get install build-essential chrpath libssl-dev libxft-dev

# Install these packages needed by PhantomJS to work correctly.
sudo apt-get install libfreetype6 libfreetype6-dev
sudo apt-get install libfontconfig1 libfontconfig1-dev

# Get it from the PhantomJS website.
cd ~
export PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2

# Once downloaded, move Phantomjs folder to /usr/local/share/ and create a symlink:
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

# Now, It should have PhantomJS properly on your system.
phantomjs --version
