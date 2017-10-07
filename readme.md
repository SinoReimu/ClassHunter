# HDU ZhengFang System Toolkits

## How to install
```
git clone https://github.com/SinoReimu/ClassHunter
cd ClassHunter
pip install -r requirements.txt
```
then you can use follow function we have already provide

## login.py
Simulate login and get cookie for later operate
```
usage : python login.py [username] [password] 
```

## timetable.py
Get timetable for logon account
```
usage : python timetable.py [current/history] [name] [code] (if history timetable [year] [term(1-3)])
```

## classHunter.py
Get selected class
```
usage : python classHunter.py [classcode]
(not open this function to open source users)
```

### more function to develop ---
### you just need to load cookie from cookie.dat
