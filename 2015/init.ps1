function CreateAOCDirectory {
    param (
        $dirName
    )
    if ( -not (Test-Path -Path $dirName)){
        Write-Host "Creating directory: $dirName"
        try {
            New-Item -Path $dirName -ItemType Directory -ErrorAction Continue | Out-Null
        }
        catch {
            Write-Error -Message "Unable to create directory '$dirName'. Error was: $_" -ErrorAction Stop
        }
    }
    else {
        Write-Host "Directory already existed"
    }

}

function CreateAOCFile {
    param(
        $fileName,
        $dirName
    )
    $filePath = "$dirName/$fileName"
    if ( -not (Test-Path -Path $filePath -PathType Leaf))
    {
        Write-Host "Creating file: $fileName"
        try {
            New-Item -Path $filePath -ItemType File -ErrorAction Continue | Out-Null
        }   
        catch {
            Write-Error -Message "Unable to create file '$filePath'. Error was: $_" -ErrorAction Stop
        }
    }
    else {
        Write-Host "File already existed"
    }
}


function InitiateAOCDirectory {
    # Create common
    CreateAOCDirectory -dirName "AOCUtils"
    CreateAOCFile -fileName 'utils.py' -dirName 'AOCUtils'
    #  Create folders for each day
    foreach ($day in 1..24)
    {
        $dirName = "day_" + $day
        CreateAOCDirectory -dirName $dirName
        
        CreateAOCFile -fileName 'main.py' -dirName $dirName
        CreateAOCFile -fileName 'input.txt' -dirName $dirName
    }
}



InitiateAOCDirectory

