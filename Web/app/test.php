<?php
for ($i = 1; $i <= 1000; $i++) {
    $x = (rand(1,3))/3 +20;
    file_get_contents("http://localhost/data?temperatura=".$x."&ph=".$x);
    sleep (1);
}
?>
