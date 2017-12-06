for i in {1..10000}
do
  x=$(( ($RANDOM % 4)/2 + 20))
  curl "localhost/data?temperatura=$x&ph=$x"
  sleep 1
done
