for i in {1..10000}
do
  r=$(( $RANDOM % 10 +10))
  curl "localhost/data?temperatura=$r&ph=$r"
  sleep 1
done
