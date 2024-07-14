$dir = "D:\source\repos\HerrickSpencer.github.io\_drafts"
Get-ChildItem -File $dir | ForEach-Object {
    $content = Get-Content $_.FullName
    $changed = $false;
    if ($content -like "*herrickspencer.wordpress.com*")
    {
        $changed = $true;
        $content = $content | %{
            if ($_ -match '<a href=\"https?://herrickspencer.wordpress.com/(\d{4})\/(\d{2})\/(\d{2})\/(.*?)\/\">(.*?)<\/a>')
            {
                $_ = $_ -replace $Matches[0], ("[{0}](/_posts/{1})" -f $Matches[5], $Matches[4]);
                $_;
            }
            else
            {$_;}
        }
        $content | %{
            if ($_ -match '<a href=\"https?://herrickspencer.wordpress.com/(\d{4})\/(\d{2})\/(\d{2})\/(.*?)\/\">(.*?)<\/a>')
            {
                ("[{0}](/_posts/{1})" -f $Matches[5], $Matches[4]);
            }
        }
    }
    if ($content -like "*wp-content*") {
        $changed = $true;    
        $content = $content -replace "https?://herrickspencer.blog/wp-content/uploads", "/{{ site.postMedia }}"
    }

    if ($changed)
    {
        $newFilename = $_.FullName; ## $_.DirectoryName + "/" + $_.BaseName + "_FIXED" + $_.Extension
        Set-Content -Path $newFilename -Value $newContent
        Write-Host "File $($_.Name) processed. New file saved as $newFilename"
    }
}
