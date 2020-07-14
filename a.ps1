add-type -assemblyname system.device;
$loc = new-object system.device.location.geocoordinatewatcher;
$loc.start();
while(($loc.status -ne "Ready") -and ($loc.permission -ne "Denied"))
{start-sleep -milliseconds 100};
$acc = 100;
while($loc.position.location.horizontalaccuracy -gt $acc)
{start-sleep -milliseconds 100; $acc = [math]::Round($acc*1.5)};
$loc.position.location.latitude;
$loc.position.location.longitude;
$loc.position.location.horizontalaccuracy;
$loc.stop()