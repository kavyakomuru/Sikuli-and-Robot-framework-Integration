@echo off
set sikulix_jar=C:\rfw\sikulixapi.jar
set robot_framework_jar=C:\rfw\robotframework-2.8.7.jar

java -cp "%robot_framework_jar%;%sikulix_jar%" ^
     -Dpython.path="%sikulix_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath=Matchmaker.sikuli ^
     --outputdir=results ^
     %*