@Echo off
Call "SetPaths"

Cd %RepoPath%

if "%1" Neq "SkipStatus" (
	"%GitExePath%" status
)

Echo %_COLOR%Git Commit%_RESET%
Set /P CommitMessage=Commit Message: 

"%GitExePath%" commit -m "%CommitMessage%"

@Pause
Cd %ThisPath%