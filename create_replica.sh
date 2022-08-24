# !/usr/bin/bash

mkdir -p rHost1 rHost2 rHost3
cd rHost1
mkdir data
mkdir log1/mongod.log
cd ..
cd rHost2
mkdir data
mkdir log2/mongod.log
cd ..
cd rHost3
mkdir data
mkdir log3/mongod.log

mongod --replSet rHost --logpath rHost1/log1 --dbpath rHost1/data --port 21017 &
mongod --replSet rHost --logpath rHost2/log2 --dbpath rHost2/data --port 21020 &
mongod --replSet rHost --logpath rHost3/log3 --dbpath rHost3/data --port 21021 &

"C:\Users\reck\OneDrive - Nokia\MongoDB\Server\4.4\bin"\mongod --replSet rHost --logpath rHost1/log1/mongod.log --dbpath rHost1/data --port 21017


C:\Users\reck\OneDrive - Nokia\DHBW\4.Semester\Datenbanken\AktuellerBranch>"C:\Users\reck\OneDrive - Nokia\MongoDB\Server\6.0\bin"\mongod --replSet rHost --logpath rHost1\log1\mongod.log --dbpath rHost1\data --port 21017

C:\Users\reck\OneDrive - Nokia\DHBW\4.Semester\Datenbanken\AktuellerBranch>"C:\Users\reck\OneDrive - Nokia\MongoDB\Server\6.0\bin"\mongod --replSet rHost --logpath rHost2\log2\mongod.log --dbpath rHost2\data --port 21020