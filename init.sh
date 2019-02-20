
if [[ ! -f '.key' ]]; then
    echo "Key file does not exist"
    python3 ./server/utilities/init_key.py # generates api key for external requests
fi

test=$(python3 ./server/tests/testConnection.py 2>&1)

if [[ $test == 0 ]]; then
    export FLASK_APP=server
    export FLASK_ENV=development
    flask run
else
    echo "ERROR CONNECTING TO RDS SERVER, CHECK THE RDS CONFIG VARIABLES"
fi