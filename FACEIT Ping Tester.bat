@ECHO OFF
mode con: lines=68
ECHO Ping To FaceIT CSGO Servers v1.1 by Defirence (Original code by Weeeishy) - August 17th 2018
ECHO ============================================================= 
ECHO -AUTO PING MODE is (ENABLED)- Please wait while first pings are loading...
:top
color 07
TITLE Ping To FaceIT CSGO Servers v1.1 by Defirence (Original code by Weeeishy) - August 17th 2018
:pads
CALL:pingtest1 88.198.52.17 148.251.124.133 46.4.35.143 82.145.38.9
CALL:pingtest2 185.16.86.1 62.210.84.115 195.154.170.125 163.172.8.51
CALL:pingtest3 195.154.170.125 46.166.189.17 185.16.84.57
CALL:pingtest4 185.62.207.33
CALL:pingtest5 165.73.240.107 165.73.240.108 165.73.240.118 165.73.240.110 165.73.240.115 165.73.240.109 165.73.240.116
CLS
ECHO Ping To FaceIT CSGO Servers v1.1 by Defirence (Original code by Weeeishy) - August 17th 2018
ECHO ============================================================= 
ECHO.[Germany]
ECHO - Germany, DE (88.198.52.17):				    (%ms1%)
ECHO - Germany, DE (148.251.124.133):				(%ms2%)
ECHO - Germany, DE (46.4.35.143):				    (%ms3%)
ECHO.
ECHO.[Great Britain]
ECHO - Great Britain, UK (82.145.38.91):			(%ms4%)
ECHO - Great Britain, UK (185.16.86.1):				(%ms5%)
ECHO - Great Britain, UK (87.117.219.99):			(%ms6%)

ECHO.
ECHO.[France]
ECHO - France, FR (62.210.84.115):				    (%ms7%)
ECHO - France, FR (163.172.8.51):				    (%ms8%)
ECHO - France, FR (195.154.170.125):				(%ms9%)
ECHO.
ECHO.[Netherlands]
ECHO - Netherlands, NL (46.166.189.17):		        (%ms10%)
ECHO - Netherlands, NL (185.16.84.57):		        (%ms11%)
ECHO.
ECHO.[Sweden]
ECHO - Sweden, SE (185.62.207.33):		           	(%ms12%)
ECHO.
ECHO.[South Africa] [Assuming all servers hosted in JHB]
ECHO - Johannesburg, ZA (165.73.240.107):			(%ms13%)
ECHO - Johannesburg, ZA (165.73.240.108):			(%ms14%)
ECHO - Johannesburg, ZA (165.73.240.118):			(%ms15%)
ECHO - Johannesburg, ZA (165.73.240.110):			(%ms16%)
ECHO - Johannesburg, ZA (165.73.240.115):			(%ms17%)
ECHO - Johannesburg, ZA (165.73.240.109):			(%ms18%)
ECHO - Johannesburg, ZA (165.73.240.116):   (%ms19%)
ECHO.
ECHO ============================================================= 
ECHO -AUTO PING MODE is (ENABLED)- The pings will automatically keep refreshing.
GOTO top
 
:pingtest1
ECHO.
SET ms1=ERROR
SET ms2=ERROR
SET ms3=ERROR
SET ms4=ERROR
ECHO + Pinging (Germany)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms1=%%i
ECHO + Pinging (Germany)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %2 ^| FIND "ms"') DO SET ms2=%%i
ECHO + Pinging (Germany)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %3 ^| FIND "ms"') DO SET ms3=%%i
ECHO + Pinging (UK)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %4 ^| FIND "ms"') DO SET ms4=%%i
GOTO:EOF

:pingtest2
ECHO.
SET ms5=ERROR
SET ms6=ERROR
SET ms7=ERROR
SET ms8=ERROR
ECHO + Pinging (UK)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms5=%%i
ECHO + Pinging (UK)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %2 ^| FIND "ms"') DO SET ms6=%%i
ECHO + Pinging (France)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %3 ^| FIND "ms"') DO SET ms7=%%i
ECHO + Pinging (France)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %4 ^| FIND "ms"') DO SET ms8=%%i
GOTO:EOF

:pingtest3
ECHO.
SET ms9=ERROR
SET ms10=ERROR
SET ms11=ERROR
SET ms12=ERROR
ECHO + Pinging (France)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms9=%%i
ECHO + Pinging (Netherlands)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %2 ^| FIND "ms"') DO SET ms10=%%i
ECHO + Pinging (Netherlands)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %3 ^| FIND "ms"') DO SET ms11=%%i
GOTO:EOF

:pingtest4
ECHO.
SET ms12=ERROR
ECHO + Pinging (Sweden)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms12=%%i
GOTO:EOF

:pingtest5
ECHO.
SET ms13=ERROR
SET ms14=ERROR
SET ms15=ERROR
SET ms16=ERROR
SET ms17=ERROR
SET ms18=ERROR
SET ms19=ERROR
ECHO + Pinging (South Africa)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms13=%%i
ECHO + Pinging (South Africa)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms14=%%i
ECHO + Pinging (South Africa)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms15=%%i
ECHO + Pinging (South Africa)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms16=%%i
ECHO + Pinging (South Africa)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms17=%%i
ECHO + Pinging (South Africa)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms18=%%i
ECHO + Pinging (South Africa)
FOR /F "tokens=4 delims==" %%i IN ('ping.exe -n 1 %1 ^| FIND "ms"') DO SET ms19=%%i
GOTO:EOF
