#!/usr/bin/env bash

# bash function
function shfunc()
    {
        printf "hello world\n"
        uname -avr	
    }

function main()
   {
       shfunc
   }
main
#for ((i=0; i<5; i++))
#   do
#        shfunc 
#   done
