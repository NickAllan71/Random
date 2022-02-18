@Echo off
Call "SetPaths"

Cd %RepoPath%
Echo %_COLOR%Git Stage All%_RESET%
"%GitExePath%" add .
"%GitExePath%" status .

@Pause
Cd %ThisPath%