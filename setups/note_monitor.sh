#!/bin/bash

port=9009
echo "Listening on port $port"



respond() {
    r=''
    h="Content-Type: text/plain\r\nContent-Length: ${#r}\r\n"
    echo -e "HTTP/1.1 200 OK\r\n$h\r\n$r"
}

serve() {
    while true; do
        echo "serving $(respond | nc -l $port | grep POST)"
    done
}

finish() {
    echo "Finished"
}

trap finish EXIT
serve



