$dir = "D:\source\repos\HerrickSpencer.github.io\_drafts"
$children = Get-ChildItem -File $dir 
foreach( $_ in $children) {
    $content = Get-Content $_.FullName
    $changed = $false;
    
    if ($content -like "*herrickspencer.wordpress.com*")
    {
    $_.FullName;
        $content = $content | %{
            if ($_ -match '<a .*?href=\"https?:\/\/herrickspencer\.wordpress\.com/(\d{4}\/)?(\d{2}\/)?(\d{2}\/)?(.*?)\/?\">(.*?)<\/a>')
            {
                $changed = $true;
                $_ = $_ -replace $Matches[0], ("[{0}](/_posts/{1})" -f $Matches[5], $Matches[4]);
            }
            $_;             
        }
    }
<#    if ($changed -eq $true)
    {
        Write-Host "CONTENT:" $content;
        break;
        }
    continue;
    Write-host "HERE"
    #>
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
