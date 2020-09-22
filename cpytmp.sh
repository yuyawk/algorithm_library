#!/bin/bash

script_template="./template.cpp"
eot=$(printf "%q" "/*------------------ the end of the template -----------------------*/")

if [ $# != 1 ]; then
    for i in `seq 1 20`
    do
        cp "${script_template}" "./notetmp/note${i}tmp.cpp" -f
    done
else
    first="$(grep -B10000  "${eot}" "${script_template}")"
    second="



signed main(void)
{
  cin.tie(0);
  ios::sync_with_stdio(false);




}"
    for i in `seq 1 20`
    do
        echo "${first}" > "./notetmp/note${i}tmp.cpp"
        echo "${second}" >> "./notetmp/note${i}tmp.cpp"
    done
fi