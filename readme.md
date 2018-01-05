HDU ZhengFang System Toolkits
=============================

[![License](https://img.shields.io/aur/license/yaourt.svg)](https://github.com/SinoReimu/ClassHunter/blob/master/license.txt)


How to install
--------------
```
git clone https://github.com/SinoReimu/ClassHunter
cd ClassHunter
pip install -r requirements.txt
```
then you can use follow function we have already provide

Toolkits
--------
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

## classhunter.py
Get selected class(building)
```
usage : python classHunter.py [classcode] [name] [code]
(not open this function to open source users)
```

## gradequery.py
Query test grade(building)
```
usage : python gradequery.py [name] [code] [year] [term]
```

### more function to develop ---
### you just need to load cookie from cookie.dat

---------------------
License GNUGPL V3.0

For better ocr code, please contact with my email sinoreimu@gmail.com
