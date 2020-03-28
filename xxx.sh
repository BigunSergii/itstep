#!/bin/bash

echo "It's script from remote host"
echo "$(date) Hello world" >> /home/scripts/hello.txt

echo "test"

function test(){
	echo "hello"
}
