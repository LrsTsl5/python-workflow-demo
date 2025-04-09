: : Opens vs-code in current directory
: : checks if vs-code insiders is installed when vs-code cannot be found.
where code >nul 2>nul
if %errorlevel% neq 0 (
    pixi run code_insiders . | exit

) else (
    pixi run code . | exit
)