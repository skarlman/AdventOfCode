$param1=$args[0]

$path = ".\day$($param1)"
If(!(test-path $path))
{
      New-Item -ItemType Directory -Force -Path $path
}

Copy-Item "template.py" -Destination "$($path)\test_day$($param1).py"

New-Item "$($path)\input.txt"
Set-Content "$($path)\input.txt" 'Not yet downloaded....'

New-Item "$($path)\exampleinput.txt"
Set-Content "$($path)\exampleinput.txt" 'Not yet copied from https://adventofcode.com/2021/day/$($param1)'

