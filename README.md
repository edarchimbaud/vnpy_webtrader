# Web Services Module for VeighNa Framework

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/vnpy-logo.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-1.0.5-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.7|3.8|3.9|3.10-blue.svg" />
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

## Description

Designed for the B-S architecture requirements of the Web services application module, the implementation provides active function call (REST) and passive data push (Websocket) Web server.

Currently only provides the basic trading and management interface, the user according to their own needs to expand the support for other VeighNa application module Web interface (such as CTA strategy auto-trading, etc.).

## Installation

The installation environment is recommended to be based on version 3.0.0 or above of [[**VeighNa Studio**](https://github.com/paperswithbacktest/vnpy)].

Use pip command directly:

``
pip install vnpy_webtrader
```


Or download the source code, unzip it and run it in cmd:

```bash
pip install .
```


## Architecture

* Active function call functionality based on Fastapi-Restful implementation, data flow:
	1. User clicks on a button in the browser to initiate a Restful function call;
	2. the web server receives the Restful request and converts it into an RPC function call to be sent to the transaction server;
	3. The transaction server receives the RPC request, executes the specific functional logic, and returns the result;
	4. the web server returns the result of the Restful request to the browser.

* Based on the Fastapi-Websocket implementation of the passive data push function, the data flow:
	1. The event engine of the transaction server forwards an event push and pushes it to the RPC client (Web server). 2;
	2. the Web server receives the event push, converts it to json format, and sends it out via Websocket;
	3. the browser receives the pushed data via Websocket and renders it on the Web front-end interface.

* The main reasons for dividing the program into two processes include:
	1. the transaction server in the strategy operation and data calculation of the computing pressure is large, need to ensure that as far as possible to ensure low latency efficiency;
	2. Web server needs to face the Internet access, the transaction-related logic can be separated to better ensure security.
