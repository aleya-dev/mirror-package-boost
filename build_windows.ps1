try
{
    &Push-Location -Path source
    &.\bootstrap.bat
    &.\b2.exe --build-type=complete msvc stage architecture=x86 address-model=64 runtime-link=shared link=static -j 23
}
finally
{
    Pop-Location
}

&conan export-pkg . --profile:all=msvc2022_x86_64_debug --user aleya --channel public
&conan export-pkg . --profile:all=msvc2022_x86_64_release --user aleya --channel public
