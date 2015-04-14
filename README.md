
A Django one-page application portal including:

An Intercom app

designed to serve
both browser and a hybrid Android app located at:

https://github.com/hamshif/Intercom.git


The django app is best run with ssl to avoid browser permission annoyance:


0. create ssl certificates according to http://www.hacksparrow.com/node-js-https-ssl-certificate.html




1.  § cd ..../cs_web27/src

2.  § python manage.py runsslserver e-10:8000 --certificate ~/ssl_cert/gid-cert.pem --key ~/ssl_cert/gid-key.pem

in addition websocket signalling server is needed to connect peers move the above to background or open another shell and:

3.  § cd ..../cs_web27/src/intercom/static/webrtc

4.  § node ws_server.js







to test https://your_url:8000/intercom/webrtc/




if you are just interested in the webrtc bit without django and python:

https://github.com/hamshif/webrtc.git



In this project there is also another attempt is a Node.js signalling backend at


cs_web27/src/intercom/static/intercom/webrtc-example/nodejs_server/index.js

To be run by a separate node server [I will work to merge these given time]


test at

https://e-10.cs.huji.ac.il:8000/intercom/webrtc_example/


