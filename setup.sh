#!/bin/bash

if [ $# -ne 5 ];
then
    echo "usage: setup.sh packagename email author description githubuser"
    echo "  where package-name must be [a-z]+"
    exit 0
fi

NAME=$(sed 's/[^a-z]//g' <<< "$1")
NAMEUP="$(tr '[:lower:]' '[:upper:]' <<< ${NAME:0:1})${NAME:1}"
EMAIL=$2
AUTHOR=$3
DESCRIPTION=$4
GITHUBUSER=$5

echo ""
echo "NAME: $NAME"
echo "EMAIL: $EMAIL"
echo "AUTHOR: $AUTHOR"
echo "DESCRIPTION: $DESCRIPTION"
echo "GITHUBUSER: $GITHUBUSER"
echo ""
read -p "Proceed ? [y]/n " go

if [ "$go" == "n" ]
then
    exit 1
fi

# do tag replacements
find . -type f -exec sed -i "s/<package>/$NAME/g" {} +
find . -type f -exec sed -i "s/<Package>/$NAMEUP/g" {} +
find . -type f -exec sed -i "s/<email>/$EMAIL/g" {} +
find . -type f -exec sed -i "s/<author>/$AUTHOR/g" {} +
find . -type f -exec sed -i "s/<description>/$DESCRIPTION/g" {} +
find . -type f -exec sed -i "s/<githubuser>/$GITHUBUSER/g" {} +

# change the package-folder name
mv phoenix "$NAME"

# replace README with the templated one
mv README.rst README.bak
mv _README.rst README.rst


echo "Done"