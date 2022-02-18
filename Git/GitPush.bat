@Echo off
Call "SetPaths"

Cd %RepoPath%

"%GitExePath%" status

Echo %_COLOR%Git Push%_RESET%

"%GitExePath%" push

@Pause
Cd %ThisPath%