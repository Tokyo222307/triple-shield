#!/usr/bin/env python3
from flask import Flask, render_template, jsonify
import bluetooth
import logging

app = Flask(__name__,template_folder=".")

@app.route("/")
def hello():
    return render_template("index.html")
@app.route('/aperta')
def scan():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)
    print("[+] Socket bluetooth creato e in ascolto")

    # Ottieni la porta
    port = server_sock.getsockname()[1]
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    print("[+] Porta relativa al socket : " + str(port))

    launch=0

    # Pubblicazione del servizio
    try:
        bluetooth.advertise_service(
            server_sock,
            "AutoAcceptServer",
            service_id=uuid,
            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
            profiles=[bluetooth.SERIAL_PORT_PROFILE]
        )
        print("[!] Servizio disponibile all'esterno")
    except bluetooth.BluetoothError as e:
        print("[-] Errore nella pubblicazione del servizio\n\t" + str(e))

    while True:
        print("[ Server in attesa di connessioni dall'esterno ]")
        try:
            client_sock, client_info = server_sock.accept()
            print("[+] Client connesso : " + str(client_info))
            print("[START Chat]")
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                var = ""+data.decode('utf-8')
                print("Ricevuto:", data.decode('utf-8'))
                if(var.strip()=="L"):
                    print("aaa")
                    launch = 1
                    break

        except OSError:
            pass

        client_sock.close()
        print("[END Chat]")
        print("[-] Client disconnesso")
        print(launch)
        if launch == 1:
            break
    server_sock.close()
    print("[Server terminato.]")
    if launch == 0:
        return "Validazione mancante!"
    print("ok")
    return render_template("forte.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
