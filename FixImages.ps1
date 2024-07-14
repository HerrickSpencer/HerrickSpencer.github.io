$dir = "D:\source\repos\HerrickSpencer.github.io\_drafts"
Get-ChildItem -File $dir | ForEach-Object {
    $content = Get-Content $_.FullName
    if ($content -like "*wp-content*") {
        $newFilename = $_.FullName; ## $_.DirectoryName + "/" + $_.BaseName + "_FIXED" + $_.Extension
        $newContent = $content -replace "https?://herrickspencer.blog/wp-content/uploads", "/{{ site.postMedia }}"
        Set-Content -Path $newFilename -Value $newContent
        Write-Host "File $($_.Name) processed. New file saved as $newFilename"
    }
}
