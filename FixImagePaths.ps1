# PowerShell script to fix image paths after postMedia config change
# Replace '/{{ site.postMedia }}' with '{{ site.postMedia }}' in all _posts/*.md files

$postsPath = "_posts"
$searchPattern = '/{{ site.postMedia }}'
$replacement = '{{ site.postMedia }}'

Write-Host "Fixing image paths in markdown files..." -ForegroundColor Green

# Get all markdown files in the _posts directory
$markdownFiles = Get-ChildItem -Path $postsPath -Filter "*.md" -Recurse

$totalFiles = 0
$totalReplacements = 0

foreach ($file in $markdownFiles) {
    Write-Host "Processing: $($file.Name)" -ForegroundColor Yellow
    
    # Read the file content
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Count matches before replacement
    $matches = ([regex]::Matches($content, [regex]::Escape($searchPattern))).Count
    
    if ($matches -gt 0) {
        # Replace the pattern
        $newContent = $content -replace [regex]::Escape($searchPattern), $replacement
        
        # Write back to file
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        
        Write-Host "  Replaced $matches instances" -ForegroundColor Cyan
        $totalReplacements += $matches
        $totalFiles++
    } else {
        Write-Host "  No changes needed" -ForegroundColor Gray
    }
}

Write-Host "`nSummary:" -ForegroundColor Green
Write-Host "Files processed: $($markdownFiles.Count)" -ForegroundColor White
Write-Host "Files modified: $totalFiles" -ForegroundColor White
Write-Host "Total replacements: $totalReplacements" -ForegroundColor White

Write-Host "`nDone! All image paths have been fixed." -ForegroundColor Green