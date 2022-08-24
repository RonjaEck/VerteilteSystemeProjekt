// """
// 1. In erstem cmd C:\Users\reck\OneDrive - Nokia\MongoDB\Server\6.0\bin>mongod --dbpath "C:\Users\reck\OneDrive - Nokia\MongoDB\Server\6.0\data" --logpath "C:\Users\reck\OneDrive - Nokia\MongoDB\Server\6.0\log\mongod.log" --port 27017 --storageEngine=wiredTiger --journal --replSet testrep startet eine Instanz auf port 27017
//      -> das ganze mehrmals um mehrere Instanzen zu starten
// 2. In zweitem cmd C:\Users\reck\OneDrive - Nokia\MongoDB\Server\4.4\bin>mongo --port 27017 öffnet mongo shell port 27017
//   - Befehl use admin
//   - rsconf={_id: "testrep", members:[     {_id:0, host : "localhost:27017"}] };
//   - rs.initiate(rsconf)
//   - rs.status()
// 3. db.shutdownServer()

// """




config = {_id: "rHost", members:[
    {_id:0, host : "localhost:27017"},
    {_id:1, host:"localhost:27020"},
    {_id: 2, host : "localhost:27021"} ]
};

bbconf = {
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
  }

rs.initiate(config);
rs.status();