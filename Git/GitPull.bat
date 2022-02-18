@Echo off
Call "SetPaths"

Cd %RepoPath%
Echo %_COLOR%Git Pull%_RESET%
"%GitExePath%" pull

@Pause