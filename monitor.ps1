$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$ping = Test-Connection -ComputerName google.com -Count 1 -Quiet
$cpu = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue
$ram = (Get-WmiObject Win32_OperatingSystem).FreePhysicalMemory
$disk = (Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='C:'").FreeSpace
$av = (Get-MpComputerStatus).AMServiceEnabled

$data = "$timestamp, $ping, $cpu, $ram, $disk, $av"
$logFile = "./logs/log-$(Get-Date -Format 'yyyy-MM-dd').csv"

if (-Not (Test-Path "./logs")) {
    New-Item -Path "./logs" -ItemType Directory
}

Add-Content -Path $logFile -Value $data