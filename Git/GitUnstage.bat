@Echo off
Call "SetPaths"

Cd %RepoPath%
Echo %_COLOR%Git Unstage All%_RESET%
"%GitExePath%" reset HEAD
"%GitExePath%" checkout .
"%GitExePath%" status .

@Pause