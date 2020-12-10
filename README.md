# Mozplaces
**API de províncias e distritos de Moçambique**

# How to run

* You must to have docker installed and configured

* Build
```bash
docker-compose build
```

* Run
```bash
docker-compose up
```

* Run app in you browser
**Check docker machine IP**
```bash
docker-machine ip default # default is name of my docker-machine. By default maybe in you case is the same
```

Open you browser and go to `http://<ip from the command>:8000/`
*Example if command above return 192.168.99.100*
`http://192.168.99.100/:8000/`
