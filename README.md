# VerteilteSystemeProjekt
1. Code downloaden
2. Terminalfenster öffnen -> in Download-Ordner navigieren -> 1. Instanz starten mit mongod --replSet rHost --logpath rHost1\log1\mongod.log --dbpath rHost1\data --port 21017
3. 2. Terminalfenster öffnen -> in Download-Ordner navigieren -> 2. Instanz starten mit mongod --replSet rHost --logpath rHost2\log2\mongod.log --dbpath rHost2\data --port 21018
4. 3. Terminalfenster öffnen -> in Download-Ordner navigieren -> 3. Instanz starten mit mongod --replSet rHost --logpath rHost3\log3\mongod.log --dbpath rHost3\data --port 21019
5. diese drei Terminalfenster geöffnet lassen
6. 4. Terminalfenster öffnen -> mongo --port 21017 (o. 21018 o. 21019 o. alle drei) -> mongo-shell öffnet sich -> 
config = {
    _id: "rHost",
    members: [
      {
       _id: 0,
       host: "localhost:21017"
      },
      {
       _id: 1,
       host: "localhost:21018"
      },
      {
       _id: 2,
       host: "localhost:21019"
      }
     ]
  } eingeben -> rs.initiate(config);
  7. rs.status(); -> zeigt Status des ReplicaSets an (z.B. wer Primary ist)
  8. in mongoDB Compass kann mit replicaSet oder einzeln mit localhost:<einer der 3 ports> verbunden werden -> darin kann der Inhalt der Db gesehen werden (auf allen drei Ports)
  9. Applikation file_service.py starten und auf 127.0.0.1:5000 Daten und File eingeben -> File wird in Ordner static gespeichert & Metadaten in der Db auf allen 3 Ports (siehe Compass oder mongo shell)
 
