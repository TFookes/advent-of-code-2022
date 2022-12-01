#!/bin/bash

DAY="$( date | awk ' { print $2 } ' )"
DAYSTR="day$DAY"
echo "Pulling input for day $DAY"
mkdir "$DAYSTR"
cp "./template.py" "$DAYSTR/1.py"
cp "./template.py" "$DAYSTR/2.py"
touch "$DAYSTR/inputs.txt"
touch "$DAYSTR/test_inputs.txt"
OUTPUT="$DAYSTR/inputs.txt"
echo "Writing to file: $OUTPUT"

URL="https://adventofcode.com/2022/day/$DAY/input"
SESSION="53616c7465645f5f9c677e64cf30665627b9357e8052e095b6402e2d4c796677df523d22b18ddb6f6f2dd27951b6faf5"

curl --location --request GET "$URL" --header "Cookie: session=$SESSION" -o "$OUTPUT"
echo "Happy Solving :)"
