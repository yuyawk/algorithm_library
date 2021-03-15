#!/bin/bash

SCRIPT_TEMPLATE="./template.cpp"
EOT="------------------ the end of the template -----------------------"
MAIN_SIMPLE="/*${EOT}*/



signed main(void)
{
  cin.tie(0);
  ios::sync_with_stdio(false);




}"

for i in $(seq 1 20)
do
    if [ $# != 1 ]; then
        cp "${SCRIPT_TEMPLATE}" "./notetmp/note${i}tmp.cpp" -f
    else
        perl -ne "print unless /${EOT}/ && exit" "$SCRIPT_TEMPLATE" > "./notetmp/note${i}tmp.cpp"; echo "${MAIN_SIMPLE}" >> "./notetmp/note${i}tmp.cpp" 
    fi
done