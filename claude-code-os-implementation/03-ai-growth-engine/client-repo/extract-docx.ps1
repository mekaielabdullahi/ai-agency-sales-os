Add-Type -AssemblyName System.IO.Compression.FileSystem

$docxPath = "C:\Users\MEKAIEL\workspace\ai-agency-sales-os\claude-code-os-implementation\03-ai-growth-engine\client-repo\Client Portfolio Repository.docx"
$outputPath = "C:\Users\MEKAIEL\workspace\ai-agency-sales-os\claude-code-os-implementation\03-ai-growth-engine\client-repo\extracted-content.txt"

$zip = [System.IO.Compression.ZipFile]::OpenRead($docxPath)
$entry = $zip.Entries | Where-Object { $_.Name -eq 'document.xml' }
$stream = $entry.Open()
$reader = New-Object System.IO.StreamReader($stream)
$content = $reader.ReadToEnd()
$reader.Close()
$stream.Close()
$zip.Dispose()

# Clean up XML tags and entities
$content = $content -replace '<[^>]+>', "`n"
$content = $content -replace '&lt;', '<'
$content = $content -replace '&gt;', '>'
$content = $content -replace '&amp;', '&'
$content = $content -replace '&quot;', '"'
$content = $content -replace '\s+', ' '
$content = $content.Trim()

$content | Out-File -FilePath $outputPath -Encoding UTF8

Write-Host "Content extracted successfully to $outputPath"
