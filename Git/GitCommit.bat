@Echo off
Call "SetPaths"

Cd %RepoPath%

"%GitExePath%" status

Echo %_COLOR%Git Commit%_RESET%
Set /P CommitMessage=Commit Message: 

"%GitExePath%" commit -m "%CommitMessage%"

@Pause