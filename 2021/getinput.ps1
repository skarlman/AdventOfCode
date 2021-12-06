
$param1=$args[0]

$path = ".\day$($param1)"
If(!(test-path $path))
{
      New-Item -ItemType Directory -Force -Path $path
}


$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("session", "53616c7465645f5fee707056c539b24e290ab8df17c66d13d47a215c9b73f6c6df3ca8ce6c349c1c877068ebf489d9a3", "/", ".adventofcode.com")))
Invoke-WebRequest -UseBasicParsing -Uri "https://adventofcode.com/2021/day/$($param1)/input" `
-WebSession $session `
-OutFile ".\day$($param1)\input.txt" `
-Headers @{
"method"="GET"
  "authority"="adventofcode.com"
  "scheme"="https"
  "path"="/2021/day/$($param1)/input"
  "cache-control"="max-age=0"
  "sec-ch-ua"="`" Not A;Brand`";v=`"99`", `"Chromium`";v=`"96`", `"Google Chrome`";v=`"96`""
  "sec-ch-ua-mobile"="?0"
  "sec-ch-ua-platform"="`"Windows`""
  "upgrade-insecure-requests"="1"
  "accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
  "sec-fetch-site"="same-origin"
  "sec-fetch-mode"="navigate"
  "sec-fetch-user"="?1"
  "sec-fetch-dest"="document"
  "referer"="https://adventofcode.com/2021/day/$($param1)"
  "accept-encoding"="gzip, deflate, br"
  "accept-language"="sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7"
}

