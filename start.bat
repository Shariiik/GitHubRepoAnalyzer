@echo off
title GitHubRepoAnalyzer v2.0.0 [Terminal]
cls
echo.
set /p target_url="[*] Enter GitHub Repository URL: "
echo.
python GitHubRepoAnalyzer.py %target_url%
echo.
pause