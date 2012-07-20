function SaveSettings() {
}

function ReloadSettings() {
}

function ResetSettings() {
}

function buttonsSetup() {
    $("#save").click(function() {
            SaveSettings();
    });

    $("#reload").click(function() {
            ReloadSettings();
    });
    $("#refresh").click(function() {
        RefreshMovies();
    });
    $("#reset").click(function() {
        ResetSettings();
    });
}