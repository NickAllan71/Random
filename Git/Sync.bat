@Echo off
Call "SetPaths"

Call "GitPull"
Call "GitStage"
Call "GitCommit" SkipStatus
Call "GitPush"
