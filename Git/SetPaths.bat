Set GitExePath=C:\Program Files\Git\cmd\git.exe
Set ThisPath=%~dp0
Set RepoPath=%ThisPath%..\

Set _bYellow=[43m
Set _fBWhite=[97m
Set _COLOR=%_fBWhite%%_bYellow%
Set _RESET=[0m

If Not Exist "%GitExePath%" (
	Echo %_COLOR%Cannot find git.exe%_RESET%
	Echo I'm looking here: %GitExePath%
	Pause
	Goto :EOF
)