#!/usr/bin/env bash
htunn="htunn thu thu"
uname="uname -avr"
disk="df -hT"

function hello()
{
	printf "Hello world %s\n" "$htunn"
	$uname
}

function world()
{
	printf "check disk usage"
 	$disk	
}

function main()
{
	hello
	world
}
main
