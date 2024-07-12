$test = "<a href=`"http://herrickspencer.blog/wp-content/uploads/2020/08/drill_and_charger_rack_render.png`"><img title=`"Drill_and_Charger_Rack_Render`" style=`"display:inline;background-image:none;`" border=`"0`" alt=`"Drill_and_Charger_Rack_Render`" src=`"http://herrickspencer.blog/wp-content/uploads/2020/08/drill_and_charger_rack_render_thumb.png`" width=`"525`" height=`"421`" /></a></p>";
exit;

$dir = "D:\source\repos\HerrickSpencer.github.io\_drafts"
gci -File $dir | %{
    $content = gc $_.FullName;
    $title = $content[2].Substring(7);
    $title 

    $content | ?{ $_ -like "*http://herrickspencer.blog/wp-content/uploads/*" }



    break;
    }
    
    