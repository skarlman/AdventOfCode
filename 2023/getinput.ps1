
$param1=$args[0]

$path = ".\day$($param1)"
If(!(test-path $path))
{
      New-Item -ItemType Directory -Force -Path $path
}




$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("session", "INSERT COOKIE HERE", "/", ".adventofcode.com")))
Invoke-WebRequest -UseBasicParsing -Uri "https://adventofcode.com/2023/day/$($param1)/input" `
-WebSession $session `
-OutFile ".\day$($param1)\input.txt" `
-Headers @{
"authority"="adventofcode.com"
  "method"="GET"
  "path"="/2023/day/$($param1)/input"
  "scheme"="https"
  "accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  "accept-encoding"="gzip, deflate, br"
  "accept-language"="sv-SE,sv;q=0.9,en-SE;q=0.8,en;q=0.7,en-US;q=0.6"
  "cache-control"="no-cache"
  "pragma"="no-cache"
  "referer"="https://adventofcode.com/2023/day/$($param1)"
  "sec-ch-ua"="`"Google Chrome`";v=`"119`", `"Chromium`";v=`"119`", `"Not?A_Brand`";v=`"24`""
  "sec-ch-ua-mobile"="?0"
  "sec-ch-ua-platform"="`"Windows`""
  "sec-fetch-dest"="document"
  "sec-fetch-mode"="navigate"
  "sec-fetch-site"="same-origin"
  "sec-fetch-user"="?1"
  "upgrade-insecure-requests"="1"
}