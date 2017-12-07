for i in {1..10000}
do
  x=$(($RANDOM % 10 + 17))
  curl "localhost/data?temperatura=$x&ph=$x"
  sleep 1
done
