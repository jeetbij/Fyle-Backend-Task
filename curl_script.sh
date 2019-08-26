#! /bin/sh

BASE_URL="https://gentle-savannah-96056.herokuapp.com"

echo "Demo user is logging in and fetching JWT token: \n"

#Demo user credentials
USERNAME="jeet"
PASSWORD="qazwsxedc"

echo "Username: $USERNAME"
echo "Password: $PASSWORD"

jwt_token=`curl -s -X POST "$BASE_URL/auth-jwt/" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"username\": \"$USERNAME\", \"password\": \"$PASSWORD\"}"`

echo 
token=`echo $jwt_token | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["token"])'`
echo "token: $token"

echo
IFSC="ABHY0065052"
echo "Getting bank detail with IFSC Code $IFSC"
ifsc_res=`curl -G -s -X GET "$BASE_URL/bank/" -H "accept: application/json" --data-urlencode "ifsc=$IFSC" -H "Authorization: JWT $token"`

echo $ifsc_res | python -m json.tool

echo

# Sample values for limit, offset, bank, city
limit=10
offset=0
bank="ALLAHABAD BANK"
city="DELHI"
name_and_city_res=`curl -G -s -X GET "$BASE_URL/bank/" -H "accept: application/json" \
                            --data-urlencode "bank_name=$bank" --data-urlencode "city=$city" \
                            --data-urlencode "offset=$offset" --data-urlencode "limit=$limit" \
                            -H "Authorization: JWT $token"`

echo "\n Searching with following data: limit=$limit offset=$offset bank=$bank city=$city\n"
echo $name_and_city_res | python -m json.tool

echo

offset=5
echo "\n Now offset is 5. Data: limit=$limit offset=$offset bank=$bank city=$city\n"
name_and_city_res=`curl -G -s -X GET "$BASE_URL/bank/" -H "accept: application/json" \
                            --data-urlencode "bank_name=$bank" --data-urlencode "city=$city" \
                            --data-urlencode "offset=$offset" --data-urlencode "limit=$limit" \
                            -H "Authorization: JWT $token"`
echo $name_and_city_res | python -m json.tool